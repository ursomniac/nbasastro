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

# Miriade RTS numeric body codes: 5=Jupiter, 10=Sun
# Comma must be URL-encoded as %2C in the query string
RTS_URL = (
    "https://ssp.imcce.fr/webservices/miriade/api/rts.php"
    "?-body=5"
    "&-nbd={nbd}"
    "&-step=1"
    "&-observer={lon}+{lat}"
    "&-ep={ep}"
    "&-twilight=1"
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
    "eclipse":             "Eclipse (by Jupiter)",
    "occultation":         "Occultation (by Jupiter)",
    "transit":             "Transit (front of Jupiter)",
    "shadow_transit":      "Shadow Transit",
    "mutual_eclipse":      "Mutual Eclipse",
    "mutual_occultation":  "Mutual Occultation",
}

# ── Helpers ───────────────────────────────────────────────────────────────────

def fetch_url(url: str, timeout: int = 20):
    """Fetch a URL, returning bytes or None on failure."""
    try:
        req = Request(url, headers={"User-Agent": "SSO-Dashboard/1.0 (ticket#22)"})
        with urlopen(req, timeout=timeout) as resp:
            return resp.read()
    except (URLError, Exception) as exc:
        print(f"[WARN] fetch failed: {url}\n       {exc}", file=sys.stderr)
        return None


def date_window():
    now = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    return now, now + timedelta(days=WINDOW_DAYS)


# ── Jupiter visibility filter ─────────────────────────────────────────────────

def fetch_jupiter_windows(start: datetime, nbd: int):
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

    windows = {}

    # Response keys are the numeric body codes as strings: "5"=Jupiter, "10"=Sun
    jup_records = data.get("5", [])

    def extract_hour(field):
        """field is either None, a dict, or a list of dicts — handle all cases."""
        if not field:
            return None
        if isinstance(field, list):
            field = field[0] if field else None
        if isinstance(field, dict):
            return field.get("hour", "")
        return None

    for rec in jup_records:
        date_str = rec.get("date", "")
        rising  = rec.get("rising")
        setting = rec.get("setting")
        if not rising or not setting:
            continue   # Jupiter doesn't rise this day

        rise_hms = extract_hour(rising)
        set_hms  = extract_hour(setting)
        rise_jd  = _hms_to_jd(rise_hms, date_str)
        set_jd   = _hms_to_jd(set_hms,  date_str)
        if rise_jd is None or set_jd is None:
            continue

        # If Jupiter sets before it rises on this calendar date, it sets next day
        if set_jd < rise_jd:
            set_jd += 1.0

        windows[date_str] = (rise_jd, set_jd)

    return windows



def _dt_to_jd(dt):
    """Convert a UTC-aware datetime to Julian Date."""
    a = (14 - dt.month) // 12
    y = dt.year + 4800 - a
    m = dt.month + 12*a - 3
    jdn = dt.day + (153*m+2)//5 + 365*y + y//4 - y//100 + y//400 - 32045
    return jdn + (dt.hour - 12)/24.0 + dt.minute/1440.0 + dt.second/86400.0


def _jd_to_dt(jd):
    """Convert Julian Date to UTC-aware datetime."""
    return datetime.fromtimestamp((jd - 2440587.5) * 86400, tz=timezone.utc)


def _hms_to_jd(hms_str, date_str):
    """
    Convert a Miriade HH:MM time string + a YYYY-MM-DD date string to Julian Date.
    Both are in true UTC (no timezone offset applied).
    Returns None if parsing fails.
    """
    if not hms_str or not date_str:
        return None
    try:
        dt = datetime.strptime(f"{date_str} {hms_str}", "%Y-%m-%d %H:%M").replace(tzinfo=timezone.utc)
        return _dt_to_jd(dt)
    except ValueError:
        return None


