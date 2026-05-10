#!/usr/bin/env python3
"""
fetch_galilean_events.py
Ticket #22 — Galilean satellite phenomena table

Fetch strategy (in priority order):
  1. IMCCE phenjupiter data file (HTTPS, authoritative NOE-5-2021 ephemerides)
     Covers all four classical phenomena: eclipse, occultation, transit, shadow transit.
  2. Project Pluto jevent.htm (fallback, same four phenomena, identical coverage)

Jupiter rise/set filtering:
  Uses IMCCE Miriade RTS API to determine whether Jupiter is above the horizon
  during night hours for each event date, at the fixed observer coordinates.
  Observer: lat=42.7°N, lon=73.11°W  (Albany/Troy NY area)
  Note: times are accurate to within ~5 minutes for observers within ~60 miles
  of this coordinate; the RTS horizon calculation does not account for terrain.

Output: static/data/galilean-events.json (relative to repo root)
Run:    python scripts/fetch_galilean_events.py
"""

import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError

# ── Configuration ──────────────────────────────────────────────────────────────

OBSERVER_LAT = float(os.environ.get("OBSERVER_LAT", "42.7"))
OBSERVER_LON = float(os.environ.get("OBSERVER_LON", "-73.11"))   # west = negative
WINDOW_DAYS  = int(os.environ.get("WINDOW_DAYS", "15"))
OUTPUT_PATH  = Path(os.environ.get("OUTPUT_PATH",
                    Path(__file__).parent.parent / "static" / "data" / "galilean-events.json"))

# Miriade RTS: body 4 = Jupiter, body 10 = Sun (for twilight)
RTS_URL = (
    "https://ssp.imcce.fr/webservices/miriade/api/rts.php"
    "?-body=4,10"
    "&-nbd={nbd}"
    "&-step=1"
    "&-observer={lon}+{lat}"
    "&-ep={ep}"
    "&-twilight=1"
    "&-tz=-5"        # EST; offset only used for display — we work in UTC
    "&-mime=json"
    "&-from=SSO-Dashboard-ticket22"
)

# IMCCE phenjupiter data file (HTTPS mirror of the FTP)
IMCCE_PHEN_URL = "https://ftp.imcce.fr/pub/ephem/satel/phenjupiter/phen_jup_2026.txt"
IMCCE_PHEN_URL_ALT = "https://ftp.imcce.fr/pub/ephem/satel/phenjupCDT/phen_jup_2026.txt"

# Project Pluto fallback
PLUTO_URL = "https://www.projectpluto.com/jevent.htm"

# ── Satellite / event-type mappings ───────────────────────────────────────────

SAT_NAME = {"I": "Io", "II": "Europa", "III": "Ganymede", "IV": "Callisto",
            "501": "Io", "502": "Europa", "503": "Ganymede", "504": "Callisto",
            "1": "Io", "2": "Europa", "3": "Ganymede", "4": "Callisto"}

# IMCCE codes (old and new style)
EVENT_TYPE_MAP = {
    # Eclipse by Jupiter
    "E.C": "eclipse_start", "E.F": "eclipse_end",
    "EC.D": "eclipse_start", "EC.F": "eclipse_end",
    # Occultation by Jupiter
    "IM": "occultation_start", "EM": "occultation_end",
    "OC.D": "occultation_start", "OC.F": "occultation_end",
    # Transit (satellite in front of Jupiter)
    "P.C": "transit_start", "P.F": "transit_end",
    "TR.D": "transit_start", "TR.F": "transit_end",
    # Shadow transit (satellite shadow on Jupiter disk)
    "O.C": "shadow_transit_start", "O.F": "shadow_transit_end",
    "SH.D": "shadow_transit_start", "SH.F": "shadow_transit_end",
}

# Project Pluto codes
PLUTO_TYPE_MAP = {
    "Ecl": "eclipse",
    "Occ": "occultation",
    "Tra": "transit",
    "Sha": "shadow_transit",
}
PLUTO_SAT_MAP = {"I": "Io", "II": "Europa", "III": "Ganymede", "IV": "Callisto"}

DISPLAY_LABELS = {
    "eclipse":        "Eclipse (by Jupiter)",
    "occultation":    "Occultation (by Jupiter)",
    "transit":        "Transit (front of Jupiter)",
    "shadow_transit": "Shadow Transit",
    # mutual events — may appear if IMCCE mutual data is included later
    "mutual_eclipse":      "Mutual Eclipse",
    "mutual_occultation":  "Mutual Occultation",
}

