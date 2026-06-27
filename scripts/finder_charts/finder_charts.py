#!/usr/bin/env python3
"""
NBAS Finder Chart Generator
=============================
Generates PNG + PDF finder charts.  Each field can contain one or more
target objects sharing a single frame.

Overlay style is driven by OBJECT TYPE:

    open_cluster        yellow circle, DASHED outline
    globular_cluster    yellow circle, SOLID outline, bisected with "+"
    emission_nebula     green rect, solid outline, rotated to orientation
    reflection_nebula   green rect, solid outline, rotated to orientation
    dark_nebula         grey rect, solid outline, rotated to orientation
    galaxy              red ellipse, solid outline, rotated to orientation
    galaxy_barred       purple ellipse, solid outline, rotated to orientation
    galaxy_dwarf_irr    blue ellipse, solid outline, rotated to orientation
    planetary_nebula    cyan, two concentric circles, NO outline

Usage
-----
  # Resolve objects by name via SIMBAD — one chart, all on one field:
  python finder_charts.py --objects "NGC 6946"
  python finder_charts.py --objects "NGC 6520" "Barnard 86" --chart-name inkspot
  python finder_charts.py --objects "M 57" --fov 1.5 --mag-limit 13

  # Run the hard-coded FIELDS list (legacy mode):
  python finder_charts.py --fields

  # Geometry self-test (no network or starplot needed):
  python finder_charts.py --selftest

--objects options (all optional):
  --chart-name STEM     output filename stem (default: slug of first object)
  --title TEXT          chart title (default: object names joined with " & ")
  --info TEXT           extra text appended to subtitle
  --fov DEG             explicit FOV in degrees (default: auto from object sizes)
  --mag-limit MAG       star fetch depth (default: 12.0)
  --no-stars            skip Vizier star fetch
  --output-dir DIR      where to write output (default: same dir as this script)
  --projection {Mercator,StereoNorth}  (default: auto; StereoNorth if dec > 75)

Assets (same directory as this script):
  nbas-logo.svg
  nbas-qrcode.svg

Requirements:
  pip install starplot astroquery astropy pandas pillow reportlab cairosvg \\
      numpy --break-system-packages
"""

import argparse
import io
import math
import os
import sys
import warnings

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageDraw

warnings.filterwarnings("ignore")

HERE     = os.path.dirname(os.path.abspath(__file__))
LOGO_PNG = os.path.join(HERE, "nbas-logo.png")
QR_SVG   = os.path.join(HERE, "nbas-qrcode.svg")

ORG_NAME = "Northern Berkshire Astronomical Society"
SITE_URL = "nbasastro.org"
TAGLINE  = "Whatever your experience, you belong under our skies."


# ─────────────────────────────────────────────────────────────────────────────
#  Object-type style registry
# ─────────────────────────────────────────────────────────────────────────────

OBJECT_STYLES = {
    "open_cluster":      {"shape": "circle",       "color": "#FFD700", "dashed": True},
    "globular_cluster":  {"shape": "circle_plus",  "color": "#FFD700", "dashed": False},
    "emission_nebula":   {"shape": "rect",         "color": "#33CC55", "dashed": False},
    "reflection_nebula": {"shape": "rect",         "color": "#33CC55", "dashed": False},
    "dark_nebula":       {"shape": "rect",         "color": "#888888", "dashed": False},
    "galaxy":            {"shape": "ellipse",      "color": "#DD3333", "dashed": False},
    "galaxy_barred":     {"shape": "ellipse",      "color": "#9933CC", "dashed": False},
    "galaxy_dwarf_irr":  {"shape": "ellipse",      "color": "#3366DD", "dashed": False},
    "planetary_nebula":  {"shape": "double_circle","color": "#33CCCC", "dashed": False},
}


def style_for(object_type: str) -> dict:
    style = OBJECT_STYLES.get(object_type)
    if style is None:
        print(f"   WARNING: unknown object_type '{object_type}', "
              f"falling back to open_cluster styling")
        style = OBJECT_STYLES["open_cluster"]
    return style


# ─────────────────────────────────────────────────────────────────────────────
#  SIMBAD resolver
# ─────────────────────────────────────────────────────────────────────────────

# Maps SIMBAD otype codes → OBJECT_STYLES keys.
# Full type table: https://simbad.cds.unistra.fr/guide/otypes.htx
SIMBAD_OTYPE_MAP = {
    "OpC": "open_cluster",    "OC?": "open_cluster",    "Cl*": "open_cluster",
    "GlC": "globular_cluster","GlB": "globular_cluster","GC?": "globular_cluster",
    "PN":  "planetary_nebula","PNe": "planetary_nebula","pA*": "planetary_nebula",
    "HII": "emission_nebula", "GNe": "emission_nebula", "EmN": "emission_nebula",
    "RNe": "reflection_nebula",
    "DNe": "dark_nebula",     "DkN": "dark_nebula",     "MoC": "dark_nebula",
    "G":   "galaxy",  "GiG": "galaxy", "GiC": "galaxy", "GiP": "galaxy",
    "AGN": "galaxy",  "SyG": "galaxy", "Sy1": "galaxy", "Sy2": "galaxy",
    "QSO": "galaxy",  "H2G": "galaxy", "SBG": "galaxy", "bCG": "galaxy",
    "EmG": "galaxy",  "LSB": "galaxy", "BiC": "galaxy", "BLL": "galaxy",
    "LIN": "galaxy",  "cD":  "galaxy",
}


