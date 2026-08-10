#!/usr/bin/env python3
"""
AWV Perseus Arm -- Deneb-to-Double-Cluster Overview Chart
=============================================================
v4 -- fixed from real render feedback: (1) dec gridline labels were
getting clipped -- the crop (set_xlim/set_ylim) was tight to the exact
content boundary, giving starplot's dec-axis labels (drawn just outside
the data area, at/near dec_min/dec_max) nowhere to render; added a 5%
margin to the crop on all sides (CROP_MARGIN_FRAC in
make_overview_chart_stereonorth) -- the 5% figure is a guess, not measured
against actual label pixel widths, confirm visually; (2) added a
--rotate {cw,ccw,none} option (default cw) that physically rotates the
finished raw chart PNG 90 deg via PIL, applied AFTER all overlay/label
drawing but BEFORE apply_branding(), so the title/footer stay upright and
only the star-map content turns. This doesn't remove the "white space" at
its root -- the field maps to a curved arc under StereoNorth (see
_sample_boundary_xy docstring), and an arc's bounding box always has empty
corners -- but if the exported canvas is currently the "wrong" orientation
relative to the content's true landscape/portrait shape, a 90 deg turn can
fill the frame much better. Direction (cw vs ccw) is an unverified guess;
rerun with --rotate ccw if cw looks wrong. See rotate_chart_image()
docstring for the full reasoning.

v3 -- fixed from real render feedback: (1) NGC 7160/NGC 7129 were showing
as two huge out-of-place blue blobs -- SIMBAD's reported size for both
(144'/120') was wrong for this purpose, now overridden to the same fixed
size every cluster uses; (2) markers read as too small -- MIN_MARKER_PX
9->16; (3) labels overlapping in the tight Cassiopeia group and the two
close pairs -- added explicit LABEL_OFFSET_OVERRIDES computed from their
real coordinates; (4) added constellation NAME labels (CASSIOPEIA, CEPHEUS,
etc.) -- no equivalent existed anywhere in finder_charts.py, built fresh in
render_constellation_labels() below, anchor positions are estimates, not
verified; (5) dropped NGC 188 and Deneb per your call that neither is
needed and both were stretching the frame more than they were worth.

v2 -- switched from Mercator to StereoNorth after the first real render
came back badly distorted (Mercator keeps RA gridlines equally spaced
regardless of declination; at this field's dec 45-70 range that's a
1.4x-3x horizontal stretch, visible in the first render as warped
constellation lines and oddly-separated cluster pairs). See "WHAT CHANGED
IN v2" below.

One-off companion to finder_charts.py, modeled on
finder_chart_awv_globulars.py (the Ophiuchus globulars overview chart),
purpose-built for the "Exploring the Perseus Arm Through Fall Open
Clusters" AWV piece. Draws every cluster named in that article -- the
Perseus Arm gallery, the Local Arm "closer than you'd think" mentions, and
the "Other" bucket (NGC 188, Berkeley 59) -- plus Deneb as the walk's
starting landmark, on one wide, landscape-oriented locator map, with:

  - Cygnus / Cepheus / Cassiopeia / Perseus / Lacerta constellation lines
  - Bayer-labeled reference stars
  - clusters color-coded by which part of the article's story they belong
    to (Perseus Arm / Local Arm / Other) -- see CATEGORY_COLOR and
    render_target_overlay_by_category() below

WHAT CHANGED IN v2
-------------------
1. Projection: Mercator -> StereoNorth. finder_charts.py's existing
   StereoNorth path (make_raw_chart_stereonorth) is built for a compact,
   roughly circular field symmetric around a center point -- appropriate
   for its usual near-pole use case, but this chart's field is a wide
   landscape rectangle, not a circle, and isn't centered anywhere near the
   true pole either (dec0 is roughly 55-60, not 90). Reused StereoNorth
   itself (still the right projection choice -- it's pole-anchored, so it
   doesn't have Mercator's equator-biased meridian spacing at ANY
   declination, not just near 90), but replaced the existing function's
   single-radius circular crop with a boundary-sampled rectangular crop:
   every point along all 4 edges of the RA/Dec box (not just the 4
   corners -- confirmed by a standalone synthetic-projection test that
   corners-only clips real content for a box shaped like this one) gets
   transformed via the same p._proj.transform_point() call
   make_raw_chart_stereonorth already uses, and the final view is set via
   ax.set_xlim/set_ylim from the min/max of ALL those points. This part of
   the geometry (the sampling + bounding logic itself) was verified
   standalone against a synthetic polar-style transform before being
   wired in here -- see the chat history for that test. What's NOT
   verified is starplot/cartopy's actual transform_point() behavior on
   this specific field -- that needs a real render.

2. Star size: STAR_SIZE_MIN/MAX carried over from
   finder_chart_awv_globulars.py were tuned for Ophiuchus's much sparser
   field and rendered as oversized, cluttering dots here (per direct
   feedback on the v1 render) -- this field sits along the Milky Way
   itself and is far more star-rich at the same mag limit. Cut roughly an
   order of magnitude smaller as a first pass (see STAR_SIZE_MIN/MAX
   below) -- still just a first pass, needs the same "look at the real
   render and adjust" step every other tuning constant in this file does.

3. Coordinates for the 12 Perseus Arm gallery objects are now hardcoded
   from your own distance-table source (both (l,b) and (ra,dec) given;
   cross-checked against each other via astropy to within 5-23 arcsec,
   consistent with rounding, not a transcription error) instead of
   resolved live via SIMBAD -- removes that uncertainty entirely for the
   objects that matter most. The other 5 targets (Local Arm x2, Other x2,
   Deneb) still resolve via SIMBAD since no hardcoded coordinates were
   given for those.

WHAT'S STILL NOT VERIFIED (need a real run to confirm)
---------------------------------------------------------
  - transform_point()'s actual behavior on this field's RA range, which
    still straddles the 0h/24h seam the same way it did under Mercator
    (unwrap-then-bound logic unchanged from v1, already confirmed correct
    as pure math -- see finder_chart_awv_globulars.py-style comments in
    compute_overview_bounds() below).
  - Whether "cyg"/"cep"/"cas"/"per"/"lac" are exactly right against your
    real constellations.0.3.3.parquet iau_id column.
  - Whether NGC 7160 / NGC 7129 / NGC 188 / Berkeley 59 / Deneb resolve
    cleanly via SIMBAD (should be fine -- all well-known -- but check the
    console output for WARNING: no SIMBAD match lines).
  - LABEL_FONT_SCALE / LABEL_GAP_SCALE / MIN_MARKER_PX, still carried over
    unchanged from the Ophiuchus script -- likely need their own tuning
    pass for this chart's different object spacing.
  - Whether the new star sizes are actually right, not just "less wrong."

Usage:
    python finder_chart_awv_perseus_arm.py
    python finder_chart_awv_perseus_arm.py --mag-limit 8.5
    python finder_chart_awv_perseus_arm.py --no-category-colors
    python finder_chart_awv_perseus_arm.py --output-dir /path/to/printable

Requirements: same as finder_charts.py (starplot, astropy, astroquery,
pandas, pillow, cairosvg, numpy).
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
#  Targets, by category
# ─────────────────────────────────────────────────────────────────────────────

# Hardcoded from your distance-table source: both (l,b) and (ra,dec) were
# given for these 12; cross-validated against each other via astropy's
# Galactic->ICRS transform to within 5-23 arcsec (consistent with the
# 2-decimal-place precision of the given l,b values, not a discrepancy).
# "M 101" in your table is treated as M 103 (NGC 581) -- confirmed by
# these coordinates matching M 103's real position; M101 (Pinwheel Galaxy)
# is nowhere near RA 1h33m/Dec +60.65, so this isn't a fresh guess, it's
# the same typo flagged and corrected two revisions ago, now with an
# independent coordinate check backing that call up further.
PERSEUS_ARM_COORDS = {
    # name         ra_deg      dec_deg     label
    "NGC 457":  (19.89654,  58.28697,  "NGC 457"),
    "M 103":    (23.34583,  60.64994,  "M 103"),
    "NGC 654":  (25.99750,  61.88272,  "NGC 654"),
    "NGC 659":  (26.10000,  60.67328,  "NGC 659"),
    "NGC 663":  (26.53758,  61.23286,  "NGC 663"),
    "NGC 7380": (341.83738, 58.13203,  "NGC 7380"),
    "NGC 7788": (359.19067, 61.39994,  "NGC 7788"),
    "NGC 7789": (359.34992, 56.70789,  "NGC 7789"),
    "NGC 7790": (359.60087, 61.20828,  "NGC 7790"),
    "NGC 869":  (34.75004,  57.12828,  "NGC 869"),
    "NGC 884":  (35.60437,  57.13869,  "NGC 884"),
    "IC 1805":  (38.20000,  61.46161,  "IC 1805"),
}
# Angular size isn't in the given table, and at this chart's wide overview
# scale it barely matters -- MIN_MARKER_PX (below) already floors every
# cluster's on-chart radius regardless of true angular size. 15' is a
# round, roughly-representative size for this list, not a precise value.
DEFAULT_SIZE_AMIN = 15.0

LOCAL_ARM = ["NGC 7160", "NGC 7129"]           # resolved via SIMBAD
OTHER = ["Berkeley 59"]                        # NGC 188 dropped per your
                                                # note -- not needed, and
                                                # its dec ~85 was a big part
                                                # of why the field was so
                                                # tall.
LANDMARK_STARS = []                            # Deneb dropped -- same
                                                # reasoning, on the RA side.

CATEGORY_COLOR = {
    "perseus_arm": "#FFD700",   # gold -- matches finder_charts.py's own
                                 # existing open_cluster convention
    "local_arm":   "#3399FF",   # blue
    "other":       "#FF6633",   # orange
}

CONSTELLATION_IDS = ["cyg", "cep", "cas", "per", "lac"]
# NOTE: dropping Deneb tightens the field enough that Cygnus itself may
# barely clip the frame now, if at all -- left in the list since the
# article's text still opens at Deneb conceptually, but don't be surprised
# if there's little or no "cyg" stick figure actually visible.

# Rough anchor points for constellation NAME labels (RA deg, Dec deg) --
# finder_charts.py has no existing function for this at all (only stick-
# figure LINES via _plot_constellation_lines(); no name-label placement
# anywhere in that file), so this is new, and these coordinates are
# estimates from general knowledge of where each constellation sits, NOT
# verified against your actual bundled constellation boundary/line data.
# Treat as a first guess -- almost certainly needs repositioning once you
# can see where these land relative to the tightened (no-Deneb, no-NGC188)
# frame and the actual stick figures.
CONSTELLATION_LABEL_ANCHORS = {
    "CASSIOPEIA": (15.0, 63.0),
    "CEPHEUS":    (325.0, 70.0),
    "PERSEUS":    (45.0, 48.0),
    "LACERTA":    (338.0, 48.0),
    "CYGNUS":     (308.0, 44.0),
}
CONSTELLATION_LABEL_COLOR = "#2255AA"   # distinct from cluster labels
                                       # (which use finder_charts.py's
                                       # fixed red LABEL_COLOR) so the two
                                       # kinds of label don't blur together

MAG_LIMIT_DEFAULT = 8.0
BOX_PADDING_DEG = 2.0

# Star marker sizes (matplotlib scatter s= units, points^2) -- see
# "WHAT CHANGED IN v2" #2 above. finder_charts.py's global defaults are
# STAR_SIZE_MIN=20.0 / STAR_SIZE_MAX=2200.0; finder_chart_awv_globulars.py
# used those unchanged. This field is far denser (Milky Way star field,
# not Ophiuchus), so both are cut roughly 7-15x smaller as a first pass.
STAR_SIZE_MIN = 3.0
STAR_SIZE_MAX = 150.0

# v3: explicit label-offset overrides for the groups the v2 render actually
# showed colliding -- the auto-nudge in fc._label_pos() only pushes a label
# away from the CENTROID of every other target, which doesn't help when
# several targets are clustered tightly together (it pushes them all the
# same direction, into each other). Values are (dra_deg, ddec_deg), added
# directly to each target's real RA/Dec before projecting -- computed from
# each group's actual coordinates to fan labels out in different directions
# rather than stacking them. First-pass estimates, same as everything else
# here -- expect another round of adjustment once you see this render.
LABEL_OFFSET_OVERRIDES = {
    # Cassiopeia group (NGC 457/M103/654/659/663), ordered low-RA to high-RA:
    "NGC 457":  (-0.4, -0.6),
    "M 103":    ( 0.0,  0.7),
    "NGC 654":  ( 0.6,  0.4),
    "NGC 659":  ( 0.3, -0.7),
    "NGC 663":  ( 0.7,  0.0),
    # Double Cluster pair:
    "NGC 869":  (-0.4, -0.4),
    "NGC 884":  ( 0.4,  0.4),
    # NGC 7788/7790 pair:
    "NGC 7788": (-0.5,  0.2),
    "NGC 7790": ( 0.5, -0.2),
}


def build_targets(use_category_colors=True):
    targets = []

    for name, (ra, dec, label) in PERSEUS_ARM_COORDS.items():
        t = {
            "name": name, "label": label, "ra": ra, "dec": dec,
            "object_type": "open_cluster", "size_amin": DEFAULT_SIZE_AMIN,
        }
        if use_category_colors:
            t["category"] = "perseus_arm"
        if name in LABEL_OFFSET_OVERRIDES:
            t["label_offset"] = LABEL_OFFSET_OVERRIDES[name]
        targets.append(t)

    other_groups = [(LOCAL_ARM, "local_arm"), (OTHER, "other")]
    for names, category in other_groups:
        resolved = fc.resolve_simbad(names)
        for t in resolved:
            if use_category_colors:
                t["category"] = category
            if t["name"] in LABEL_OFFSET_OVERRIDES:
                t["label_offset"] = LABEL_OFFSET_OVERRIDES[t["name"]]
            # Override whatever SIMBAD reported for size -- confirmed by
            # the v2 render that this is NOT safe to trust as-is: SIMBAD
            # returned size≈144' for NGC 7160 and size≈120' for NGC 7129
            # (2-2.4 degrees!), which rendered as two huge, out-of-place
            # blue blobs. Same reasoning as the 12 hardcoded objects above
            # -- true angular size barely matters at this chart's scale
            # (MIN_MARKER_PX floors it anyway), so consistency beats
            # whatever SIMBAD's galdim_majaxis happens to mean for a given
            # entry (a broader associated region, in at least these two
            # cases, not the compact cluster itself).
            if t.get("object_type") in ("open_cluster", "globular_cluster"):
                t["size_amin"] = DEFAULT_SIZE_AMIN
        targets.extend(resolved)

    landmarks = fc.resolve_simbad(LANDMARK_STARS)
    for t in landmarks:
        if t["name"] in LABEL_OFFSET_OVERRIDES:
            t["label_offset"] = LABEL_OFFSET_OVERRIDES[t["name"]]
    targets.extend(landmarks)

    resolved_names = {t["name"] for t in targets}
    requested_names = (set(PERSEUS_ARM_COORDS) | set(LOCAL_ARM) |
                      set(OTHER) | set(LANDMARK_STARS))
    missing = requested_names - resolved_names
    if missing:
        print(f"\n   *** {len(missing)} object(s) did NOT resolve and are "
              f"MISSING from the chart: {sorted(missing)} ***\n")

    return targets


def compute_overview_bounds(targets, padding_deg=BOX_PADDING_DEG):
    """Unchanged from v1 -- see module docstring / finder_chart_awv_globulars.py
    for why the RA-wraparound handling here is needed and how it was verified.
    Still produces ra_min/ra_max outside [0, 360) for this seam-straddling
    field; that's fine for StereoNorth's boundary-sampling crop below, which
    wraps every RA value with % 360.0 right before calling transform_point."""
    if not targets:
        raise ValueError("no targets to bound")

    def unwrap(ra, ref_ra):
        d = ((ra - ref_ra + 180.0) % 360.0) - 180.0
        return ref_ra + d

    best = None
    for ref_t in targets:
        ref_ra = ref_t["ra"]
        ras, decs, radii = [], [], []
        for t in targets:
            ras.append(unwrap(t["ra"], ref_ra))
            decs.append(t["dec"])
            radii.append(fc.target_radius_deg(t))

        dec_min = min(d - r for d, r in zip(decs, radii)) - padding_deg
        dec_max = max(d + r for d, r in zip(decs, radii)) + padding_deg

        ra_ext_min, ra_ext_max = [], []
        for ra, dec, r in zip(ras, decs, radii):
            cosd = max(math.cos(math.radians(dec)), 0.05)
            ra_ext_min.append(ra - r / cosd)
            ra_ext_max.append(ra + r / cosd)
        ra_min = min(ra_ext_min) - padding_deg
        ra_max = max(ra_ext_max) + padding_deg

        if ra_min >= 0 and (best is None or ra_min < best[0]):
            best = (ra_min, ra_max, dec_min, dec_max)

    if best is not None:
        return best

    ref_ra = targets[0]["ra"]
    ras   = [unwrap(t["ra"], ref_ra) for t in targets]
    decs  = [t["dec"] for t in targets]
    radii = [fc.target_radius_deg(t) for t in targets]
    dec_min = min(d - r for d, r in zip(decs, radii)) - padding_deg
    dec_max = max(d + r for d, r in zip(decs, radii)) + padding_deg
    ra_ext_min, ra_ext_max = [], []
    for ra, dec, r in zip(ras, decs, radii):
        cosd = max(math.cos(math.radians(dec)), 0.05)
        ra_ext_min.append(ra - r / cosd)
        ra_ext_max.append(ra + r / cosd)
    return (min(ra_ext_min) - padding_deg, max(ra_ext_max) + padding_deg,
            dec_min, dec_max)


def render_target_overlay_by_category(img_path, ax_pos, t, proj_ctx,
                                      outline_width=6, cross_width=4,
                                      min_r_px=None):
    """Like fc.render_target_overlay(proj_ctx=...), but overrides fill
    color by THIS CHART's category (Perseus Arm / Local Arm / Other)
    instead of by astronomical object_type -- see v1's version of this
    function for the full rationale. Updated for v2 to always use the
    projection-aware path (fc.axes_frac_proj), matching the switch to
    StereoNorth -- there is no more flat-linear (Mercator) branch."""
    style = fc.style_for(t["object_type"])
    shape, dashed = style["shape"], style["dashed"]
    color = CATEGORY_COLOR.get(t.get("category"), style["color"])

    if shape not in ("circle", "circle_plus"):
        fc.render_target_overlay(img_path, ax_pos, t, None,
                                 proj_ctx=proj_ctx,
                                 outline_width=outline_width,
                                 cross_width=cross_width, min_r_px=min_r_px)
        return

    ra0, dec0 = t["ra"], t["dec"]
    cx_ax, cy_ax, spd = fc.axes_frac_proj(proj_ctx, ra0, dec0, ra0, dec0 + 1.0)
    r_ax = t["size_amin"] / 60 / 2 * spd

    if shape == "circle":
        fc.add_overlay_circle(img_path, ax_pos, cx_ax, cy_ax, r_ax,
                              color, dashed,
                              outline_width=outline_width, min_r_px=min_r_px)
    else:
        fc.add_overlay_circle(img_path, ax_pos, cx_ax, cy_ax, r_ax,
                              color, dashed, bisect=True,
                              outline_width=outline_width,
                              cross_width=cross_width, min_r_px=min_r_px)


def render_constellation_labels(img_path, ax_pos, proj_ctx, anchors,
                                color=CONSTELLATION_LABEL_COLOR,
                                font_scale=0.020):
    """Draws a constellation NAME label at each (ra, dec) anchor in
    `anchors`. There's no equivalent of this anywhere in finder_charts.py
    -- _plot_constellation_lines() only draws the stick-figure lines, no
    text -- so this reimplements just enough of fc.add_overlay_label()'s
    pixel math to place text at an arbitrary (ra, dec) with a color other
    than that function's hardcoded LABEL_COLOR (red, same as every cluster
    label -- reusing it as-is here would make constellation names blend
    into the exact clutter this chart is trying to reduce).

    Skips anchors that fall outside the current view (a wrapped-around
    label would otherwise land at some meaningless mirrored position) --
    detected by just checking whether the projected point falls within the
    axes' current data limits.
    """
    from PIL import Image, ImageDraw

    for text, (ra, dec) in anchors.items():
        x_data, y_data = proj_ctx._proj.transform_point(
            ra % 360.0, dec, proj_ctx._crs)
        xlim, ylim = proj_ctx.ax.get_xlim(), proj_ctx.ax.get_ylim()
        if not (min(xlim) <= x_data <= max(xlim) and
                min(ylim) <= y_data <= max(ylim)):
            print(f"   Constellation label '{text}' is outside the "
                  f"current frame -- skipped, not drawn off-chart.")
            continue
        cx_ax = (x_data - xlim[0]) / (xlim[1] - xlim[0])
        cy_ax = (y_data - ylim[0]) / (ylim[1] - ylim[0])

        img = Image.open(img_path)
        W, H = img.size
        al, ar = ax_pos.x0 * W, ax_pos.x1 * W
        at, ab = (1 - ax_pos.y1) * H, (1 - ax_pos.y0) * H
        aw, ah = ar - al, ab - at
        x = al + cx_ax * aw
        y = ab - cy_ax * ah
        draw = ImageDraw.Draw(img)
        draw.text((x, y), text,
                  font=fc._label_font(max(14, int(ah * font_scale))),
                  fill=fc._hex_to_rgb(color), anchor="mm")
        img.save(img_path)
        print(f"   Constellation label: {text}")


def _sample_boundary_xy(p, ra_min, ra_max, dec_min, dec_max, n=60):
    """Samples n points along each of the 4 edges of the (ra_min, ra_max,
    dec_min, dec_max) box, transforms each through the plot's actual
    projection, and returns (xs, ys) in projected-plane coordinates.

    Full-boundary sampling rather than just the 4 corners -- verified
    standalone (see v2 changelog above) that corners-only can clip real
    content for a box shaped like this one, because edges of an RA/Dec
    rectangle are curved, not straight, once transformed through a polar
    projection.

    Every RA value is wrapped with % 360.0 immediately before being handed
    to transform_point() -- defensive, since this field's RA bounds
    (from compute_overview_bounds()) land outside [0, 360) by construction
    for this seam-straddling field, and whether transform_point() itself
    tolerates that hasn't been confirmed.
    """
    xs, ys = [], []
    for i in range(n + 1):
        f = i / n
        ra = ra_min + f * (ra_max - ra_min)
        for dec in (dec_min, dec_max):
            x, y = p._proj.transform_point(ra % 360.0, dec, p._crs)
            xs.append(x); ys.append(y)
        dec = dec_min + f * (dec_max - dec_min)
        for ra in (ra_min, ra_max):
            x, y = p._proj.transform_point(ra % 360.0, dec, p._crs)
            xs.append(x); ys.append(y)
    return xs, ys


def make_overview_chart_stereonorth(targets, ra_min, ra_max, dec_min, dec_max,
                                    mag_limit, out_path,
                                    constellation_ids=None, star_labels=True,
                                    use_category_colors=True):
    from starplot import MapPlot, StereoNorth
    from starplot.styles import PlotStyle, extensions

    ra0 = ((ra_min + ra_max) / 2.0) % 360.0
    dec0 = (dec_min + dec_max) / 2.0
    ra_span, dec_span = ra_max - ra_min, dec_max - dec_min
    # Safe (never-too-small) star-fetch radius: raw-degree RA differences
    # are always >= the true angular separation they represent (real
    # angular RA contribution is raw_degrees * cos(dec) <= raw_degrees),
    # so using raw ra_span/dec_span directly here over-fetches slightly
    # rather than under-fetching -- same reasoning as v1, unaffected by
    # the projection change.
    radius_deg = math.hypot(ra_span, dec_span) / 2.0

    print(f"\n── Perseus Arm walk overview (StereoNorth)  "
          f"RA [{ra_min:.2f}, {ra_max:.2f}] deg  "
          f"Dec [{dec_min:.2f}, {dec_max:.2f}] deg  "
          f"({len(targets)} targets)")

    style = PlotStyle().extend(extensions.GRAYSCALE, extensions.MAP)
    # StereoNorth needs the pole in its initial view (mirrors
    # finder_charts.make_raw_chart_stereonorth's own pattern) -- full RA
    # range, dec from a bit below our real dec_min up to the pole (or
    # dec_max + margin, whichever's lower). The REAL crop happens below via
    # set_xlim/set_ylim from the boundary sampling, not from these bounds.
    dec_lo = max(-90.0, dec_min - 2.0)
    dec_hi = min(90.0, dec_max + 2.0)
    p = MapPlot(projection=StereoNorth(center_ra=ra0),
                ra_min=0, ra_max=360,
                dec_min=dec_lo, dec_max=dec_hi,
                style=style, resolution=3200,
                ephemeris=fc.EPHEMERIS)

    if constellation_ids:
        fc._plot_constellation_lines(p, constellation_ids)

    mag_min, mag_max, size_fn = fc._plot_stars(
        p, ra0, dec0, radius_deg * 1.15, mag_limit,
        size_min=STAR_SIZE_MIN, size_max=STAR_SIZE_MAX,
        bayer_labels=star_labels, flamsteed_labels=False, name_labels=False)

    # Tight rectangular crop -- see _sample_boundary_xy() docstring.
    # v4: crop to the EXACT boundary box left the dec gridline labels (which
    # starplot draws just outside the data area, at/near the dec_min/dec_max
    # edges) with nowhere to render -- they were being sliced off by this
    # same tight edge. Fix: pad the crop itself by a few percent of each
    # axis's span before setting xlim/ylim, so labels sitting right at the
    # edge have room. This is a guess at the right margin (5%), not measured
    # against actual label pixel widths -- confirm visually.
    xs, ys = _sample_boundary_xy(p, ra_min, ra_max, dec_min, dec_max)
    x_lo, x_hi = min(xs), max(xs)
    y_lo, y_hi = min(ys), max(ys)
    CROP_MARGIN_FRAC = 0.05
    x_pad = (x_hi - x_lo) * CROP_MARGIN_FRAC
    y_pad = (y_hi - y_lo) * CROP_MARGIN_FRAC
    p.ax.set_xlim(x_lo - x_pad, x_hi + x_pad)
    p.ax.set_ylim(y_lo - y_pad, y_hi + y_pad)

    # tick_marks=False, NOT True: cartopy's set_xticks() (what tick_marks=True
    # triggers, via starplot's _tick_marks() helper) explicitly refuses
    # non-rectangular projections -- confirmed by the real traceback this
    # produced under StereoNorth ("RuntimeError: Cannot handle
    # non-rectangular coordinate systems"). finder_charts.py's OWN
    # make_raw_chart_stereonorth() already does exactly this
    # (tick_marks=False) for this exact reason -- missed matching it when
    # this function was first written. Gridlines and their labels still
    # draw fine without tick_marks; it only controls the small perpendicular
    # tick marks along the frame, which don't make sense on a curved-frame
    # projection anyway.
    p.gridlines(tick_marks=False,
                ra_locations =fc._nice_ra_ticks(ra_min, ra_max),
                dec_locations=fc._nice_dec_ticks(dec_min, dec_max),
                ra_formatter_fn=fc.ra_fmt, dec_formatter_fn=fc.dec_fmt)
    # Same tick-label caveat as v1: fc.ra_fmt does raw_degrees/15 -> h/m
    # with no mod-24 wrap, and this field's ra_min/ra_max land outside
    # [0, 360) by construction. The v1 Mercator render's ticks actually
    # DID show correctly ("22h 00m" / "2h 00m", not "26h 00m"), which
    # suggests starplot handles this fine somewhere in its own gridline
    # pipeline -- but that was under Mercator; still worth a direct look
    # at this chart's actual tick labels now that it gets past this point.

    p.export(out_path, padding=0.3)
    ax_pos = p.ax.get_position()
    plt.close("all")
    print(f"   Starfield + constellation lines → {os.path.basename(out_path)}")

    LABEL_FONT_SCALE = 0.010
    LABEL_GAP_SCALE = 0.35
    fov_for_labels = max(ra_span, dec_span) * LABEL_GAP_SCALE
    # v3: bumped from 9 -- per feedback, markers (nearly all floored to
    # this value once size_amin was made consistent -- see build_targets())
    # read as "a little too small." Still a guess at the right number, not
    # a measured one.
    MIN_MARKER_PX  = 16
    OUTLINE_WIDTH  = 2
    CROSS_WIDTH    = 2

    if constellation_ids:
        render_constellation_labels(out_path, ax_pos, p,
                                    CONSTELLATION_LABEL_ANCHORS)

    for t in targets:
        if use_category_colors:
            render_target_overlay_by_category(
                out_path, ax_pos, t, p,
                outline_width=OUTLINE_WIDTH, cross_width=CROSS_WIDTH,
                min_r_px=MIN_MARKER_PX)
        else:
            fc.render_target_overlay(
                out_path, ax_pos, t, None, proj_ctx=p,
                outline_width=OUTLINE_WIDTH, cross_width=CROSS_WIDTH,
                min_r_px=MIN_MARKER_PX)
        fc.render_target_label(out_path, ax_pos, t, fov_for_labels, None,
                               others=targets, proj_ctx=p,
                               font_scale=LABEL_FONT_SCALE)
        print(f"   Overlay + label: {t['name']}"
              f"{' (' + t['category'] + ')' if t.get('category') else ''}")


def rotate_chart_image(img_path, direction):
    """Rotates the raw chart PNG in place by 90 deg, physically, before
    branding (title/footer) is composited on top -- so the title stays
    upright and only the star-map content reorients.

    WHY a rotation helps at all: the field is a wide-in-RA, shallow-in-Dec
    strip that is NOT centered on the pole, so under StereoNorth it maps to
    a curved arc sweeping through a real fraction of a circle around the
    pole -- not a straight horizontal band. The axis-aligned bounding box
    around a curved arc necessarily has empty area in its corners (like the
    bounding box of a bent banana), which is almost certainly the "lots of
    white space" being seen. Rotating the OUTPUT IMAGE 90 deg doesn't remove
    that curvature -- the arc is still an arc -- but if the exported canvas
    currently comes out portrait-shaped while the content's true bounding
    box is landscape (or vice versa), a 90 deg turn can make the content
    fill the frame much better simply by matching canvas orientation to
    content orientation.

    NOT verified against the actual render (no access to the output image
    or to starplot's internal figure-sizing here) -- if this rotates the
    wrong way, rerun with --rotate ccw instead of --rotate cw (or vice
    versa); direction is a guess, not a measurement.
    """
    from PIL import Image
    if direction not in ("cw", "ccw"):
        return
    angle = -90 if direction == "cw" else 90  # PIL rotate() is CCW-positive
    img = Image.open(img_path)
    img = img.rotate(angle, expand=True)
    img.save(img_path)
    print(f"   Rotated chart image 90 deg ({direction}) to reduce "
          f"bounding-box white space.")


def main():
    parser = argparse.ArgumentParser(
        prog="finder_chart_awv_perseus_arm.py",
        description="Deneb-to-Double-Cluster Perseus Arm overview chart")
    parser.add_argument("--mag-limit", type=float, default=MAG_LIMIT_DEFAULT,
                        dest="mag_limit")
    parser.add_argument("--no-star-labels", action="store_true",
                        dest="no_star_labels")
    parser.add_argument("--no-constellation-lines", action="store_true",
                        dest="no_constellation_lines")
    parser.add_argument("--no-category-colors", action="store_true",
                        dest="no_category_colors")
    parser.add_argument("--rotate", choices=["cw", "ccw", "none"],
                        default="cw", dest="rotate",
                        help="Rotate the map 90 deg to reduce bounding-box "
                             "white space (default: cw). Direction is a "
                             "guess -- pass ccw or none if cw looks wrong.")
    parser.add_argument("--output-dir", default=None, dest="output_dir")
    parser.add_argument("--chart-name", default="awv-perseus-arm-overview",
                        dest="chart_name")
    args = parser.parse_args()

    use_category_colors = not args.no_category_colors

    out_dir = args.output_dir or HERE
    os.makedirs(out_dir, exist_ok=True)
    out_jpg = os.path.join(out_dir, f"{fc.slug(args.chart_name)}.jpg")

    print("Resolving objects (12 hardcoded, 5 via SIMBAD) …")
    targets = build_targets(use_category_colors=use_category_colors)
    if not targets:
        sys.exit("ERROR: no objects resolved.")

    ra_min, ra_max, dec_min, dec_max = compute_overview_bounds(targets)

    title = "The Perseus Arm — Deneb to the Double Cluster"
    subtitle = f"V ≤ {args.mag_limit:g} · Cygnus, Cepheus, Cassiopeia & Perseus"

    with tempfile.NamedTemporaryFile(suffix="_raw.png", delete=False) as tmp:
        raw_png = tmp.name
    try:
        make_overview_chart_stereonorth(
            targets, ra_min, ra_max, dec_min, dec_max,
            mag_limit=args.mag_limit,
            out_path=raw_png,
            constellation_ids=(None if args.no_constellation_lines
                              else CONSTELLATION_IDS),
            star_labels=not args.no_star_labels,
            use_category_colors=use_category_colors,
        )
        if args.rotate != "none":
            rotate_chart_image(raw_png, args.rotate)
        print("   Applying NBAS branding …")
        fc.apply_branding(raw_png, out_jpg, title, subtitle)
    finally:
        if os.path.exists(raw_png):
            os.remove(raw_png)

    print(f"\n✓  Overview chart complete → {out_jpg}")


if __name__ == "__main__":
    main()