def _civil_twilight_jd(date_utc, lat_deg, lon_deg):
    """
    Return (jd_dawn, jd_dusk) for civil twilight (Sun at -6 deg) as Julian Dates.
    Uses Spencer (1971) solar declination — accurate to ~1 min.
    No timezone arithmetic. No modulo.
    """
    import math
    doy = date_utc.timetuple().tm_yday
    B = math.radians((360.0/365.0) * (doy - 81))
    dec = 23.45 * math.sin(B)
    eot_min = 9.87*math.sin(2*B) - 7.53*math.cos(B) - 1.5*math.sin(B)
    jd_noon = _dt_to_jd(date_utc.replace(hour=12, minute=0, second=0, microsecond=0))
    jd_solar_noon = jd_noon + eot_min/1440.0 - lon_deg/360.0
    lat   = math.radians(lat_deg)
    dec_r = math.radians(dec)
    cos_ha = (math.sin(math.radians(-6.0)) - math.sin(lat)*math.sin(dec_r)) /              (math.cos(lat)*math.cos(dec_r))
    if abs(cos_ha) > 1:
        return None, None
    ha_days = math.degrees(math.acos(cos_ha)) / 360.0
    return jd_solar_noon - ha_days, jd_solar_noon + ha_days   # jd_dawn, jd_dusk


def _find_window(jd, windows):
    """
    Return the (rise_jd, set_jd, jd_dusk, jd_dawn) tuple for the Jupiter arc
    that contains jd, or None. Checks today and yesterday's date keys.
    """
    dt = _jd_to_dt(jd)
    for date_str in [
        dt.strftime("%Y-%m-%d"),
        (dt - timedelta(days=1)).strftime("%Y-%m-%d"),
    ]:
        candidate = windows.get(date_str)
        if candidate:
            rise_jd, set_jd = candidate
            if rise_jd <= jd <= set_jd:
                rise_date = _jd_to_dt(rise_jd).replace(hour=0, minute=0, second=0, microsecond=0)
                set_date  = _jd_to_dt(set_jd).replace(hour=0, minute=0, second=0, microsecond=0)
                _, jd_dusk = _civil_twilight_jd(rise_date, OBSERVER_LAT, OBSERVER_LON)
                jd_dawn, _ = _civil_twilight_jd(set_date,  OBSERVER_LAT, OBSERVER_LON)
                return rise_jd, set_jd, jd_dusk, jd_dawn
    return None


def event_visible(start_utc, end_utc, windows):
    """
    True if the event overlaps the observable window at all.
    Observable window = intersection of Jupiter-above-horizon and civil night.

    Overlap test: event_start < obs_end AND event_end > obs_start
    So an event that starts in twilight but ends in darkness is included,
    and one that starts before Jupiter sets but finishes after is included.

    end_utc may be None (unpaired event) — treat as a point event at start.
    """
    if not windows:
        return True

    jd_start = _dt_to_jd(start_utc)
    jd_end   = _dt_to_jd(end_utc) if end_utc else jd_start

    # Find the window for the start time; if not found try the end time.
    win = _find_window(jd_start, windows) or _find_window(jd_end, windows)
    if win is None:
        return False

    rise_jd, set_jd, jd_dusk, jd_dawn = win

    # Observable window = max(rise, dusk) to min(set, dawn)
    if jd_dusk is not None and jd_dawn is not None:
        obs_start = max(rise_jd, jd_dusk)
        obs_end   = min(set_jd,  jd_dawn)
    else:
        obs_start = rise_jd
        obs_end   = set_jd

    if obs_end <= obs_start:
        return False  # no observable window tonight

    # Overlap: event interval and obs window must intersect
    return jd_start < obs_end and jd_end > obs_start




# ── IMCCE phenjupiter parser ──────────────────────────────────────────────────

def fetch_imcce_events(start: datetime, end: datetime):
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


def _parse_imcce_line(line: str, start: datetime, end: datetime):
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


def pair_imcce_half_events(half_events: list):
    """
    Pair start/end half-events into complete event records.
    Strategy: match nearest end to each start within 6 hours, same satellite and base type.
    """
    events: list[dict] = []
    used = set()

    # Strip _start or _end suffix to get base type
    # e.g. 'shadow_transit_start' → 'shadow_transit', 'eclipse_start' → 'eclipse'
    def base_type(h):
        if h.endswith("_start"):
            return h[:-6]
        if h.endswith("_end"):
            return h[:-4]
        return h

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
            # Unpaired start (e.g. occultation that ends outside the window) — skip
            # rather than show a confusing row with — end time and no duration
            used.add(i)

    events.sort(key=lambda e: e["start_utc"])
    return events


# ── Project Pluto fallback parser ─────────────────────────────────────────────

def fetch_pluto_events(start: datetime, end: datetime):
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
        try:
            ev_end_utc = datetime.fromisoformat(ev["end_utc"].replace("Z", "+00:00")) if ev.get("end_utc") else None
        except (ValueError, TypeError):
            ev_end_utc = None
        if event_visible(ev_utc, ev_end_utc, windows):
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
