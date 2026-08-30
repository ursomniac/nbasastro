#!/usr/bin/env python3
"""
NBAS Finder Chart Generator
=============================
Generates a single branded JPG finder chart per field (no separate raw PNG
or PDF kept around -- mirrors the starmap pattern). Each field can contain
one or more target objects sharing a single frame.

Overlay style is driven by OBJECT TYPE:

    open_cluster        yellow circle, DASHED outline
    globular_cluster    yellow circle, SOLID outline, bisected with "+"
    emission_nebula     green rect, solid outline, rotated to orientation
    reflection_nebula   green rect, solid outline, rotated to orientation
    dark_nebula         grey rect, solid outline, rotated to orientation
    galaxy              red ellipse, solid outline, rotated to orientation
    galaxy_barred       purple ellipse, solid outline, rotated to orientation
    galaxy_dwarf_irr    blue ellipse, solid outline, rotated to orientation
    compact_group       indigo circle, solid outline
    planetary_nebula    cyan, two concentric circles, NO outline

Usage
-----
  # Resolve objects by name via SIMBAD — one chart, all on one field:
  python finder_charts.py --objects "NGC 6946"
  python finder_charts.py --objects "NGC 6520" "Barnard 86" --chart-name inkspot
  python finder_charts.py --objects "M 57" --fov 1.5 --mag-limit 13

  # Geometry self-test (no network or starplot needed):
  python finder_charts.py --selftest

--objects options (all optional):
  --chart-name STEM     output filename stem (default: slug of first object)
  --title TEXT          chart title (default: object names joined with " & ")
  --info TEXT           extra text appended to subtitle
  --fov DEG             explicit FOV in degrees (default: auto from object sizes)
  --mag-limit MAG       star depth (default: 12.0); mag_limit <= 11 uses the
                        local mag11 BigSky catalog, mag_limit > 11 uses the
                        deeper mag16 catalog (capped at 16.0) -- see star
                        source note below
  --no-stars            skip star plotting entirely
  --output-dir DIR      where to write output (default: same dir as this script)
  --projection {Mercator,StereoNorth}  (default: auto; StereoNorth if dec > 75)

Star source: stars are plotted from the local BigSky catalog already used by
scripts/starmaps/generate.py (via starplot's own stars() method and the
STARPLOT_DATA_PATH env var set at the top of this file) -- not a live
Vizier/NOMAD query. This was a deliberate change after a live-fetch
approach proved unreliable (server-side empty responses, timeouts, a
filter+truncation interaction that silently zeroed out real results) and,
separately, after discovering the per-star p.marker() loop it used for
rendering never actually displayed markers at all. A dormant fetch_stars()
(live Vizier) function is still defined in this file but not called by the
default path.

Assets (same directory as this script):
  nbas-logo.svg
  nbas-qrcode.svg

Requirements:
  pip install starplot astroquery astropy pandas pillow cairosvg \\
      numpy --break-system-packages
"""

import argparse
import io
import math
import os
import sys
import tempfile
import warnings

HERE = os.path.dirname(os.path.abspath(__file__))

# scripts/starmaps/finder_charts/ is a self-contained local data bundle
# (BigSky star catalog, the duckdb "spatial" extension pre-downloaded,
# constellations/Milky Way outlines, its own de421.bsp) that
# scripts/starmaps/generate.py already points starplot at via this exact
# env var, and that pipeline runs reliably with zero network access at
# render time. finder_charts.py previously did its own thing instead: a
# hand-rolled live Vizier/NOMAD fetch plus a per-star marker() loop for
# rendering. That turned out to be broken on two independent counts --
# the live query was unreliable (see fetch_stars() below), and marker()
# turned out not to be the right API for bulk star plotting at all: stars
# were being fetched successfully but never actually appearing on the
# rendered chart. starplot's own stars() method (used by generate.py) is
# the documented, correct way to do this, and it's what's used now.
# MUST be set before starplot is imported anywhere (starplot reads this
# once at import time) -- hence this sits above every other import here.
STARPLOT_SHARED_DATA_DIR = os.path.normpath(
    os.path.join(HERE, "..", "starmaps", "finder_charts"))
os.environ.setdefault("STARPLOT_DATA_PATH", STARPLOT_SHARED_DATA_DIR)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageDraw

warnings.filterwarnings("ignore")

LOGO_PNG  = os.path.join(HERE, "nbas-logo.png")
QR_SVG    = os.path.join(HERE, "nbas-qrcode.svg")
# Shared across scripts/finder_charts and scripts/starmaps -- lives once in
# scripts/assets rather than as a separate copy under each script directory.
# Passed explicitly to MapPlot(ephemeris=...) rather than relying on
# skyfield's default loader, which resolves bare filenames against the
# process's cwd rather than this script's directory.
EPHEMERIS = os.path.normpath(os.path.join(HERE, "..", "assets", "de421.bsp"))

# Same local BigSky (mag<=11) catalog scripts/starmaps/generate.py already
# uses, resolved automatically by starplot itself once STARPLOT_DATA_PATH
# (above) points at its directory -- this constant is only needed here for
# fetch_stars_local()'s own direct pandas read (used to compute real
# min/max magnitude for the adaptive size_fn and the custom legend, kept
# in sync with what stars() actually renders). Left in its existing
# location under scripts/starmaps/ rather than deduped into scripts/assets/
# (like de421.bsp was) -- that would mean touching scripts/starmaps/
# generate.py too, which is explicitly out of scope for this session.
# Two BigSky depths are present in STARPLOT_SHARED_DATA_DIR: the mag11
# file scripts/starmaps/generate.py already used, and a mag16 file
# (deeper, ~2.5M stars vs ~984K) added alongside it. Both fetch_stars_local()
# (used only for min/max stats + legend) and _plot_stars()'s call into
# starplot's own p.stars() (used for the actual rendered markers) must pick
# the SAME file for a given request, or the legend and the chart disagree.
# See _select_local_catalog() below -- this used to be a single hardcoded
# path+limit pair, which is why --mag-limit above 11 silently did nothing:
# both consumers were pinned to the mag11 file no matter what was requested.
LOCAL_STAR_CATALOG_MAG11 = os.path.join(STARPLOT_SHARED_DATA_DIR, "stars.bigksy.0.1.3.mag11.parquet")
LOCAL_STAR_CATALOG_MAG16 = os.path.join(STARPLOT_SHARED_DATA_DIR, "stars.bigksy.0.1.3.mag16.parquet")