def otype_to_object_type(otype: str) -> str:
    if not otype or str(otype).strip() in ("", "--", "nan"):
        return "open_cluster"
    ot = str(otype).strip()
    if ot in SIMBAD_OTYPE_MAP:
        return SIMBAD_OTYPE_MAP[ot]
    for key, val in SIMBAD_OTYPE_MAP.items():
        if ot.startswith(key):
            return val
    print(f"   WARNING: unknown SIMBAD otype '{ot}', defaulting to open_cluster style")
    return "open_cluster"


def _safe_float(val, default=None):
    try:
        f = float(val)
        return default if (math.isnan(f) or math.isinf(f)) else f
    except (TypeError, ValueError):
        return default


def resolve_simbad(names: list) -> list:
    """Query SIMBAD for each name; return target dicts for use in a field."""
    from astroquery.simbad import Simbad

    targets = []
    for name in names:
        print(f"   Querying SIMBAD: {name!r} …")
        tap_ok = False
        ra_deg = dec_deg = otype = None
        maj = mino = None
        pa = 0.0

        # Modern TAP interface (astroquery >= 0.4.7, current SIMBAD schema).
        # Uses correct column names: galdim_majaxis / galdim_minaxis / galdim_angle.
        try:
            escaped = name.replace("'", "''")
            result = Simbad.query_tap(
                f"SELECT TOP 1 basic.ra, basic.dec, basic.otype, "
                f"basic.galdim_majaxis, basic.galdim_minaxis, basic.galdim_angle "
                f"FROM basic JOIN ident ON ident.oidref = basic.oid "
                f"WHERE ident.id = '{escaped}'"
            )
            if result is not None and len(result) > 0:
                row     = result[0]
                ra_deg  = float(row["ra"])
                dec_deg = float(row["dec"])
                otype   = str(row["otype"] or "").strip()
                maj     = _safe_float(row["galdim_majaxis"])
                mino    = _safe_float(row["galdim_minaxis"])
                pa      = _safe_float(row["galdim_angle"], default=0.0)
                tap_ok  = True
            else:
                print(f"   WARNING: no SIMBAD match for {name!r}, skipping")
                continue
        except Exception as exc:
            print(f"   WARNING: SIMBAD TAP query failed for {name!r}: {exc}")

        # Legacy fallback (older astroquery — only RA/Dec/otype, no dimensions).
        if not tap_ok:
            try:
                from astropy.coordinates import SkyCoord
                import astropy.units as u
                s = Simbad()
                s.add_votable_fields("otype")
                leg = s.query_object(name)
                if leg is None or len(leg) == 0:
                    print(f"   WARNING: no SIMBAD match for {name!r}, skipping")
                    continue
                row     = leg[0]
                coord   = SkyCoord(row["RA"], row["DEC"],
                                   unit=(u.hourangle, u.deg), frame="icrs")
                ra_deg  = float(coord.ra.deg)
                dec_deg = float(coord.dec.deg)
                otype   = str(row.get("OTYPE", "") or "").strip()
            except Exception as exc2:
                print(f"   WARNING: SIMBAD legacy query also failed for {name!r}: {exc2}")
                continue

        obj_type = otype_to_object_type(otype)

        shape = style_for(obj_type)["shape"]
        t = {"name": name, "label": name,
             "ra": ra_deg, "dec": dec_deg, "object_type": obj_type}

        if shape in ("circle", "circle_plus"):
            t["size_amin"] = maj or 5.0
        elif shape in ("rect", "ellipse"):
            t["width_amin"]  = maj  or 10.0
            t["height_amin"] = mino or (maj * 0.5 if maj else 5.0)
            t["angle_deg"]   = pa   or 0.0
        else:  # double_circle
            t["width_amin"]  = maj or 3.0
            t["height_amin"] = maj or 3.0
            t["angle_deg"]   = 0.0

        size_val = t.get("size_amin") or t.get("width_amin")
        print(f"   → RA {ra_deg:.4f}°  Dec {dec_deg:.4f}°  "
              f"otype={otype!r} → {obj_type}  "
              f"size≈{size_val:.1f}′" if size_val else "  size unknown")
        targets.append(t)

    return targets


# ─────────────────────────────────────────────────────────────────────────────
#  Hard-coded field definitions  (used by --fields)
# ─────────────────────────────────────────────────────────────────────────────

FIELDS = [
    {
        "chart_name": "inkspot",
        "title": 'NGC 6520 ("Dead Man\'s Chest") & Barnard 86 ("the Ink Spot")',
        "info": "Sgr · ~6 kly · cluster ~150 Myr · B86 a candidate birth cloud",
        "fov_deg": None,
        "mag_limit": 12.0,
        "fetch_stars": True,
        "targets": [
            {
                "name": 'NGC 6520 ("Dead Man\'s Chest")',
                "label": "NGC 6520",
                "ra": 270.8546, "dec": -27.8911,
                "object_type": "open_cluster",
                "size_amin": 6.0,
            },
            {
                "name": 'Barnard 86 ("the Ink Spot")',
                "label": "B 86",
                "ra": 270.708, "dec": -27.850,
                "object_type": "dark_nebula",
                "width_amin": 5.0, "height_amin": 3.5, "angle_deg": 35.0,
            },
        ],
    },
]

MAG_LIMIT   = 12.0
FOV_PADDING = 3.0   # finder charts need plenty of context around targets
FOV_MIN_DEG = 2.0   # never show less than 2° so observers can navigate
SCALE       = 2048 / 4096


# ─────────────────────────────────────────────────────────────────────────────
#  Helpers
# ─────────────────────────────────────────────────────────────────────────────

def marker_size(mag: float) -> float:
    # Scale: mag 1 ≈ 28, mag 6 ≈ 8, mag 10 ≈ 3, mag 12 ≈ 2
    return 30.0 * (10.0 ** (-0.12 * mag))


def slug(name: str) -> str:
    out = name.lower()
    for ch in ["&", "(", ")", '"']:
        out = out.replace(ch, "")
    return out.strip().replace(" ", "_")


