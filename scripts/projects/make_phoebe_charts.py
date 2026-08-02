#!/usr/bin/env python3
"""
Generate biweekly finder charts for Phoebe (or any slow-drifting faint
target) from a JPL Horizons ephemeris text export.

Charts are keyed to 1st-15th / 16th-end calendar chunks (for filenames and
gallery ordering), but each chart's actual plotted date range is widened
past that nominal chunk -- 6 days earlier, 5 days later, clipped to the
ephemeris's actual date range -- so consecutive charts overlap by about a
week and a half. That overlap gives the reader a few days of already-seen
sky to reorient by when they move to the next chart in the gallery, rather
than every chart starting from an unfamiliar field.

Fetches a deep background star field (DSS2 by default -- limiting mag
~20-21, comfortably past the mag 16-17 range you need) centered on each
window from SkyView, and overplots the target's daily positions with a few
date labels.

Install:
    pip install astroquery astropy matplotlib numpy

Usage:
    python make_phoebe_charts.py horizons_results-phoebe.txt

Output:
    phoebe_202609a.png, phoebe_202609b.png, ... one PNG per nominal period,
    ready to drop into the gallery shortcode.
"""

import argparse
import re
import sys
from pathlib import Path
from datetime import datetime, timedelta
import calendar

import numpy as np
import matplotlib.pyplot as plt
from astropy.coordinates import SkyCoord, Angle
from astropy.wcs import WCS
import astropy.units as u
from astroquery.skyview import SkyView

# Matches lines like:
#  2026-Sep-01 00:00     00 51 59.38 +02 38 50.1   16.381   8.820  1134.113/*
LINE_RE = re.compile(
    r"^\s*(\d{4}-\w{3}-\d{2})\s+\d{2}:\d{2}\s+"
    r"(\d{2}\s\d{2}\s[\d.]+)\s+"
    r"([+-]\d{2}\s\d{2}\s[\d.]+)\s+"
    r"([\d.]+)\s+([\d.]+)\s+([\d.]+)/"
)

# Site palette (from 01-variables.css) for the chrome (title/axes/grid).
# The path/marker color is deliberately NOT the site's gold accent: these
# charts render on a near-white DSS background (gray_r), where pale gold
# has almost no contrast. Red is also out -- it vanishes under a red
# flashlight, which defeats the point for anyone using this at the eyepiece.
# A dark, saturated blue reads clearly against white or black stars, and
# survives red-light viewing (it doesn't get cancelled out the way red does).
DEEP_BG = "#0d1421"
PATH_COLOR = "#1a56db"
TEXT_MAIN = "#d1d1d1"


def parse_horizons(path):
    rows = []
    for line in Path(path).read_text().splitlines():
        m = LINE_RE.match(line)
        if not m:
            continue
        date_s, ra_s, dec_s, mag_s, sbrt_s, sep_s = m.groups()
        rows.append(dict(
            date=datetime.strptime(date_s, "%Y-%b-%d"),
            ra=Angle(ra_s, unit=u.hourangle).deg,
            dec=Angle(dec_s, unit=u.deg).deg,
            mag=float(mag_s),
            sep_arcsec=float(sep_s),
        ))
    if not rows:
        raise ValueError(
            f"No rows parsed from {path} -- check it's the raw $$SOE...$$EOE "
            "Horizons text table, not a reformatted copy."
        )
    return rows


def biweekly_periods(rows):
    """1st-15th / 16th-end chunks, matching the table built by hand.

    Used only to enumerate which nominal (year, month, first_half) periods
    exist -- the actual per-chart row selection comes from
    extended_window(), not from the groupings returned here.
    """
    periods = {}
    for r in rows:
        key = (r["date"].year, r["date"].month, r["date"].day <= 15)
        periods.setdefault(key, []).append(r)
    # sort by (year, month, first-half-before-second-half) -- plain tuple
    # sort would put False (second half) before True (first half) within
    # the same month, since False < True.
    return dict(sorted(periods.items(), key=lambda kv: (kv[0][0], kv[0][1], not kv[0][2])))


def nominal_period_bounds(year, month, first_half):
    """Calendar start/end of the strict 1st-15th / 16th-end chunk."""
    if first_half:
        return datetime(year, month, 1), datetime(year, month, 15)
    last_day = calendar.monthrange(year, month)[1]
    return datetime(year, month, 16), datetime(year, month, last_day)


