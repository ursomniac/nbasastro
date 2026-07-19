#!/usr/bin/env python3
"""
build_comet_candidates.py — PROTOTYPE, Script 1 of the two-script comet curation
design (see comet-curation-v2-design.md). NOT wired into the site build.

Each candidate also carries a "visibility" tier (naked-eye / binocular /
telescope, thresholds set by Bob 2026-07-19: mag<=3.0 / mag<=8.5) and a
"trend" (brightening / fading / near-peak), derived from current_mag vs
peak_mag/peak_mag_date since COBS's API does not expose a trend field itself
(confirmed against both comet_list.api and comet.api docs directly, version
1.3 -- see derive_trend()'s docstring for the exact fields checked).

ARCHITECTURE (rewritten 2026-07-19, second pass): COBS-primary, MPC-residual.

The first version of this script tried to independently predict comet
brightness from MPC's raw orbital elements via a hand-rolled two-body Kepler
propagation plus the standard comet magnitude law. That approach was dropped
after this session found real, verified problems with it: MPC's own magnitude
parameters are frequently rough defaults (confirmed against real data --
10P/Tempel computed to magnitude 4.6 against a real COBS-observed value of
8.9), and the wider literature agrees this is a known, structural limitation
(a BAA forum thread independently hit the same problem with 289P/Blanpain;
MPC's H/G values were described there as "generally based on nuclear
magnitudes... often very inaccurate", and comet brightness in general as "a
law unto themselves").

Instead, this version leans on COBS (the Comet Observation Database), which
already computes forward-looking brightness predictions (peak_mag /
peak_mag_date) from real observational data when enough exists. Confirmed
live (2026-07-19) that this correctly flags comets that are currently very
faint but will become bright within a real window -- e.g. 2P/Encke, current
observed magnitude 20.3 (undetectable) today, but peak_mag 3.6 predicted for
2027-02-10, correctly present in COBS's data well ahead of time. That's
exactly the forward-projection job the old Kepler/formula code existed to do,
already done, against real data, by someone else.

Pipeline:
  1. Pull COBS's full is-observed=true comet list in ONE bulk call, no
     server-side magnitude filter (confirmed live: this is small -- a few
     hundred objects, a single response page, nowhere near the 5000-item
     pagination ceiling -- so there's no efficiency reason to filter
     server-side, and doing it client-side lets both current_mag and
     peak_mag be considered together).
  2. Include a comet if EITHER its current observed magnitude, OR its
     predicted peak magnitude (bounded to fall within the requested window),
     is <= --mag-cutoff.
  3. Separately, check MPC's CometEls.txt for the one gap COBS can't cover by
     definition: comets with NO observations submitted to COBS at all (brand
     new, or not yet picked up by the observer community). Bob's expectation
     (2026-07-19): this list should usually be small to empty -- "until, of
     course, it isn't," which is exactly the case it exists to catch.
  4. For each of those residual comets, compute a CRUDE magnitude estimate
     (added 2026-07-19, second pass) using the two-body Kepler propagation +
     magnitude-law approach this script originally used for everything, now
     scoped down to just this small residual set (a handful of comets, not
     the full ~1000-comet catalog, so the earlier performance argument against
     it doesn't apply here). This estimate is NOT trusted as an actual
     number -- see estimate_crude_magnitude()'s docstring for why -- but the
     confirmed direction of its error (optimistic/too-bright, never too
     faint) makes it safe to use as a one-sided drop filter: if even the
     optimistic estimate is fainter than --mag-cutoff, the real comet is
     expected to be fainter still, so it's dropped outright. If it passes,
     the comet is kept and clearly flagged as a crude, unreliable estimate --
     never presented as equivalent to a COBS-observed number. If the estimate
     can't be computed at all (missing/invalid orbital elements), the comet
     is kept as an unconfirmed watchlist entry with no magnitude claimed,
     rather than guessed away.
  5. Final output = COBS-qualified candidates + surviving MPC-only residual
     entries (crude-but-passing, or unconfirmed-with-no-estimate).

Two real bugs found and fixed against the LIVE COBS API this session (not
guessed -- confirmed against actual server responses, not just docs):
  - `cur-mag` must be an int in the request URL. A float (e.g. "13.0") is
    silently ignored server-side, returning zero results with no error at
    all -- this produced a real empty-result run before being caught.
  - `is-observed` must be the literal string "true"/"false". COBS's own docs
    examples show "is-observed=1", but the live server rejects that with
    HTTP 400 ("neither 'true' nor 'false'"). The docs are wrong here; the
    server's own error message was trusted over them.

What's NOT verified yet:
  - Pagination beyond one page hasn't been exercised against live data (the
    real is-observed=true query returned everything in a single page). The
    loop handles it, but an actual >5000-item response hasn't been seen.
  - The MPC <-> COBS merge key (packed designation, e.g. "0010P") is
    confirmed working for numbered comets; provisional/long-period comets
    fall back to weaker free-text matching (see mpc_packed_number).
  - The crude-magnitude drop filter's one-sidedness (optimistic-only bias)
    rests on two confirmed data points (10P/Tempel computed-vs-real; the BAA
    289P/Blanpain thread) plus Bob's own long-standing manual-curation
    experience ("I've had to routinely mark a comet's brightness down...
    off by 1-2 magnitudes"). That's real, verified evidence, not a
    guess -- but it is not a large-sample statistical guarantee. Worth
    re-checking if a comet the filter dropped later turns out to have
    actually been bright enough (see --always-include as the escape hatch).

CONFIRMED REAL GAP (found via testing, 2026-07-19, not a matching bug):
  107P/Wilson-Harrington is COBS-observed but has NO record in either MPC's
  CometEls.txt or the broader AllCometEls.txt -- confirmed by searching both
  files directly, not inferred. Reason: 107P is dual-catalogued as asteroid
  4015 Wilson-Harrington; it showed cometary activity only once (1949) and
  MPC tracks it as asteroid-primary now, so it's absent from MPC's comet
  files even though COBS (and common usage) still lists it as periodic
  comet 107P. This means perihelion_au/type enrichment will legitimately
  fail for any such dual-status object -- the WARN this script prints when
  a COBS candidate has no MPC match is doing its job here, not flagging a
  code defect. Left as None/unenriched rather than guessed.

Usage:
  pip install pandas skyfield jplephem
  python3 scripts/build_comet_candidates.py --mag-cutoff 13 --days-forward 60 \\
      --output /tmp/candidates.json
"""
import argparse
import json
import math
import re
import sys
import time
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

