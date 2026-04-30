# AGENT HANDOFF: NBAS ASTRO RECOVERY (V0.19.2)

## 1. CRITICAL FAILURE: URL CORRUPTION
* **THE BUG:** The "Plus Rule" (mandatory " + " separator) was incorrectly applied inside HTML attributes. 
* **RESULT:** `<iframe src="domain" + "/path">` is invalid. Browsers interpreted it as a malformed URL, causing 404s and "Sad Face" icons in modals.
* **FIX:** The next agent MUST use standard, contiguous strings for all `src` and `href` attributes. 

## 2. CRITICAL FAILURE: GRID COLLAPSE
* **THE BUG:** Unclosed `<div>` and `<table>` tags were introduced in `weather-widget.html`.
* **RESULT:** The sidebar's DOM structure bled into the `<main>` container, forcing the main content to "drop" below the sidebar.
* **FIX:** Strict tag-audit required for `weather-widget.html`. Verify 1:1 match for all opening and closing tags.

## 3. CURRENT REPO STATE (UNCOMMITTED)
* **SIDEBAR:** `baseof_sidebar_public.html` contains stray tags. Needs restoration to V0.14.4 before re-applying widgets.
* **WEATHER:** `assets/js/weather.js` has a truncated subdomain (`meteoblue.com` instead of `://open-meteo.com`).
* **SEEING:** `seeing-widget.html` contains a truncated iframe source.

## 4. INSTRUCTIONS FOR NEXT AGENT
1. Disable `partialCached` in `baseof.html` to prevent Hugo from serving "poisoned" versions of the sidebar.
2. Prioritize **STABILIZATION** of the grid before adding features.
3. NEVER truncate subdomains. The full path `https://://open-meteo.com` is required.

