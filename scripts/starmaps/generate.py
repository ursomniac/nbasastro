#!/usr/bin/env python3
"""
NBAS Starmap Generator -- three-tier architecture (see GitHub issue #36)

Tier 1, evergreen monthly reference charts: 12 anchor dates (15th of each
month), rendered WITHOUT planets (stars/constellations/Milky Way are
effectively identical year to year for a fixed date+time -- only planetary
position varies). Generated once, rarely re-touched. Both a light and a
dark (inverted) JPG are baked per month at generation time, so the site
never needs Hugo's runtime image-processing pipeline for these.

Tier 2, current week, with planets: a single "current" slot -- JPG always,
PDF only if --pdf is passed. This is slot 1 of --slots mode below.

Tier 3, rolling near-term buffer, with planets: the next N weeks, using
FIXED SLOT filenames (starmap-slot1.jpg ... starmap-slotN.jpg) overwritten
in place each run -- nothing date-named accumulates, so there's nothing to
prune. A sidecar YAML file (data/starmap_slots.yaml, kept separate from the
live data/starmaps.yaml for now) records which real calendar date each slot
currently represents.

Legacy ad hoc mode (single date / --weeks N / --yaml) is kept for manual
testing and matches the old CLI; it does not touch the sidecar file.

Usage:
    python generate.py                     # ad hoc: next Wednesday
    python generate.py 2026-06-18          # ad hoc: specific date
    python generate.py --weeks 4           # ad hoc: next 4 Wednesdays
    python generate.py --pdf               # ad hoc: also emit a print PDF
    python generate.py --evergreen         # tier 1: all 12 monthly anchors
    python generate.py --slots             # tier 2/3: current + rolling buffer
    python generate.py --slots --weeks 6 --pdf  # 6-slot buffer, PDF for current only
"""

import argparse
import io
import math
import os
import tempfile
from datetime import date as date_cls, datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

# ── Ephemeris: reuse the copy already committed in this repo (item 6, issue ──
# ── #36) instead of letting skyfield download a fresh, duplicate one.       ──
# Must be set before `import starplot`: starplot reads this env var once at
# import time to decide where its data Loader (and therefore skyfield) looks
# for cached files, including de421.bsp.
SCRIPT_DIR        = Path(__file__).parent
FINDER_CHARTS_DIR = SCRIPT_DIR / "finder_charts"
EPHEMERIS_FILE    = "de421.bsp"
os.environ.setdefault("STARPLOT_DATA_PATH", str(FINDER_CHARTS_DIR))

import matplotlib.pyplot as plt
import resvg_py
import yaml
from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas as rl_canvas
from starplot import ZenithPlot, Observer, _
from starplot.styles import PlotStyle, extensions

# ── Configuration ──────────────────────────────────────────────────────────────

LAT      = 42.699          # North Adams, MA
LON      = -73.108
TIMEZONE = ZoneInfo("America/New_York")
OUTPUT   = Path(__file__).parent / "output"

# Shared branding assets live once at the repo root (not copied per-feature) --
# scripts/generate.py -> ../assets/
ASSETS    = Path(__file__).parent.parent / "assets"
LOGO_PATH = ASSETS / "nbas-logo.png"
QR_PATH   = ASSETS / "nbas-qrcode.svg"

# Tier-3 sidecar data file. Deliberately NOT data/starmaps.yaml -- that file
# still drives the currently-deployed list.html template with the old flat
# schema. Writing tier-3 slot data to a separate path means running --slots
# today can't break the live site; list.html gets cut over in a later step.
SIDECAR_PATH = Path(__file__).parent.parent.parent / "data" / "starmap_slots.yaml"

TIER3_SLOT_COUNT   = 5   # current + next 4, per issue #36 ("4-6 week buffer")
EVERGREEN_MONTH_DAY = 15  # anchor day-of-month for tier-1 reference charts