from skyfield.api import Loader
from skyfield.constants import GM_SUN_Pitjeva_2005_km3_s2 as GM_SUN
from skyfield.data import mpc

COBS_LIST_API = "https://cobs.si/api/comet_list.api"

# Cache CometEls.txt and de421.bsp here instead of the current working
# directory, so they're fetched once and reused -- not re-pulled on every
# run. CometEls.txt is live data that does go stale; use --reload-comets to
# force a fresh copy. de421.bsp is a static ephemeris and never needs reload.
ASSETS_DIR = Path(__file__).resolve().parent / "assets"


def mpc_packed_number(number, orbit_type):
    """Build the packed designation format COBS's `mpc_name` field uses (e.g.
    10 + 'P' -> '0010P'), confirmed against COBS's own API docs example
    ("mpc_name": "0249P" for comet 249P) and against a live query (10P came
    back as "10P" -- COBS appears to not always zero-pad to 4 digits, so
    matching should treat this loosely; see main() where both the padded and
    live-observed forms are considered). Only meaningful for numbered comets
    -- COBS's docs show mpc_name as null for purely provisional objects."""
    try:
        return f"{int(number):04d}{orbit_type}"
    except (TypeError, ValueError):
        return None


def normalize_packed(packed):
    """Zero-pad a packed MPC designation to 4 digits if it looks like a
    numeric+letter packed form (e.g. '10P' -> '0010P'). Returns None/the
    input unchanged if it doesn't look like that shape. Needed because
    COBS's mpc_name field isn't consistently zero-padded (confirmed live:
    2P/Encke and 10P/Tempel both came back unpadded, e.g. "2P" not "0002P"),
    while build_mpc_lookup()'s keys (built via mpc_packed_number(), straight
    from MPC's own number/orbit_type columns) always ARE zero-padded. Used
    to bridge the two when looking up a COBS candidate's MPC record -- a
    real bug caught by testing this against actual cached data before this
    was added: every real candidate came back "unmatched" without it."""
    if not packed:
        return packed
    if packed[:-1].isdigit():
        return f"{int(packed[:-1]):04d}{packed[-1]}"
    return packed


def fetch_cobs_list(cur_mag=None, is_observed=True, timeout=30, debug=False):
    """Bulk-pull COBS's comet list. cur_mag is optional and defaults to no
    server-side magnitude filter at all: confirmed live that the full
    is-observed=true set is small enough to just pull everything and filter
    client-side using both current_mag AND peak_mag -- a server-side cur-mag
    filter would incorrectly exclude currently-faint-but-will-brighten comets
    like 2P/Encke, which is the whole reason this rewrite happened."""
    results = []
    page = 1
    while True:
        params = [f"page={page}"]
        if cur_mag is not None:
            params.append(f"cur-mag={int(round(cur_mag))}")
        params.append(f"is-observed={'true' if is_observed else 'false'}")
        url = f"{COBS_LIST_API}?{'&'.join(params)}"
        with urllib.request.urlopen(url, timeout=timeout) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
        objects = payload.get("objects", [])
        info = payload.get("info", {})
        if debug:
            print(f"  [DEBUG] GET {url}", file=sys.stderr)
            print(f"  [DEBUG] info: {info}", file=sys.stderr)
        results.extend(objects)
        if page >= info.get("pages", 1):
            break
        page += 1
    return results