def _select_local_catalog(mag_limit: float):
    """Pick the shallowest local BigSky parquet that can satisfy mag_limit,
    and the true depth ceiling of that file (used to compute effective_limit
    -- not a fixed constant). mag16 is the deepest catalog present on disk;
    requests deeper than 16 are clamped to 16, same as before for 11."""
    if mag_limit <= 11.0:
        return LOCAL_STAR_CATALOG_MAG11, 11.0
    return LOCAL_STAR_CATALOG_MAG16, 16.0

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
    "compact_group":     {"shape": "circle",       "color": "#8010C0", "dashed": False},
    "planetary_nebula":  {"shape": "double_circle","color": "#33CCCC", "dashed": False},
    # star: small circle with inward N/S/E/W ticks (classic finder-chart reticle)
    "star":              {"shape": "star_target",  "color": "#3366FF", "dashed": False},
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
    "AGN": "galaxy",  "SyG": "galaxy", "Sy1": "galaxy", "Sy2": "galaxy", "AG?": "galaxy",
    "QSO": "galaxy",  "H2G": "galaxy", "SBG": "galaxy", "bCG": "galaxy",
    "EmG": "galaxy",  "LSB": "galaxy", "BiC": "galaxy", "BLL": "galaxy",
    "LIN": "galaxy",  "cD":  "galaxy", "CGG": "compact_group",
    # Stars — single, multiple, variable, proper-motion, spectral subtypes, etc.
    "*":   "star",   "**":  "star",   "V*":  "star",   "PM*": "star",
    "HB*": "star",   "RG*": "star",   "sg*": "star",   "SB*": "star",
    "BY*": "star",   "RS*": "star",   "LP*": "star",   "s*r": "star",
    "EB*": "star",   "Al*": "star",   "bL*": "star",   "WU*": "star",
    "K*":  "star",   "G*":  "star",   "MS*": "star",   "su*": "star",
    # X-ray binaries and related compact-object systems -- what's actually
    # findable at the eyepiece/in an image is the optical companion star
    # (e.g. HDE 226868 for Cygnus X-1), so these should render with the
    # small star-reticle style, not the open-cluster dashed circle.
    "HXB": "star",   "LXB": "star",   "XB*": "star",   "X":   "star",
    "Psr": "star",   "Pu*": "star",   "No*": "star",   "WD*": "star",
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
        elif shape == "star_target":
            # Fixed reticle ring radius (arcmin) -- a point-source marker,
            # not a real angular size, so this is purely cosmetic. Was
            # 10.0' (20' diameter), which visibly outsized real deep-sky
            # object outlines in the same field (e.g. a 16'x9' nebula) and
            # read as "the star matters more than the nebula" -- shrunk so
            # it reads as a locator mark, not a competing shape.
            t["size_amin"] = 3.0
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


MAG_LIMIT     = 12.0
# Marker sizes are in matplotlib scatter's native s= units (marker AREA in
# points^2) -- these values are handed straight to starplot's stars()
# (size_fn), which passes them straight to ax.scatter(s=...), NOT to the old
# per-point p.marker(style={"marker":{"size":...}}) API this used to go
# through. That's an important distinction found the hard way: the old
# STAR_SIZE_MIN/MAX (3.0/26.0) were calibrated for that old API's own
# internal scaling and rendered as barely-visible gray specks once actually
# passed through scatter() at these units -- confirmed by diffing rendered
# pixels with/without stars plotted (real markers were present, just
# effectively invisible at ~3-26 points^2). starplot's own default size
# function (callables.size_by_magnitude) uses 20-3800 in this same unit for
# reference; these are recalibrated to a comparable range.
STAR_SIZE_MIN = 20.0    # floor marker size (points^2) — faint stars are otherwise invisible
STAR_SIZE_MAX = 2200.0  # ceiling marker size (points^2) — cap for the brightest star present
# Reference magnitude anchors for the *absolute* brightness->size curve
# (see marker_size() below) -- deliberately independent of what's plotted
# in any one field, so "how bright is this star, really" always means the
# same thing on a fixed scale rather than a field-relative one.
ABS_MAG_REF_BRIGHT = 0.0
ABS_MAG_REF_FAINT  = 13.0
FOV_PADDING   = 3.0   # finder charts need plenty of context around targets
FOV_MIN_DEG   = 2.0   # never show less than 2° so observers can navigate


# ─────────────────────────────────────────────────────────────────────────────
#  Helpers
# ─────────────────────────────────────────────────────────────────────────────

def marker_size(mag: float, size_min: float = STAR_SIZE_MIN,
                 size_max: float = STAR_SIZE_MAX) -> float:
    # Absolute brightness->size curve, anchored to fixed reference
    # magnitudes (ABS_MAG_REF_BRIGHT..ABS_MAG_REF_FAINT) rather than a
    # hardcoded constant -- so it scales correctly no matter what
    # size_min/size_max units are in use (points for the old marker() API,
    # points^2 for the current scatter()-based one). Used as the shape
    # reference for size_fn_for_range() below, not called directly for
    # chart rendering -- an absolute scale alone makes a field's brightest
    # star huge even when that star is only, say, mag 7 and nothing else
    # is close.
    def raw(m):
        return 10.0 ** (-0.12 * m)
    r_bright, r_faint = raw(ABS_MAG_REF_BRIGHT), raw(ABS_MAG_REF_FAINT)
    m_clamped = max(ABS_MAG_REF_BRIGHT, min(ABS_MAG_REF_FAINT, mag))
    t = (raw(m_clamped) - r_faint) / (r_bright - r_faint)
    return max(size_min, size_min + t * (size_max - size_min))