def target_radius_deg(t: dict) -> float:
    shape = style_for(t["object_type"])["shape"]
    if shape in ("circle", "circle_plus"):
        return t["size_amin"] / 60.0 / 2.0
    if shape in ("rect", "ellipse"):
        return max(t["width_amin"], t["height_amin"]) / 60.0 / 2.0
    if shape == "double_circle":
        return t["height_amin"] / 60.0 / 2.0
    return 0.0


def compute_field_center_and_fov(field: dict):
    targets = field["targets"]
    decs = [t["dec"] for t in targets]
    ras  = [t["ra"]  for t in targets]
    dec0 = sum(decs) / len(decs)
    ra0  = sum(ras)  / len(ras)
    cosd = max(math.cos(math.radians(dec0)), 0.05)

    if field.get("fov_deg") is not None:
        return ra0, dec0, field["fov_deg"]

    max_half = 0.0
    for t in targets:
        dra  = (t["ra"]  - ra0) * cosd
        ddec =  t["dec"] - dec0
        max_half = max(max_half,
                       math.hypot(dra, ddec) + target_radius_deg(t))

    return ra0, dec0, max(FOV_MIN_DEG, 2.0 * max_half * FOV_PADDING)


def fetch_stars(ra_deg, dec_deg, radius_deg, mag_limit) -> pd.DataFrame:
    from astroquery.vizier import Vizier
    from astropy.coordinates import SkyCoord
    import astropy.units as u

    v = Vizier(columns=["RAJ2000", "DEJ2000", "Vmag"],
               column_filters={"Vmag": f"<{mag_limit}"}, row_limit=-1)
    coord = SkyCoord(ra=ra_deg, dec=dec_deg, unit="deg", frame="icrs")
    try:
        result = v.query_region(coord, radius=radius_deg * u.deg,
                                catalog="I/297/out")
    except Exception as exc:
        print(f"  WARNING: Vizier query failed ({exc})")
        return pd.DataFrame(columns=["ra", "dec", "magnitude"])
    if not result:
        print("  WARNING: Vizier returned no results.")
        return pd.DataFrame(columns=["ra", "dec", "magnitude"])
    df = (result[0].to_pandas()
          .rename(columns={"RAJ2000": "ra", "DEJ2000": "dec", "Vmag": "magnitude"})
          .dropna(subset=["magnitude"]))
    df = df[df["magnitude"].between(1.0, mag_limit)].copy()
    for col in ("ra", "dec", "magnitude"):
        df[col] = df[col].astype(float)
    return df[["ra", "dec", "magnitude"]].reset_index(drop=True)


def ra_fmt(r: float) -> str:
    h = int(r);  m = int(round((r - h) * 60))
    if m == 60: h += 1; m = 0
    return f"{h}h {m:02d}m"


def dec_fmt(d: float) -> str:
    sign = "+" if d >= 0 else "−";  d = abs(d)
    deg = int(d);  am = int(round((d - deg) * 60))
    if am == 60: deg += 1; am = 0
    return f"{sign}{deg}° {am:02d}′"


def _hex_to_rgb(h: str):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


# ─────────────────────────────────────────────────────────────────────────────
#  PIL overlays
# ─────────────────────────────────────────────────────────────────────────────

def _blend(img_path, mask_layer):
    img = Image.open(img_path).convert("RGB")
    blended = np.clip(
        np.array(img, dtype=np.float32) *
        np.array(mask_layer, dtype=np.float32) / 255.0,
        0, 255).astype(np.uint8)
    Image.fromarray(blended).save(img_path)


