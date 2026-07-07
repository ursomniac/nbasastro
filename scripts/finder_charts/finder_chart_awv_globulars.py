#!/usr/bin/env python3
"""
AWV Globulars -- Whole-Ophiuchus Overview Chart
=================================================
One-off companion to finder_charts.py, purpose-built for the "Natives,
Immigrants, and Suspects" A Wider View piece. Rather than 20 individual
finder charts, this draws all 20 observed globular clusters (plus NGC 6325,
mentioned in the text but not yet observed) on a single wide-field locator
map, with:

  - Ophiuchus constellation stick-figure lines, for orientation
  - Bayer (Greek-letter) labeled reference stars
  - the same NBAS globular-cluster overlay convention (yellow circle,
    solid outline, bisected with "+") used by every other finder chart

Why this is a separate script rather than a --objects run of
finder_charts.py: that script's field-framing helper
(compute_field_center_and_fov / FOV_PADDING=3.0) is tuned for tight
single/pair-object fields where "plenty of context around the target"
means a degree or two of padding around a small angular size. Run against
this 21-target, ~22 deg (RA) x 33 deg (Dec) spread, it produces a ~133 deg
FOV -- confirmed by direct calculation, not a guess -- because a fixed 3x
padding multiplier on a bounding-CIRCLE radius around a widely-scattered,
elongated point cloud blows up fast. A real locator map for "the whole
constellation" needs a plain padded bounding RECTANGLE instead, which is
what compute_overview_bounds() below does.

Everything else (star source, branding, overlay styling, label placement,
gridlines, magnitude legend) is reused directly from finder_charts.py --
see the `import finder_charts as fc` block below -- so this chart matches
the rest of the site's finder charts in look and convention.

Cluster coordinates: computed at runtime from each cluster's Galactic
(l, b) as listed in this article's own table.md, via astropy's Galactic
-> ICRS transform (a closed-form coordinate conversion, no network
needed). Distance is irrelevant to this transform -- (l, b) alone fixes
a direction on the sky -- so table.md's distance column doesn't need to
be touched here.

Star depth: table.md-adjacent research (direct read of the same local
BigSky mag<=11 parquet finder_charts.py already uses, cross-matched
against its bundled star_designations table for Bayer letters) found
these real star counts in the padded field this script actually draws:

    V <= 7.0   :   320 stars
    V <= 7.5   :   511 stars
    V <= 8.0   :   899 stars   <- MAG_LIMIT default
    V <= 8.5   : 1,560 stars
    V <= 9.0   : 2,634 stars
    V <= 10.0  : 7,120 stars
    V <= 11.0  : 16,658 stars (full mag<=11 field, no padding)

67 unique Bayer-designated stars sit in the padded field, brightest at
mag 2.43 (eta Oph, "Sabik"), faintest at mag 9.62 -- i.e. every real
Bayer-lettered star in this part of the sky is comfortably brighter than
MAG_LIMIT=8.0 except that single mag-9.62 outlier, so the default depth
loses essentially none of the reference-star labeling value. Override
with --mag-limit if a denser (or sparser) field is wanted after seeing
the actual rendered chart -- per finder_charts.py's own long-standing
practice, there's no substitute for looking at the real output.

Usage:
    python finder_chart_awv_globulars.py
    python finder_chart_awv_globulars.py --mag-limit 9.0
    python finder_chart_awv_globulars.py --output-dir /path/to/printable

Requirements: same as finder_charts.py (starplot, astropy, astroquery,
pandas, pillow, cairosvg, numpy) -- astroquery is not actually used here
(no SIMBAD lookups; coordinates come from astropy's Galactic frame
instead), but is left in the shared requirement list since it lives
alongside finder_charts.py's own SIMBAD-driven --objects mode.
"""

import argparse
import math
import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import finder_charts as fc  # noqa: E402  (STARPLOT_DATA_PATH env var must be
                              # set before starplot is imported anywhere --
                              # finder_charts.py does that at its own module
                              # level, so it must be imported first.)

import matplotlib.pyplot as plt  # noqa: E402


# ─────────────────────────────────────────────────────────────────────────────
#  The 21 clusters -- (name, label, l_deg, b_deg, size_amin)
# ─────────────────────────────────────────────────────────────────────────────
#
# l, b, and size_amin (angular diameter) are taken directly from this
# article's table.md. NGC 6325 is included for completeness (it's named
# in the article's closing section) even though it has no observation
# photo of its own yet -- see observed=False below, which only affects
# this script not at all today, but is kept as an honest record in case a
# future revision wants to visually distinguish "observed" vs "not yet"
# on this chart (e.g. a hollow vs filled marker). Left as a flag rather
# than silently indistinguishable from the other 20.

