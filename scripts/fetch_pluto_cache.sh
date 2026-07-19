#!/usr/bin/env bash
# scripts/fetch_pluto_cache.sh
#
# Refreshes the cached copy of Project Pluto's jevent.htm that
# fetch_galilean_events.py falls back to when a live fetch from inside
# GitHub Actions doesn't come back with real data (see the module docstring
# in fetch_galilean_events.py for the full story).
#
# The page covers the entire year in one listing, so this is a one-time
# seed, not a recurring chore -- a cache downloaded today stays correct
# for every script run between now and roughly mid-January 2027, when
# Project Pluto's site rolls over to next year's page.
#
# Usage:  bash scripts/fetch_pluto_cache.sh   (run from repo root)

set -euo pipefail

OUT="static/data/_cache/jevent.htm"
URL="https://www.projectpluto.com/jevent.htm"

mkdir -p "$(dirname "$OUT")"

curl -s -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36" \
  "$URL" -o "$OUT"

LINES=$(wc -l < "$OUT")
BYTES=$(wc -c < "$OUT")
HITS=$(grep -oE '\b(Ecl|Occ|Tra|Sha)\b' "$OUT" | wc -l)

echo "Wrote $OUT  ($BYTES bytes, $LINES lines, $HITS event-code hits)"

if [ "$HITS" -lt 20 ]; then
  echo "WARNING: that doesn't look like a populated events page -- check $OUT before committing." >&2
  exit 1
fi

echo "Looks good. Now: git add $OUT && git commit -m 'Seed Pluto events cache for CI fallback' && git push"