# Tier-1 "dark" variant: rendered directly with starplot's own dark style,
# NOT a color-inversion of the light chart. A naive RGB invert of the light
# chart's soft blue Milky Way tint (BLUE_MEDIUM's #94c5e3) produces a muddy
# brown -- inverting a light blue gives a dark orange/brown complement, not
# a clean color. Rendering a second, purpose-built dark chart avoids that
# entirely. BLUE_DARK is a moderate dark blue; swap to extensions.BLUE_NIGHT
# for a near-black background with a more prominent Milky Way band.
EVERGREEN_DARK_EXTENSION = extensions.BLUE_DARK

MAG_LIMIT       = 5.5   # stars plotted (Bortle 4)
MAG_LABEL_LIMIT = 2.4   # stars labeled

# Shared render resolution for the chart, used for both the JPG and (if
# requested) the PDF. 2400px is ~330 DPI at the map's ~7.3" printed size --
# well beyond what any home printer resolves -- while being a fraction of
# the previous 4096px used for both outputs. Tune here in one place.
CHART_RESOLUTION = 2400
JPEG_QUALITY     = 90

# Constellation line color for the LIGHT/print styles (BLUE_MEDIUM, GRAYSCALE)
# only: a medium blue that reads clearly against BLUE_MEDIUM's near-white
# background (#f1f6fe) and prints as a distinct medium grey in greyscale.
# Do NOT reuse this for dark styles (BLUE_DARK/BLUE_NIGHT) -- against their
# dark navy backgrounds it has almost no contrast (this was the "invisible
# constellation lines" bug in the dark evergreen variant). Dark styles use
# their own built-in constellation_lines color instead (see
# _weekly_style_overrides(constellation_color=None) in generate_evergreen).
CONSTELLATION_LINE_COLOR = "#2a5ba8"

ORG_NAME    = "Northern Berkshire Astronomical Society"
ORG_URL     = "https://nbasastro.org/"
ORG_TAGLINE = "Whatever your experience, you belong under our skies."

# ── Helpers ────────────────────────────────────────────────────────────────────

def next_wednesday(from_date=None):
    """Return the next Wednesday on or after from_date (defaults to today)."""
    d = from_date or datetime.now(TIMEZONE).date()
    days_ahead = (2 - d.weekday()) % 7  # 2 = Wednesday
    if days_ahead == 0:
        days_ahead = 7  # already Wednesday → next week
    return d + timedelta(days=days_ahead)