def size_fn_for_range(mag_min: float, mag_max: float,
                       size_min: float = STAR_SIZE_MIN,
                       size_max: float = STAR_SIZE_MAX,
                       headroom: float = 1.3):
    """Build a mag → marker-size function using the brightest (mag_min) and
    faintest (mag_max) star actually present in this field -- a hybrid of
    relative and absolute scaling, because the two goals pull in opposite
    directions and both matter:

      - RELATIVE: a field with a narrow, uniformly-faint magnitude spread
        (say, everything between mag 9 and 12, nothing brighter) needs its
        faint end pulled up toward size_max, or those stars render as
        "almost microscopic" dots -- there's no bright star in the field to
        anchor a purely absolute scale against.

      - ABSOLUTE: but that same stretching must not let a field's "brightest
        star" hog the full size_max ceiling just because it's the best of a
        faint bunch -- a field whose brightest star is only mag 7 shouldn't
        render that star at the same size as a true mag 1-2 showpiece
        elsewhere. Size should still mean something about real brightness.

    Resolution: compute the relative (min-max-stretched) size as before, but
    cap every star at what its own absolute magnitude would earn (with a bit
    of `headroom` for being the local standout), and take the smaller of the
    two. A genuinely bright star's absolute cap is generously large so the
    relative value usually wins; a merely-locally-bright but absolutely
    faint star gets pulled back down by its cap.
    """
    def raw(m):
        return 10.0 ** (-0.12 * m)

    def absolute_size(m):
        return max(size_min, min(size_max, marker_size(m, size_min, size_max) * headroom))

    if mag_max <= mag_min + 1e-9:
        # Degenerate case: a single star, or every star at ~the same
        # magnitude. No meaningful range to stretch across -- fall back to
        # pure absolute sizing (still clamped to [size_min, size_max]).
        sz = absolute_size(mag_min)
        return lambda m: sz

    raw_faint  = raw(mag_max)   # smallest raw value  (faintest star)
    raw_bright = raw(mag_min)   # largest raw value   (brightest star)
    span = raw_bright - raw_faint

    def f(m):
        m_clamped = max(mag_min, min(mag_max, m))
        t = (raw(m_clamped) - raw_faint) / span
        relative = size_min + t * (size_max - size_min)
        return min(relative, absolute_size(m_clamped))

    return f


def slug(name: str) -> str:
    out = name.lower()
    for ch in ["&", "(", ")", '"']:
        out = out.replace(ch, "")
    return out.strip().replace(" ", "_")


def target_radius_deg(t: dict) -> float:
    shape = style_for(t["object_type"])["shape"]
    if shape in ("circle", "circle_plus"):
        return t["size_amin"] / 60.0 / 2.0
    if shape == "star_target":
        return t.get("size_amin", 10.0) / 60.0
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


def _vizier_table_rowcount(result) -> int:
    if not result or len(result) == 0:
        return 0
    return len(result[0])


_local_star_catalog_cache = {}  # module-level cache keyed by path -- mag11 and
                                 # mag16 are separate files and may both be
                                 # loaded in a single process


def fetch_stars_local(ra_deg, dec_deg, radius_deg, mag_limit) -> pd.DataFrame:
    """Fallback star source, used only when live Vizier/NOMAD comes back
    empty or fails outright. Reads whichever local BigSky catalog file
    (mag11 or mag16 -- see _select_local_catalog()) covers the requested
    mag_limit. Filters with a flat-sky cos(dec) approximation, which is
    what the rest of this script already uses for FOV geometry at these
    field sizes (a few degrees at most), so it's consistent with the
    precision used elsewhere, not a new source of error.

    Depth caps out at whatever the selected file's ceiling is (11 or 16)
    if mag_limit asks for more than that -- clearly logged, since a chart
    generated this way would be shallower than a real NOMAD fetch.
    """
    global _local_star_catalog_cache
    catalog_path, catalog_ceiling = _select_local_catalog(mag_limit)

    if not os.path.exists(catalog_path):
        print(f"  WARNING: local star catalog fallback not found at {catalog_path}")
        return pd.DataFrame(columns=["ra", "dec", "magnitude"])

    if catalog_path not in _local_star_catalog_cache:
        print(f"   Loading local star catalog fallback ({os.path.basename(catalog_path)}) …")
        # Read all columns rather than passing columns=[...] -- this
        # particular file's parquet metadata references an index column
        # that isn't in the actual schema, which pyarrow chokes on when
        # asked to project down to a column subset up front. Select the
        # subset afterward in pandas instead.
        _local_star_catalog_cache[catalog_path] = pd.read_parquet(catalog_path)[
            ["ra", "dec", "magnitude"]]
    cat = _local_star_catalog_cache[catalog_path]

    effective_limit = min(mag_limit, catalog_ceiling)
    if mag_limit > catalog_ceiling:
        print(f"   NOTE: local catalog fallback only reaches mag "
              f"{catalog_ceiling:.1f} (requested {mag_limit:.1f}) -- "
              f"chart will be shallower than a live NOMAD fetch would be.")

    cosd = max(math.cos(math.radians(dec_deg)), 0.05)
    dra_raw = cat["ra"] - ra_deg
    dra_wrapped = ((dra_raw + 180.0) % 360.0) - 180.0   # correct RA 0/360 wraparound
    dra = dra_wrapped * cosd
    ddec = cat["dec"] - dec_deg
    sep = np.hypot(dra, ddec)

    mask = (sep <= radius_deg) & cat["magnitude"].notna() & cat["magnitude"].between(1.0, effective_limit)
    out = cat.loc[mask, ["ra", "dec", "magnitude"]].reset_index(drop=True).copy()
    for col in ("ra", "dec", "magnitude"):
        out[col] = out[col].astype(float)
    return out