CLUSTERS = [
    # name         label        l      b     size_amin  observed
    ("M 9",        "M 9",         5.5,  10.7, 12.0, True),
    ("M 10",       "M 10",       15.1,  23.1, 20.0, True),
    ("M 12",       "M 12",       15.7,  26.3, 15.8, True),
    ("M 14",       "M 14",       21.3,  14.8, 11.0, True),
    ("M 19",       "M 19",      356.9,   9.4, 17.0, True),
    ("M 62",       "M 62",      353.6,   7.3, 15.1, True),
    ("M 107",      "M 107",       3.4,  23.0, 12.9, True),
    ("NGC 6235",   "NGC 6235",  358.9,  13.5,  5.0, True),
    ("NGC 6284",   "NGC 6284",  358.3,   9.9,  6.2, True),
    ("NGC 6287",   "NGC 6287",    0.1,  11.0,  4.8, True),
    ("NGC 6293",   "NGC 6293",  357.6,   7.8,  8.1, True),
    ("NGC 6304",   "NGC 6304",  355.8,   5.4,  7.9, True),
    ("NGC 6316",   "NGC 6316",  357.2,   5.8,  5.4, True),
    ("NGC 6342",   "NGC 6342",    4.9,   9.7,  4.4, True),
    ("NGC 6355",   "NGC 6355",  359.6,   5.4,  4.2, True),
    ("NGC 6356",   "NGC 6356",    6.7,  10.2, 10.0, True),
    ("NGC 6366",   "NGC 6366",   18.4,  16.0, 12.9, True),
    ("NGC 6401",   "NGC 6401",    3.5,   4.0,  4.8, True),
    ("NGC 6426",   "NGC 6426",   28.1,  16.2,  4.2, True),
    ("NGC 6517",   "NGC 6517",   19.2,   6.8,  4.0, True),
    ("NGC 6325",   "NGC 6325",    1.0,   8.0,  4.0, False),
]

CONSTELLATION_IDS = ["oph"]  # Ophiuchus -- verified against the real bundled
                             # constellations.0.3.3.parquet `iau_id` column
                             # (89 rows, one per IAU constellation; "oph" is
                             # the exact key for Ophiuchus in that table).

MAG_LIMIT_DEFAULT = 8.0      # see module docstring for the real star-count
                             # evidence behind this default
BOX_PADDING_DEG = 2.0        # flat degrees of margin added on every side of
                             # the clusters' own bounding box -- NOT a
                             # multiplicative factor (see module docstring
                             # for why compute_field_center_and_fov's 3x
                             # circumscribe-and-pad approach is wrong here)

# Explicit (dra_deg, ddec_deg) label-placement overrides, found necessary
# by looking at an actual test render (not guessed up front) -- see
# finder_charts._label_pos()'s own "no substitute for looking at the
# actual rendered chart" note, which applies just as much here:
#
#   M 107     -- the westernmost target (lowest RA) in the whole set.
#               _label_pos()'s default "nudge away from the mean of all
#               other targets" pushes its label EVEN FURTHER west (i.e.
#               further right on-screen, since RA increases leftward
#               here) because every other target sits to its east --
#               which drove the label straight off the right edge of the
#               chart in the first test render. Pulled back toward the
#               interior (higher RA => further left on-screen) instead.
#   NGC 6356  -- sits only ~0.7 deg (dec) / 1.1 deg (RA) from M 9, close
#               enough that the generic away-from-centroid nudge (which
#               reacts to the mean position of all 20 OTHER targets, not
#               specifically its nearest neighbor) left the two labels
#               overlapping in the first test render. Nudged further
#               north, clear of M 9.
LABEL_OFFSET_OVERRIDES = {
    "M 107":    (1.6, 0.3),
    "NGC 6356": (0.3, 1.2),
}


def build_targets():
    """Converts CLUSTERS' (l, b) to (ra, dec) via astropy's Galactic->ICRS
    transform and returns finder_charts.py-style target dicts."""
    from astropy.coordinates import SkyCoord
    import astropy.units as u

    targets = []
    for name, label, l_deg, b_deg, size_amin, observed in CLUSTERS:
        c = SkyCoord(l=l_deg * u.deg, b=b_deg * u.deg, frame="galactic").icrs
        t = {
            "name": name,
            "label": label,
            "ra": c.ra.deg,
            "dec": c.dec.deg,
            "object_type": "globular_cluster",
            "size_amin": size_amin,
            "observed": observed,
        }
        if name in LABEL_OFFSET_OVERRIDES:
            t["label_offset"] = LABEL_OFFSET_OVERRIDES[name]
        targets.append(t)
    return targets


