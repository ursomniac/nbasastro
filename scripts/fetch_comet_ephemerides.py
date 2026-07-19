#!/usr/bin/env python3
"""
fetch_comet_ephemerides.py
Ticket #28 — SSO Comet Panel

MERGED 2026-07-19: this script used to read a hand-curated data/comets.yaml.
It now generates its own candidate list at build time (COBS-primary,
MPC-residual -- see build_comet_candidates.py's module docstring for the
full design/verification history) and feeds that straight into the existing
Horizons ephemeris fetch below. Zero manual curation: comets appear as they
become viable within the window and drop off automatically as they fade,
per Bob's original Milestone 2 goal for this feature. data/comets.yaml is
no longer read by this script -- left in the repo, unused, pending Bob's
call on whether to remove it (never delete without confirmation).

Fetches a WINDOW_DAYS ephemeris for each generated candidate from JPL
Horizons, and writes JSON output to static/data/comets/.

Output files:
  static/data/comets/index.json        — manifest of all comets + metadata
  static/data/comets/<slug>.json       — per-comet ephemeris

Stale files (comets no longer in this run's candidate list) are pruned at
the end, but ONLY after all fetches have completed — so a Horizons outage,
or a COBS/MPC outage that yields zero candidates, leaves existing data
intact rather than wiping the live panel.

MAGNITUDE CORRECTION (added 2026-07-19): confirmed live that JPL Horizons'
own T-mag is frequently very wrong for comets, for the exact same structural
reason MPC's magnitude_g/magnitude_k are unreliable (see
build_comet_candidates.py's docstring) -- Horizons uses its own separately-
maintained M1/k1 photometric parameters (`T-mag = M1 + 5*log10(delta) +
k1*log10(r)`, confirmed directly from a live Horizons query's documentation
block), and those parameters can be stale by years, fit from whatever
apparition the comet was last well-photometered at rather than kept current.
Two real, verified examples from the same session that built this:
  - 10P/Tempel: Horizons M1=14, k1=5.75 -> computes T-mag 13.079 today.
    Real COBS-observed value: 8.9. Off by ~4 magnitudes. (Orbital solution
    itself is fresh -- solved 2 days prior, 6095 observations through
    2026 -- so POSITION is trustworthy; only the magnitude model is stale.)
  - 383P/Christensen: Horizons M1=18.6, k1=7.5, fit from a 2006-2019 data
    arc (its discovery apparition, when it was much fainter/farther) ->
    computes T-mag 20.268 today. Real COBS value: 11.2. Off by ~9
    magnitudes. Object match confirmed correct (numbered 383P), so this is
    not a wrong-target bug -- purely a stale photometric model.
A third-party amateur reference (aerith.net) independently corroborates the
COBS-scale numbers, not Horizons'.

Given Horizons' geometry (r, delta, and therefore the SHAPE of the
brightening/fading curve across the ephemeris window) remains reliable even
when its absolute photometric zero-point is wrong, each comet with a real
COBS current_mag gets a constant additive offset computed once
(COBS current_mag minus Horizons' T-mag for today's row) and applied across
every row's T-mag to produce `our_mag_est` -- an anchored-to-reality
estimate for the whole window, not just today. Rounded to the nearest
MAG_EST_ROUND_STEP as a hedge (this is a correction, not real per-day
photometry). Comets with no COBS current_mag anchor (crude MPC-watchlist
survivors) get no correction -- `our_mag_est` is left null rather than
compounding two unreliable numbers, and the raw (unreliable) T-mag is what
the frontend falls back to displaying for those, same as before.

Requires: pandas, skyfield, jplephem (candidate generation) -- all stdlib
otherwise (Horizons fetch/parse).

Usage:
  python scripts/fetch_comet_ephemerides.py

Environment variables (all optional):
  COMET_OUT_DIR         path to output directory        default: static/data/comets
  WINDOW_DAYS           Horizons ephemeris window, days  default: 30
  STEP_SIZE             Horizons step size               default: 1d
  CANDIDATE_MAG_CUTOFF  candidate selection mag cutoff    default: 13.0
  CANDIDATE_DAYS_BACK   candidate selection window start  default: 0
  CANDIDATE_DAYS_FORWARD candidate selection window end   default: 60
  NAKED_EYE_CUTOFF      visibility tier threshold         default: 3.0
  BINOCULAR_CUTOFF      visibility tier threshold         default: 8.5
  MAX_COMET_AGE_DAYS    CometEls.txt cache staleness      default: 10
  ASSETS_DIR            CometEls.txt/de421.bsp cache dir  default: scripts/assets
  ALWAYS_INCLUDE        comma-separated forced designations, optional
  MAG_EST_ROUND_STEP    rounding step for our_mag_est     default: 0.5
"""

