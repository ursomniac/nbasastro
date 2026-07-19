# Handoff: Comet Widget Fixes — NBASAstro

Written for a fresh agent with no memory of prior sessions. Read this fully before
touching anything. The user (Bob) has had a very rough night with a related but separate
piece of this codebase (the Jupiter/Galilean events widget) — read the "Process rules"
section before doing anything, it exists for real reasons.

## Repo

- Real path: `/Users/robertdonahue/Projects/NBAS/NBASAstro` (Hugo site, no theme, deploys
  to `https://nbasastro.org` via GitHub Actions on push to `main`).
- If working through Cowork/a similar tool: request direct folder access to that path
  rather than shuffling files through a scratch/outputs folder and asking the user to
  copy things manually. That indirection caused real, serious problems in the prior
  session — wrong file copied, ambiguous instructions, user lost hours over it.
- Note on tool path mapping if using a sandboxed bash tool alongside direct file
  Read/Write/Edit access: the same folder may be mounted at a *different* path for bash
  specifically (e.g. `/sessions/.../mnt/NBASAstro`) than for Read/Write/Edit/Grep/Glob
  (which use the real Mac path above). Don't mix them up.

## Current state (verified, not assumed)

Live production data at `https://nbasastro.org/data/comets/index.json` is fresh and
correct as of this writing (`generated_utc` matched the most recent nightly Action run,
all 5 comets present with real JPL Horizons data). **The fetch pipeline works.** JPL
Horizons (`https://ssd.jpl.nasa.gov/api/horizons.api`) is an official API and has not
shown any sign of blocking/truncating GitHub Actions' network, unlike a different,
unrelated widget on this site (Project Pluto scraping) that does have that problem —
don't assume the two widgets share a root cause, they don't.

Do not trust the local repo copy of `static/data/comets/*.json` as a freshness signal —
those are git-tracked placeholder files (last real commit dated May), not live data. They
are never written back to git by the nightly Action (the workflow has no commit/push
step — it fetches fresh data into the ephemeral runner, builds, and deploys the built
`public/` artifact directly; nothing generated during a run is ever committed). Always
check the *live* URL above for real freshness, not files on disk.

## Confirmed bug #1 — missing cache-busting on fetch (low risk, mechanical fix)

File: `layouts/partials/comets.html`, in the `<script>` block near the bottom.

Current:
```js
fetch('/data/comets/index.json')
  ...
return fetch(entry.ephemeris_file)
```

Fix: add `{ cache: 'no-store' }` as the second argument to both calls. Without it, a
visitor's browser can cache the first response it ever sees for these URLs and never
re-fetch, so the table can look frozen even though the server has fresh data every night.
This exact bug, same fix, was already found and fixed in a sibling widget
(`layouts/partials/galilean-events.html` — look at that file's `fetch(...)` call as a
reference for the fixed pattern before editing this one).

## Confirmed bug #2 — partial fetch failure deletes good cached data

File: `scripts/fetch_comet_ephemerides.py`, `main()`, near the end (search for
`Prune stale files`).

The module docstring claims a Horizons outage "leaves existing data intact." That's only
true if *every* comet fails (script exits early in that case). If some comets succeed and
one doesn't (a single timeout/rate-limit/malformed response), the prune loop deletes that
one comet's previously-good JSON file, because it only protects filenames that are in
`slugs_written` (this run's successes) — it doesn't distinguish "still in comets.yaml but
failed this run" from "no longer in comets.yaml at all." Net effect: one flaky fetch makes
a comet silently vanish from the live site with no fallback, contradicting the stated
design intent.

Fix approach: compute the full set of slugs that *should* exist (everything currently in
`comets.yaml`, regardless of whether this run's fetch succeeded for it) and only delete a
file if its slug is not in that full set. Never delete a file just because this run's
fetch for it failed.

## Open question, not a bug — needs a decision, not code

`data/comets.yaml`'s header says it's a manually curated list, reviewed monthly by hand.
There is no code anywhere that filters comets by current brightness or visibility — the
script fetches an ephemeris for literally every YAML entry regardless of whether it's
actually worth showing. Confirmed live: `C/2025 R3` is currently magnitude ~16.7 (not
visible to typical amateur equipment) and still appears in the table.

If the user wants this automated eventually, that requires the user to first decide what
"worth showing" means numerically (a magnitude cutoff? months-from-perihelion cutoff?) —
don't invent a threshold and implement it without asking; this is a judgment call for the
user, not something to guess at.

## Unresolved, flagged, not explained

Bob previously pasted terminal output showing a successful local run of this script. The
actual tracked files in the repo (`static/data/comets/*.json`) are dated May 10 with zero
uncommitted changes — meaning that run, wherever/whenever it happened, didn't write into
this repo as it currently sits. Not diagnosed. Worth a quick sanity check (`git status`,
`ls -la static/data/comets/`) before assuming the local dev loop is in a known-good state.

## Process rules (please actually follow these)

1. **Verify live state with a real fetch before claiming anything is fixed or broken.**
   Don't reason from git logs or file contents alone — hit the actual
   `nbasastro.org/data/...` URL and read what comes back.
2. **Never commit or push without the user explicitly saying to.** Staging/showing a diff
   is fine; `git commit`/`git push` is not a default action.
3. **Show the actual diff, not a prose description, before it's committed.** The user
   has explicitly asked for this after being burned by prose-only descriptions earlier.
4. **If a proposed fix requires running something that only works from a machine with
   normal outbound network access (not a sandboxed agent environment), say so plainly and
   give the user the exact command to run themselves** — don't imply you'll handle it and
   then fail silently the same way twice.
5. **No guessing.** If something is ambiguous (file location, whether a change was
   actually deployed, whether a value is stale), check it directly before stating it as
   fact.

## Suggested order of work

1. Fix #1 (cache-busting) — small, low-risk, isolated to one file.
2. Fix #2 (prune logic) — small, isolated to one function, but think through the edge
   case (comet removed from yaml *and* fetch failed same night) before writing it.
3. Bring the "should this be automatic" question back to the user as a question, not a
   decision already made.

No code has been changed as of this handoff. Full original analysis (with more detail and
the exact live JSON that was checked) is in `comet-widget-analysis.md` alongside this
file, if more context is needed.