# Known VizieR mirrors, tried in order. The default (vizier.cds.unistra.fr,
# left as None here -- "whatever astroquery is already configured to use")
# has been observed, verified by hand against the raw VizieR CGI endpoint,
# to return HTTP 200 with a syntactically valid but genuinely EMPTY VOTable
# for perfectly good queries -- not a timeout, not an exception, zero rows
# -- while vizier.cfa.harvard.edu answers the identical query correctly.
# That's a live service issue on that specific mirror, not a code/filter
# bug, so the fix is a mirror fallback rather than anything about the query
# itself: try the configured default first, then fall back to a
# known-good alternate if it comes back empty or errors out.
VIZIER_MIRRORS = [None, "vizier.cfa.harvard.edu"]


def fetch_stars(ra_deg, dec_deg, radius_deg, mag_limit) -> pd.DataFrame:
    from astroquery.vizier import Vizier, conf as vizier_conf
    from astropy.coordinates import SkyCoord
    import astropy.units as u

    coord = SkyCoord(ra=ra_deg, dec=dec_deg, unit="deg", frame="icrs")
    default_server = vizier_conf.server

    # IMPORTANT: no server-side column_filters on Vmag here, by design.
    # Verified by hand: filtering server-side with column_filters={"Vmag":
    # "<12.0"} (or the "0.0..12.0" range form) reliably came back with 0
    # rows on a real ~1.4 deg-radius NOMAD query, on both the default and
    # fallback mirrors -- even though the identical query WITHOUT that
    # constraint returned thousands of real rows, a meaningful fraction of
    # which do have Vmag < 12. NOMAD is a merged catalog and most rows have
    # no Vmag at all (photographic-only detections); VizieR's -out.max row
    # cap appears to be applied to its raw catalog scan *before* the Vmag
    # constraint is evaluated, so a capped, constrained query can land on
    # zero qualifying rows even though plenty exist in the field. Fetching
    # unfiltered and cutting on magnitude client-side (below) sidesteps
    # that entirely and was confirmed to recover real stars (V<12) in
    # testing. row_limit=20000 is not a magic number, just what was
    # confirmed working in that test -- large enough to comfortably find
    # V<12 stars in a multi-square-degree field without pushing the
    # request into whatever caused a separate, larger-cap request to come
    # back empty (consistent with this server's general intermittent-empty
    # behavior, not something diagnosed further here).
    # NOTE: mirror selection is passed as the vizier_server= constructor
    # kwarg, not by mutating the global astroquery.vizier.conf.server --
    # a first attempt at this mutated conf.server instead, and the
    # resulting request still hit the original host regardless (visible
    # in testing as the reported exception's host never actually
    # changing). vizier_server= is the documented per-instance override
    # (see astroquery.vizier.core.VizierClass.__init__) and was confirmed
    # to work.
    result = None
    last_exc = None
    for mirror in VIZIER_MIRRORS:
        server = mirror if mirror is not None else default_server
        v = Vizier(columns=["RAJ2000", "DEJ2000", "Vmag"],
                   row_limit=20000, timeout=90, vizier_server=server)
        try:
            result = v.query_region(coord, radius=radius_deg * u.deg,
                                    catalog="I/297/out")
            last_exc = None
        except Exception as exc:
            last_exc = exc
            result = None
            print(f"  WARNING: Vizier query via {server} failed ({exc})")
            continue
        n = _vizier_table_rowcount(result)
        if n > 0:
            break
        print(f"  NOTE: {server} returned 0 rows for this query.")

    if _vizier_table_rowcount(result) == 0:
        if last_exc is not None:
            print(f"  WARNING: Vizier query failed on all mirrors ({last_exc})")
        else:
            print("  WARNING: Vizier returned no results from any mirror.")
        print("   Falling back to local star catalog …")
        return fetch_stars_local(ra_deg, dec_deg, radius_deg, mag_limit)
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


