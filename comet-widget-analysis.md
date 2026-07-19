# Comet Ephemerides Pipeline — End-to-End Analysis

Scope: `scripts/fetch_comet_ephemerides.py`, `data/comets.yaml`, `layouts/partials/comets.html`,
the "Fetch comet ephemerides" step in `.github/workflows/hugo.yml`, and the live deployed
data at nbasastro.org. Analysis only — no code was changed.

## Bottom line

The data pipeline itself works. This is a materially different situation from the
Jupiter/Galilean-events problem: JPL Horizons is an official NASA/JPL API meant for
programmatic access, not a scraped hobbyist page, and it is not blocking or truncating
GitHub Actions' network the way Project Pluto's site does. Verified live just now:

```
https://nbasastro.org/data/comets/index.json
generated_utc: 2026-07-19T06:02:24Z   ← this morning's run, real data, all 5 comets present
```

So "is the comet data fetch broken" — no, not right now. There are two real, separate
problems underneath it, both concrete and fixable, plus one architectural gap that answers
your question about comet selection.

## Problem 1 (confirmed bug): same browser-cache issue the Galilean events table had

`layouts/partials/comets.html`, lines ~463 and ~477:

```js
fetch('/data/comets/index.json')
  ...
return fetch(entry.ephemeris_file)
```

Neither call uses `{ cache: 'no-store' }`. This is the exact bug class that caused the
Galilean events table to look "stuck since May" for anyone whose browser had already
cached the response — the server can be updating every night and a visitor's browser will
never know, because the default HTTP cache will keep serving the first response it ever
saw for that URL. The server-side data is fine; a browser that loaded this page once could
still show stale positions indefinitely. This wasn't caught when the widget shipped because
it's not visible from the server side — you have to actually hit reload twice and compare.

Fix is mechanical and low-risk: add `{ cache: 'no-store' }` to both fetch calls, same as
was just done for `galilean-events.html`.

## Problem 2 (confirmed logic bug): a partial fetch failure silently deletes good data

In `fetch_comet_ephemerides.py`, the module docstring claims:

> Stale files (comets removed from comets.yaml) are pruned at the end, but ONLY after all
> fetches have completed — so a Horizons outage leaves existing data intact.

That's only true for a *total* outage. Look at the actual prune logic (lines ~436-441):

```python
written_set = set(slugs_written)
for existing in COMET_OUT.glob("*.json"):
    if existing.stem != "index" and existing.stem not in written_set:
        existing.unlink()
```

`slugs_written` only contains comets that succeeded *this run*. If 4 of 5 comets fetch
fine and one has a transient Horizons hiccup (timeout, malformed response, temporary rate
limit), that one comet's slug is not in `written_set` — so this loop deletes its
previously-good JSON file, and it also won't appear in the new `index.json` (which is only
built from `slugs_written`). Net effect: a single flaky fetch makes a comet vanish from the
live site with no fallback to yesterday's good data, contradicting the stated design intent.
The "leaves existing data intact" behavior only actually triggers on a 100% total failure
(`if not slugs_written: sys.exit(0)`), not a partial one — which is the far more likely
real-world failure mode.

Fix: track "comets that were supposed to run this time" (i.e., everything in
`comets.yaml`) separately from "comets successfully fetched," and only prune files for
comets that were *removed from comets.yaml entirely* — never prune a file just because its
fetch failed this one time.

## Your question: how does the system know which comets belong in the table?

It doesn't, automatically — and confirming that gap is a legitimate finding, not a gap in
my analysis. `data/comets.yaml`'s own header says it plainly:

> Manually curated list of comets worth showing in the SSO Comet Panel.
> Maintainer: review monthly. Add comets as they become viable, remove when faded.

There is no code anywhere in `fetch_comet_ephemerides.py` that filters by current
magnitude, visibility, or proximity to perihelion. The script fetches an ephemeris for
literally every entry in the YAML file, unconditionally, every night, regardless of whether
it's actually worth showing. Live proof of this right now: C/2025 R3 is currently sitting
at **magnitude 16.7** (invisible to anything but a large telescope, arguably not
"worth showing" to a club audience) and is still in the table, while 2P/Encke is listed
even though its own `warning` field says "Not yet observable — brightening from December
2026." Both are technically correct outputs of the pipeline; neither reflects an automatic
"should this actually be shown right now" decision, because that decision doesn't exist in
code. It's 100% on whoever edits the YAML file by hand.

This isn't a bug so much as an intentionally unfinished piece — Gemini built the fetch/
render pipeline but never built (or was never asked to build) the curation logic. If you
want that automated, the natural approach would be a threshold check in `main()` before
fetching — skip (or flag) any comet whose `peak_magnitude` is fainter than some cutoff, or
whose `perihelion_date` is more than N months away — but that requires you to decide what
"worth showing" actually means numerically, which is a judgment call, not something I
should guess at.

## Things checked and found fine

- **No duplicate-ID rendering bug** (the class of bug that broke the SSD widget): `comets`
  partial is included exactly once, in `layouts/shortcodes/sso-table.html` line 363.
- **Workflow step is structurally correct**: installs PyYAML, creates the output dir,
  passes `WINDOW_DAYS=30`, runs after the Galilean events step, before CDS charts. No
  ordering or environment issues.
- **JSON schema matches what the frontend expects**: `index.json`'s `ephemeris_file`,
  `designation`, `current.*` fields and each per-comet file's `ephemeris[].date_utc` /
  `ra_deg` / `t_mag` etc. line up with exactly what `comets.html`'s JS reads
  (`interpolate()`, `renderTable()`, `openModal()`).
- **Live data is scientifically live**: spot-checked `10P/Tempel 2`'s live entry
  (`t_mag: 13.079`, approaching its stated July 25 perihelion) against its own
  `comets.yaml` note ("Expected to peak July–August 2026") — consistent, not stale, not
  contradictory.

## One thing I could not verify, and won't guess at

At the very start of this analysis you pasted terminal output showing a local run of this
script completing successfully just now. The actual files on disk in your repo
(`static/data/comets/*.json`, tracked in git) are dated **May 10**, and `git status` shows
no local modifications to them — meaning whatever that pasted output was, it didn't write
into this repo as it currently sits on this mount. I don't know whether that was output
from a different location, an earlier session, or something else — flagging it rather than
assuming either way.

## Suggested priority, not started

1. Add `cache: 'no-store'` to the two fetch calls in `comets.html` (mechanical, ~2 line
   change, same pattern already applied to the Galilean events partial).
2. Fix the prune-on-partial-failure logic in `fetch_comet_ephemerides.py` so one flaky
   comet fetch can't delete good cached data for that comet.
3. Decide, on your own time, whether comet inclusion should ever be automatic — and if so,
   what the actual cutoff should be. Not urgent; the manual-curation model is at least
   honest about what it is right now.

No files were modified as part of this analysis.