def compute_overview_bounds(targets, padding_deg=BOX_PADDING_DEG):
    """Plain padded bounding RECTANGLE around every target's position (not
    the circumscribe-a-circle-then-pad-3x approach in
    finder_charts.compute_field_center_and_fov, which is tuned for tight
    single/pair-object fields -- see module docstring). Each target's own
    angular radius is added to its extreme-position contribution so a big
    cluster near the edge doesn't get clipped.

    Returns (ra_min, ra_max, dec_min, dec_max) in degrees.
    """
    ras, decs, radii = [], [], []
    for t in targets:
        ras.append(t["ra"])
        decs.append(t["dec"])
        radii.append(fc.target_radius_deg(t))

    # Declination is a simple linear extent. RA needs a per-target
    # cos(dec) correction to convert "how far this target's own angular
    # radius reaches in RA" into real RA degrees, since 1 deg of RA
    # subtends less real angle at higher |dec|.
    dec_min = min(d - r for d, r in zip(decs, radii)) - padding_deg
    dec_max = max(d + r for d, r in zip(decs, radii)) + padding_deg

    ra_extents_min, ra_extents_max = [], []
    for ra, dec, r in zip(ras, decs, radii):
        cosd = max(math.cos(math.radians(dec)), 0.05)
        ra_extents_min.append(ra - r / cosd)
        ra_extents_max.append(ra + r / cosd)
    ra_min = min(ra_extents_min) - padding_deg
    ra_max = max(ra_extents_max) + padding_deg

    return ra_min, ra_max, dec_min, dec_max


def make_overview_chart(targets, ra_min, ra_max, dec_min, dec_max,
                        mag_limit, out_path, constellation_ids=None,
                        star_labels=True):
    """Modeled closely on finder_charts.make_raw_chart(), but takes an
    explicit rectangular (ra_min, ra_max, dec_min, dec_max) box instead of
    deriving one from a single FOV/half value -- see module docstring for
    why that matters for a 21-target, non-circular field like this one."""
    from starplot import MapPlot, Mercator
    from starplot.styles import PlotStyle, extensions

    ra0  = (ra_min + ra_max) / 2.0
    dec0 = (dec_min + dec_max) / 2.0
    ra_span, dec_span = ra_max - ra_min, dec_max - dec_min
    radius_deg = math.hypot(ra_span, dec_span) / 2.0  # for the star-fetch
                                                       # search radius only

    print(f"\n── Ophiuchus globular cluster overview  "
          f"RA [{ra_min:.2f}, {ra_max:.2f}] deg  "
          f"Dec [{dec_min:.2f}, {dec_max:.2f}] deg  "
          f"({len(targets)} targets)")

    style = PlotStyle().extend(extensions.GRAYSCALE, extensions.MAP)
    p = MapPlot(projection=Mercator(),
                ra_min=ra_min, ra_max=ra_max,
                dec_min=dec_min, dec_max=dec_max,
                style=style, resolution=3200,   # larger than the 2048 default
                ephemeris=fc.EPHEMERIS)         # -- this field is much wider
                                                 # than a typical finder chart
                                                 # and needs the extra pixels
                                                 # to keep 20+ labels legible.

    if constellation_ids:
        fc._plot_constellation_lines(p, constellation_ids)

    # bayer_labels=True / flamsteed_labels=False / name_labels=False --
    # per direct feedback on a real test render, Flamsteed numbers and
    # (especially) plain star names ("Sabik", "Paikauhale", ...) added
    # clutter without adding reference value once Bayer (Greek-letter)
    # labels are already doing the identification work.
    mag_min, mag_max, size_fn = fc._plot_stars(
        p, ra0, dec0, radius_deg * 1.1, mag_limit,
        bayer_labels=star_labels, flamsteed_labels=False, name_labels=False)

    p.gridlines(tick_marks=True,
                ra_locations =fc._nice_ra_ticks(ra_min, ra_max),
                dec_locations=fc._nice_dec_ticks(dec_min, dec_max),
                ra_formatter_fn=fc.ra_fmt, dec_formatter_fn=fc.dec_fmt)
    # No magnitude legend on this chart -- per feedback, the default
    # legend box (sized as a fraction of the whole figure, same as every
    # other finder chart) reads as oversized with huge inter-swatch
    # gaps at this chart's much larger absolute resolution, and isn't
    # pulling its weight next to 21 labeled clusters and Bayer stars.

    p.export(out_path, padding=0.3)
    ax_pos = p.ax.get_position()
    plt.close("all")
    print(f"   Starfield + constellation lines → {os.path.basename(out_path)}")

    ra_bounds = (ra_min, ra_max, dec_min, dec_max)
    # A 21-target field packed with 899+ background stars needs much
    # smaller on-chart text than finder_charts.py's own default (0.022,
    # tuned for a single/pair-target close-up chart with 2-3 labels total)
    # -- confirmed by a real test render at the default scale, where every
    # label spanned a large fraction of the image width and the 8-object
    # Main-Bulge core clump was almost entirely illegible overlapping text.
    LABEL_FONT_SCALE = 0.010
    # finder_charts._label_pos()'s default nudge distance (r + 0.025*fov)
    # reads as "labels floating far from their marker" at this chart's
    # scale -- per feedback. Scaling the fov value fed into that formula
    # down proportionally tightens every label's gap without touching
    # finder_charts.py's own default behavior for other charts.
    LABEL_GAP_SCALE = 0.35
    fov_for_labels = max(ra_span, dec_span) * LABEL_GAP_SCALE
    # Marker styling for THIS chart only (finder_charts.py's own single/
    # pair-object charts keep their existing 6px outline / 4px cross,
    # sized for a much larger true-to-scale marker at a tight FOV).
    # MIN_MARKER_PX enforces a visible yellow-fill + black-rim floor --
    # per feedback + a real test render, several of the smallest clusters
    # (4-5 arcmin) rendered at true angular scale here round down to just
    # 1-2px, at which point even a thin outline swallows the fill
    # entirely and only the label is visible, no marker at all.
    MIN_MARKER_PX  = 9
    OUTLINE_WIDTH  = 2
    CROSS_WIDTH    = 2
    for t in targets:
        fc.render_target_overlay(out_path, ax_pos, t, ra_bounds,
                                 outline_width=OUTLINE_WIDTH,
                                 cross_width=CROSS_WIDTH,
                                 min_r_px=MIN_MARKER_PX)
        fc.render_target_label(out_path, ax_pos, t, fov_for_labels,
                               ra_bounds, others=targets,
                               font_scale=LABEL_FONT_SCALE)
        print(f"   Overlay + label: {t['name']}")