def _dashed(draw, pts, color, n_segs=32, width=6):
    n = len(pts); seg = max(1, n // n_segs)
    for i in range(0, n - 1, seg):
        if (i // seg) % 2 == 0:
            chunk = pts[i:min(i + seg + 1, n)]
            if len(chunk) >= 2:
                draw.line(chunk, fill=color, width=width)


def _solid(draw, pts, color, width=6):
    draw.line(pts, fill=color, width=width)


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
                       r_ax, color, dashed, bisect=False,
                       outline_width=6, cross_width=4, min_r_px=None):
    al, ar, at, ab, img = _ax_to_px(img_path, ax_pos)
    W, H = img.size; aw, ah = ar-al, ab-at
    cx = al + cx_ax*aw; cy = ab - cy_ax*ah; r = r_ax*ah
    if min_r_px is not None:
        # Enforced visibility floor -- a true-to-angular-size circle for a
        # small object (a few arcmin) can round down to just 1-2px at a
        # wide-FOV overview scale, at which point the outline/cross
        # strokes (outline_width/cross_width) swallow the fill entirely
        # and it reads as a plain black dot instead of a yellow-filled,
        # black-rimmed marker. Confirmed by a real test render before this
        # was added: several of the smallest clusters in the AWV overview
        # chart showed no visible marker, just their label.
        r = max(r, min_r_px)
    rgb = _hex_to_rgb(color)
    mask = Image.new("RGB", (W,H), (255,255,255))
    ImageDraw.Draw(mask).ellipse([cx-r,cy-r,cx+r,cy+r], fill=rgb)
    _blend(img_path, mask)
    res = Image.open(img_path); d = ImageDraw.Draw(res)
    pts = _circle_pts(cx, cy, r)
    if bisect:
        _solid(d, pts, (0,0,0), width=outline_width)
        d.line([(cx-r,cy),(cx+r,cy)], fill=(0,0,0), width=cross_width)
        d.line([(cx,cy-r),(cx,cy+r)], fill=(0,0,0), width=cross_width)
    elif dashed: _dashed(d, pts, (0,0,0), width=outline_width)
    else:        _solid(d, pts, (0,0,0), width=outline_width)
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


def add_overlay_star_target(img_path, ax_pos, cx_ax, cy_ax, r_ax, color):
    """Small circle with inward N/S/E/W tick marks — classic finder-chart reticle."""
    al, ar, at, ab, img = _ax_to_px(img_path, ax_pos)
    W, H = img.size; aw, ah = ar-al, ab-at
    cx = al + cx_ax * aw
    cy = ab - cy_ax * ah
    r  = r_ax * ah
    tick = r * 0.40   # inward tick length = 40% of radius
    rgb  = _hex_to_rgb(color)
    res  = Image.open(img_path)
    d    = ImageDraw.Draw(res)
    _solid(d, _circle_pts(cx, cy, r), rgb)
    lw = 5
    d.line([(cx,       cy - r),        (cx,       cy - r + tick)], fill=rgb, width=lw)  # N
    d.line([(cx,       cy + r),        (cx,       cy + r - tick)], fill=rgb, width=lw)  # S
    d.line([(cx - r,   cy),            (cx - r + tick, cy)],       fill=rgb, width=lw)  # E
    d.line([(cx + r,   cy),            (cx + r - tick, cy)],       fill=rgb, width=lw)  # W
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
    """Axes-fraction position of (ra0,dec0), plus 'spd' = axes-fraction
    distance per degree of declination, sampled toward dec_ref.

    Near the pole, dec_ref (conventionally dec0+1.0, chosen by the caller)
    can exceed +90°. cartopy's transform_point doesn't raise for that --
    it silently evaluates the projection past its valid domain and returns
    a point mirrored to the wrong side of the pole, which corrupts spd and
    produces misplaced/misshapen overlays for targets very close to the
    pole. Clamp the sample point to stay inside ±90° and renormalize by the
    actual (possibly shortened) delta actually used, so spd stays a true
    per-degree scale regardless of how close dec0 is to the pole.
    """
    x_c,y_c = p._proj.transform_point(ra0, dec0, p._crs)
    delta = dec_ref - dec0
    if dec0 + delta > 90.0:
        delta = 90.0 - dec0 - 1e-6
    elif dec0 + delta < -90.0:
        delta = -90.0 - dec0 + 1e-6
    if abs(delta) < 1e-9:
        delta = 1e-6
    x_r,y_r = p._proj.transform_point(ra_ref, dec0 + delta, p._crs)
    d2a = p.ax.transData + p.ax.transAxes.inverted()
    cx_ax,cy_ax = d2a.transform((x_c,y_c))
    rx_ax,ry_ax = d2a.transform((x_r,y_r))
    dist = math.hypot(rx_ax-cx_ax, ry_ax-cy_ax)
    return cx_ax, cy_ax, dist / abs(delta)


LABEL_COLOR = (200, 20, 20)


def _label_font(size_px):
    from PIL import ImageFont
    import matplotlib.font_manager as fm
    try:
        prop = fm.FontProperties(family="sans-serif", weight="bold")
        return ImageFont.truetype(fm.findfont(prop), size_px)
    except Exception:
        return ImageFont.load_default()


def add_overlay_label(img_path, ax_pos, cx_ax, cy_ax, text, font_scale=0.022):
    img = Image.open(img_path)
    W, H = img.size
    al, ar = ax_pos.x0*W, ax_pos.x1*W
    at, ab = (1-ax_pos.y1)*H, (1-ax_pos.y0)*H
    aw, ah = ar-al, ab-at
    x = al + cx_ax*aw; y = ab - cy_ax*ah
    draw = ImageDraw.Draw(img)
    draw.text((x,y), text, font=_label_font(max(14,int(ah*font_scale))),
              fill=LABEL_COLOR, anchor="lm")
    img.save(img_path)


def render_target_overlay(img_path, ax_pos, t, ra_bounds, proj_ctx=None,
                          outline_width=6, cross_width=4, min_r_px=None):
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
                           t["size_amin"]/60/2*spd, color,dashed,
                           outline_width=outline_width, min_r_px=min_r_px)
    elif shape == "circle_plus":
        add_overlay_circle(img_path,ax_pos,cx_ax,cy_ax,
                           t["size_amin"]/60/2*spd, color,dashed,bisect=True,
                           outline_width=outline_width, cross_width=cross_width,
                           min_r_px=min_r_px)
    elif shape == "star_target":
        add_overlay_star_target(img_path,ax_pos,cx_ax,cy_ax,
                                t.get("size_amin",10.0)/60*spd, color)
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
                        others=None, proj_ctx=None, font_scale=0.022):
    lra, ldec = _label_pos(t, fov, others)
    if proj_ctx is not None:
        cx_ax,cy_ax,_ = axes_frac_proj(proj_ctx,lra,ldec,lra,ldec+1.0)
    else:
        ra_min,ra_max,dec_min,dec_max = ra_bounds
        cx_ax,cy_ax = axes_frac_linear(lra,ldec,ra_min,ra_max,dec_min,dec_max)
    add_overlay_label(img_path,ax_pos,cx_ax,cy_ax,t.get("label",t["name"]),
                      font_scale=font_scale)


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


def _make_branded_jpg(chart, title, subtitle, out_path, quality=88):
    """Composite the title/subtitle header and the NBAS-branded footer
    (logo, QR, org name/site/tagline) onto the raw chart, same layout as
    the old PNG output, and save as a single JPEG. This replaces the old
    _make_png()/_make_pdf() pair -- one printable, on-screen-friendly
    image, no separate PDF."""
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
    canvas.save(out_path, format="JPEG", quality=quality)
    print(f"   Saved {out_path}")


def apply_branding(raw_chart_path, out_path, title, subtitle):
    """Composite branding onto the raw chart and save the single output
    JPG at out_path. raw_chart_path is a transient intermediate (written
    by starplot's export(), which needs a real file path) -- it is not
    part of the deliverable and the caller is expected to clean it up."""
    chart = Image.open(raw_chart_path).convert("RGB")
    _make_branded_jpg(chart, title, subtitle, out_path)


