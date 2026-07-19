# Comet Curation v2 — Design Sketch (not implemented)

Status: proposal only. No code written against this. Captures the Milestone 2
discussion from the 2026-07-19 session so it isn't lost if we run out of time box.

## Problem (as stated by Bob)

`data/comets.yaml` is 100% manually curated — reviewed monthly by hand. Two failure
modes result:
1. A newly discovered comet that brightens fast can go unnoticed until someone
   manually adds it — there's no automatic "hey, this is now worth showing" signal.
2. A comet already in the file can fade past usefulness (e.g. `C/2025 R3` currently
   sitting at mag ~16.7, confirmed live in the prior analysis) and nothing removes it
   automatically.

JPL Horizons stays the source of truth for the actual per-day numbers shown in the
table (RA/Dec/magnitude) — that part isn't in question. The gap is upstream of
Horizons: how do we decide *which* comets to even ask Horizons about, without a human
re-reading the whole sky every month.

## Proposed shape: two scripts, decoupled schedules

Revised per Bob (2026-07-19, mid-session): not one pipeline, but two independent
scripts with different cadences.

```
Script 1 — candidate-list builder (NEW, not built)
  MPC comet catalog (all known comets, orbital elements)
        │  broad pull, no per-object network cost
        ▼
  Physics-based observability filter (perihelion date/distance + magnitude estimate)
        │  pure math over already-downloaded elements, cheap
        ▼
  Candidate list (e.g. data/comet_candidates.generated.yaml) — committed to the repo

Script 2 — Horizons poller (EXISTING: fetch_comet_ephemerides.py, already fixed)
  Reads a candidate list (today: hand-edited comets.yaml; future: Script 1's output)
        │  existing Horizons fetch, unchanged
        ▼
  static/data/comets/*.json  (same output shape as today, runs every night at build time)
```

Why split: Script 2 needs to run every night at build time (nightly GitHub Action,
same as today). Script 1 doesn't — polling the *entire* MPC catalog nightly is
wasteful and gives Bob no chance to sanity-check the algorithm's picks before they go
live. Decoupling lets Script 1 run on its own (slower) cadence and produce a reviewable
artifact rather than silently driving the live site.

### Open question: who runs Script 1, and when?

Bob's own framing: Script 1 could be local-only initially (run by hand, output
committed/pushed, then consumed by Script 2 at build time) — but that "still requires
someone to remember to run it," which is the same failure mode as the current
monthly-manual-review process, just one level removed. Bob flagged this as needing a
broader "system check / curation / housekeeping" process eventually, not just this one
script.

One concrete option worth naming: this Cowork session already has a scheduled-task
mechanism (recurring runs, e.g. "every month"). That could own Script 1's cadence —
either running it and hard-committing the result, or running it and handing Bob a
diff to approve before it touches the live candidate list. Not built, not decided —
flagging as a real option rather than leaving "remembering" as pure human overhead.

## Data source for stage 1 — confirmed, needs one more verification pass