import json
import math
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

# build_comet_candidates.py lives alongside this script -- Python puts this
# script's own directory on sys.path automatically when run as
# `python scripts/fetch_comet_ephemerides.py`, so this sibling import needs
# no extra path setup.
import build_comet_candidates as candidate_builder

# ── Configuration ──────────────────────────────────────────────────────────────

COMET_OUT    = Path(os.environ.get("COMET_OUT_DIR", "static/data/comets"))
WINDOW_DAYS  = int(os.environ.get("WINDOW_DAYS", "30"))
STEP_SIZE    = os.environ.get("STEP_SIZE", "1d")
MAG_EST_ROUND_STEP = float(os.environ.get("MAG_EST_ROUND_STEP", "0.5"))

HORIZONS_URL = "https://ssd.jpl.nasa.gov/api/horizons.api"

# Quantities:
#   1  = RA, Dec (ICRF)
#   9  = Visual magnitude (T-mag, N-mag)
#   19 = Solar elongation + lead/trail flag
#   23 = Heliocentric distance r + rdot
#   24 = Observer distance delta
#   29 = Constellation
QUANTITIES = "1,9,19,20,23,24,29"

# ── Horizons API ───────────────────────────────────────────────────────────────

def build_command(designation, comet_type):
    """
    Build the Horizons COMMAND string for a comet designation.
    Short-period comets get ;NOFRAG to avoid fragment matches.
    Long-period and sungrazer comets just get ;CAP.
    CAP = closest apparition to current date — always picks the right epoch.
    """
    base = f"DES={designation};CAP"
    if comet_type == "short-period":
        return base + ";NOFRAG"
    return base


def fetch_horizons(designation, comet_type, start, stop):
    """
    Fetch an observer ephemeris from JPL Horizons.
    Returns the raw result string, or None on failure.
    """
    command = build_command(designation, comet_type)

    params = {
        "format":       "json",
        "COMMAND":      f"'{command}'",
        "EPHEM_TYPE":   "'OBSERVER'",
        "CENTER":       "'500@399'",       # geocenter
        "START_TIME":   f"'{start}'",
        "STOP_TIME":    f"'{stop}'",
        "STEP_SIZE":    f"'{STEP_SIZE}'",
        "QUANTITIES":   f"'{QUANTITIES}'",
        "OBJ_DATA":     "'NO'",
        "CSV_FORMAT":   "'YES'",
    }

    url = HORIZONS_URL + "?" + urlencode(params)

    try:
        req = Request(url, headers={"User-Agent": "SSO-Dashboard/1.0 (ticket#28)"})
        with urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
            result = data.get("result", "")
            if "$$SOE" not in result:
                print(f"[WARN] No ephemeris data in Horizons response for {designation}",
                      file=sys.stderr)
                print(f"[WARN] Response snippet: {result[:300]}", file=sys.stderr)
                return None
            return result
    except (URLError, json.JSONDecodeError, Exception) as exc:
        print(f"[WARN] Horizons fetch failed for {designation}: {exc}", file=sys.stderr)
        return None


# ── Ephemeris parser ───────────────────────────────────────────────────────────