# ─────────────────────────────────────────────────────────────────────────────
#  Chart builders
# ─────────────────────────────────────────────────────────────────────────────

def _plot_stars(p, ra0, dec0, radius_deg, mag_limit,
                 size_min: float = STAR_SIZE_MIN, size_max: float = STAR_SIZE_MAX,
                 bayer_labels: bool = False, flamsteed_labels: bool = False,
                 name_labels: bool = False):
    """Plot field stars using starplot's own documented stars() method
    (the same one scripts/starmaps/generate.py already relies on), backed
    by the local BigSky catalog that STARPLOT_DATA_PATH points at (see
    module-level setup near the top of this file) -- not a live query.

    This replaces an earlier hand-rolled approach that (a) fetched stars
    from live Vizier/NOMAD, which proved unreliable across an entire
    session of testing (server-side empty responses, timeouts, a
    server-side filter+truncation interaction that zeroed out real
    results), and (b) plotted each star with p.marker() in a loop, which
    is not the right API for bulk star plotting -- stars were being
    fetched successfully in testing but never actually appearing on the
    rendered chart. stars() handles the correct coordinate projection,
    proper motion, and rendering in one call; this function's only job is
    to compute real min/max magnitude (for the adaptive size_fn and the
    custom legend) and hand stars() a size_fn built from that range.

    bayer_labels / flamsteed_labels: forwarded straight to stars() as its
    own bayer_labels=/flamsteed_labels= kwargs. These used to be handled by
    a separate call to p.bayer_labels()/p.flamsteed_labels() after this
    function returned -- checked directly against the installed starplot
    0.20.4 API (`dir(MapPlot)` / plotters/stars.py) and neither method
    exists on MapPlot at all in this version, only these two kwargs on
    stars() itself. The old call sites were wrapped in a try/except that
    silently swallowed the resulting AttributeError and printed a
    "skipped" warning, so --star-labels has never actually drawn a label
    in this script's history. Fixed here rather than left in place.

    name_labels: if False (default), suppresses stars() own "common name"
    label pass (e.g. "Sabik", "Alnasl") by passing label_fn=lambda s: None
    -- stars() always draws that pass regardless of bayer_labels/
    flamsteed_labels, so leaving it on prints proper names alongside every
    Bayer letter, which reads as redundant clutter once Bayer letters are
    already doing the identification work. Confirmed against a real test
    render for the AWV overview chart: proper names like "Paikauhale" and
    "Rosaliadecastro" were taking up real space next to their own Bayer
    letters with no added value for a star-hopping reference chart.

    Returns (mag_min, mag_max, size_fn), or (None, None, None) if no stars
    are found in the field -- matching the old function's contract so the
    legend code didn't need to change.
    """
    from starplot import _ as where_
    # starplot's own MapPlot.stars() takes a `catalog=` kwarg that defaults
    # to BIG_SKY_MAG11 (confirmed directly against the installed starplot
    # source, starplot/plotters/stars.py) if not passed explicitly. This is
    # independent of the `where=` magnitude filter below -- passing a higher
    # mag_limit in `where` does nothing if the underlying catalog file only
    # contains stars down to mag 11 in the first place. This was the actual
    # cause of --mag-limit having no visible effect: the two prior fixes
    # only touched the LOCAL_STAR_CATALOG_MAG_LIMIT clamp (used for legend
    # stats via fetch_stars_local()), never this call, so the rendered
    # chart kept using BIG_SKY_MAG11 no matter what was requested.
    from starplot.data.catalogs import BIG_SKY, BIG_SKY_MAG11

    catalog_path, effective_limit = _select_local_catalog(mag_limit)
    starplot_catalog = BIG_SKY if catalog_path == LOCAL_STAR_CATALOG_MAG16 else BIG_SKY_MAG11

    stats_df = fetch_stars_local(ra0, dec0, radius_deg, mag_limit)
    if stats_df.empty:
        return None, None, None

    mag_min = float(stats_df["magnitude"].min())
    mag_max = float(stats_df["magnitude"].max())
    size_fn = size_fn_for_range(mag_min, mag_max, size_min, size_max)

    def star_size_fn(star):
        return size_fn(star.magnitude)

    label_kwargs = {} if name_labels else {"label_fn": lambda s: None}

    from matplotlib.collections import PathCollection
    collections_before = set(id(c) for c in p.ax.collections)

    p.stars(
        where=[where_.magnitude < effective_limit],
        catalog=starplot_catalog,
        size_fn=star_size_fn,
        legend_label=None,  # we draw our own multi-swatch magnitude legend
        bayer_labels=bayer_labels,
        flamsteed_labels=flamsteed_labels,
        **label_kwargs,
    )

    # GeoAxes carries an opaque, full-extent "_ViewClippedPathPatch" (part
    # of cartopy's own view-boundary handling) that renders at zorder=1 --
    # the exact same zorder stars() uses for its marker collection -- and
    # ends up drawn AFTER the stars regardless of call order (confirmed by
    # inspecting ax.get_children(): this patch is consistently last in the
    # child list no matter when stars()/gridlines() are called). At equal
    # zorder, later-drawn wins, so that opaque white patch was painting
    # directly over every star marker -- stars were being fetched and
    # plotted correctly the whole time, just invisibly. Forcing the new
    # star collection(s) to a clearly higher zorder fixes this regardless
    # of draw order.
    for coll in p.ax.collections:
        if isinstance(coll, PathCollection) and id(coll) not in collections_before:
            coll.set_zorder(50)

    return mag_min, mag_max, size_fn