The Minor Planet Center publishes a plain-text **Ephemerides and Orbital Elements**
export for comets. Column layout, confirmed directly from MPC's own format doc
(https://www.minorplanetcenter.net/iau/info/CometOrbitFormat.html) just now:

- Periodic comet number, orbit type, designation
- Year/month/day of perihelion passage
- Perihelion distance (AU)
- Orbital eccentricity
- Argument of perihelion, longitude of ascending node, inclination
- **Absolute magnitude** and **slope parameter** — the two values needed to estimate
  brightness at an arbitrary future date without calling Horizons
- Designation and name, reference

This is exactly the field set stage 2 needs (perihelion date + distance + the two
magnitude parameters). What I have **not** yet verified and would check before writing
code: the exact machine-readable download URL/filename for this dataset (the doc page
references an "Extended Computer Service" and a general orbital-elements listing page,
but I didn't pin down the direct file URL or its update cadence/rate limits). Canonical
place to check: https://www.minorplanetcenter.net/iau/Ephemerides/EphemOrbEls.html and
https://www.minorplanetcenter.net/data before writing any fetch code.

Alternative/backup source spotted but not verified in this session: JPL's own
Small-Body Database Query API (https://ssd-api.jpl.nasa.gov/doc/sbdb.html), which the
same JPL org already trusted for Horizons. It's queryable and reportedly updated daily,
but I couldn't load its parameter docs in this session (fetch timed out) — don't build
against it without confirming actual query parameters and response schema first.

**Blocker found this session, still open pending Gareth:** MPC's "Orbital Elements for
Software Packages" page references "new downloading restrictions" on its status page.
Bob's read: usage this small (~150KB file, infrequent polling) is almost certainly
fine, this note may be legacy/stale, and asked Gareth directly. Not resolved yet, but
not treated as blocking further design work — Script 1 code just shouldn't ship until
confirmed.

**Confirmed, independently, since:** the exact file is
`https://www.minorplanetcenter.net/iau/MPCORB/CometEls.txt` — found cited directly in
Skyfield's own documentation (an actively-maintained astronomy library, not MPC's own
marketing copy), whose own example loads 864 comets from it. Matches Bob's ~150KB
estimate. This is the standard, widely-used source for exactly this purpose.

**Performance ("can this run quickly over ~1000 targets"):** yes, conceptually —
comet position at a given time is the classical two-body Kepler problem (solve
Kepler's/Barker's/hyperbolic-Kepler equation depending on eccentricity, a few
Newton-Raphson iterations, microseconds). This is how every planetarium app animates
thousands of objects live. Skyfield already implements all three orbit-type solvers
and dispatches automatically by eccentricity — the filter script never needs to
special-case orbit type. One real caveat from Skyfield's own docs: no
batched/vectorized multi-comet call yet, so ~860 comets × a few sample epochs is a
plain Python loop. Should still be seconds not minutes, but "should" isn't good enough
per this repo's rules — a timing test script was written
(`scripts/prototype_mpc_timing_test.py`, not part of the pipeline, throwaway) to get
a real number. Couldn't run it from the sandboxed session that drafted this doc — both
a direct `curl` and the fetch tool failed to reach minorplanetcenter.net (connection
error, then timeout). Needs to run from a machine with normal network access.

**Winnowing strategy — resolved conceptually, doesn't need orbit-type branching:**
don't special-case "perihelion in the window" vs. "perihelion outside the window" vs.
hyperbolic vs. periodic at all. Sample estimated apparent magnitude (from heliocentric
distance r and geocentric distance Δ, both cheap per-epoch outputs of the Kepler
propagation above) at a handful of evenly-spaced epochs across the window (e.g. 5
points across 60 days). Take the best (lowest) estimated magnitude across those
samples as "how bright does this get during the window," and threshold that. This
uniformly covers: past-perihelion-but-still-bright (88P/Howell today), a comet
approaching perihelion later in the window (2P/Encke today), and an edge case like a
hyperbolic interstellar object that's already past perihelion but still close/bright —
all the same code path, no branching on `e` or on perihelion-date-vs-window at all.

## Stage 2 — the filter itself (needs a decision, not just code)

Given perihelion distance/date + absolute magnitude + slope parameter, you can estimate
a comet's apparent magnitude on any given date using the standard comet brightness
relation used throughout amateur/professional software (Stellarium, Guide, etc.).
**I'm not stating the exact formula here** — conventions for how the slope parameter
combines with the log terms vary slightly between sources, and CLAUDE.md's rule in this
repo is explicit about not guessing at this kind of thing. Before implementing, confirm
the exact formula against a canonical source (MPC's own docs, or JPL Horizons'
documentation of how it derives T-mag/N-mag) rather than trusting a remembered formula.

Decided by Bob:
1. **Magnitude cutoff** — start at **15.5** (imaging cutoff; single list, not split
   visual/imaging). Explicitly a starting point to iterate on: if 15.5 produces too
   many candidates (Bob's target: script 1's output list should be **< 20 comets**),
   tighten toward 14.5, etc. Should not be hardcoded — expose as a script argument.
2. **Time window** — start at **60 days from run time**, exposed as an optional
   `--days-back` / `--days-forward` argument rather than hardcoded, since the right
   window partly depends on how often Script 1 itself runs (see cadence discussion
   above — not nightly, possibly not even weekly, if a full run takes more than a few
   seconds and produces a near-identical list run to run).

## What doesn't change

- `fetch_comet_ephemerides.py`'s actual Horizons call, output JSON shape, and the two
  bug fixes from Milestone 1 (cache-busting, prune-on-partial-failure) — stage 3 is
  this same script, just driven by a generated shortlist instead of a hand-maintained
  YAML file.
- `comets.html` rendering — unaffected, it only reads `index.json`.

## Resolved: `note`/`warning` prose is not actually rendered on the live site

Investigated and settled by Bob: those fields don't appear anywhere on the SSD comet
panel as currently built — likely leftover from hand-editing against aerith.net
commentary at some point, never wired into the frontend. **Since it's not shown, it
can be ignored/removed.** No prose-preservation constraint on Script 1's design after
all — this un-does the "gap" flagged earlier in this doc.

## `comets.yaml`'s role going forward — resolved for now: no override mechanism

Considered and explicitly deferred by Bob. The only override scenario either of us
could construct is a comet with a very brief, very bright window that the sampled-epoch
filter (above) could plausibly miss between sample points. Simplest fix if it's ever
needed: an `--always-include <designation>` flag. **For now: document the possibility,
build nothing.** Assume the filter does its job; add an override mechanism only if a
real miss is observed.

## Suggested next steps

1. ~~Confirm MPC download URL~~ — done. ~~Confirm brightness formula~~ — done:
   `m = magnitude_g + 5*log10(delta) + magnitude_k*log10(r)`, confirmed against the
   BAA Comet Section's magnitude-parameters page
   (https://people.ast.cam.ac.uk/~jds/magpars.htm), an independently maintained
   source, not assumed from memory. ~~Confirm Skyfield's parsed column names~~ —
   done, by reading Skyfield's actual installed source in this session (not
   guessed): `magnitude_g`, `magnitude_k`, `perihelion_distance_au`, `eccentricity`,
   `designation`, etc. `scripts/build_comet_candidates.py` is a real, syntax-checked
   prototype implementing all of this. Still pending: Gareth on the downloading
   restrictions note; the `designation` field's exact string format needs checking
   against real output (see script docstring — MPC's spec says it's a combined
   "Designation and Name" field, this script's split logic is unverified).

   **Performance — partially measured, not just theorized:** the heliocentric-only
   half of the computation (Kepler-solving, the algorithmically expensive part) was
   timed against 860 synthetic comets × 5 sample epochs each in this sandbox:
   **14.8 seconds total, ~17ms/comet** — confirms "seconds, not minutes." The
   geocentric half (needed for the magnitude formula's Δ term) requires downloading
   JPL's `de421.bsp` ephemeris file, which this sandbox's network policy blocked
   (403 via its proxy) — unrelated to the MPC question, and not expected to be a
   real-world issue (Bob's own machine, or the GitHub Actions runner that already
   successfully calls this same JPL org's Horizons API today, should have normal
   access). `scripts/prototype_mpc_timing_test.py` will get the full end-to-end
   number once run somewhere with real network access.
2. ~~Bob picks a magnitude cutoff and a time-window rule~~ — done: mag 15.5, 60-day
   window, both as script arguments, iterate from there.
3. Prototype Script 1 as a standalone script that just prints a candidate list —
   verify it against the current hand-picked `comets.yaml` (does it agree on today's
   5 comets, roughly?) before wiring it into the pipeline. Bob's expectation: won't
   fully agree, and that's fine — the list *existing at all*, and its size relative to
   the <20 target, is the useful signal from this first pass.
4. Only then integrate into `fetch_comet_ephemerides.py` as the new input source.
   `comets.yaml` stops being hand-curated once Script 1 is trusted; no override
   mechanism planned unless a real miss is observed (see above).

## Addendum (2026-07-19, later same session): architecture pivot, MPC magnitude
## estimation dropped, COBS made primary

Everything above this line describes the original all-MPC design. It was superseded
within the same session after real (not guessed) evidence showed the Kepler +
magnitude-formula approach in `build_comet_candidates.py` produces unreliable
brightness estimates:

- 10P/Tempel: script computed magnitude 4.6. Real COBS-observed value: 8.9. Even a
  more careful historical BAA fit only got to 7.54. MPC's own `magnitude_g`/`magnitude_k`
  values for this object are rough defaults, not a real photometric fit.
- Independently confirmed via literature: a BAA forum thread on 289P/Blanpain
  documents the same ~13-magnitude-scale failure mode, describing MPC's H/G values as
  "generally based on nuclear magnitudes... often very inaccurate."

Bob's question that triggered the pivot: does COBS (Comet Observation Database) already
solve this, i.e. can Script 1 become "poll COBS, get positions from Horizons, use COBS
magnitudes" and skip independent MPC-based prediction? Confirmed live: **yes.**

- COBS has a REST API: `https://cobs.si/api/comet_list.api` (bulk, paginated at
  5000/page) and `comet.api` (single lookup). Key fields (confirmed against live
  responses): `current_mag` (real observed), `peak_mag` / `peak_mag_date` (COBS's own
  forward-looking prediction, calibrated against real observations per their docs),
  `mpc_name` (packed MPC designation, not always zero-padded — confirmed live: 10P/Encke
  came back as `"2P"`, not `"0002P"`), `is_observed`.
- Verified live that `peak_mag`/`peak_mag_date` already does the forward-projection job
  the MPC/Kepler code existed for: 2P/Encke shows `current_mag: 20.3` (currently
  undetectable) but `peak_mag: 3.6`, `peak_mag_date: 2027-02-10` — correctly flagging a
  future bright apparition well ahead of time, from real observational calibration
  rather than a raw two-body/magnitude-law guess.
- Two live API bugs found and fixed (not from docs — from actually hitting the
  endpoint): `cur-mag` must be an int in the URL (a float like `13.0` is silently
  ignored, returns zero results, no error); `is-observed` must be the literal string
  `"true"`/`"false"` — COBS's own docs show `is-observed=1` as an example, but the live
  server returns HTTP 400 for that value.

Bob's framing of the remaining role for MPC: "is there any subset of 'things we should
list' that pass the MPC filter but do not pass the COBS polling?" — yes, in principle
(a comet with zero submitted observations, e.g. brand new or in a very sparse
sky region), but expected to be small: "my expectation is that this sliver is going to
be extremely small — until, of course, it isn't." Decision: keep MPC in the pipeline,
but only as a residual watchlist — flag comets whose MPC perihelion date falls in the
window AND that have no COBS observations at all, with no invented magnitude attached,
rather than running independent Kepler/magnitude-formula prediction for the full
catalog.

**Current architecture** (implemented in `build_comet_candidates.py`, this version):
1. Pull COBS's full `is-observed=true` list in one bulk call (confirmed live:
   fits in a single page, no server-side magnitude filter applied — a tight filter
   would wrongly exclude currently-faint-but-will-brighten comets like 2P/Encke).
2. Include a comet if `current_mag <= mag_cutoff` OR (`peak_mag <= mag_cutoff` AND
   `peak_mag_date` falls in the requested window).
3. Separately check MPC's CometEls.txt, but only for comets NOT already matched via
   COBS (by packed designation, matching both zero-padded and unpadded forms since
   live COBS data doesn't consistently zero-pad). Flag as an unconfirmed watchlist
   entry (no magnitude) if MPC's perihelion date falls in the window.
4. Final list = COBS-qualified candidates + MPC-only watchlist entries.

This removes `de421.bsp`, `GM_SUN`, `tqdm`, and the Kepler-orbit-propagation machinery
from this script entirely — magnitude estimation is no longer this script's job. MPC's
`mpc.load_comets_dataframe_slow` + `Loader`-based caching of `CometEls.txt` remain, used
only for the residual watchlist check.

**Verified, not guessed:** syntax-checked (`py_compile`); unit-tested
(`parse_cobs_date`, `mpc_packed_number`, `to_float`, `fetch_cobs_list` pagination and
int/string param casting, and the current-OR-peak-in-window selection logic) against
synthetic data covering the four relevant cases (bright-now, faint-now-bright-later-
in-window, faint-now-bright-later-outside-window, faint-throughout); re-confirmed live
against the real COBS endpoint that field names (`current_mag`, `peak_mag`,
`peak_mag_date`, `mpc_name`, `fullname`) and the single-page response size are
unchanged, and that the 2P/Encke forward-prediction case still holds.

**Not yet verified:** end-to-end run of the MPC watchlist pass against live
`CometEls.txt` (sandbox network to minorplanetcenter.net has been unreliable this
session; COBS has been consistently reachable via the fetch tool but the sandboxed
shell's own `urllib` call is blocked by the sandbox's outbound proxy — confirmed via a
direct run, `Tunnel connection failed: 403 Forbidden`). Needs to run from a machine
with normal network access (Bob's own machine, per the pattern established earlier
this session, or the GitHub Actions runner). Also not yet exercised: real COBS
pagination beyond one page (live query has stayed within a single page every time it's
been checked).