def main():
    parser = argparse.ArgumentParser(
        prog="finder_chart_awv_globulars.py",
        description="Whole-Ophiuchus overview chart for the AWV globulars article")
    parser.add_argument("--mag-limit", type=float, default=MAG_LIMIT_DEFAULT,
                        dest="mag_limit",
                        help=f"Star depth (default: {MAG_LIMIT_DEFAULT} -- "
                             f"see module docstring for the real star-count "
                             f"evidence behind this default)")
    parser.add_argument("--no-star-labels", action="store_true",
                        dest="no_star_labels",
                        help="Skip Bayer/Flamsteed star labels")
    parser.add_argument("--no-constellation-lines", action="store_true",
                        dest="no_constellation_lines",
                        help="Skip Ophiuchus constellation lines")
    parser.add_argument("--output-dir", default=None, dest="output_dir",
                        help="Output directory (default: this script's directory)")
    parser.add_argument("--chart-name", default="awv-globulars-overview",
                        dest="chart_name", help="Output filename stem")
    args = parser.parse_args()

    out_dir = args.output_dir or HERE
    os.makedirs(out_dir, exist_ok=True)
    out_jpg = os.path.join(out_dir, f"{fc.slug(args.chart_name)}.jpg")

    targets = build_targets()
    ra_min, ra_max, dec_min, dec_max = compute_overview_bounds(targets)

    title = "Globular Clusters of Ophiuchus — Overview"
    subtitle = f"V ≤ {args.mag_limit:g} · Ophiuchus constellation lines"

    with tempfile.NamedTemporaryFile(suffix="_raw.png", delete=False) as tmp:
        raw_png = tmp.name
    try:
        make_overview_chart(
            targets, ra_min, ra_max, dec_min, dec_max,
            mag_limit=args.mag_limit,
            out_path=raw_png,
            constellation_ids=(None if args.no_constellation_lines
                              else CONSTELLATION_IDS),
            star_labels=not args.no_star_labels,
        )
        print("   Applying NBAS branding …")
        fc.apply_branding(raw_png, out_jpg, title, subtitle)
    finally:
        if os.path.exists(raw_png):
            os.remove(raw_png)

    print(f"\n✓  Overview chart complete → {out_jpg}")


if __name__ == "__main__":
    main()