# ── Helpers ───────────────────────────────────────────────────────────────────

def fetch_url(url: str, timeout: int = 20) -> bytes | None:
    """Fetch a URL, returning bytes or None on failure."""
    try:
        req = Request(url, headers={"User-Agent": "SSO-Dashboard/1.0 (ticket#22)"})
        with urlopen(req, timeout=timeout) as resp:
            return resp.read()
    except (URLError, Exception) as exc:
        print(f"[WARN] fetch failed: {url}\n       {exc}", file=sys.stderr)
        return None


def date_window() -> tuple[datetime, datetime]:
    now = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    return now, now + timedelta(days=WINDOW_DAYS)


# ── Jupiter visibility filter ─────────────────────────────────────────────────

def fetch_jupiter_windows(start: datetime, nbd: int) -> dict[str, dict]:
    """
    Returns {date_str: {"rise_utc": HH:MM, "set_utc": HH:MM,
                         "astro_dusk": HH:MM, "astro_dawn": HH:MM}}
    for each day in the window.  Any day where Jupiter doesn't rise or
    rises only during daytime is omitted → events on those days are filtered out.
    """
    url = RTS_URL.format(
        nbd=nbd,
        lon=OBSERVER_LON,
        lat=OBSERVER_LAT,
        ep=start.strftime("%Y-%m-%d"),
    )
    raw = fetch_url(url)
    if raw is None:
        print("[WARN] Miriade RTS unavailable — skipping visibility filter", file=sys.stderr)
        return {}

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        print(f"[WARN] Miriade RTS JSON parse error: {exc}", file=sys.stderr)
        return {}

    windows: dict[str, dict] = {}

    # Response structure: {"4": [{date record}, ...], "10": [...]}
    jup_records = data.get("4", [])
    sun_records  = data.get("10", [])

    # Index Sun records by date for cross-referencing twilight
    sun_by_date: dict[str, dict] = {}
    for rec in sun_records:
        d = rec.get("date", "")
        sun_by_date[d] = rec

    for rec in jup_records:
        date_str = rec.get("date", "")
        rising  = rec.get("rising")
        setting = rec.get("setting")
        if rising is None or setting is None:
            continue   # Jupiter doesn't rise (conjunction, or circumpolar gap)

        rise_h = _hms_to_frac(rising.get("hour", ""))
        set_h  = _hms_to_frac(setting.get("hour", ""))
        if rise_h is None or set_h is None:
            continue

        sun_rec = sun_by_date.get(date_str, {})
        astro_dusk = _hms_to_frac((sun_rec.get("dusk-astronomical") or {}).get("hour", ""))
        astro_dawn = _hms_to_frac((sun_rec.get("dawn-astronomical") or {}).get("hour", ""))

        windows[date_str] = {
            "rise_h":     rise_h,
            "set_h":      set_h,
            "dusk_h":     astro_dusk,   # None if not available
            "dawn_h":     astro_dawn,
        }

    return windows


def _hms_to_frac(hms: str) -> float | None:
    """Convert 'HH:MM' or 'HH:MM:SS' sexagesimal string to fractional hours."""
    if not hms:
        return None
    parts = hms.split(":")
    try:
        h = float(parts[0])
        m = float(parts[1]) if len(parts) > 1 else 0
        s = float(parts[2]) if len(parts) > 2 else 0
        return h + m / 60 + s / 3600
    except (ValueError, IndexError):
        return None


def event_visible(event_utc: datetime, windows: dict) -> bool:
    """
    Return True if the event's UTC time falls within Jupiter's nightly window
    (after astronomical dusk AND before astronomical dawn, AND Jupiter is up).
    If windows dict is empty (RTS unavailable), allow all events through.
    """
    if not windows:
        return True

    date_str = event_utc.strftime("%Y-%m-%d")
    win = windows.get(date_str)
    if win is None:
        # Try previous calendar day — event near midnight might belong there
        prev = (event_utc - timedelta(days=1)).strftime("%Y-%m-%d")
        win = windows.get(prev)
    if win is None:
        return False

    event_h = event_utc.hour + event_utc.minute / 60

    in_jupiter_window = win["rise_h"] <= event_h <= win["set_h"]

    dusk_h = win["dusk_h"]
    dawn_h = win["dawn_h"]
    if dusk_h is not None and dawn_h is not None:
        # Night wraps midnight: dusk > dawn possible
        if dusk_h > dawn_h:
            in_night = event_h >= dusk_h or event_h <= dawn_h
        else:
            in_night = dusk_h <= event_h <= dawn_h
    else:
        in_night = True  # Can't determine twilight; don't filter

    return in_jupiter_window and in_night


