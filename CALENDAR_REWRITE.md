# V0.14.0 ARCHITECTURAL PLAN: UNIFIED CALENDAR WIDGET

## 1. OBJECTIVE
Replace the existing Google Calendar iframe and standalone Almanac widget with a single, high-density, tabbed UI component powered by local flat files.

## 2. DATA ARCHITECTURE
**Format:** Pipe-Delimited Flat Files (`.txt` or `.csv`). One entry per line.
**Location:** `data/calendar_nbas.txt`, `data/calendar_astro.txt`, `data/calendar_almanac.txt`.
**Schema:** `YYYY-MM-DD | HH:MM | Event Description`
*   *Note:* Use `--:--` for events without specific start times.

## 3. COMPONENT STRUCTURE (layouts/partials/calendar-widget.html)
*   **Header (Nav):** Three Tab Buttons: [NBAS] [ALMANAC] [ASTRO].
*   **Body:** High-density list (Next 5 items).
    *   *Formatting:* `MMM DD | HH:MM | Event Title`
*   **Footer:** Month/Year dropdown for archive browsing.

## 4. CSS STRATEGY (assets/css/02-layout.css or new file)
*   **Container:** `display: block` or `flex` with a grounded background.
*   **Tabs:** Active state styling (NBAS Gold) for the selected feed.
*   **List Items:** `line-height` optimization and `font-family: monospace` for the date/time column to ensure vertical alignment.
*   **Spacing:** Aggressive vertical conservation (minimal padding/margins between rows).

## 5. HUGO PARSER LOGIC (Pseudo-code)
```html
{{ $source := "data/calendar_nbas.txt" }}
{{ $content := readFile $source }}
{{ $lines := split $content "\n" }}
<div class="calendar-list">
  {{ range first 5 $lines }}
    {{ $entry := split . " | " }}
    <div class="cal-row">
      <span class="cal-date">{{ index $entry 0 }}</span>
      <span class="cal-time">{{ index $entry 1 }}</span>
      <span class="cal-text">{{ index $entry 2 }}</span>
    </div>
  {{ end }}
</div>

## 6. PIPELINE / AUTOMATION
NBAS Feed: GitHub Action fetches .ics from Google Workspace, converts to flat-file, and commits to data/.

Almanac/Astro Feed: Pre-generated locally (indefinite period) and committed to the repo.

## 7. RECOVERY & STABILITY (CANARY)
Rule #1: No inline styles in the partial.
Rule #2: Use readFile to ensure no remote dependencies at build-time.
Standardization: All date parsing should use Hugo's time function for consistent MMM DD display regardless of source format.

*   **7.1: ISSUE** SOME things are in the local time zone (EST or EDT) - nbas, almanac
        * OTHER THINGS (like astro) are typically in UTC - we might want to 
          try to think of a way for the astro calendar to show both times