# Horizons date format in CSV output: " 2026-May-10 00:00"
HORIZONS_DATE_RE = re.compile(
    r"^\s*(\d{4})-(\w{3})-(\d{2})\s+(\d{2}):(\d{2})\s*$"
)
MONTH_MAP = {
    "Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,
    "Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12
}


def parse_date(date_str):
    """Parse a Horizons date string to an ISO 8601 UTC string."""
    m = HORIZONS_DATE_RE.match(date_str)
    if not m:
        return None
    yr, mon_s, day, hr, mn = m.groups()
    mon = MONTH_MAP.get(mon_s)
    if not mon:
        return None
    return f"{yr}-{mon:02d}-{int(day):02d}T{hr}:{mn}:00Z"


def hms_to_deg(hms):
    """Convert 'HH MM SS.ss' RA string to decimal degrees."""
    parts = hms.strip().split()
    if len(parts) != 3:
        return None
    h, m, s = float(parts[0]), float(parts[1]), float(parts[2])
    return (h + m/60 + s/3600) * 15


def dms_to_deg(dms):
    """Convert 'sDD MM SS.s' Dec string to decimal degrees (s = sign)."""
    dms = dms.strip()
    sign = -1 if dms.startswith("-") else 1
    parts = dms.lstrip("+-").split()
    if len(parts) != 3:
        return None
    d, m, s = float(parts[0]), float(parts[1]), float(parts[2])
    return sign * (d + m/60 + s/3600)


def safe_float(s):
    """Return float or None for 'n.a.' and other non-numeric strings."""
    s = s.strip()
    if s in ("n.a.", "", "N/A", "---"):
        return None
    try:
        return float(s)
    except ValueError:
        return None


def angular_separation_deg(ra1, dec1, ra2, dec2):
    """
    Great-circle distance between two points in decimal degrees.
    Used to compute daily motion rate.
    """
    r = math.pi / 180
    lat1, lat2 = dec1*r, dec2*r
    dlon = (ra2 - ra1) * r
    a = (math.sin((lat2-lat1)/2)**2
         + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2)
    return 2 * math.degrees(math.asin(math.sqrt(min(a, 1.0))))


def motion_pa_deg(ra1, dec1, ra2, dec2):
    """
    Position angle of motion from point 1 to point 2, degrees E of N.
    """
    r = math.pi / 180
    dra  = (ra2 - ra1) * r
    ddec = (dec2 - dec1) * r
    pa = math.degrees(math.atan2(dra * math.cos(dec1*r), ddec))
    return pa % 360