# ── IMCCE phenjupiter parser ──────────────────────────────────────────────────

def fetch_imcce_events(start: datetime, end: datetime) -> list[dict] | None:
    """
    Attempt to download and parse the IMCCE phenjupiter flat-text prediction file.
    Returns a list of raw half-events (each line is one start or end boundary),
    or None if download fails.

    File format (two variants depending on year):
    Old:  YYYY MMM DD  HH:MM  <SAT>  <CODE>
    New:  <SAT_NUM>  YYYY-MM-DD  HH:MM:SS.S  <CODE>

    We try both URL forms and both parse approaches.
    """
    raw = fetch_url(IMCCE_PHEN_URL) or fetch_url(IMCCE_PHEN_URL_ALT)
    if raw is None:
        return None

    text = raw.decode("utf-8", errors="replace")
    half_events: list[dict] = []

    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        ev = _parse_imcce_line(line, start, end)
        if ev:
            half_events.append(ev)

    if not half_events:
        print("[WARN] IMCCE file parsed but yielded 0 events in window", file=sys.stderr)
        return None

    return half_events


def _parse_imcce_line(line: str, start: datetime, end: datetime) -> dict | None:
    """
    Try to parse one line of an IMCCE phenjupiter file.
    Returns a dict with keys: satellite, event_half (e.g. 'eclipse_start'), utc
    """
    # New format (2024+): "501 2026-05-12 21:14:00.0 EC.D"
    m = re.match(
        r"^(\d{3})\s+(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2}(?:\.\d+)?)\s+(\S+)",
        line
    )
    if m:
        sat_num, date_s, time_s, code = m.groups()
        sat = SAT_NAME.get(sat_num)
        ev_half = EVENT_TYPE_MAP.get(code)
        if not sat or not ev_half:
            return None
        try:
            utc = datetime.fromisoformat(f"{date_s}T{time_s[:8]}+00:00")
        except ValueError:
            return None
        if start <= utc < end:
            return {"satellite": sat, "event_half": ev_half, "utc": utc}
        return None

    # Old format: "2026 May 12  21:14  I  E.C"
    m = re.match(
        r"^(\d{4})\s+(\w{3})\s+(\d{1,2})\s+(\d{2}:\d{2})\s+(I{1,3}V?|IV)\s+(\S+)",
        line
    )
    if m:
        yr, mon, day, hm, sat_roman, code = m.groups()
        sat = SAT_NAME.get(sat_roman)
        ev_half = EVENT_TYPE_MAP.get(code)
        if not sat or not ev_half:
            return None
        try:
            utc = datetime.strptime(f"{yr} {mon} {day} {hm}", "%Y %b %d %H:%M")
            utc = utc.replace(tzinfo=timezone.utc)
        except ValueError:
            return None
        if start <= utc < end:
            return {"satellite": sat, "event_half": ev_half, "utc": utc}
        return None

    return None


def pair_imcce_half_events(half_events: list[dict]) -> list[dict]:
    """
    Pair start/end half-events into complete event records.
    Strategy: match nearest end to each start within 6 hours, same satellite and base type.
    """
    events: list[dict] = []
    used = set()

    base_type = lambda h: h.split("_")[0]   # 'eclipse_start' → 'eclipse'

    for i, start_ev in enumerate(half_events):
        if i in used:
            continue
        if not start_ev["event_half"].endswith("_start"):
            continue

        btype = base_type(start_ev["event_half"])
        best_j = None
        best_gap = timedelta(hours=6)

        for j, end_ev in enumerate(half_events):
            if j in used or j == i:
                continue
            if not end_ev["event_half"].endswith("_end"):
                continue
            if base_type(end_ev["event_half"]) != btype:
                continue
            if end_ev["satellite"] != start_ev["satellite"]:
                continue
            gap = end_ev["utc"] - start_ev["utc"]
            if timedelta(0) < gap < best_gap:
                best_gap = gap
                best_j = j

        if best_j is not None:
            end_ev = half_events[best_j]
            used.add(i)
            used.add(best_j)
            dur_min = round(best_gap.total_seconds() / 60)
            events.append({
                "type":       btype,
                "satellite":  start_ev["satellite"],
                "start_utc":  start_ev["utc"].strftime("%Y-%m-%dT%H:%M:%SZ"),
                "end_utc":    end_ev["utc"].strftime("%Y-%m-%dT%H:%M:%SZ"),
                "duration_min": dur_min,
            })
        else:
            # Unpaired start — emit with estimated end unknown
            events.append({
                "type":       btype,
                "satellite":  start_ev["satellite"],
                "start_utc":  start_ev["utc"].strftime("%Y-%m-%dT%H:%M:%SZ"),
                "end_utc":    None,
                "duration_min": None,
            })
            used.add(i)

    events.sort(key=lambda e: e["start_utc"])
    return events