def chart_datetime(date):
    """
    Return a UTC datetime for the chart, scaled by season:

      Summer solstice → 02:30 UTC  (~10:30 PM EDT, well after dark)
      Winter solstice → 01:00 UTC  (~8:00 PM EST, comfortably dark)

    Uses a cosine to smoothly interpolate between those limits.
    Returns UTC; caller converts to local for display only.
    """
    SUMMER_UTC = 2.5   # hours UTC at summer solstice
    WINTER_UTC = 1.0   # hours UTC at winter solstice
    SUMMER_SOLSTICE_DOY = 172  # ~June 21

    doy = date.timetuple().tm_yday
    midpoint  = (SUMMER_UTC + WINTER_UTC) / 2       # 1.75
    amplitude = (SUMMER_UTC - WINTER_UTC) / 2       # 0.75

    utc_hours = midpoint + amplitude * math.cos(
        2 * math.pi * (doy - SUMMER_SOLSTICE_DOY) / 365.25
    )

    # Round to nearest half hour
    total_minutes = round(utc_hours * 60 / 30) * 30
    hour   = (total_minutes // 60) % 24
    minute = total_minutes % 60

    # utc_hours < 12 means early-morning UTC = that night, so date+1
    chart_date = date + timedelta(days=1) if utc_hours < 12 else date
    return datetime(chart_date.year, chart_date.month, chart_date.day,
                    hour, minute, tzinfo=timezone.utc)


def _ensure_ephemeris_available():
    """Belt-and-suspenders check: warn loudly instead of silently letting
    skyfield fall through to a network download if the committed de421.bsp
    is somehow missing from finder_charts/."""
    committed = FINDER_CHARTS_DIR / EPHEMERIS_FILE
    if not committed.exists():
        print(f"  ! WARNING: expected ephemeris file not found at {committed}\n"
              f"    Falling back to a network download via skyfield -- this\n"
              f"    shouldn't happen in normal use; re-add the committed file.")


def _ensure_assets_available():
    """Warn loudly (instead of silently rendering with no logo/QR) if the
    shared branding assets aren't where they're expected."""
    for path in (LOGO_PATH, QR_PATH):
        if not path.exists():
            print(f"  ! WARNING: branding asset not found at {path}\n"
                  f"    Chart will render without it -- no error, just missing.")


def _labels_for(date):
    dt_utc   = chart_datetime(date)
    dt_local = dt_utc.astimezone(TIMEZONE)
    time_str = dt_local.strftime("%-I:%M %p %Z")
    date_str = dt_local.strftime("%-d %b %Y")
    return dt_utc, dt_local, date_str, time_str


def _weekly_style_overrides(constellation_color=CONSTELLATION_LINE_COLOR):
    """constellation_color=None leaves the style's own built-in constellation
    line color untouched -- use that for dark styles (BLUE_DARK/BLUE_NIGHT),
    which already ship a line color tuned for their own dark background."""
    overrides = {"milky_way": {"alpha": 0.45}}
    if constellation_color:
        overrides["constellation_lines"] = {"color": constellation_color}
    return overrides


# ── Chart generation ───────────────────────────────────────────────────────────

def _build_plot(observer, style, resolution=CHART_RESOLUTION, include_planets=True):
    """Shared chart construction. include_planets=False for tier-1 evergreen
    charts: stars/constellations/Milky Way don't meaningfully change year to
    year for a fixed date+time -- only planetary position does."""
    p = ZenithPlot(
        observer=observer,
        style=style,
        resolution=resolution,
        autoscale=True,
    )
    p.milky_way()
    p.horizon()
    p.constellations()
    p.stars(
        where=[_.magnitude < MAG_LIMIT],
        where_labels=[_.magnitude < MAG_LABEL_LIMIT],
    )
    p.constellation_labels()
    if include_planets:
        p.planets()
    return p


def _load_icon(path, target_px):
    """
    Load a branding icon (PNG or SVG) as an RGBA PIL image, sized to fit
    within a target_px x target_px box (aspect ratio preserved). SVGs are
    rasterized directly at the target resolution via resvg_py (a Rust-backed
    renderer with self-contained wheels -- no system Cairo/rlPyCairo install
    required, unlike the reportlab renderPM route); raster formats are opened
    and thumbnailed down the normal way.
    """
    if path.suffix.lower() == ".svg":
        png_bytes = resvg_py.svg_to_bytes(svg_path=str(path), width=target_px)
        return Image.open(io.BytesIO(bytes(png_bytes))).convert("RGBA")
    else:
        img = Image.open(path).convert("RGBA")
        img.thumbnail((target_px, target_px))
        return img


def _build_pdf(chart_img, out_path, date_str, time_str):
    """Compose the full-page printable PDF using reportlab. Opt-in via --pdf."""
    PW, PH = letter          # 612 × 792 pt  (8.5" × 11")

    c = rl_canvas.Canvas(str(out_path), pagesize=letter)

    # ── Title ──────────────────────────────────────────────────────────────────
    c.setFont('Helvetica-Bold', 26)
    c.drawCentredString(PW / 2, PH - 0.65 * inch, 'NBAS StarMap')

    # ── Date (upper left) ──────────────────────────────────────────────────────
    c.setFont('Helvetica-Bold', 11)
    c.drawString(0.6 * inch, PH - 1.10 * inch, 'Date:')
    c.setFont('Helvetica', 11)
    c.drawString(0.6 * inch, PH - 1.32 * inch, date_str)
    c.drawString(0.6 * inch, PH - 1.52 * inch, time_str)

    # ── Location (upper right) ─────────────────────────────────────────────────
    c.setFont('Helvetica-Bold', 11)
    c.drawRightString(PW - 0.6 * inch, PH - 1.10 * inch, 'Location:')
    c.setFont('Helvetica', 11)
    c.drawRightString(PW - 0.6 * inch, PH - 1.32 * inch, 'North Adams, MA')
    c.drawRightString(PW - 0.6 * inch, PH - 1.52 * inch,
                      f'{abs(LON):.2f}° W   {LAT:.2f}° N')

    # ── Star chart (centered) ──────────────────────────────────────────────────
    MAP_SIZE = 7.3 * inch
    map_x    = (PW - MAP_SIZE) / 2
    map_y    = PH - 1.65 * inch - MAP_SIZE      # top of map at 1.65" from top
    c.drawImage(str(chart_img), map_x, map_y,
                width=MAP_SIZE, height=MAP_SIZE,
                preserveAspectRatio=True, anchor='c')

    # ── Footer ─────────────────────────────────────────────────────────────────
    LOGO_SZ   = 1.05 * inch
    QR_SZ     = 0.95 * inch
    footer_y  = map_y - 0.12 * inch        # baseline for footer images
    text_x    = 0.5 * inch + LOGO_SZ + 0.15 * inch
    text_mid  = footer_y - LOGO_SZ / 2

    ICON_RASTER_PX = 600  # rasterize at print quality; reportlab scales to the inch box below

    if LOGO_PATH.exists():
        logo_reader = ImageReader(_load_icon(LOGO_PATH, ICON_RASTER_PX))
        c.drawImage(logo_reader, 0.4 * inch, footer_y - LOGO_SZ,
                    width=LOGO_SZ, height=LOGO_SZ,
                    preserveAspectRatio=True, mask='auto')

    if QR_PATH.exists():
        qr_reader = ImageReader(_load_icon(QR_PATH, ICON_RASTER_PX))
        c.drawImage(qr_reader, PW - 0.4 * inch - QR_SZ, footer_y - QR_SZ,
                    width=QR_SZ, height=QR_SZ,
                    preserveAspectRatio=True, mask='auto')

    c.setFont('Helvetica-Bold', 13)
    c.drawString(text_x, text_mid + 0.22 * inch,
                 'Northern Berkshire Astronomical Society')
    c.setFont('Helvetica', 11)
    c.drawString(text_x, text_mid, 'https://nbasastro.org/')
    c.setFont('Helvetica-Oblique', 10)
    c.drawString(text_x, text_mid - 0.22 * inch,
                 'Whatever your experience, you belong under our skies.')

    c.save()


# ── Cross-platform font resolution ─────────────────────────────────────────
# generate.py was written and only ever run locally on macOS until this
# branch's CI step (hugo.yml, ubuntu-latest) started actually executing it in
# a real pipeline. The original hardcoded macOS system-font paths silently
# fell back to PIL's tiny fixed-size default font on Linux (ImageFont.
# truetype raises OSError there, caught and swallowed). Candidate lists try
# macOS first (unchanged local behavior), then the common Ubuntu locations --
# Liberation Sans (metric-compatible with Arial, installed explicitly in
# hugo.yml's CI step below to guarantee it exists rather than hoping the
# runner image happens to include it) and DejaVu Sans as a second fallback.
BOLD_FONT_CANDIDATES = [
    '/System/Library/Fonts/Supplemental/Arial Bold.ttf',
    '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',
    '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
]
REGULAR_FONT_CANDIDATES = [
    '/System/Library/Fonts/Supplemental/Arial.ttf',
    '/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf',
    '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
]
ITALIC_FONT_CANDIDATES = [
    '/System/Library/Fonts/Supplemental/Arial Italic.ttf',
    '/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf',
    '/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf',
]


def _load_font(candidates, size):
    """Try font file paths in order, returning the first that loads at the
    given size. Only falls back to PIL's tiny fixed-size default font if
    NONE of the candidates exist -- which should no longer happen given the
    explicit font install in hugo.yml's CI step."""
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def _composite_chart(chart, bg_color, title, label):
    """
    Composite a raw chart export into a fully-branded canvas: header band
    (title + date/time) + chart + footer band (logo, org info, QR code).
    Shared by the legacy ad hoc path and the tier-1/2/3 generators below so
    branding can't drift between them.
    """
    W, H = chart.size
    HDR  = H // 9          # header height ≈ 11% of chart
    FTR  = H // 7          # footer height ≈ 14% of chart (logo + text + QR)

    canvas = Image.new('RGB', (W, H + HDR + FTR), color=bg_color)
    canvas.paste(chart, (0, HDR))

    draw = ImageDraw.Draw(canvas)
    title_font = _load_font(BOLD_FONT_CANDIDATES, W // 28)
    label_font = _load_font(REGULAR_FONT_CANDIDATES, W // 38)

    draw.text((W // 2, HDR * 1 // 3), title,
              font=title_font, fill='white', anchor='mm')
    draw.text((W // 2, HDR * 2 // 3), label,
              font=label_font, fill='white', anchor='mm')

    footer_top = HDR + H
    pad        = int(FTR * 0.10)
    box        = FTR - 2 * pad

    if LOGO_PATH.exists():
        logo = _load_icon(LOGO_PATH, box)
        ly = footer_top + (FTR - logo.height) // 2
        canvas.paste(logo, (pad, ly), logo)

    if QR_PATH.exists():
        qr = _load_icon(QR_PATH, box)
        qy = footer_top + (FTR - qr.height) // 2
        canvas.paste(qr, (W - pad - qr.width, qy), qr)

    org_font = _load_font(BOLD_FONT_CANDIDATES, W // 34)
    url_font = _load_font(REGULAR_FONT_CANDIDATES, W // 42)
    tag_font = _load_font(ITALIC_FONT_CANDIDATES, W // 46)

    text_x   = pad * 2 + box
    text_mid = footer_top + FTR // 2
    draw.text((text_x, text_mid - FTR * 0.22), ORG_NAME,
              font=org_font, fill='white', anchor='lm')
    draw.text((text_x, text_mid), ORG_URL,
              font=url_font, fill='white', anchor='lm')
    draw.text((text_x, text_mid + FTR * 0.22), ORG_TAGLINE,
              font=tag_font, fill='white', anchor='lm')

    return canvas


def _render_chart(observer, style, resolution=CHART_RESOLUTION, include_planets=True):
    """Render a chart via starplot and return (chart_image, bg_color).
    Closes the underlying matplotlib figure before returning -- ZenithPlot
    creates one per call and never closes it itself, so a batch run (24
    evergreen charts, N slots) would otherwise leak figures and eventually
    hit matplotlib's "more than 20 figures open" warning/memory bloat."""
    p = _build_plot(observer, style, resolution=resolution, include_planets=include_planets)
    fig_bg   = p.fig.get_facecolor()
    bg_color = tuple(int(c * 255) for c in fig_bg[:3])
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
        tmp_path = Path(tmp.name)
    p.export(str(tmp_path), padding=0.3)
    plt.close(p.fig)
    chart = Image.open(tmp_path)
    tmp_path.unlink()
    return chart, bg_color


def _save_jpeg(canvas, path, quality=None):
    """Save a composited canvas as JPEG. quality=None uses the module default
    (JPEG_QUALITY) -- pass an explicit value (e.g. from --quality) to override."""
    canvas.save(str(path), format='JPEG', quality=quality or JPEG_QUALITY,
                optimize=True, dpi=(300, 300))


def generate(date, make_pdf=False, output_dir=None, quality=None, resolution=None):
    """Legacy ad hoc mode: single WITH-planets map, date-stamped filename.
    For manual testing -- does not touch the tier-3 sidecar file."""
    output_dir = Path(output_dir) if output_dir else OUTPUT
    resolution = resolution or CHART_RESOLUTION
    output_dir.mkdir(parents=True, exist_ok=True)
    _ensure_ephemeris_available()
    _ensure_assets_available()

    dt_utc, dt_local, date_str, time_str = _labels_for(date)
    stem = date.strftime("%Y-%m-%d")

    print(f"  Date   : {date_str}")
    print(f"  Time   : {time_str}  ({dt_utc.strftime('%H:%M UTC')})")

    observer = Observer(lat=LAT, lon=LON, dt=dt_utc)
    overrides = _weekly_style_overrides()

    # JPG — color, serves both web display AND printing (branding baked in)
    img_path = output_dir / f"{stem}.jpg"
    img_style = PlotStyle().extend(extensions.BLUE_MEDIUM, overrides)
    chart, bg_color = _render_chart(observer, img_style, resolution=resolution,
                                     include_planets=True)
    canvas = _composite_chart(
        chart, bg_color,
        title=ORG_NAME,
        label=f"Date: {date_str}, {time_str} – Location: North Adams, MA",
    )
    _save_jpeg(canvas, img_path, quality=quality)
    print(f"  ✓ JPG  : {img_path}  ({img_path.stat().st_size / 1024:.0f} KB)")

    # PDF — optional, full-page printable layout via reportlab (opt-in via --pdf)
    if make_pdf:
        pdf_path = output_dir / f"{stem}.pdf"
        with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as tmp:
            chart_tmp = Path(tmp.name)
        p_print = _build_plot(observer, PlotStyle().extend(extensions.GRAYSCALE, overrides),
                               resolution=resolution)
        p_print.export(str(chart_tmp), format='jpg', pil_kwargs={'quality': 92})
        plt.close(p_print.fig)
        _build_pdf(chart_tmp, pdf_path, date_str, time_str)
        chart_tmp.unlink()
        print(f"  ✓ PDF  : {pdf_path}")


# ── Tier 2/3: current + rolling slots (--slots) ────────────────────────────────

def generate_slot(date, slot_label, make_pdf=False, output_dir=None, quality=None, resolution=None):
    """Render one WITH-planets chart into a fixed slot filename (e.g.
    starmap-slot1.jpg), overwriting whatever was there before -- nothing
    date-named accumulates, so there's nothing to prune."""
    output_dir = Path(output_dir) if output_dir else OUTPUT
    resolution = resolution or CHART_RESOLUTION
    output_dir.mkdir(parents=True, exist_ok=True)
    _ensure_ephemeris_available()
    _ensure_assets_available()

    dt_utc, dt_local, date_str, time_str = _labels_for(date)
    print(f"  {slot_label}: {date_str}, {time_str} ({dt_utc.strftime('%H:%M UTC')})")

    observer = Observer(lat=LAT, lon=LON, dt=dt_utc)
    overrides = _weekly_style_overrides()
    label = f"Date: {date_str}, {time_str} – Location: North Adams, MA"

    style = PlotStyle().extend(extensions.BLUE_MEDIUM, overrides)
    chart, bg_color = _render_chart(observer, style, resolution=resolution,
                                     include_planets=True)
    canvas = _composite_chart(chart, bg_color, title=ORG_NAME, label=label)

    jpg_path = output_dir / f"{slot_label}.jpg"
    _save_jpeg(canvas, jpg_path, quality=quality)
    print(f"    ✓ JPG : {jpg_path.name}  ({jpg_path.stat().st_size / 1024:.0f} KB)")

    pdf_path = None
    if make_pdf:
        pdf_path = output_dir / f"{slot_label}.pdf"
        with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as tmp:
            chart_tmp = Path(tmp.name)
        p_print = _build_plot(observer, PlotStyle().extend(extensions.GRAYSCALE, overrides),
                               resolution=resolution)
        p_print.export(str(chart_tmp), format='jpg', pil_kwargs={'quality': 92})
        plt.close(p_print.fig)
        _build_pdf(chart_tmp, pdf_path, date_str, time_str)
        chart_tmp.unlink()
        print(f"    ✓ PDF : {pdf_path.name}  ({pdf_path.stat().st_size / 1024:.0f} KB)")

    return {
        "slot": slot_label,
        "date": date.isoformat(),
        "label": date_str,
        "time": time_str,
        "jpg": jpg_path.name,
        "pdf": pdf_path.name if pdf_path else None,
    }


def generate_slots(weeks=TIER3_SLOT_COUNT, make_pdf=False, start=None, output_dir=None,
                    quality=None, resolution=None):
    """Tier 2 + tier 3: starmap-slot1 (current, tier 2, the only slot
    eligible for --pdf) through starmap-slotN (tier 3 rolling buffer).
    Writes/updates the sidecar YAML recording each slot's real date."""
    output_dir = Path(output_dir) if output_dir else OUTPUT
    start = start or next_wednesday()
    dates = []
    d = start
    for _ in range(weeks):
        dates.append(d)
        d = next_wednesday(d)

    entries = [
        generate_slot(date, f"starmap-slot{i}", make_pdf=(make_pdf and i == 1),
                      output_dir=output_dir, quality=quality, resolution=resolution)
        for i, date in enumerate(dates, start=1)
    ]

    SIDECAR_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(SIDECAR_PATH, "w") as f:
        yaml.safe_dump({"slots": entries}, f, sort_keys=False)
    print(f"\n  ✓ Sidecar data written: {SIDECAR_PATH}")
    print("    (list.html doesn't read this file yet -- data/starmaps.yaml still")
    print("     drives the live page until that template step lands.)")


# ── Tier 1: evergreen monthly reference charts (no planets) ───────────────────

def generate_evergreen(year=None, output_dir=None, quality=None, resolution=None):
    """12 anchor dates (the 15th of each month), rendered WITHOUT planets --
    stars/constellations/Milky Way are effectively the same every year for a
    fixed date+time, so this only needs to run once, or very rarely (e.g. a
    star-catalog update). Saves a light JPG (BLUE_MEDIUM, print-friendly) and
    a dark JPG (EVERGREEN_DARK_EXTENSION, web/dark-mode) per month -- each
    rendered directly by starplot with its own real color style, not derived
    by inverting the other. See the EVERGREEN_DARK_EXTENSION comment above:
    RGB-inverting a light blue Milky Way tint produces a muddy brown, so the
    dark variant gets its own purpose-built render instead."""
    output_dir = Path(output_dir) if output_dir else OUTPUT
    resolution = resolution or CHART_RESOLUTION
    evergreen_dir = output_dir / "evergreen"
    evergreen_dir.mkdir(parents=True, exist_ok=True)
    _ensure_ephemeris_available()
    _ensure_assets_available()

    year = year or date_cls.today().year
    light_style = PlotStyle().extend(extensions.BLUE_MEDIUM, _weekly_style_overrides())
    # constellation_color=None: keep BLUE_DARK's own built-in line color
    # (#b4c2d0) instead of clobbering it with the light style's #2a5ba8,
    # which has almost no contrast against a dark navy background.
    dark_style = PlotStyle().extend(EVERGREEN_DARK_EXTENSION,
                                     _weekly_style_overrides(constellation_color=None))

    for month in range(1, 13):
        anchor_date = date_cls(year, month, EVERGREEN_MONTH_DAY)
        dt_utc, dt_local, date_str, time_str = _labels_for(anchor_date)
        month_slug = anchor_date.strftime("%m-%b").lower()
        label = f"Sky on/near: {date_str}, {time_str} – North Adams, MA"

        print(f"  {month_slug}: {date_str}, {time_str} ({dt_utc.strftime('%H:%M UTC')})")

        observer = Observer(lat=LAT, lon=LON, dt=dt_utc)

        # Light (print-friendly) variant
        chart, bg_color = _render_chart(observer, light_style, resolution=resolution,
                                         include_planets=False)
        canvas = _composite_chart(chart, bg_color, title=ORG_NAME, label=label)
        light_path = evergreen_dir / f"starmap-{month_slug}-light.jpg"
        _save_jpeg(canvas, light_path, quality=quality)
        print(f"    ✓ light : {light_path.name}  ({light_path.stat().st_size / 1024:.0f} KB)")

        # Dark (web/dark-mode) variant -- separate real render, see docstring
        dark_chart, dark_bg_color = _render_chart(observer, dark_style, resolution=resolution,
                                                   include_planets=False)
        dark_canvas = _composite_chart(dark_chart, dark_bg_color, title=ORG_NAME, label=label)
        dark_path = evergreen_dir / f"starmap-{month_slug}-dark.jpg"
        _save_jpeg(dark_canvas, dark_path, quality=quality)
        print(f"    ✓ dark  : {dark_path.name}  ({dark_path.stat().st_size / 1024:.0f} KB)")


# ── CLI ────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Generate NBAS starmaps (tier 1 evergreen, tier 2/3 slots, or legacy ad hoc)",
        epilog="Examples:\n"
               "  generate.py                      # ad hoc: next Wednesday, JPG only\n"
               "  generate.py 2026-08-26           # ad hoc: specific date (single map)\n"
               "  generate.py --weeks 4            # ad hoc: next 4 Wednesdays from today\n"
               "  generate.py 2026-08-26 --weeks 12  # ad hoc: 12 weeks starting 2026-08-26\n"
               "  generate.py --pdf                # ad hoc: also emit a print PDF\n"
               "  generate.py --evergreen          # tier 1: all 12 monthly anchors\n"
               "  generate.py --slots              # tier 2/3: current + rolling buffer\n"
               "  generate.py --slots --weeks 6 --pdf  # 6-slot buffer, PDF for current only\n"
               "  generate.py --slots --output ../static/starmap  # write straight into static/\n",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("date",    nargs="?",
                        help="Ad hoc start date YYYY-MM-DD (default: next Wednesday)")
    parser.add_argument("--weeks", type=int, metavar="N",
                        help="Ad hoc: consecutive Wednesdays. With --slots: slot count.")
    parser.add_argument("--yaml", action="store_true",
                        help="Print starmaps.yaml entries to stdout instead of generating images")
    parser.add_argument("--pdf", action="store_true",
                        help="Also generate a print PDF (ad hoc: for that date; "
                             "--slots: for the current slot only)")
    parser.add_argument("--evergreen", action="store_true",
                        help="Generate tier-1 evergreen monthly reference charts (light+dark)")
    parser.add_argument("--slots", action="store_true",
                        help="Generate tier-2 current + tier-3 rolling buffer, update sidecar")
    parser.add_argument("--output", "-o", metavar="DIR", default=None,
                        help="Directory to write images into (default: ./output). "
                             "E.g. --output ../static/starmap to write straight into "
                             "static/ (evergreen mode will use DIR/evergreen).")
    parser.add_argument("--quality", type=int, metavar="N", default=None,
                        help=f"JPEG quality 1-95 (default: {JPEG_QUALITY}). "
                             "Lower = smaller files; try 80-85 to shrink further.")
    parser.add_argument("--resolution", type=int, metavar="PX", default=None,
                        help=f"Chart render resolution in px (default: {CHART_RESOLUTION}). "
                             "Lower = smaller files but less print sharpness.")
    args = parser.parse_args()

    output_dir = Path(args.output) if args.output else OUTPUT

    if args.evergreen:
        print("Generating tier-1 evergreen monthly reference charts …")
        generate_evergreen(output_dir=output_dir, quality=args.quality, resolution=args.resolution)
        print("\nDone.")
        return

    if args.slots:
        weeks = args.weeks or TIER3_SLOT_COUNT
        print(f"Generating tier-2/3 slots (current + {weeks - 1} upcoming) …")
        generate_slots(weeks=weeks, make_pdf=args.pdf, output_dir=output_dir,
                        quality=args.quality, resolution=args.resolution)
        print("\nDone.")
        return

    # Legacy ad hoc mode
    start = datetime.strptime(args.date, "%Y-%m-%d").date() if args.date else next_wednesday()

    if args.weeks:
        dates = []
        d = start
        for _ in range(args.weeks):
            dates.append(d)
            d = next_wednesday(d)
    else:
        dates = [start]

    # --yaml mode: just print YAML entries, no image generation
    if args.yaml:
        print("maps:")
        for date in dates:
            dt_utc   = chart_datetime(date)
            dt_local = dt_utc.astimezone(TIMEZONE)
            print(f'  - date: "{date}"')
            print(f'    label: "{dt_local.strftime("%-d %b %Y")}"')
            print(f'    time:  "{dt_local.strftime("%-I:%M %p %Z")}"')
        return

    for date in dates:
        print(f"\nGenerating starmap for {date} …")
        generate(date, make_pdf=args.pdf, output_dir=output_dir,
                 quality=args.quality, resolution=args.resolution)

    print("\nDone.")


if __name__ == "__main__":
    main()
