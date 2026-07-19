#!/usr/bin/env python3
"""
fetch_comet_ephemerides.py
Ticket #28 — SSO Comet Panel

Reads data/comets.yaml, fetches a 30-day ephemeris for each comet from
JPL Horizons, and writes JSON output to static/data/comets/.

Output files:
  static/data/comets/index.json        — manifest of all comets + metadata
  static/data/comets/<slug>.json       — per-comet 30-day ephemeris

Stale files (comets removed from comets.yaml) are pruned at the end,
but ONLY after all fetches have completed — so a Horizons outage leaves
existing data intact.

Requires: PyYAML  (pip install pyyaml --break-system-packages)
All other dependencies are stdlib.

Usage:
  python scripts/fetch_comet_ephemerides.py

Environment variables (all optional):
  COMET_YAML     path to comets.yaml        default: data/comets.yaml
  COMET_OUT_DIR  path to output directory   default: static/data/comets
  WINDOW_DAYS    ephemeris window in days   default: 30
  STEP_SIZE      Horizons step size         default: 1d
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

try:
    import yaml
except ImportError:
    print("[ERROR] PyYAML not installed. Run: pip install pyyaml --break-system-packages",
          file=sys.stderr)
    sys.exit(1)

# ── Configuration ──────────────────────────────────────────────────────────────

COMET_YAML   = Path(os.environ.get("COMET_YAML",   "data/comets.yaml"))
COMET_OUT    = Path(os.environ.get("COMET_OUT_DIR", "static/data/comets"))
WINDOW_DAYS  = int(os.environ.get("WINDOW_DAYS", "30"))
STEP_SIZE    = os.environ.get("STEP_SIZE", "1d")

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


# ── Slug generation ────────────────────────────────────────────────────────────

def designation_to_slug(designation):
    """
    Convert a comet designation to a safe filename slug.
    '10P'       → '10p'
    'C/2025 R3' → 'c2025r3'
    '88P'       → '88p'
    """
    return re.sub(r"[^a-z0-9]", "", designation.lower())


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    # Load curated comet list
    if not COMET_YAML.exists():
        print(f"[ERROR] {COMET_YAML} not found", file=sys.stderr)
        sys.exit(1)

    with open(COMET_YAML) as f:
        config = yaml.safe_load(f)

    comets = config.get("comets", [])
    if not comets:
        print("[WARN] No comets in comets.yaml — nothing to do", file=sys.stderr)
        sys.exit(0)

    print(f"[INFO] Loaded {len(comets)} comet(s) from {COMET_YAML}")

    # Full set of slugs that *should* exist based on comets.yaml right now,
    # independent of whether this run's fetch succeeds for each one. Used at
    # prune time so a failed fetch this run doesn't delete a still-curated
    # comet's previously-good file -- only a comet actually removed from
    # comets.yaml should ever be pruned.
    expected_slugs = {
        designation_to_slug(c.get("designation", "").strip())
        for c in comets
        if c.get("designation", "").strip()
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

        # Per-comet output file
        comet_out = {
            "designation":    designation,
            "name":           name,
            "type":           comet_type,
            "generated_utc":  generated_utc,
            "window_days":    WINDOW_DAYS,
            # Pass through all yaml metadata for the panel to use
            "discovery_year":     comet.get("discovery_year"),
            "perihelion_date":    comet.get("perihelion_date"),
            "perihelion_au":      comet.get("perihelion_au"),
            "peak_magnitude":     comet.get("peak_magnitude"),
            "binocular":          comet.get("binocular", False),
            "telescope_required": comet.get("telescope_required", False),
            "note":               comet.get("note"),
            "warning":            comet.get("warning"),
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
            "telescope_required": comet.get("telescope_required", False),
            "peak_magnitude":     comet.get("peak_magnitude"),
            "perihelion_date":    comet.get("perihelion_date"),
            "warning":            comet.get("warning"),
            "note":               comet.get("note"),
            # Snapshot of first-row position for quick access
            "current": {
                "date_utc":      first["date_utc"],
                "ra_hms":        first["ra_hms"],
                "dec_dms":       first["dec_dms"],
                "t_mag":         first["t_mag"],
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

    # Prune stale files. A file is only pruned if its comet is no longer in
    # comets.yaml at all -- NOT just because this run's fetch for it failed.
    # (A comet that's still curated but had a transient fetch failure this
    # run keeps its last-known-good file; it just won't appear in this run's
    # index.json until the next successful fetch.)
    skipped_this_run = expected_slugs - set(slugs_written)
    if skipped_this_run:
        print(f"[WARN] {len(skipped_this_run)} curated comet(s) failed to fetch this run "
              f"and were left out of index.json (files preserved): "
              f"{', '.join(sorted(skipped_this_run))}", file=sys.stderr)

    for existing in COMET_OUT.glob("*.json"):
        if existing.stem != "index" and existing.stem not in expected_slugs:
            existing.unlink()
            print(f"[INFO] Pruned stale file: {existing.name}")

    print(f"[INFO] Done — {len(slugs_written)} comet(s) written")


if __name__ == "__main__":
    main()