def classify_visibility(display_mag, naked_eye_cutoff, binocular_cutoff):
    """Equipment tier from display_mag alone -- naked-eye / binocular /
    telescope, thresholds set by Bob (2026-07-19): naked_eye_cutoff=3.0,
    binocular_cutoff=8.5 (his call, not derived/guessed). Returns None if
    display_mag itself is unknown (e.g. an unconfirmed MPC watchlist entry
    with no computable estimate) -- no equipment tier claimed for a comet
    with no magnitude at all."""
    if display_mag is None:
        return None
    if display_mag <= naked_eye_cutoff:
        return "naked-eye"
    if display_mag <= binocular_cutoff:
        return "binocular"
    return "telescope"


def derive_trend(current_mag, peak_mag, peak_date, now):
    """Brightening / fading / near-peak, derived entirely from fields COBS
    already provides (current_mag, peak_mag, peak_mag_date) -- added because
    COBS's own API does NOT expose a trend field (confirmed directly against
    both the comet_list.api and comet.api documentation pages, version 1.3:
    the only magnitude-related fields are current_mag, perihelion_mag,
    peak_mag, peak_mag_date -- no "trend"/"T" field). The "T" arrows shown on
    cobs.si's own homepage table are a website-only feature, not exposed by
    either documented API, so they can't be pulled through directly -- this
    is an independently-derived equivalent, not a copy of COBS's internal
    logic (which isn't public).

    Logic: compare today's magnitude to the predicted peak, and note whether
    that peak lies ahead of or behind today.
      - peak still ahead (peak_date > now):
          currently fainter than the predicted peak -> "brightening"
          already at or brighter than the predicted peak -> "near-peak"
      - peak already passed (peak_date <= now):
          currently fainter than the peak was -> "fading"
          currently at or brighter than the recorded peak -> "near-peak"
            (the peak estimate may simply be conservative/stale)
    Returns None if any required field is missing -- no trend claimed
    without enough data to support one."""
    if current_mag is None or peak_mag is None or peak_date is None:
        return None
    if peak_date > now:
        return "brightening" if current_mag > peak_mag else "near-peak"
    else:
        return "fading" if current_mag > peak_mag else "near-peak"


def parse_cobs_date(s):
    """COBS dates observed as 'YYYY-MM-DD' or 'YYYY-MM-DD hh:mm'. Returns an
    aware UTC datetime, or None if missing/unparseable."""
    if not s:
        return None
    for fmt in ("%Y-%m-%d %H:%M", "%Y-%m-%d"):
        try:
            return datetime.strptime(s, fmt).replace(tzinfo=timezone.utc)
        except ValueError:
            continue
    return None