def _plot_constellation_lines(p, iau_ids, color="#4a90d9", width=2.0, alpha=0.65):
    """Draws constellation stick-figure lines for the given IAU
    abbreviation(s) (e.g. ["oph"] for Ophiuchus), using starplot's own
    constellations() method -- backed by the same local, offline
    constellations parquet + BigSky star catalog already required for
    field stars (see STARPLOT_DATA_PATH setup above), not a new network
    dependency.

    iau_ids: list of lowercase 3-letter IAU constellation abbreviations.
    Verified directly against the real bundled catalog (not guessed):
    reading constellations.0.3.3.parquet's own `iau_id` column confirms
    the key is the standard 3-letter abbreviation (e.g. "oph", "sgr",
    "sco"), lowercase, one row per constellation, 89 rows total.

    where=[_.iau_id.isin(iau_ids)] restricts the stick figure to exactly
    the requested constellation(s) -- without this filter, constellations()
    draws every constellation whose extent intersects the plot's viewing
    window, which for a wide field would pull in neighboring constellations
    (Ophiuchus borders Scorpius, Sagittarius, Serpens, Hercules, and more)
    that aren't wanted as reference clutter.
    """
    from ibis import _
    from starplot.styles import LineStyle

    style = LineStyle(color=color, width=width, alpha=alpha)
    p.constellations(where=[_.iau_id.isin(iau_ids)], style=style)
    print(f"   Constellation lines: {', '.join(iau_ids)}")


def _nice_ra_ticks(ra_min_deg, ra_max_deg, target_n=5):
    """RA gridline positions (degrees), snapped to standard RA-minute boundaries.
    Starplot divides by 15 before calling ra_formatter_fn, so we work in
    RA-minutes (1 RA-min = 0.25°) to ensure labels land on round clock values."""
    span_min = (ra_max_deg - ra_min_deg) * 4.0   # degrees → RA minutes
    nice_min = [1, 2, 5, 10, 15, 20, 30, 60, 120]
    step_min = next((s for s in nice_min if span_min / s <= target_n), 120)
    step_deg = step_min / 4.0                     # RA minutes → degrees
    first = math.ceil(ra_min_deg / step_deg) * step_deg
    ticks, t = [], first
    while t <= ra_max_deg + 1e-9:
        ticks.append(round(t, 8))
        t += step_deg
    return ticks


def _nice_dec_ticks(dec_min, dec_max, target_n=5):
    """Dec gridline positions (degrees), snapped to standard degree boundaries."""
    span = dec_max - dec_min
    nice_deg = [0.25, 0.5, 1.0, 2.0, 5.0, 10.0, 15.0, 30.0]
    step = next((s for s in nice_deg if span / s <= target_n), 30.0)
    first = math.ceil(dec_min / step) * step
    ticks, t = [], first
    while t <= dec_max + 1e-9:
        ticks.append(round(t, 8))
        t += step
    return ticks


def _mag_legend(fig, mag_min, mag_max, size_fn):
    """Legend swatches at (up to) 4 steps spanning the actual brightest→
    faintest star present in the field, drawn with the same size_fn used
    for the real markers -- so the legend always matches what's on the
    chart, instead of showing fixed V=6/8/10/12 reference sizes that may
    have nothing to do with what was actually plotted."""
    if size_fn is None:
        return  # no stars plotted -- nothing to show a legend for
    leg = fig.add_axes([0.71, 0.03, 0.27, 0.25])
    leg.set_xlim(0,1); leg.set_ylim(0,1)
    leg.set_facecolor("white"); leg.patch.set_alpha(0.88)
    for sp in leg.spines.values():
        sp.set_edgecolor("#aaaaaa"); sp.set_linewidth(0.8)
    leg.tick_params(left=False,bottom=False,labelleft=False,labelbottom=False)
    leg.text(.5,.93,"Magnitude",ha="center",va="top",
             fontsize=20,fontweight="bold",transform=leg.transAxes)
    if mag_max > mag_min:
        steps = [mag_min + f * (mag_max - mag_min) for f in (0.0, 1/3, 2/3, 1.0)]
    else:
        steps = [mag_min]
    ys = [.72, .52, .33, .14][:len(steps)]
    for mag, y in zip(steps, ys):
        sz = size_fn(mag)
        # sz is already in matplotlib scatter's native s= units (points^2)
        # now that size_fn's range matches what's used for the real star
        # markers on the main plot -- no separate rescaling needed here
        # (an earlier version compensated for the old, much smaller
        # STAR_SIZE_MIN/MAX range; that compensation would now wildly
        # over-inflate these swatches).
        leg.scatter([.18],[y],s=sz,c="black",zorder=5)
        leg.text(.34,y,f"V = {mag:.1f}",va="center",fontsize=20)


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

    style = PlotStyle().extend(extensions.GRAYSCALE, extensions.MAP)
    p = MapPlot(projection=Mercator(),
                ra_min=ra_min, ra_max=ra_max,
                dec_min=dec_min, dec_max=dec_max,
                style=style, resolution=2048,
                ephemeris=EPHEMERIS)
    constellation_ids = field.get("constellation_lines")
    if constellation_ids:
        _plot_constellation_lines(p, constellation_ids)

    size_min = field.get("star_size_min", STAR_SIZE_MIN)
    size_max = field.get("star_size_max", STAR_SIZE_MAX)
    star_labels = field.get("star_labels", False)
    if field.get("fetch_stars", True):
        mag_min, mag_max, size_fn = _plot_stars(
            p, ra0, dec0, max(half_ra, half) * 1.15, ml, size_min, size_max,
            bayer_labels=star_labels, flamsteed_labels=star_labels)
    else:
        mag_min, mag_max, size_fn = None, None, None
        print("   Star fetch disabled")

    p.gridlines(tick_marks=True,
                ra_locations =_nice_ra_ticks(ra_min,  ra_max),
                dec_locations=_nice_dec_ticks(dec_min, dec_max),
                ra_formatter_fn=ra_fmt, dec_formatter_fn=dec_fmt)
    _mag_legend(p.fig, mag_min, mag_max, size_fn)
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

    # Near the pole, dec0+half can exceed +90°, which starplot/cartopy will
    # reject outright. Clamp the northern edge at the pole itself -- you
    # physically can't have a symmetric FOV that goes past it anyway.
    dec_hi = min(90.0, dec0 + half)
    if dec_hi < dec0 + half:
        print(f"   NOTE: FOV clipped at the pole (dec0+half = {dec0+half:.2f}° > 90°)")

    print(f"\n── {field['title']}  FOV {fov:.2f}° (StereoNorth)  ({len(targets)} target(s))")

    style = PlotStyle().extend(extensions.GRAYSCALE, extensions.MAP)
    p = MapPlot(projection=StereoNorth(center_ra=ra0),
                ra_min=0, ra_max=360,
                dec_min=dec0-half, dec_max=dec_hi,
                style=style, resolution=2048,
                ephemeris=EPHEMERIS)
    xc,yc = p._proj.transform_point(ra0,dec0,p._crs)
    xn,yn = p._proj.transform_point(ra0,dec_hi,p._crs)
    r = math.sqrt((xn-xc)**2+(yn-yc)**2)
    p.ax.set_xlim(xc-r,xc+r); p.ax.set_ylim(yc-r,yc+r)

    constellation_ids = field.get("constellation_lines")
    if constellation_ids:
        _plot_constellation_lines(p, constellation_ids)

    size_min = field.get("star_size_min", STAR_SIZE_MIN)
    size_max = field.get("star_size_max", STAR_SIZE_MAX)
    star_labels = field.get("star_labels", False)
    if field.get("fetch_stars", True):
        mag_min, mag_max, size_fn = _plot_stars(
            p, ra0, dec0, half * 1.15, ml, size_min, size_max,
            bayer_labels=star_labels, flamsteed_labels=star_labels)
    else:
        mag_min, mag_max, size_fn = None, None, None
        print("   Star fetch disabled")

    p.gridlines(tick_marks=False,
                ra_locations =_nice_ra_ticks(ra0 - half, ra0 + half),
                dec_locations=_nice_dec_ticks(dec0 - half, dec_hi),
                ra_formatter_fn=ra_fmt, dec_formatter_fn=dec_fmt)
    _mag_legend(p.fig, mag_min, mag_max, size_fn)
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
  python finder_charts.py --selftest        # geometry checks, no network needed