def extended_window(rows, year, month, first_half, before_days=6, after_days=5):
    """Rows for one chart: the nominal chunk widened by before_days/after_days
    on each side, clipped to the ephemeris's actual date range, so
    consecutive charts overlap instead of butting up against a hard
    boundary."""
    nominal_start, nominal_end = nominal_period_bounds(year, month, first_half)
    lo = min(r["date"] for r in rows)
    hi = max(r["date"] for r in rows)
    win_start = max(lo, nominal_start - timedelta(days=before_days))
    win_end = min(hi, nominal_end + timedelta(days=after_days))
    return [r for r in rows if win_start <= r["date"] <= win_end]


def period_label(period_rows):
    first, last = period_rows[0]["date"], period_rows[-1]["date"]
    if first.month == last.month:
        return f"{first.strftime('%b %-d')}–{last.strftime('%-d, %Y')}"
    return f"{first.strftime('%b %-d')}–{last.strftime('%b %-d, %Y')}"


# NOTE on plate-boundary artifacts (Sep 1-15 chart): DSS2 is built from
# ~6-degree Schmidt plates; where SkyView has to stitch two of them inside
# one cutout it tries to zero out the offset between them ("edge reduction"),
# but that only matches a constant, not a slope -- so if one plate has a
# real or instrumental intensity gradient near the seam, the join can show
# up as a visible band/wedge. Documented here:
# https://skyview.gsfc.nasa.gov/blog/index.php/2009/11/05/features-in-the-gallery-image-boundaries/index.html
# It's a DSS mosaic artifact, not a bug in this script. The plate grid is
# shared across DSS2 Red/Blue (same tiling scheme, different photographic
# emulsion), so switching bands alone won't move a seam that falls in this
# patch of sky -- confirmed by testing (Sep 1-15 showed the same wedge in
# both). Two things worth trying instead, in order:
#   1. A genuinely different plate set with its own tiling, e.g. plain
#      "DSS" (first-generation DSS1) -- its plates don't share DSS2's
#      boundaries, so a DSS2 seam may simply not exist in DSS1.
#   2. Nudge the cutout center off the seam with --ra-offset/--dec-offset
#      (degrees). The seam is a roughly straight line in a specific spot;
#      shifting the center perpendicular to it by even a few tenths of a
#      degree can move the whole cutout onto one plate. pad_factor leaves
#      headroom so Phoebe's path should still fit in frame after a small
#      offset -- check the printed field size vs. offset if it doesn't.
#   python make_phoebe_charts.py horizons_results-phoebe.txt \
#       --period 202609a --survey "DSS"
#   python make_phoebe_charts.py horizons_results-phoebe.txt \
#       --period 202609a --dec-offset 0.3
# IMPORTANT on survey names: SkyView's documentation page titles (e.g.
# "Original Digitized Sky Survey") are NOT what astroquery validates
# against -- astroquery.skyview scrapes the exact option text out of the
# live query form's <select name="survey"> dropdown, which uses shorter
# strings. Confirmed valid short names (from astroquery's own source/
# docstring and your own successful runs): "DSS2 Red", "DSS2 Blue", "DSS"
# (= first-generation DSS1). "DSS1 Red"/"DSS1 Blue" by analogy with the
# DSS2 pair are NOT independently confirmed -- if you want a specific DSS1
# band rather than plain "DSS", check list_surveys() output first:
#   python -c "from astroquery.skyview import SkyView; SkyView.list_surveys()"
# There is no Pan-STARRS/PS1 survey in SkyView at all -- that's a separate
# service and isn't reachable through this script's --survey flag.
def make_chart(period_rows, label, out_path, survey="DSS2 Red",
                pad_factor=1.6, min_field_deg=0.5, pixels=1200,
                ra_offset=0.0, dec_offset=0.0):
    ras = [r["ra"] for r in period_rows]
    decs = [r["dec"] for r in period_rows]
    cra, cdec = (max(ras) + min(ras)) / 2, (max(decs) + min(decs)) / 2
    cra += ra_offset
    cdec += dec_offset
    ra_span = max(ras) - min(ras)
    dec_span = max(decs) - min(decs)
    field_deg = max(max(ra_span, dec_span) * pad_factor + 0.25, min_field_deg)

    # SkyCoord defaults to ICRS, which is what we want here: Horizons'
    # ephemeris columns are "astrometric RA/DEC ... ICRF", and SkyView's
    # DSS2 cutouts carry J2000-equinox WCS -- ICRS and J2000/FK5 agree to
    # sub-arcsecond precision, so no precession correction is needed between
    # the two. (Horizons docs: https://ssd.jpl.nasa.gov/horizons/manual.html
    # -- "astrometric" = ICRF/J2000, light-time+aberration corrected, NOT
    # precessed to date. SkyView docs confirm J2000 is its default equinox.)
    center = SkyCoord(ra=cra * u.deg, dec=cdec * u.deg)
    imgs = SkyView.get_images(
        position=center, survey=[survey],
        width=field_deg * u.deg, height=field_deg * u.deg,
        pixels=(pixels, pixels),
    )
    hdu = imgs[0][0]
    wcs = WCS(hdu.header)
    data = hdu.data

    fig = plt.figure(figsize=(8, 8), facecolor=DEEP_BG)
    ax = fig.add_subplot(111, projection=wcs)
    ax.imshow(
        data, cmap="gray_r", origin="lower",
        vmin=np.percentile(data, 5), vmax=np.percentile(data, 99.5),
    )

    path = SkyCoord(ra=np.array(ras) * u.deg, dec=np.array(decs) * u.deg)
    ax.plot(
        path.ra.deg, path.dec.deg, transform=ax.get_transform("world"),
        color=PATH_COLOR, lw=1.5, marker="o", ms=3, mfc=PATH_COLOR, mec="none",
    )

    # Label start, midpoint, end so the direction/pace of drift is legible
    for i in (0, len(period_rows) // 2, -1):
        r = period_rows[i]
        ax.text(
            r["ra"], r["dec"], "  " + r["date"].strftime("%b %-d"),
            transform=ax.get_transform("world"), color=PATH_COLOR, fontsize=9,
        )

    ax.set_title(f"Phoebe — {label}", color=TEXT_MAIN, fontsize=13)
    ax.coords.grid(color=TEXT_MAIN, alpha=0.15)
    ax.coords[0].set_axislabel("RA", color=TEXT_MAIN)
    ax.coords[1].set_axislabel("Dec", color=TEXT_MAIN)
    ax.tick_params(colors=TEXT_MAIN)
    for spine in ax.spines.values():
        spine.set_color(TEXT_MAIN)

    fig.savefig(out_path, dpi=150, facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"  field {field_deg:.2f}°, center RA {cra:.3f} Dec {cdec:.3f} -> {out_path}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("horizons_file")
    ap.add_argument(
        "--survey", default="DSS2 Red",
        help="SkyView survey name -- must match the exact option text in "
             "SkyView's own query form, not its documentation page titles. "
             "Confirmed working: 'DSS2 Red', 'DSS2 Blue', 'DSS' "
             "(first-gen DSS1). Run "
             "`python -c \"from astroquery.skyview import SkyView; "
             "SkyView.list_surveys()\"` to see the full live list if in "
             "doubt. Try a different one if a cutout comes back with a "
             "plate-boundary artifact -- see note above make_chart(). "
             "(No Pan-STARRS here -- SkyView doesn't host it; that'd need "
             "a separate fetch path.) Default: 'DSS2 Red'.",
    )
    ap.add_argument(
        "--period", default=None,
        help="Only build one period, e.g. '202609a' or '202611a' "
             "(YYYYMM + a/b for 1st-15th / 16th-end). Handy for re-testing "
             "a single problem chart without rebuilding all eight.",
    )
    ap.add_argument(
        "--ra-offset", type=float, default=0.0,
        help="Shift the cutout center in RA (degrees) -- use with --period "
             "to nudge a cutout off a DSS plate-boundary seam.",
    )
    ap.add_argument(
        "--dec-offset", type=float, default=0.0,
        help="Shift the cutout center in Dec (degrees) -- same idea as "
             "--ra-offset.",
    )
    args = ap.parse_args()

    rows = parse_horizons(args.horizons_file)
    print(f"parsed {len(rows)} rows, {rows[0]['date'].date()} to {rows[-1]['date'].date()}")
    print(f"mag range: {min(r['mag'] for r in rows):.2f}"
          f"-{max(r['mag'] for r in rows):.2f}")

    for (year, month, first_half) in biweekly_periods(rows).keys():
        suffix = "a" if first_half else "b"
        key = f"{year}{month:02d}{suffix}"
        if args.period and key != args.period:
            continue
        window_rows = extended_window(rows, year, month, first_half)
        out = f"phoebe_{key}.png"
        label = period_label(window_rows)
        print(f"building {out} ({label}) using survey={args.survey!r} "
              f"offset=({args.ra_offset:+.2f}, {args.dec_offset:+.2f}) ...")
        make_chart(window_rows, label, out, survey=args.survey,
                   ra_offset=args.ra_offset, dec_offset=args.dec_offset)

    print("done.")