def parse_ephemeris(raw):
    """
    Parse the CSV ephemeris block between $$SOE and $$EOE.

    Column mapping (0-indexed after splitting on comma):
      0  date/time
      1  solar presence flag   (blank at 1d geocentric step)
      2  lunar presence flag   (blank at 1d geocentric step)
      3  RA  (HMS, space-separated within the field)
      4  Dec (DMS, space-separated within the field)
      5  T-mag
      6  N-mag
      7  r (heliocentric AU)    ← quantity 23
      8  rdot (km/s)
      9  delta (observer AU)    ← quantity 20
      10 deldot (km/s)
      11 S-O-T (solar elongation deg)
      12 /r flag (/L or /T)    ← quantity 19
      13 constellation          ← quantity 29
      (S-T-O phase not returned by current quantity set)

    Returns list of dicts, one per row.
    """
    in_block = False
    rows = []

    for line in raw.splitlines():
        if "$$SOE" in line:
            in_block = True
            continue
        if "$$EOE" in line:
            break
        if not in_block:
            continue

        parts = line.split(",")
        if len(parts) < 15:
            continue

        date_utc = parse_date(parts[0])
        if not date_utc:
            continue

        ra_hms  = parts[3].strip()
        dec_dms = parts[4].strip()
        ra_deg  = hms_to_deg(ra_hms)
        dec_deg = dms_to_deg(dec_dms)

        t_mag    = safe_float(parts[5])
        n_mag    = safe_float(parts[6])
        r_au     = safe_float(parts[7])
        rdot     = safe_float(parts[8])
        delta_au = safe_float(parts[9])
        deldot   = safe_float(parts[10])
        elong    = safe_float(parts[11])
        lr_flag  = parts[12].strip()   # "/L" or "/T"
        phase    = safe_float(parts[13])
        cnst     = parts[14].strip()

        # Tidy up the lead/trail flag
        sky_position = None
        if "/L" in lr_flag:
            sky_position = "morning"   # leads Sun = morning sky
        elif "/T" in lr_flag:
            sky_position = "evening"   # trails Sun = evening sky

        rows.append({
            "date_utc":    date_utc,
            "ra_deg":      round(ra_deg, 5)  if ra_deg  is not None else None,
            "dec_deg":     round(dec_deg, 5) if dec_deg is not None else None,
            "ra_hms":      ra_hms,
            "dec_dms":     dec_dms,
            "t_mag":       t_mag,
            "n_mag":       n_mag,
            "delta_au":    delta_au,
            "deldot_km_s": deldot,
            "r_au":        r_au,
            "rdot_km_s":   rdot,
            "elong_deg":   elong,
            "sky_position": sky_position,
            "phase_deg":   phase,
            "constellation": cnst,
        })

    # Compute motion rate and PA between consecutive rows
    for i, row in enumerate(rows):
        if i == 0 or rows[i-1]["ra_deg"] is None or row["ra_deg"] is None:
            row["motion_deg_per_day"] = None
            row["motion_pa_deg"]      = None
        else:
            prev = rows[i-1]
            sep = angular_separation_deg(
                prev["ra_deg"], prev["dec_deg"],
                row["ra_deg"],  row["dec_deg"]
            )
            pa = motion_pa_deg(
                prev["ra_deg"], prev["dec_deg"],
                row["ra_deg"],  row["dec_deg"]
            )
            row["motion_deg_per_day"] = round(sep, 4)
            row["motion_pa_deg"]      = round(pa, 1)

    return rows


# ── COBS-anchored magnitude correction ────────────────────────────────────────

def round_to_step(value, step):
    """Round to the nearest multiple of step (e.g. step=0.5 -> 8.7 rounds to
    8.5). Deliberately coarser than Horizons' 3-decimal T-mag -- this is a
    corrected estimate, not real per-day photometry, and shouldn't look more
    precise than it is."""
    if step <= 0:
        return value
    return round(round(value / step) * step, 2)


def apply_mag_correction(rows, current_mag):
    """Anchor Horizons' T-mag curve to a real COBS observation. See this
    module's docstring for why this exists (Horizons' T-mag confirmed
    unreliable, sometimes by close to 10 magnitudes, for reasons unrelated
    to orbital/positional accuracy). Computes one constant offset from
    row[0] (today) and applies it to every row, mutating rows in place by
    adding an "our_mag_est" key. Returns the offset used, or None if no
    correction could be applied (missing current_mag or missing/unparseable
    today's T-mag) -- callers should leave our_mag_est absent/null in that
    case rather than fabricate a number."""
    if current_mag is None or not rows or rows[0].get("t_mag") is None:
        for row in rows:
            row["our_mag_est"] = None
        return None
    offset = current_mag - rows[0]["t_mag"]
    for row in rows:
        row["our_mag_est"] = (round_to_step(row["t_mag"] + offset, MAG_EST_ROUND_STEP)
                               if row.get("t_mag") is not None else None)
    return round(offset, 2)


# ── Slug generation ────────────────────────────────────────────────────────────

def designation_to_slug(designation):
    """
    Convert a comet designation to a safe filename slug.
    '10P'       → '10p'
    'C/2025 R3' → 'c2025r3'
    '88P'       → '88p'
    """
    return re.sub(r"[^a-z0-9]", "", designation.lower())


# ── Candidate generation ───────────────────────────────────────────────────────

def env_float(name, default):
    return float(os.environ.get(name, default))


def env_int(name, default):
    return int(os.environ.get(name, default))