assets (place alongside this script):
  nbas-logo.svg      branding logo  (gracefully skipped if absent)
  nbas-qrcode.svg    QR code        (gracefully skipped if absent)
""")

    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--objects", nargs="+", metavar="NAME",
                      help="Object name(s) to resolve via SIMBAD — one chart, "
                           "all objects sharing a single field")
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
    parser.add_argument("--no-stars",    action="store_true", dest="no_stars",
                        help="Skip Vizier star fetch")
    parser.add_argument("--star-labels",   action="store_true", dest="star_labels",
                        help="Add Bayer (Greek letter) and Flamsteed number labels")
    parser.add_argument("--constellation-lines", nargs="+", default=None,
                        metavar="IAU_ID", dest="constellation_lines",
                        help="Draw stick-figure lines for these constellations "
                             "(lowercase 3-letter IAU abbreviations, e.g. oph sgr). "
                             "Restricted to exactly the ones listed -- see "
                             "_plot_constellation_lines() for why.")
    parser.add_argument("--min-star-size", type=float, default=STAR_SIZE_MIN,
                        dest="min_star_size",
                        help=f"Minimum star marker size, matplotlib scatter s= units i.e. "
                             f"points^2 (default: {STAR_SIZE_MIN}; increase to make faint "
                             f"stars more visible)")
    parser.add_argument("--max-star-size", type=float, default=STAR_SIZE_MAX,
                        dest="max_star_size",
                        help=f"Maximum star marker size, matplotlib scatter s= units i.e. "
                             f"points^2 (default: {STAR_SIZE_MAX}; caps how big the "
                             f"brightest star in the FIELD is drawn -- auto-scaling uses "
                             f"this together with --min-star-size and the brightest/"
                             f"faintest star actually present, so a field with no truly "
                             f"bright stars won't force its brightest one to this size)")
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
        "fetch_stars":   not args.no_stars,
        "star_labels":   args.star_labels,
        "constellation_lines": args.constellation_lines,
        "star_size_min": args.min_star_size,
        "star_size_max": args.max_star_size,
        "targets":       targets,
    }
    if args.projection:
        field["projection"] = args.projection
    else:
        _, dec0, _ = compute_field_center_and_fov(field)
        if dec0 > 75:
            field["projection"] = "StereoNorth"

    fields = [field]

    os.makedirs(out_dir, exist_ok=True)

    for field in fields:
        s       = slug(field["chart_name"])
        out_jpg = os.path.join(out_dir, f"{s}.jpg")
        _, _, fov = compute_field_center_and_fov(field)
        names    = ", ".join(t["name"] for t in field["targets"])
        subtitle = (f"{names} · FOV {fov:.2f}°"
                    + (f" · {field['info']}" if field.get("info") else ""))

        # The unbranded chart is a transient intermediate -- starplot's
        # export() needs a real file path to write to, but it's not part
        # of the deliverable (no more *_raw.png kept alongside the output,
        # matching the starmap pattern). Write it to a temp file and
        # remove it once branding has been composited on top.
        with tempfile.NamedTemporaryFile(suffix="_raw.png", delete=False) as tmp:
            raw_png = tmp.name
        try:
            if field.get("projection") == "StereoNorth":
                make_raw_chart_stereonorth(field, raw_png)
            else:
                make_raw_chart(field, raw_png)

            print("   Applying NBAS branding …")
            apply_branding(raw_png, out_jpg, field["title"], subtitle)
        finally:
            if os.path.exists(raw_png):
                os.remove(raw_png)

    n = len(fields)
    print(f"\n✓  {n} finder chart{'s' if n != 1 else ''} complete.")


if __name__ == "__main__":
    main()
