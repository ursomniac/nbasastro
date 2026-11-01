#!/usr/bin/env bash
# scripts/local_data.sh
# Generate the same data files the GitHub "Deploy" workflow makes, so
# `hugo server` on localhost shows them. Run from anywhere:
#     scripts/local_data.sh            # data only
#     scripts/local_data.sh --serve    # data, then hugo server -D -F
#
# Mirrors .github/workflows/hugo.yml (keep the two in step if that changes).
# Steps that need something you don't have locally are skipped with a note,
# not failed.

set -u
cd "$(git rev-parse --show-toplevel)" || exit 1

PY="${PYTHON:-python3}"
mkdir -p static/data static/data/comets

echo "== Galilean satellite events"
OBSERVER_LAT="42.7" OBSERVER_LON="-73.11" WINDOW_DAYS="15" \
OUTPUT_PATH="static/data/galilean-events.json" \
  "$PY" scripts/fetch_galilean_events.py || echo "   (galilean step failed; continuing)"

echo "== Comet ephemerides"
if "$PY" -c "import pandas, skyfield, jplephem" 2>/dev/null; then
  WINDOW_DAYS="30" "$PY" scripts/fetch_comet_ephemerides.py || echo "   (comet step failed; continuing)"
else
  echo "   skipped: needs  pip install pandas skyfield jplephem"
fi

echo "== Calendar"
if "$PY" -c "import requests, icalendar, recurring_ical_events" 2>/dev/null; then
  "$PY" scripts/sync_calendar.py || echo "   (calendar step failed; continuing)"
else
  echo "   skipped: needs  pip install requests icalendar recurring_ical_events"
fi

echo "== ISS passes"
if [ -n "${N2YO_API_KEY:-}" ]; then
  curl -s "https://api.n2yo.com/rest/v1/satellite/visualpasses/25544/42.7/-73.11/300/10/40/?apiKey=${N2YO_API_KEY}" \
    -o static/data/iss-passes.json && echo "   wrote static/data/iss-passes.json"
else
  echo "   skipped: set N2YO_API_KEY to fetch"
fi

# Starmaps and the Clear Sky Chart are left out: slow, and not needed to preview articles.

if [ "${1:-}" = "--serve" ]; then
  echo "== hugo server (drafts + future-dated)"
  exec hugo server -D -F
fi