def generate_comets():
    """Run the COBS-primary/MPC-residual candidate pipeline (see
    build_comet_candidates.py) and shape its output into the same
    "comet" dict fields the rest of this script (unchanged since the old
    comets.yaml days) already expects: designation, name, type, plus the
    display metadata written into each JSON file. This replaces reading
    data/comets.yaml -- see this module's docstring for the merge history.
    """
    always_include = [
        s.strip() for s in os.environ.get("ALWAYS_INCLUDE", "").split(",") if s.strip()
    ]
    args = candidate_builder.default_args(
        mag_cutoff=env_float("CANDIDATE_MAG_CUTOFF", 13.0),
        days_back=env_int("CANDIDATE_DAYS_BACK", 0),
        days_forward=env_int("CANDIDATE_DAYS_FORWARD", 60),
        naked_eye_cutoff=env_float("NAKED_EYE_CUTOFF", 3.0),
        binocular_cutoff=env_float("BINOCULAR_CUTOFF", 8.5),
        max_comet_age_days=env_int("MAX_COMET_AGE_DAYS", 10),
        assets_dir=os.environ.get("ASSETS_DIR", str(candidate_builder.ASSETS_DIR)),
        always_include=always_include,
    )
    raw_candidates = candidate_builder.build_candidates(args)
    candidate_builder.print_candidates(raw_candidates, args)

    comets = []
    for c in raw_candidates:
        # visibility naked-eye/binocular both mean "no telescope required" --
        # comets.html's only equipment badge is the single "binocular" flag.
        binocular = c["visibility"] in ("naked-eye", "binocular")
        comets.append({
            "designation":     c["clean_designation"],
            "name":            c["display_name"],
            "type":            c["type"] or "long-period",
            "perihelion_date": c["perihelion_date"],
            "perihelion_au":   c["perihelion_au"],
            "peak_magnitude":  c["display_mag"],
            "binocular":       binocular,
            "warning":         c["caveat"],
            # Real COBS-observed "today" magnitude, kept separate from
            # display_mag/peak_magnitude above (which can be a future peak
            # value, e.g. 10P's display_mag is its peak, not today's actual
            # brightness) -- this is specifically the anchor point for the
            # Horizons T-mag correction below, added 2026-07-19 after
            # confirming Horizons' own comet magnitudes are frequently very
            # wrong (see module docstring addendum).
            "current_mag":     c["current_mag"],
        })
    return comets


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    comets = generate_comets()
    if not comets:
        print("[WARN] No candidates generated this run — nothing to do", file=sys.stderr)
        sys.exit(0)

    print(f"[INFO] Generated {len(comets)} candidate(s) this run")

    # Full set of slugs that *should* exist based on THIS run's candidate
    # list, independent of whether this run's Horizons fetch succeeds for
    # each one. Used at prune time so a failed fetch this run doesn't delete
    # a still-candidate comet's previously-good file -- only a comet that's
    # dropped out of the candidate list entirely should ever be pruned.
    expected_slugs = {
        designation_to_slug(c["designation"])
        for c in comets
        if c.get("designation")
    }

    COMET_OUT.mkdir(parents=True, exist_ok=True)

    now   = datetime.now(timezone.utc)
    start = now.strftime("%Y-%m-%d")
    stop  = (now + timedelta(days=WINDOW_DAYS)).strftime("%Y-%m-%d")
    generated_utc = now.strftime("%Y-%m-%dT%H:%M:%SZ")

    print(f"[INFO] Ephemeris window: {start} → {stop} ({WINDOW_DAYS}d)")

    slugs_written = []
    index_entries = []

    for comet in comets:
        designation  = comet.get("designation", "").strip()
        name         = comet.get("name", designation)
        comet_type   = comet.get("type", "long-period")
        slug         = designation_to_slug(designation)

        if not designation:
            print("[WARN] Skipping comet entry with no designation", file=sys.stderr)
            continue

        print(f"[INFO] Fetching {designation} ({name}) …")
        raw = fetch_horizons(designation, comet_type, start, stop)

        if raw is None:
            print(f"[WARN] Skipping {designation} — no data returned", file=sys.stderr)
            continue

        rows = parse_ephemeris(raw)
        if not rows:
            print(f"[WARN] Skipping {designation} — ephemeris parsed 0 rows", file=sys.stderr)
            continue

        print(f"[INFO]   → {len(rows)} rows parsed")

        mag_offset = apply_mag_correction(rows, comet.get("current_mag"))
        if mag_offset is not None:
            print(f"[INFO]   → mag correction: COBS-anchored offset {mag_offset:+.2f} "
                  f"applied to Horizons T-mag across all rows")
        else:
            print(f"[INFO]   → no COBS current_mag anchor -- our_mag_est left null, "
                  f"frontend falls back to raw (unreliable) Horizons T-mag")

        # Per-comet output file
        comet_out = {
            "designation":    designation,
            "name":           name,
            "type":           comet_type,
            "generated_utc":  generated_utc,
            "window_days":    WINDOW_DAYS,
            "perihelion_date":    comet.get("perihelion_date"),
            "perihelion_au":      comet.get("perihelion_au"),
            "peak_magnitude":     comet.get("peak_magnitude"),
            "binocular":          comet.get("binocular", False),
            "warning":            comet.get("warning"),
            "mag_offset":         mag_offset,
            "ephemeris":          rows,
        }

        out_path = COMET_OUT / f"{slug}.json"
        out_path.write_text(json.dumps(comet_out, indent=2, ensure_ascii=False))
        print(f"[INFO]   → wrote {out_path}")

        slugs_written.append(slug)

        # Summary for index (first row gives current position)
        first = rows[0]
        index_entries.append({
            "designation":        designation,
            "name":               name,
            "type":               comet_type,
            "slug":               slug,
            "ephemeris_file":     f"/data/comets/{slug}.json",
            "binocular":          comet.get("binocular", False),
            "peak_magnitude":     comet.get("peak_magnitude"),
            "perihelion_date":    comet.get("perihelion_date"),
            "warning":            comet.get("warning"),
            # Snapshot of first-row position for quick access
            "current": {
                "date_utc":      first["date_utc"],
                "ra_hms":        first["ra_hms"],
                "dec_dms":       first["dec_dms"],
                "t_mag":         first["t_mag"],
                "our_mag_est":   first.get("our_mag_est"),
                "elong_deg":     first["elong_deg"],
                "sky_position":  first["sky_position"],
                "constellation": first["constellation"],
            },
        })

    if not slugs_written:
        print("[WARN] No comets successfully fetched — leaving existing data intact",
              file=sys.stderr)
        sys.exit(0)

    # Write index
    index = {
        "generated_utc": generated_utc,
        "window_days":   WINDOW_DAYS,
        "comet_count":   len(slugs_written),
        "comets":        index_entries,
    }
    index_path = COMET_OUT / "index.json"
    index_path.write_text(json.dumps(index, indent=2, ensure_ascii=False))
    print(f"[INFO] Wrote index → {index_path}")

    # Prune stale files. A file is only pruned if its comet is not in THIS
    # run's candidate list at all -- NOT just because this run's fetch for
    # it failed. (A comet that's still a candidate but had a transient fetch
    # failure this run keeps its last-known-good file; it just won't appear
    # in this run's index.json until the next successful fetch.)
    skipped_this_run = expected_slugs - set(slugs_written)
    if skipped_this_run:
        print(f"[WARN] {len(skipped_this_run)} candidate(s) failed to fetch this run "
              f"and were left out of index.json (files preserved): "
              f"{', '.join(sorted(skipped_this_run))}", file=sys.stderr)

    for existing in COMET_OUT.glob("*.json"):
        if existing.stem != "index" and existing.stem not in expected_slugs:
            existing.unlink()
            print(f"[INFO] Pruned stale file: {existing.name}")

    print(f"[INFO] Done — {len(slugs_written)} comet(s) written")


if __name__ == "__main__":
    main()