def to_float(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def sample_epochs(ts, window_start, window_end, n=5):
    """n evenly-spaced Skyfield times across [window_start, window_end],
    confirming the "sample a handful of points, take the brightest" strategy
    already decided in comet-curation-v2-design.md -- covers a comet peaking
    mid-window, at either edge, or already past perihelion but still bright,
    all with the same code path, no branching on orbit type or perihelion
    date needed."""
    if window_end <= window_start:
        return [ts.from_datetime(window_start)]
    step = (window_end - window_start) / (n - 1)
    return [ts.from_datetime(window_start + step * i) for i in range(n)]


def estimate_crude_magnitude(row, ts, sun, earth, epochs):
    """Rough apparent-magnitude estimate for MPC candidates with ZERO COBS
    observations, using the classical two-parameter comet magnitude law
    (m = magnitude_g + 5*log10(delta) + magnitude_k*log10(r); delta =
    geocentric distance, r = heliocentric distance -- confirmed earlier this
    session against the BAA Comet Section's magnitude-parameters page,
    https://people.ast.cam.ac.uk/~jds/magpars.htm).

    KNOWN, CONFIRMED LIMITATION: MPC's magnitude_g/magnitude_k values are
    frequently rough defaults, not real photometric fits. Real-data check
    this session: 10P/Tempel computed to magnitude 4.6 vs a real COBS-
    observed 8.9. Independently corroborated: a BAA forum thread on
    289P/Blanpain describes MPC's H/G values as "generally based on nuclear
    magnitudes... often very inaccurate." Bob's own manual-curation
    experience matches the SAME direction: "I've had to routinely mark a
    comet's brightness down manually because it'll be off by 1-2
    magnitudes." All three data points agree: the error runs toward
    OPTIMISTIC (predicted brighter than reality), never the reverse. That
    directional consistency -- not the number's absolute accuracy -- is what
    this function's caller relies on: a comet whose crude estimate already
    fails the magnitude cutoff is expected to fail it in reality too, so
    it's safe to drop. A comet that passes is NOT confirmed bright -- it's
    flagged "crude" downstream and never treated as equivalent to a
    COBS-observed number.

    Returns the brightest (lowest) magnitude across the sampled epochs, or
    None if the orbit can't be propagated or magnitude_g/magnitude_k are
    missing -- callers must treat None as "unknown", not "too faint"."""
    g = to_float(row.get("magnitude_g"))
    k = to_float(row.get("magnitude_k"))
    if g is None or k is None:
        return None
    try:
        orbit = mpc.comet_orbit(row, ts, GM_SUN)
    except Exception:
        return None
    comet = sun + orbit
    best = None
    for t in epochs:
        try:
            r = orbit.at(t).distance().au
            delta = earth.at(t).observe(comet).apparent().distance().au
            if r <= 0 or delta <= 0:
                continue
            m = g + 5 * math.log10(delta) + k * math.log10(r)
        except Exception:
            continue
        if best is None or m < best:
            best = m
    return best


def mpc_comet_type(orbit_type):
    """'P' (periodic) -> "short-period", anything else -> "long-period".
    Matches fetch_comet_ephemerides.py's own logic exactly: it only special-
    cases comet_type == "short-period" to add Horizons' ;NOFRAG flag, so the
    only distinction that matters is periodic-vs-not."""
    return "short-period" if orbit_type == "P" else "long-period"


def cobs_comet_type(t):
    """Same mapping, from COBS's own 'type' field (documented values: P, N,
    C, I, A or M -- confirmed against the comet_list.api docs). Only 'P'
    matters for the short-period/NOFRAG distinction, same as mpc_comet_type."""
    if t is None:
        return None
    return "short-period" if t == "P" else "long-period"


def build_mpc_lookup(comets, now):
    """One MPC row per composite key (packed designation, falling back to
    free-text designation), choosing whichever apparition's perihelion date
    is closest to 'now'. This replicates the fragmentation/stale-apparition
    fix from earlier this session: a single MPC `number` can span multiple
    physically distinct apparitions (e.g. 332P has 8 fragment rows sharing
    one number), and picking by file order or by the free-text `reference`
    field does not reflect chronological order. Used for BOTH the residual
    watchlist pass and to backfill perihelion_au/type onto COBS-sourced
    candidates (added 2026-07-19: Bob's point that a COBS-observed comet
    should essentially always have an MPC record too, since COBS observers
    report through the same MPC/IAU channel -- so one MPC load can serve
    double duty instead of needing a second data source)."""
    best = {}
    for _, row in comets.iterrows():
        packed = mpc_packed_number(row["number"], row["orbit_type"])
        key = packed or row["designation"]
        try:
            peri = datetime(int(row["perihelion_year"]), int(row["perihelion_month"]),
                             int(row["perihelion_day"]), tzinfo=timezone.utc)
        except (ValueError, TypeError):
            continue
        dist = abs((peri - now).total_seconds())
        if key not in best or dist < best[key][0]:
            best[key] = (dist, row)
    return {k: v[1] for k, v in best.items()}


def clean_horizons_designation(mpc_packed, fallback_designation):
    """Build the designation string Horizons' DES= parameter expects, added
    2026-07-19 for the fetch_comet_ephemerides.py merge. Two shapes needed:
      - Numbered comets: existing comets.yaml uses the UNPADDED short form
        ("10P", "169P", "2P", not "0010P") -- confirmed by reading the
        current file's own entries, not guessed. Built directly from
        mpc_packed if it looks like a zero-padded number+letter.
      - Provisional comets: the candidate's raw designation string carries a
        trailing " (Name)" (e.g. "P/2009 Q4 (Boattini)", straight from COBS's
        fullname or MPC's combined designation field) that Horizons does NOT
        want -- existing comets.yaml's one provisional example, "C/2025 R3",
        confirms the space-separated form WITHOUT a parenthetical name is
        what's expected. Strips that trailing parenthetical only."""
    if mpc_packed and mpc_packed[:-1].isdigit():
        return f"{int(mpc_packed[:-1])}{mpc_packed[-1]}"
    return re.sub(r"\s*\([^)]*\)\s*$", "", fallback_designation).strip()


def extract_display_name(s):
    """Pull just the proper/discoverer name out of a designation string, to
    match comets.yaml's existing "name" field style (e.g. "Tempel 2",
    "Encke" -- NOT the full "10P/Tempel"). Added 2026-07-19 for the
    fetch_comet_ephemerides.py merge. Two shapes:
      - Trailing parenthetical wins if present: "P/2009 Q4 (Boattini)" ->
        "Boattini" (provisional comets, COBS fullname or MPC designation
        field both use this shape).
      - Otherwise split on the first '/': "10P/Tempel" -> "Tempel",
        "107P/Wilson-Harrington" -> "Wilson-Harrington" (numbered comets).
      - Falls back to the input unchanged if neither shape matches."""
    m = re.search(r"\(([^)]+)\)\s*$", s)
    if m:
        return m.group(1)
    if "/" in s:
        return s.split("/", 1)[1].strip()
    return s


def comets_file_stale(assets_dir, max_age_days, filename="CometEls.txt"):
    """True if the cached CometEls.txt is missing or older than max_age_days.
    Added 2026-07-19 per Bob: checked MPC's own docs for an explicit update
    cadence for this file and found no citable exact number -- they publish
    a DAILY.DAT described as "orbits from the latest MPEC", and MPECs go out
    continuously as new orbits are determined, not on a fixed schedule. No
    hard guarantee either way, but that's consistent with "at least daily,"
    which makes a 10-day default (Bob's number) comfortably conservative --
    worst case is up to max_age_days of staleness before a newly-discovered
    comet shows up in the residual watchlist pass, which Bob assessed as
    "highly unlikely" to matter in practice for the CURRENT-observed COBS
    pass (unaffected by this -- COBS is always queried fresh, no caching)."""
    path = Path(assets_dir) / filename
    if not path.exists():
        return True
    age_days = (time.time() - path.stat().st_mtime) / 86400
    return age_days > max_age_days


def default_args(**overrides):
    """A plain object with the same attributes argparse would produce, all
    at their defaults, for callers that want to invoke build_candidates()
    programmatically (added 2026-07-19 for the fetch_comet_ephemerides.py
    merge) without going through the CLI. Pass keyword overrides for
    anything non-default."""
    class Args:
        pass
    a = Args()
    a.mag_cutoff = 13.0
    a.days_back = 0
    a.days_forward = 60
    a.always_include = []
    a.naked_eye_cutoff = 3.0
    a.binocular_cutoff = 8.5
    a.skip_mpc_watchlist = False
    a.no_crude_filter = False
    a.max_comet_age_days = 10
    a.reload_comets = False
    a.assets_dir = str(ASSETS_DIR)
    a.output = None
    a.cobs_debug = False
    for k, v in overrides.items():
        setattr(a, k, v)
    return a


def build_candidates(args):
    """Core candidate-generation pipeline (COBS-primary, MPC-residual --
    see module docstring). Takes an args object with the same attributes
    argparse's main() produces (or build with default_args()) and returns
    the final candidates list. Split out from main() 2026-07-19 so
    fetch_comet_ephemerides.py can call this directly instead of re-running
    build_comet_candidates.py as a subprocess."""
    now = datetime.now(timezone.utc)
    window_start = now - timedelta(days=args.days_back)
    window_end = now + timedelta(days=args.days_forward)

    # --- COBS pass: primary source ------------------------------------------
    print("Querying COBS (is-observed=true, no server-side mag filter) ...",
          file=sys.stderr)
    cobs_objects = fetch_cobs_list(cur_mag=None, is_observed=True,
                                    debug=args.cobs_debug)
    print(f"  {len(cobs_objects)} observed comet(s) in COBS", file=sys.stderr)

    candidates = []
    cobs_keys = set()
    for obj in cobs_objects:
        packed = obj.get("mpc_name")
        key = packed or obj.get("name") or obj.get("fullname")
        if key:
            cobs_keys.add(key)
            # COBS's mpc_name isn't always zero-padded to 4 digits the way
            # mpc_packed_number() builds it (confirmed live: 10P came back as
            # "10P", not "0010P") -- register both forms so the MPC pass
            # below can match either way without over-claiming a fix that
            # hasn't been checked across the whole dataset.
            if packed and packed[:-1].isdigit():
                cobs_keys.add(f"{int(packed[:-1]):04d}{packed[-1]}")

        current_mag = to_float(obj.get("current_mag"))
        peak_mag = to_float(obj.get("peak_mag"))
        peak_date = parse_cobs_date(obj.get("peak_mag_date"))

        reasons = []
        if current_mag is not None and current_mag <= args.mag_cutoff:
            reasons.append("current")
        if (peak_mag is not None and peak_mag <= args.mag_cutoff and
                peak_date is not None and window_start <= peak_date <= window_end):
            reasons.append("peak-in-window")

        if not reasons:
            continue

        # display_mag must only draw from a value that actually justified
        # inclusion. peak_mag/peak_mag_date is COBS's forward prediction --
        # for a comet already past its peak (peak_mag_date in the past,
        # "peak-in-window" not in reasons), that field is a STALE historical
        # number, not a current-conditions estimate. Bug found against real
        # live output: 107P/Wilson-Harrington has current_mag=12.0 but
        # peak_mag=7.2 dated 2022-08-03 (its last apparition) -- blindly
        # taking min(current_mag, peak_mag) displayed "7.2" for a comet that
        # is actually at 12.0 today, which is materially misleading for the
        # "reasonable magnitude estimate" requirement. Only use peak_mag here
        # when peak-in-window is one of the reasons this candidate qualified.
        candidate_mags = []
        if "current" in reasons:
            candidate_mags.append(current_mag)
        if "peak-in-window" in reasons:
            candidate_mags.append(peak_mag)
        display_mag = min(candidate_mags) if candidate_mags else None

        raw_designation = obj.get("fullname") or obj.get("name")
        candidates.append({
            "designation": raw_designation,
            "clean_designation": clean_horizons_designation(packed, raw_designation),
            "display_name": extract_display_name(raw_designation),
            "mpc_packed": packed,
            "sources": ["cobs"],
            "display_mag": display_mag,
            "current_mag": current_mag,
            "peak_mag": peak_mag,
            "peak_mag_date": obj.get("peak_mag_date"),
            "reasons": reasons,
            "caveat": None,
            "visibility": classify_visibility(display_mag, args.naked_eye_cutoff,
                                               args.binocular_cutoff),
            "trend": derive_trend(current_mag, peak_mag, peak_date, now),
            # type comes straight from COBS's own field when present; both
            # this and perihelion_au get backfilled from MPC below if COBS
            # didn't have them (COBS's list API doesn't carry perihelion
            # distance at all).
            "type": cobs_comet_type(obj.get("type")),
            "perihelion_au": None,
            # COBS's own perihelion_date, e.g. "2026-08-03 12:00" -- kept as
            # the raw string COBS gives (frontend only displays it, never
            # parses it). Backfilled from MPC in the enrichment pass below
            # if COBS didn't have it.
            "perihelion_date": obj.get("perihelion_date"),
        })

    # --- MPC pass: enrichment for COBS candidates + residual watchlist -----
    watchlist = []
    dropped_too_faint = []
    if not args.skip_mpc_watchlist:
        reload_needed = args.reload_comets or comets_file_stale(
            args.assets_dir, args.max_comet_age_days)
        reason = ("forced via --reload-comets" if args.reload_comets else
                   f"cache older than {args.max_comet_age_days}d" if reload_needed else
                   f"cache fresh (<{args.max_comet_age_days}d old)")
        print(f"\nChecking MPC CometEls.txt (cache: {args.assets_dir}, {reason}) ...",
              file=sys.stderr)
        loader = Loader(args.assets_dir)
        with loader.open(mpc.COMET_URL, reload=reload_needed) as f:
            comets = mpc.load_comets_dataframe_slow(f)
        print(f"  {len(comets)} MPC orbit record(s) loaded", file=sys.stderr)

        mpc_lookup = build_mpc_lookup(comets, now)

        # Enrichment: every COBS-sourced candidate SHOULD have an MPC record
        # (Bob's point, 2026-07-19: MPC is the canonical international
        # clearinghouse comet observers report through, so a COBS-observed
        # comet with zero MPC record would be a real anomaly -- either a
        # genuinely unusual data gap or a bug in our key-matching, not a
        # normal outcome). Backfill perihelion_au/type from the same MPC
        # load already needed for the watchlist pass below -- no second
        # data source required.
        unmatched = []
        for c in candidates:
            row = mpc_lookup.get(c["mpc_packed"])
            if row is None:
                row = mpc_lookup.get(normalize_packed(c["mpc_packed"]))
            if row is None:
                unmatched.append(c["designation"])
                continue
            c["perihelion_au"] = to_float(row.get("perihelion_distance_au"))
            if c["type"] is None:
                c["type"] = mpc_comet_type(row["orbit_type"])
            if not c.get("perihelion_date"):
                try:
                    c["perihelion_date"] = (
                        f"{int(row['perihelion_year']):04d}-"
                        f"{int(row['perihelion_month']):02d}-"
                        f"{int(row['perihelion_day']):02d}")
                except (ValueError, TypeError):
                    pass
        if unmatched:
            print(f"  [WARN] {len(unmatched)} COBS-observed comet(s) have NO "
                  f"matching MPC record -- unexpected (MPC is the canonical "
                  f"source COBS observations should trace back to); "
                  f"investigate before trusting this list: "
                  f"{', '.join(unmatched)}", file=sys.stderr)

        ts = loader.timescale()
        eph = loader("de421.bsp")
        sun, earth = eph["sun"], eph["earth"]
        epochs = sample_epochs(ts, window_start, window_end)

        for key, row in mpc_lookup.items():
            if key in cobs_keys:
                continue
            packed = mpc_packed_number(row["number"], row["orbit_type"])
            try:
                peri = datetime(int(row["perihelion_year"]),
                                 int(row["perihelion_month"]),
                                 int(row["perihelion_day"]),
                                 tzinfo=timezone.utc)
            except (ValueError, TypeError):
                continue
            if not (window_start <= peri <= window_end):
                continue
            perihelion_au = to_float(row.get("perihelion_distance_au"))
            comet_type = mpc_comet_type(row["orbit_type"])
            clean_designation = clean_horizons_designation(packed, row["designation"])
            display_name = extract_display_name(row["designation"])
            perihelion_date_str = peri.strftime("%Y-%m-%d")

            if args.no_crude_filter:
                watchlist.append({
                    "designation": row["designation"],
                    "clean_designation": clean_designation,
                    "display_name": display_name,
                    "mpc_packed": packed,
                    "sources": ["mpc-watchlist"],
                    "display_mag": None,
                    "current_mag": None,
                    "peak_mag": None,
                    "peak_mag_date": None,
                    "reasons": ["not yet observed by COBS, perihelion in window"],
                    "caveat": None,
                    "visibility": None,
                    "trend": None,
                    "type": comet_type,
                    "perihelion_au": perihelion_au,
                    "perihelion_date": perihelion_date_str,
                })
                continue

            crude_mag = estimate_crude_magnitude(row, ts, sun, earth, epochs)
            if crude_mag is None:
                # Can't compute -- unknown is not the same as too faint. Keep
                # it, claim nothing.
                watchlist.append({
                    "designation": row["designation"],
                    "clean_designation": clean_designation,
                    "display_name": display_name,
                    "mpc_packed": packed,
                    "sources": ["mpc-watchlist"],
                    "display_mag": None,
                    "current_mag": None,
                    "peak_mag": None,
                    "peak_mag_date": None,
                    "reasons": ["not yet observed by COBS, perihelion in window, "
                                "crude magnitude estimate unavailable"],
                    "caveat": None,
                    "visibility": None,
                    "trend": None,
                    "type": comet_type,
                    "perihelion_au": perihelion_au,
                    "perihelion_date": perihelion_date_str,
                })
            elif crude_mag <= args.mag_cutoff:
                watchlist.append({
                    "designation": row["designation"],
                    "clean_designation": clean_designation,
                    "display_name": display_name,
                    "mpc_packed": packed,
                    "sources": ["mpc-watchlist-crude"],
                    "display_mag": round(crude_mag, 1),
                    "current_mag": None,
                    "peak_mag": None,
                    "peak_mag_date": None,
                    "reasons": ["not yet observed by COBS, perihelion in window"],
                    "caveat": "CRUDE MPC-derived estimate, not COBS-observed -- "
                              "known to run optimistic (too bright), sometimes by "
                              "several magnitudes. Treat as a rough guess only.",
                    "visibility": classify_visibility(round(crude_mag, 1),
                                                       args.naked_eye_cutoff,
                                                       args.binocular_cutoff),
                    "trend": None,
                    "type": comet_type,
                    "perihelion_au": perihelion_au,
                    "perihelion_date": perihelion_date_str,
                })
            else:
                # Confirmed one-sided bias (see estimate_crude_magnitude
                # docstring): this optimistic estimate is already fainter
                # than the cutoff, so the real comet is expected to be
                # fainter still -- safe to drop rather than list as an
                # unconfirmed "?" entry.
                dropped_too_faint.append((row["designation"], round(crude_mag, 1)))

        print(f"  {len(watchlist)} watchlist entry(ies) kept: perihelion in "
              f"window, zero COBS observations", file=sys.stderr)
        if dropped_too_faint:
            print(f"  {len(dropped_too_faint)} dropped as too faint per crude "
                  f"MPC estimate:", file=sys.stderr)
            for desig, mag in dropped_too_faint:
                print(f"    {desig:32s} crude est. mag: {mag}", file=sys.stderr)

    candidates.extend(watchlist)

    for forced in args.always_include:
        if not any(c["designation"] == forced or c["mpc_packed"] == forced
                   for c in candidates):
            candidates.append({
                "designation": forced, "clean_designation": forced,
                "display_name": forced, "mpc_packed": None, "sources": ["forced"],
                "display_mag": None, "current_mag": None, "peak_mag": None,
                "peak_mag_date": None, "reasons": ["forced"], "caveat": None,
                "visibility": None, "trend": None, "type": None, "perihelion_au": None,
                "perihelion_date": None,
            })

    candidates.sort(key=lambda c: (c["display_mag"] is None, c["display_mag"] or 0))
    return candidates


def print_candidates(candidates, args):
    """CLI reporting -- prints the summary table and (if requested) writes
    the JSON output file. Split out from the old main() 2026-07-19 so
    build_candidates() itself stays a pure function callers can use
    programmatically (e.g. fetch_comet_ephemerides.py) without CLI-only
    side effects."""
    print(f"\n{len(candidates)} candidate(s) total (mag <= {args.mag_cutoff}, "
          f"window -{args.days_back}/+{args.days_forward} days):")
    vis_abbrev = {"naked-eye": "NE", "binocular": "BIN", "telescope": "TEL"}
    trend_arrow = {"brightening": "^", "fading": "v", "near-peak": "="}
    for c in candidates:
        mag_str = c["display_mag"] if c["display_mag"] is not None else "?"
        reason_str = ", ".join(c["reasons"])
        flag = " [CRUDE]" if "mpc-watchlist-crude" in c["sources"] else ""
        vis = vis_abbrev.get(c["visibility"], "--")
        trend = trend_arrow.get(c["trend"], " ")
        print(f"  {c['designation']:32s} mag: {str(mag_str):>6} {vis:>3} {trend}"
              f"{flag} [{reason_str}]")
    if any("mpc-watchlist-crude" in c["sources"] for c in candidates):
        print("\n[CRUDE] = MPC-derived estimate, not COBS-observed. Known to run "
              "optimistic (too bright) -- treat as a rough guess only.")

    if args.output:
        with open(args.output, "w") as f:
            json.dump(candidates, f, indent=2)
        print(f"\nWrote {len(candidates)} candidate(s) to {args.output}", file=sys.stderr)


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--mag-cutoff", type=float, default=13.0,
                     help="keep a comet if EITHER its current observed magnitude "
                          "or its predicted peak magnitude (with peak_mag_date "
                          "falling in the window) is <= this value (default: 13.0)")
    ap.add_argument("--days-back", type=int, default=0,
                     help="window start, days before now (default: 0)")
    ap.add_argument("--days-forward", type=int, default=60,
                     help="window end, days after now (default: 60)")
    ap.add_argument("--always-include", action="append", default=[],
                     help="designation to force-include regardless of magnitude "
                          "(documented override hook -- expected to rarely if "
                          "ever be needed)")
    ap.add_argument("--naked-eye-cutoff", type=float, default=3.0,
                     help="display_mag <= this value gets the naked-eye tier "
                          "(default: 3.0, Bob's call 2026-07-19)")
    ap.add_argument("--binocular-cutoff", type=float, default=8.5,
                     help="display_mag <= this value (and > naked-eye cutoff) gets "
                          "the binocular tier; above it, telescope (default: 8.5, "
                          "Bob's call 2026-07-19)")
    ap.add_argument("--skip-mpc-watchlist", action="store_true",
                     help="COBS-observed candidates only, skip the MPC pass -- "
                          "loses the 'brand new, not yet observed by anyone' "
                          "safety net entirely")
    ap.add_argument("--no-crude-filter", action="store_true",
                     help="don't compute crude MPC magnitude estimates for the "
                          "residual watchlist -- keep every perihelion-in-window, "
                          "zero-COBS-observation comet with no magnitude claimed "
                          "and nothing dropped (old behavior, useful for comparison "
                          "or if orbit propagation is unavailable/undesired)")
    ap.add_argument("--max-comet-age-days", type=int, default=10,
                     help="re-download CometEls.txt automatically if the cached "
                          "copy is older than this (default: 10, Bob's call "
                          "2026-07-19 -- comfortably conservative given MPC has no "
                          "documented exact update cadence but appears to update "
                          "at least daily)")
    ap.add_argument("--reload-comets", action="store_true",
                     help="force a fresh download of CometEls.txt regardless of "
                          "the cached copy's age -- overrides --max-comet-age-days, "
                          "does not replace it")
    ap.add_argument("--assets-dir", default=str(ASSETS_DIR),
                     help=f"directory to cache CometEls.txt in (default: {ASSETS_DIR})")
    ap.add_argument("--output", default=None,
                     help="write the final candidate list to this path as JSON "
                          "(in addition to printing it)")
    ap.add_argument("--cobs-debug", action="store_true",
                     help="print each COBS request URL and the raw 'info' block")
    args = ap.parse_args()

    candidates = build_candidates(args)
    print_candidates(candidates, args)


if __name__ == "__main__":
    main()