def _dashed(draw, pts, color, n_segs=32):
    n = len(pts); seg = max(1, n // n_segs)
    for i in range(0, n - 1, seg):
        if (i // seg) % 2 == 0:
            chunk = pts[i:min(i + seg + 1, n)]
            if len(chunk) >= 2:
                draw.line(chunk, fill=color, width=6)


def _solid(draw, pts, color):
    draw.line(pts, fill=color, width=6)


def _circle_pts(cx, cy, r, n=200):
    return [(cx + r * math.cos(2*math.pi*i/n),
             cy + r * math.sin(2*math.pi*i/n)) for i in range(n+1)]


def _ellipse_pts(cx, cy, w, h, a, n=200):
    hw, hh = w/2, h/2
    ca, sa = math.cos(a), math.sin(a)
    pts = []
    for i in range(n+1):
        t = 2*math.pi*i/n
        x, y = hw*math.cos(t), -hh*math.sin(t)
        pts.append((cx + x*ca - y*sa, cy + x*sa + y*ca))
    return pts


def _rect_pts(cx, cy, w, h, a, nps=50):
    hw, hh = w/2, h/2
    corners = [(-hw,-hh),(hw,-hh),(hw,hh),(-hw,hh),(-hw,-hh)]
    ca, sa = math.cos(a), math.sin(a)
    pts = []
    for k in range(len(corners)-1):
        x0,y0 = corners[k]; x1,y1 = corners[k+1]
        for t in range(nps+1):
            f = t/nps
            x,y = x0+(x1-x0)*f, y0+(y1-y0)*f
            pts.append((cx + x*ca - y*sa, cy + x*sa + y*ca))
    return pts


def _selftest_position_angle_convention():
    EPS = 1e-4

    def tip(a):
        return min(_rect_pts(0,0,EPS,40,-math.radians(a),1), key=lambda p:p[1])

    t0, t90 = tip(0), tip(90)
    assert abs(t0[0]) < 1e-3 and t0[1] < -1,  f"PA=0 should point up, got {t0}"
    assert t90[0] < -1 and abs(t90[1]) < 1e-3, f"PA=90 should point left, got {t90}"

    def etip(a):
        return max(_ellipse_pts(0,0,EPS,40,-math.radians(a),400),
                   key=lambda p: math.hypot(*p))

    e0, e90 = etip(0), etip(90)
    assert abs(e0[0]) < 1e-3 and e0[1] < -1,  f"ellipse PA=0 up, got {e0}"
    assert e90[0] < -1 and abs(e90[1]) < 1e-3, f"ellipse PA=90 left, got {e90}"

    print("Self-test passed: PA=0 → north/up, PA=90 → east/left (rect + ellipse).")


def _ax_to_px(img_path, ax_pos):
    img = Image.open(img_path)
    W, H = img.size
    return (ax_pos.x0*W, ax_pos.x1*W,
            (1-ax_pos.y1)*H, (1-ax_pos.y0)*H,
            img)


def _center_px(ax_pos, img_path, cx_ax, cy_ax):
    al, ar, at, ab, img = _ax_to_px(img_path, ax_pos)
    aw, ah = ar-al, ab-at
    return al + cx_ax*aw, ab - cy_ax*ah, ah, img.size


def add_overlay_circle(img_path, ax_pos, cx_ax, cy_ax,
                       r_ax, color, dashed, bisect=False):
    al, ar, at, ab, img = _ax_to_px(img_path, ax_pos)
    W, H = img.size; aw, ah = ar-al, ab-at
    cx = al + cx_ax*aw; cy = ab - cy_ax*ah; r = r_ax*ah
    rgb = _hex_to_rgb(color)
    mask = Image.new("RGB", (W,H), (255,255,255))
    ImageDraw.Draw(mask).ellipse([cx-r,cy-r,cx+r,cy+r], fill=rgb)
    _blend(img_path, mask)
    res = Image.open(img_path); d = ImageDraw.Draw(res)
    pts = _circle_pts(cx, cy, r)
    if bisect:
        _solid(d, pts, (0,0,0))
        d.line([(cx-r,cy),(cx+r,cy)], fill=(0,0,0), width=4)
        d.line([(cx,cy-r),(cx,cy+r)], fill=(0,0,0), width=4)
    elif dashed: _dashed(d, pts, (0,0,0))
    else:        _solid(d, pts, (0,0,0))
    res.save(img_path)


def add_overlay_double_circle(img_path, ax_pos, cx_ax, cy_ax, r_ax, color):
    al, ar, at, ab, img = _ax_to_px(img_path, ax_pos)
    W, H = img.size; aw, ah = ar-al, ab-at
    cx = al+cx_ax*aw; cy = ab-cy_ax*ah
    ro = r_ax*ah; ri = ro*0.55; rgb = _hex_to_rgb(color)
    mask = Image.new("RGB",(W,H),(255,255,255)); md = ImageDraw.Draw(mask)
    md.ellipse([cx-ro,cy-ro,cx+ro,cy+ro], fill=rgb)
    md.ellipse([cx-ri,cy-ri,cx+ri,cy+ri], fill=rgb)
    _blend(img_path, mask)
    res = Image.open(img_path); d = ImageDraw.Draw(res)
    _solid(d, _circle_pts(cx,cy,ro), rgb)
    _solid(d, _circle_pts(cx,cy,ri), rgb)
    res.save(img_path)


def add_overlay_rect(img_path, ax_pos, cx_ax, cy_ax,
                     w_ax, h_ax, angle_deg, color, dashed):
    al, ar, at, ab, img = _ax_to_px(img_path, ax_pos)
    W, H = img.size; aw, ah = ar-al, ab-at
    cx = al+cx_ax*aw; cy = ab-cy_ax*ah
    pts = _rect_pts(cx, cy, w_ax*ah, h_ax*ah, -math.radians(angle_deg))
    rgb = _hex_to_rgb(color)
    mask = Image.new("RGB",(W,H),(255,255,255))
    ImageDraw.Draw(mask).polygon(pts, fill=rgb)
    _blend(img_path, mask)
    res = Image.open(img_path); d = ImageDraw.Draw(res)
    (_dashed if dashed else _solid)(d, pts, (0,0,0))
    res.save(img_path)


def add_overlay_ellipse(img_path, ax_pos, cx_ax, cy_ax,
                        w_ax, h_ax, angle_deg, color, dashed):
    al, ar, at, ab, img = _ax_to_px(img_path, ax_pos)
    W, H = img.size; aw, ah = ar-al, ab-at
    cx = al+cx_ax*aw; cy = ab-cy_ax*ah
    pts = _ellipse_pts(cx, cy, w_ax*ah, h_ax*ah, -math.radians(angle_deg))
    rgb = _hex_to_rgb(color)
    mask = Image.new("RGB",(W,H),(255,255,255))
    ImageDraw.Draw(mask).polygon(pts, fill=rgb)
    _blend(img_path, mask)
    res = Image.open(img_path); d = ImageDraw.Draw(res)
    (_dashed if dashed else _solid)(d, pts, (0,0,0))
    res.save(img_path)


def axes_frac_linear(ra0, dec0, ra_min, ra_max, dec_min, dec_max):
    return (1.0 - (ra0-ra_min)/(ra_max-ra_min),
            (dec0-dec_min)/(dec_max-dec_min))


def axes_frac_proj(p, ra0, dec0, ra_ref, dec_ref):
    x_c,y_c = p._proj.transform_point(ra0, dec0, p._crs)
    x_r,y_r = p._proj.transform_point(ra_ref, dec_ref, p._crs)
    d2a = p.ax.transData + p.ax.transAxes.inverted()
    cx_ax,cy_ax = d2a.transform((x_c,y_c))
    rx_ax,ry_ax = d2a.transform((x_r,y_r))
    return cx_ax, cy_ax, math.hypot(rx_ax-cx_ax, ry_ax-cy_ax)


LABEL_COLOR = (200, 20, 20)


def _label_font(size_px):
    from PIL import ImageFont
    import matplotlib.font_manager as fm
    try:
        prop = fm.FontProperties(family="sans-serif", weight="bold")
        return ImageFont.truetype(fm.findfont(prop), size_px)
    except Exception:
        return ImageFont.load_default()


def add_overlay_label(img_path, ax_pos, cx_ax, cy_ax, text):
    img = Image.open(img_path)
    W, H = img.size
    al, ar = ax_pos.x0*W, ax_pos.x1*W
    at, ab = (1-ax_pos.y1)*H, (1-ax_pos.y0)*H
    aw, ah = ar-al, ab-at
    x = al + cx_ax*aw; y = ab - cy_ax*ah
    draw = ImageDraw.Draw(img)
    draw.text((x,y), text, font=_label_font(max(14,int(ah*0.022))),
              fill=LABEL_COLOR, anchor="lm")
    img.save(img_path)


def render_target_overlay(img_path, ax_pos, t, ra_bounds, proj_ctx=None):
    style  = style_for(t["object_type"])
    shape  = style["shape"]; color = style["color"]; dashed = style["dashed"]
    ra0, dec0 = t["ra"], t["dec"]

    if proj_ctx is not None:
        cx_ax, cy_ax, spd = axes_frac_proj(proj_ctx, ra0, dec0, ra0, dec0+1.0)
    else:
        ra_min,ra_max,dec_min,dec_max = ra_bounds
        cx_ax, cy_ax = axes_frac_linear(ra0,dec0,ra_min,ra_max,dec_min,dec_max)
        spd = 1.0/(dec_max-dec_min)

    if shape == "circle":
        add_overlay_circle(img_path,ax_pos,cx_ax,cy_ax,
                           t["size_amin"]/60/2*spd, color,dashed)
    elif shape == "circle_plus":
        add_overlay_circle(img_path,ax_pos,cx_ax,cy_ax,
                           t["size_amin"]/60/2*spd, color,dashed,bisect=True)
    elif shape == "double_circle":
        add_overlay_double_circle(img_path,ax_pos,cx_ax,cy_ax,
                                  t["height_amin"]/60/2*spd, color)
    elif shape == "rect":
        add_overlay_rect(img_path,ax_pos,cx_ax,cy_ax,
                         t["width_amin"]/60*spd, t["height_amin"]/60*spd,
                         t.get("angle_deg",0.0), color,dashed)
    elif shape == "ellipse":
        add_overlay_ellipse(img_path,ax_pos,cx_ax,cy_ax,
                            t["width_amin"]/60*spd, t["height_amin"]/60*spd,
                            t.get("angle_deg",0.0), color,dashed)
    else:
        print(f"   WARNING: unhandled shape '{shape}' for {t.get('name','?')}")


def _label_pos(t, fov, others=None):
    off = t.get("label_offset", "auto")
    if off != "auto":
        return t["ra"]+off[0], t["dec"]+off[1]
    r = target_radius_deg(t)
    if others:
        rest = [o for o in others if o is not t]
        if rest:
            mr = sum(o["ra"]  for o in rest)/len(rest)
            md = sum(o["dec"] for o in rest)/len(rest)
            dra, dde = t["ra"]-mr, t["dec"]-md
            n = math.hypot(dra, dde)
            if n > 1e-9:
                dra /= n; dde /= n
                return (t["ra"] + dra*(r+0.025*fov),
                        t["dec"]+ dde*(r+0.025*fov))
    return t["ra"]+0.015*fov, t["dec"]+r+0.025*fov


def render_target_label(img_path, ax_pos, t, fov, ra_bounds,
                        others=None, proj_ctx=None):
    lra, ldec = _label_pos(t, fov, others)
    if proj_ctx is not None:
        cx_ax,cy_ax,_ = axes_frac_proj(proj_ctx,lra,ldec,lra,ldec+1.0)
    else:
        ra_min,ra_max,dec_min,dec_max = ra_bounds
        cx_ax,cy_ax = axes_frac_linear(lra,ldec,ra_min,ra_max,dec_min,dec_max)
    add_overlay_label(img_path,ax_pos,cx_ax,cy_ax,t.get("label",t["name"]))


# ─────────────────────────────────────────────────────────────────────────────
#  Branding  (inlined from compose_branding.py)
# ─────────────────────────────────────────────────────────────────────────────

def _svg_to_pil(path: str, size: int) -> Image.Image:
    """Rasterize an SVG file to PIL RGBA at the given pixel size."""
    try:
        import cairosvg
        data = cairosvg.svg2png(url=path, output_width=size, output_height=size)
        return Image.open(io.BytesIO(data)).convert("RGBA")
    except ImportError:
        pass
    try:
        from svglib.svglib import svg2rlg
        from reportlab.graphics import renderPM
        drawing = svg2rlg(path)
        scale = size / max(drawing.width, drawing.height)
        drawing.width *= scale; drawing.height *= scale
        drawing.transform = (scale,0,0,scale,0,0)
        buf = io.BytesIO()
        renderPM.drawToFile(drawing, buf, fmt="PNG")
        buf.seek(0)
        return Image.open(buf).convert("RGBA")
    except ImportError:
        pass
    raise RuntimeError(
        "SVG rasterizer not found.\n"
        "Install: pip install cairosvg  OR  pip install svglib"
    )


def _brand_font(size, bold=False):
    from PIL import ImageFont
    import matplotlib.font_manager as fm
    prop = fm.FontProperties(family="sans-serif",
                             weight="bold" if bold else "normal")
    try:
        return ImageFont.truetype(fm.findfont(prop), size)
    except Exception:
        return ImageFont.load_default()


def _make_png(chart, title, subtitle, out_path):
    W, H = chart.size; P = W / 100
    TH = int(P*5); FH = int(P*16); PAD = int(P*1.5); ICH = FH-2*PAD
    canvas = Image.new("RGB", (W, TH+H+FH), "white")
    draw = ImageDraw.Draw(canvas)
    draw.text((W//2, TH//2-int(P*1.2)), title,
              font=_brand_font(int(P*2.0),True),  fill="#111111", anchor="mm")
    draw.text((W//2, TH//2+int(P*1.0)), subtitle,
              font=_brand_font(int(P*1.4),False), fill="#555555", anchor="mm")
    canvas.paste(chart, (0, TH))
    sy = TH+H
    draw.line([(0,sy),(W,sy)], fill="#cccccc", width=2)

    logo_ok = qr_ok = False
    if os.path.exists(LOGO_PNG):
        try:
            logo = Image.open(LOGO_PNG).convert("RGBA").resize((ICH, ICH), Image.LANCZOS)
            canvas.paste(logo, (PAD, sy+PAD), logo)
            logo_ok = True
        except Exception as e:
            print(f"   WARNING: could not load logo PNG ({e})")
    lr = PAD + (ICH+PAD if logo_ok else 0)

    if os.path.exists(QR_SVG):
        try:
            qr = _svg_to_pil(QR_SVG, ICH)
            qrx = W-PAD-ICH
            canvas.paste(qr, (qrx, sy+PAD), qr)
            qr_ok = True
        except Exception as e:
            print(f"   WARNING: could not render QR ({e})")
    qrx = W-PAD-(ICH if qr_ok else 0)

    cx = (lr + qrx)//2
    lh = int(P*2.0); y0 = sy+PAD+int(FH*0.08)
    draw.text((cx,y0),       ORG_NAME, font=_brand_font(int(P*1.8),True),  fill="#111111", anchor="mt")
    draw.text((cx,y0+lh),    SITE_URL, font=_brand_font(int(P*1.3),False), fill="#0044cc", anchor="mt")
    draw.text((cx,y0+2*lh),  TAGLINE,  font=_brand_font(int(P*1.1),False), fill="#555555", anchor="mt")
    canvas.save(out_path)
    print(f"   Saved {out_path}")


def _make_pdf(chart, title, subtitle, out_path):
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.units    import inch
    from reportlab.pdfgen       import canvas as rl
    from reportlab.lib.utils    import ImageReader

    PW, PH = letter
    MG   = 0.35 * inch   # page margin
    AW   = PW - 2 * MG   # usable width

    # Fixed-height blocks
    TSZ=16; SSZ=11; TL=22; TH=TL*2+6   # title block
    GAP = 8                              # gap between blocks
    FH  = 80; LSZ = 64; FP = (FH-LSZ)/2 # footer block

    # Total vertical space consumed by everything except the chart
    overhead = TH + GAP + GAP + FH

    # Scale chart to fill all remaining vertical space on the page
    iw, ih = chart.size
    max_cph = PH - 2*MG - overhead
    # Start at full available width, then clamp height if needed
    cpw = AW
    cph = ih * (cpw / iw)
    if cph > max_cph:
        cph = max_cph
        cpw = iw * (cph / ih)

    # Centre the chart horizontally if it got narrower than AW
    chart_x = MG + (AW - cpw) / 2.0

    # Lay out from the top of the usable area downward
    title_y    = PH - MG - TL          # baseline of title line
    subtitle_y = title_y - TL           # baseline of subtitle line
    chart_top  = subtitle_y - GAP       # top of chart image
    chart_bot  = chart_top - cph        # bottom of chart image
    footer_top = chart_bot - GAP        # top of footer rule
    footer_y   = footer_top - FH        # bottom of footer block

    c = rl.Canvas(out_path, pagesize=letter)
    c.setTitle(title); c.setAuthor(ORG_NAME)

    # Title block
    c.setFont("Helvetica-Bold", TSZ); c.setFillColorRGB(.07,.07,.07)
    c.drawCentredString(PW/2, title_y, title)
    c.setFont("Helvetica", SSZ);      c.setFillColorRGB(.35,.35,.35)
    c.drawCentredString(PW/2, subtitle_y, subtitle)

    # Chart image
    buf = io.BytesIO(); chart.save(buf, format="PNG"); buf.seek(0)
    c.drawImage(ImageReader(buf), chart_x, chart_bot,
                width=cpw, height=cph, preserveAspectRatio=True)

    # Footer rule
    c.setStrokeColorRGB(.8,.8,.8); c.setLineWidth(.5)
    c.line(MG, footer_top, PW-MG, footer_top)

    # Logo (left)
    logo_right = MG
    if os.path.exists(LOGO_PNG):
        try:
            lp = Image.open(LOGO_PNG).convert('RGBA').resize(
                (int(LSZ*4), int(LSZ*4)), Image.LANCZOS)
            lb = io.BytesIO(); lp.save(lb, format="PNG"); lb.seek(0)
            logo_y = footer_top - FP - LSZ
            c.drawImage(ImageReader(lb), MG, logo_y,
                        width=LSZ, height=LSZ, mask="auto")
            logo_right = MG + LSZ
        except Exception as e:
            print(f"   WARNING: logo PNG skipped in PDF ({e})")

    # QR code (right)
    qr_left = PW - MG
    if os.path.exists(QR_SVG):
        try:
            qp = _svg_to_pil(QR_SVG, int(LSZ*4))
            qb = io.BytesIO(); qp.save(qb, format="PNG"); qb.seek(0)
            qr_x = PW - MG - LSZ
            qr_y = footer_top - FP - LSZ
            c.drawImage(ImageReader(qb), qr_x, qr_y,
                        width=LSZ, height=LSZ, mask="auto")
            qr_left = qr_x
        except Exception as e:
            print(f"   WARNING: QR skipped in PDF ({e})")

    # Branding text centred between logo and QR
    tcx = (logo_right + qr_left) / 2.0
    ofs=11; sfs=9; lsp=14
    tt = footer_top - FP - ofs
    c.setFont("Helvetica-Bold", ofs); c.setFillColorRGB(.07,.07,.07)
    c.drawCentredString(tcx, tt,          ORG_NAME)
    c.setFont("Helvetica", sfs);          c.setFillColorRGB(0,.27,.8)
    c.drawCentredString(tcx, tt - lsp,    SITE_URL)
    c.setFillColorRGB(.35,.35,.35)
    c.drawCentredString(tcx, tt - 2*lsp,  TAGLINE)

    c.save()
    print(f"   Saved {out_path}")


def apply_branding(raw_png, out_stem, title, subtitle):
    chart = Image.open(raw_png).convert("RGB")
    _make_png(chart, title, subtitle, out_stem+".png")
    _make_pdf(chart, title, subtitle, out_stem+".pdf")


# ─────────────────────────────────────────────────────────────────────────────
#  Chart builders
# ─────────────────────────────────────────────────────────────────────────────

def _star_markers(p, df):
    for _, row in df.sort_values("magnitude", ascending=False).iterrows():
        mag = float(row["magnitude"])
        p.marker(ra=float(row["ra"]), dec=float(row["dec"]),
                 skip_bounds_check=True,
                 style={"marker": {"size": marker_size(mag), "symbol": "circle",
                                   "fill": "full", "color": "#000000",
                                   "edge_color": None, "alpha": 0.9, "zorder": 50}})


def _mag_legend(fig, mag_limit):
    LEG_S = 16
    leg = fig.add_axes([0.71, 0.03, 0.27, 0.25])
    leg.set_xlim(0,1); leg.set_ylim(0,1)
    leg.set_facecolor("white"); leg.patch.set_alpha(0.88)
    for sp in leg.spines.values():
        sp.set_edgecolor("#aaaaaa"); sp.set_linewidth(0.8)
    leg.tick_params(left=False,bottom=False,labelleft=False,labelbottom=False)
    leg.text(.5,.93,"Magnitude",ha="center",va="top",
             fontsize=20,fontweight="bold",transform=leg.transAxes)
    for mag,y in zip([6,8,10,min(12,mag_limit)],[.72,.52,.33,.14]):
        sz = marker_size(mag)
        leg.scatter([.18],[y],s=(sz*SCALE)**2*LEG_S,c="black",zorder=5)
        leg.text(.34,y,f"V = {mag:g}",va="center",fontsize=20)


def make_raw_chart(field, out_path):
    from starplot import MapPlot, Mercator
    from starplot.styles import PlotStyle, extensions

    targets = field["targets"]
    ra0,dec0,fov = compute_field_center_and_fov(field)
    half = fov/2; ml = field.get("mag_limit",MAG_LIMIT)

    # RA spans more degrees than Dec at high declinations because
    # 1° RA = cos(dec)° on sky.  Expand RA bounds so the chart shows
    # equal sky coverage in both axes.
    cosd = max(math.cos(math.radians(dec0)), 0.05)
    half_ra = half / cosd
    ra_min,ra_max   = ra0 - half_ra, ra0 + half_ra
    dec_min,dec_max = dec0 - half,    dec0 + half

    print(f"\n── {field['title']}  FOV {fov:.2f}°  ({len(targets)} target(s))")

    if field.get("fetch_stars", True):
        print(f"   Fetching stars V ≤ {ml} from NOMAD …")
        df = fetch_stars(ra0, dec0, max(half_ra, half) * 1.15, ml)
        print(f"   {len(df)} stars" if len(df) else "   0 stars returned")
    else:
        df = pd.DataFrame(columns=["ra","dec","magnitude"])
        print("   Star fetch disabled")

    style = PlotStyle().extend(extensions.GRAYSCALE, extensions.MAP)
    p = MapPlot(projection=Mercator(),
                ra_min=ra_min, ra_max=ra_max,
                dec_min=dec_min, dec_max=dec_max,
                style=style, resolution=2048)
    _star_markers(p, df)

    n = 5
    ra_step  = (ra_max  - ra_min)  / (n - 1)
    dec_step = (dec_max - dec_min) / (n - 1)
    p.gridlines(tick_marks=True,
                ra_locations =[ra_min  + ra_step  * i for i in range(n)],
                dec_locations=[dec_min + dec_step * i for i in range(n)],
                ra_formatter_fn=ra_fmt, dec_formatter_fn=dec_fmt)
    _mag_legend(p.fig, ml)
    p.export(out_path, padding=0.3)
    ax_pos = p.ax.get_position()
    plt.close("all")
    print(f"   Starfield → {os.path.basename(out_path)}")

    for t in targets:
        render_target_overlay(out_path,ax_pos,t,(ra_min,ra_max,dec_min,dec_max))
        render_target_label(out_path,ax_pos,t,fov,(ra_min,ra_max,dec_min,dec_max),
                            others=targets)
        print(f"   Overlay + label: {t['name']}")


def make_raw_chart_stereonorth(field, out_path):
    from starplot import MapPlot, StereoNorth
    from starplot.styles import PlotStyle, extensions

    targets = field["targets"]
    ra0,dec0,fov = compute_field_center_and_fov(field)
    half = fov/2; ml = field.get("mag_limit",MAG_LIMIT)

    print(f"\n── {field['title']}  FOV {fov:.2f}° (StereoNorth)  ({len(targets)} target(s))")

    if field.get("fetch_stars", True):
        print(f"   Fetching stars V ≤ {ml} from NOMAD …")
        df = fetch_stars(ra0, dec0, half*1.15, ml)
        print(f"   {len(df)} stars" if len(df) else "   0 stars returned")
    else:
        df = pd.DataFrame(columns=["ra","dec","magnitude"])
        print("   Star fetch disabled")

    style = PlotStyle().extend(extensions.GRAYSCALE, extensions.MAP)
    p = MapPlot(projection=StereoNorth(center_ra=ra0),
                ra_min=0, ra_max=360,
                dec_min=dec0-half, dec_max=dec0+half,
                style=style, resolution=2048)
    xc,yc = p._proj.transform_point(ra0,dec0,p._crs)
    xn,yn = p._proj.transform_point(ra0,dec0+half,p._crs)
    r = math.sqrt((xn-xc)**2+(yn-yc)**2)
    p.ax.set_xlim(xc-r,xc+r); p.ax.set_ylim(yc-r,yc+r)
    _star_markers(p, df)
    p.gridlines(tick_marks=False,
                ra_locations=list(range(0,360,15)),
                dec_locations=[round(dec0-half+half*2*i/6,2) for i in range(7)],
                ra_formatter_fn=ra_fmt, dec_formatter_fn=dec_fmt)
    _mag_legend(p.fig, ml)
    p.export(out_path, padding=0.3)
    ax_pos = p.ax.get_position()
    for t in targets:
        render_target_overlay(out_path,ax_pos,t,None,proj_ctx=p)
        render_target_label(out_path,ax_pos,t,fov,None,others=targets,proj_ctx=p)
        print(f"   Overlay + label: {t['name']}")
    plt.close("all")
    print(f"   Starfield + overlays → {os.path.basename(out_path)}")


# ─────────────────────────────────────────────────────────────────────────────
#  Main
# ─────────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        prog="finder_charts.py",
        description="NBAS Finder Chart Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
examples:
  python finder_charts.py --objects "NGC 6946"
  python finder_charts.py --objects "NGC 6520" "Barnard 86" --chart-name inkspot
  python finder_charts.py --objects "M 57" --fov 1.5 --mag-limit 13
  python finder_charts.py --fields          # run hard-coded FIELDS list
  python finder_charts.py --selftest        # geometry checks, no network needed

assets (place alongside this script):
  nbas-logo.svg      branding logo  (gracefully skipped if absent)
  nbas-qrcode.svg    QR code        (gracefully skipped if absent)
""")

    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--objects", nargs="+", metavar="NAME",
                      help="Object name(s) to resolve via SIMBAD — one chart")
    mode.add_argument("--fields", action="store_true",
                      help="Run the hard-coded FIELDS list in this script")
    mode.add_argument("--selftest", action="store_true",
                      help="Run geometry self-tests and exit")

    parser.add_argument("--chart-name", default=None, dest="chart_name",
                        help="Output filename stem (default: slug of first object)")
    parser.add_argument("--title",      default=None,
                        help="Chart title (default: object names joined with ' & ')")
    parser.add_argument("--info",       default="",
                        help="Extra text appended to subtitle")
    parser.add_argument("--fov",        type=float, default=None,
                        help="Explicit FOV in degrees (default: auto)")
    parser.add_argument("--mag-limit",  type=float, default=MAG_LIMIT,
                        dest="mag_limit",
                        help=f"Star fetch limit (default: {MAG_LIMIT})")
    parser.add_argument("--no-stars",   action="store_true", dest="no_stars",
                        help="Skip Vizier star fetch")
    parser.add_argument("--output-dir", default=None, dest="output_dir",
                        help="Output directory (default: script directory)")
    parser.add_argument("--projection",
                        choices=["Mercator","StereoNorth"], default=None,
                        help="Map projection (default: auto)")

    args = parser.parse_args()

    if args.selftest:
        _selftest_position_angle_convention()
        sys.exit(0)

    out_dir = args.output_dir or HERE

    if args.objects:
        print(f"\nResolving {len(args.objects)} object(s) from SIMBAD …")
        targets = resolve_simbad(args.objects)
        if not targets:
            sys.exit("ERROR: no objects resolved from SIMBAD.")

        chart_name = args.chart_name or slug(args.objects[0])
        title      = args.title      or " & ".join(args.objects)

        field = {
            "chart_name":  chart_name,
            "title":       title,
            "info":        args.info,
            "fov_deg":     args.fov,
            "mag_limit":   args.mag_limit,
            "fetch_stars": not args.no_stars,
            "targets":     targets,
        }
        if args.projection:
            field["projection"] = args.projection
        else:
            _, dec0, _ = compute_field_center_and_fov(field)
            if dec0 > 75:
                field["projection"] = "StereoNorth"

        fields = [field]
    else:
        fields = FIELDS

    for field in fields:
        s        = slug(field["chart_name"])
        raw_png  = os.path.join(out_dir, f"{s}_raw.png")
        out_stem = os.path.join(out_dir, s)
        _, _, fov = compute_field_center_and_fov(field)
        names    = ", ".join(t["name"] for t in field["targets"])
        subtitle = (f"{names} · FOV {fov:.2f}°"
                    + (f" · {field['info']}" if field.get("info") else ""))

        if field.get("projection") == "StereoNorth":
            make_raw_chart_stereonorth(field, raw_png)
        else:
            make_raw_chart(field, raw_png)

        print("   Applying NBAS branding …")
        apply_branding(raw_png, out_stem, field["title"], subtitle)

    n = len(fields)
    print(f"\n✓  {n} finder chart{'s' if n != 1 else ''} complete.")


if __name__ == "__main__":
    main()