# ── Project Pluto fallback parser ─────────────────────────────────────────────

def fetch_pluto_events(start: datetime, end: datetime) -> list[dict] | None:
    """
    Scrape and parse projectpluto.com/jevent.htm.
    Format:  "<SAT_ROMAN> <CODE> <phase>: <YYYY> <Mon> <DD> <HH:MM>"
    e.g.:    "II Sha start: 2026 Jan 01 02:01"
    """
    raw = fetch_url(PLUTO_URL)
    if raw is None:
        return None

    text = raw.decode("utf-8", errors="replace")

    pattern = re.compile(
        r"^(I{1,3}V?|IV)\s+(Ecl|Occ|Tra|Sha)\s+(start|end)\s*:\s*"
        r"(\d{4})\s+(\w{3})\s+(\d{1,2})\s+(\d{2}:\d{2})",
        re.MULTILINE
    )

    half_events: list[dict] = []
    for m in pattern.finditer(text):
        sat_roman, code, phase, yr, mon, day, hm = m.groups()
        sat = PLUTO_SAT_MAP.get(sat_roman)
        btype = PLUTO_TYPE_MAP.get(code)
        if not sat or not btype:
            continue
        try:
            utc = datetime.strptime(f"{yr} {mon} {day} {hm}", "%Y %b %d %H:%M")
            utc = utc.replace(tzinfo=timezone.utc)
        except ValueError:
            continue
        if start <= utc < end:
            half_events.append({
                "satellite":  sat,
                "event_half": f"{btype}_{phase}",
                "utc":        utc,
            })

    if not half_events:
        return None

    # Reuse IMCCE pairing logic
    return pair_imcce_half_events(half_events)


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    start, end = date_window()
    print(f"[INFO] Window: {start.date()} → {end.date()} ({WINDOW_DAYS}d)")
    print(f"[INFO] Observer: lat={OBSERVER_LAT}, lon={OBSERVER_LON}")

    # 1. Fetch Jupiter visibility windows
    print("[INFO] Fetching Jupiter rise/set via Miriade RTS …")
    windows = fetch_jupiter_windows(start, WINDOW_DAYS + 1)
    print(f"[INFO] Got visibility data for {len(windows)} days")

    # 2. Fetch event data
    print("[INFO] Trying IMCCE phenjupiter data file …")
    half_events = fetch_imcce_events(start, end)
    source = "IMCCE-phenjupiter"

    if half_events is None:
        print("[WARN] IMCCE unavailable; falling back to Project Pluto …")
        events = fetch_pluto_events(start, end)
        source = "Project-Pluto"
        if events is None:
            print("[ERROR] Both sources failed — writing empty JSON", file=sys.stderr)
            events = []
    else:
        events = pair_imcce_half_events(half_events)

    print(f"[INFO] Raw events before filter: {len(events)}")

    # 3. Apply Jupiter visibility filter
    visible_events = []
    for ev in events:
        try:
            ev_utc = datetime.fromisoformat(ev["start_utc"].replace("Z", "+00:00"))
        except (ValueError, TypeError):
            visible_events.append(ev)
            continue
        if event_visible(ev_utc, windows):
            visible_events.append(ev)

    print(f"[INFO] Events after visibility filter: {len(visible_events)}")

    # 4. Annotate with display label
    for ev in visible_events:
        ev["type_label"] = DISPLAY_LABELS.get(ev["type"], ev["type"].replace("_", " ").title())

    # 5. Write JSON
    output = {
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": source,
        "observer": {
            "lat": OBSERVER_LAT,
            "lon": OBSERVER_LON,
            "note": "Times accurate to ~5 min for observers within ~60 miles of this coordinate",
        },
        "window_days": WINDOW_DAYS,
        "event_count": len(visible_events),
        "events": visible_events,
    }

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(output, indent=2, ensure_ascii=False))
    print(f"[INFO] Wrote {len(visible_events)} events → {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
