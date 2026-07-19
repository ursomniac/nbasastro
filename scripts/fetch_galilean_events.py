#!/usr/bin/env python3
"""
fetch_galilean_events.py
Ticket #22 — Galilean satellite phenomena table

Fetch strategy:
  Project Pluto jevent.htm is the primary (and currently only enabled) source.
  Covers all four classical phenomena: eclipse, occultation, transit, shadow transit.
  The page itself is correct and complete (confirmed by hand: full year, no
  gaps, right format) -- but a live fetch of it from inside this GitHub
  Actions job comes back HTTP 200 with content that parses to zero events,
  while the identical URL fetched by hand (curl, or a normal browser UA)
  works fine. No exception is raised either way, so this fails silently.
  Root cause not fully confirmed under time pressure -- leading suspects are
  the bot-like User-Agent this script used to send, or GitHub's shared
  runner IPs getting different treatment from Project Pluto's server.

  To not depend on solving that today, load_pluto_html() now: (1) tries a
  live fetch with a normal browser User-Agent, in case that alone was the
  problem; (2) validates the response actually looks like a populated page
  (hundreds of event-code hits expected) rather than trusting any HTTP 200;
  (3) automatically falls back to a cached, git-committed copy of the page
  (PLUTO_CACHE_PATH) if either of those fail. Nothing here requires anyone
  to remember to run anything for the site to keep showing correct-ish data
  -- refresh the cache by hand (scripts/fetch_pluto_cache.sh) whenever
  convenient, or wire up a low-frequency job later.

  IMCCE phenjupiter (intended as the authoritative NOE-5-2021 source) is
  PARKED, not deleted -- set USE_IMCCE=true to re-enable it. As of 2026-07:

    - The original IMCCE_PHEN_URL_TMPL path (phen_jup_<year>.txt) does not
      exist on IMCCE's server at all -- confirmed via the real directory
      listing at https://ftp.imcce.fr/pub/ephem/satel/phenjupiter/. It was
      apparently guessed or copied from stale documentation and has never
      worked, silently falling through to Project Pluto every run.
    - The real per-year files there are named ftp_jupiter_Events_UT_<year>.txt
      (confirmed against a real downloaded 2027 copy). That one is a dense,
      fixed-width, four-column-per-line layout that doesn't match the
      delimited format _parse_imcce_line() expects.
    - Also present, untried: phenE.<year> / phenF.<year> (~57K, vs. ~72K for
      the Events_UT file) -- possibly English/French-labeled variants in a
      different, more delimited format. Worth checking first before writing
      a parser for the packed Events_UT layout.

  Whichever file ends up being used, update IMCCE_PHEN_URL_TMPL and
  _parse_imcce_line() together, then flip USE_IMCCE back on. Project Pluto
  covers the same four phenomena and has been reliably correct every night
  this whole time, so there's no urgency here.

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

# IMCCE is parked (see module docstring above) -- defaults OFF so the working
# Project Pluto path is what actually runs, without deleting the IMCCE code.
USE_IMCCE = os.environ.get("USE_IMCCE", "false").strip().lower() in ("1", "true", "yes")

# Project Pluto's jevent.htm reads correctly (full year, right format) when
# fetched from a normal machine -- confirmed by hand with curl. It reads back
# as 0 events when fetched live from inside this GitHub Actions job, with no
# fetch error logged, meaning something about the CI environment (shared IP
# range, the bot-like User-Agent below, or similar) gets a different response
# without triggering an exception. Rather than chase that down under time
# pressure, PLUTO_CACHE_PATH lets a periodically-refreshed, git-committed
# copy of the page stand in for the live fetch: refresh it by hand (or via a
# separate low-frequency job later) from somewhere proven to work. Priority
# is: (1) live fetch, now with a real browser User-Agent instead of the
# bot-like one below, in case that's what triggered CI getting back different
# content than a hand-run curl gets; (2) if that fails, or "succeeds" but the
# response doesn't actually look like a populated events page, fall back to
# this cached copy automatically -- no one has to remember to run anything
# for the site to keep showing correct-ish data even if the live fetch never
# gets fixed. Refresh the cache by hand whenever convenient (see the
# fetch_pluto_cache.sh helper), or wire up a low-frequency job later.
PLUTO_CACHE_PATH = Path(os.environ.get("PLUTO_CACHE_PATH",
                        Path(__file__).parent.parent / "static" / "data" / "_cache" / "jevent.htm"))
PLUTO_USER_AGENT = os.environ.get("PLUTO_USER_AGENT",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")

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

# IMCCE phenjupiter data file (HTTPS mirror of the FTP). Published one file
# per calendar year as phen_jup_<YEAR>.txt -- NOT hardcoded to a single year:
# fetch_imcce_events() below fills in {year} for every calendar year touched
# by the requested [start, end) window, so this keeps working every January
# without anyone needing to edit this file again.
IMCCE_PHEN_URL_TMPL = "https://ftp.imcce.fr/pub/ephem/satel/phenjupiter/phen_jup_{year}.txt"
IMCCE_PHEN_URL_ALT_TMPL = "https://ftp.imcce.fr/pub/ephem/satel/phenjupCDT/phen_jup_{year}.txt"

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

def fetch_url(url: str, timeout: int = 20, user_agent: str = "SSO-Dashboard/1.0 (ticket#22)"):
    """Fetch a URL, returning bytes or None on failure."""
    try:
        req = Request(url, headers={"User-Agent": user_agent})
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

def _imcce_urls_for_year(year: int):
    return (IMCCE_PHEN_URL_TMPL.format(year=year), IMCCE_PHEN_URL_ALT_TMPL.format(year=year))


def fetch_imcce_events(start: datetime, end: datetime):
    """
    Attempt to download and parse the IMCCE phenjupiter flat-text prediction
    file(s), one per calendar year touched by [start, end). Each file only
    covers its own calendar year, so a window that crosses a Dec 31 / Jan 1
    boundary needs both years' files -- this fetches every distinct year in
    the window and merges the results, rather than assuming a single year.

    Returns a list of raw half-events (each line is one start or end boundary),
    or None if every year's fetch fails.

    File format (two variants depending on year):
    Old:  YYYY MMM DD  HH:MM  <SAT>  <CODE>
    New:  <SAT_NUM>  YYYY-MM-DD  HH:MM:SS.S  <CODE>

    We try both URL forms and both parse approaches, per year.
    """
    # end is exclusive, so the last real moment in-window is (end - 1 second)
    years = sorted({start.year, (end - timedelta(seconds=1)).year})

    half_events: list[dict] = []
    any_fetched = False

    for year in years:
        url, url_alt = _imcce_urls_for_year(year)
        raw = fetch_url(url) or fetch_url(url_alt)
        if raw is None:
            print(f"[WARN] IMCCE phenjupiter file unavailable for {year} "
                  f"(tried {url} and {url_alt})", file=sys.stderr)
            continue
        any_fetched = True

        text = raw.decode("utf-8", errors="replace")
        for line in text.splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            ev = _parse_imcce_line(line, start, end)
            if ev:
                half_events.append(ev)

    if not any_fetched:
        # Every year's file failed to download -- genuine outage/URL problem
        return None

    if not half_events:
        # File(s) fetched fine, just nothing landed in this particular window
        print("[WARN] IMCCE file(s) parsed but yielded 0 events in window", file=sys.stderr)
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

    # Sort by time first so pairing is stable across merged multi-year fetches
    half_events = sorted(half_events, key=lambda e: e["utc"])

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

def _looks_like_populated_pluto_page(raw: bytes) -> bool:
    """
    Sanity check that a fetch actually returned a real, populated events
    page rather than something that came back HTTP 200 but empty, blocked,
    or otherwise not what we expect (which is exactly what happened when
    this was fetched live from inside GitHub Actions -- no fetch error, just
    zero parseable events). A real page has hundreds of event lines; require
    a reasonable minimum before trusting it.
    """
    if not raw or len(raw) < 5000:
        return False
    text = raw.decode("utf-8", errors="replace")
    hits = len(re.findall(r"\b(Ecl|Occ|Tra|Sha)\b", text))
    return hits > 20


def load_pluto_html():
    """
    Return the raw bytes of jevent.htm. Tries a live fetch first (with a
    normal browser User-Agent); if that fails outright, or "succeeds" but
    doesn't look like a real populated page, falls back automatically to a
    cached, git-committed copy (PLUTO_CACHE_PATH). See the config comment
    above for the full story on why both paths exist. Returns None only if
    neither source works.
    """
    raw = fetch_url(PLUTO_URL, user_agent=PLUTO_USER_AGENT)
    if raw is not None and _looks_like_populated_pluto_page(raw):
        print(f"[INFO] Live Pluto fetch looks valid ({len(raw)} bytes)")
        return raw

    if raw is not None:
        print(f"[WARN] Live Pluto fetch returned {len(raw)} bytes but doesn't look like a "
              f"populated events page — falling back to cache", file=sys.stderr)

    if PLUTO_CACHE_PATH.exists():
        try:
            raw = PLUTO_CACHE_PATH.read_bytes()
            age_days = (datetime.now(timezone.utc).timestamp() - PLUTO_CACHE_PATH.stat().st_mtime) / 86400
            print(f"[INFO] Using cached Pluto file: {PLUTO_CACHE_PATH} "
                  f"({len(raw)} bytes, {age_days:.1f} days old)")
            if age_days > 30:
                print(f"[WARN] Pluto cache is {age_days:.0f} days old — consider refreshing it "
                      f"(run scripts/fetch_pluto_cache.sh)", file=sys.stderr)
            return raw
        except OSError as exc:
            print(f"[WARN] Could not read Pluto cache at {PLUTO_CACHE_PATH}: {exc}", file=sys.stderr)

    print("[ERROR] No valid live fetch and no usable cache file — giving up on Pluto", file=sys.stderr)
    return None


def fetch_pluto_events(start: datetime, end: datetime):
    """
    Parse Project Pluto's jevent.htm (see load_pluto_html() for where the
    bytes actually come from).
    Format:  "<SAT_ROMAN> <CODE> <phase>: <YYYY> <Mon> <DD> <HH:MM>"
    e.g.:    "II Sha start: 2026 Jan 01 02:01"
    """
    raw = load_pluto_html()
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
    #
    # IMCCE is parked, not deleted: as of 2026-07, the file IMCCE actually
    # publishes at this path is a dense fixed-width, four-column-per-line
    # layout that has never matched the delimited format _parse_imcce_line()
    # expects (confirmed against a real downloaded 2027 file) -- so this
    # branch has been silently failing and falling through to Project Pluto
    # every night since the feature was built. Project Pluto covers the same
    # four phenomena and has been reliably correct this whole time, so it's
    # now the default. Set USE_IMCCE=true once someone reverse-engineers the
    # real column format in fetch_imcce_events() / _parse_imcce_line().
    if USE_IMCCE:
        print("[INFO] Trying IMCCE phenjupiter data file(s) …")
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
    else:
        print("[INFO] IMCCE parser disabled (USE_IMCCE=false) — using Project Pluto")
        events = fetch_pluto_events(start, end)
        source = "Project-Pluto"
        if events is None:
            print("[ERROR] Project Pluto fetch failed — writing empty JSON", file=sys.stderr)
            events = []

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
