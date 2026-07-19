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

## Proposed shape: three-stage pipeline

```
MPC comet catalog (all known comets, orbital elements)
        │  stage 1: broad pull, no per-object network cost
        ▼
Physics-based observability filter (perihelion date/distance + magnitude estimate)
        │  stage 2: pure math over already-downloaded elements, cheap
        ▼
Shortlist (candidates that pass the filter)
        │  stage 3: existing Horizons fetch, unchanged, just fed a different input list
        ▼
static/data/comets/*.json  (same output shape as today)
```

This directly matches what Bob described: poll MPC for the full list, filter to a
small candidate set using orbital elements, then only hit Horizons (existing script,
unchanged behavior) for that shortlist.

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

## Stage 2 — the filter itself (needs a decision, not just code)

Given perihelion distance/date + absolute magnitude + slope parameter, you can estimate
a comet's apparent magnitude on any given date using the standard comet brightness
relation used throughout amateur/professional software (Stellarium, Guide, etc.).
**I'm not stating the exact formula here** — conventions for how the slope parameter
combines with the log terms vary slightly between sources, and CLAUDE.md's rule in this
repo is explicit about not guessing at this kind of thing. Before implementing, confirm
the exact formula against a canonical source (MPC's own docs, or JPL Horizons'
documentation of how it derives T-mag/N-mag) rather than trusting a remembered formula.

Two numbers Bob needs to decide, not something to invent silently:
1. **Magnitude cutoff** — estimated apparent magnitude below which a comet is "worth
   showing" (current YAML entries range mag 6–11 at peak; the currently-included but
   arguably-too-faint C/2025 R3 is at 16.7).
2. **Time window** — how far ahead/behind perihelion a comet stays in the candidate
   set (2P/Encke is already in the curated list "for advance planning" months before
   it's observable — do we want that lead time preserved automatically, and how long?).

## What doesn't change

- `fetch_comet_ephemerides.py`'s actual Horizons call, output JSON shape, and the two
  bug fixes from Milestone 1 (cache-busting, prune-on-partial-failure) — stage 3 is
  this same script, just driven by a generated shortlist instead of a hand-maintained
  YAML file.
- `comets.html` rendering — unaffected, it only reads `index.json`.

## Open question on `comets.yaml`'s role going forward

Does the curated YAML disappear entirely (fully automatic), or does it become an
override list (force-include/force-exclude specific designations on top of the
automatic filter, for judgment calls the formula can't make — e.g. "technically above
the cutoff but not actually visible in light-polluted skies")? Bob's call.

## Suggested next steps (not started)

1. Confirm the exact MPC download URL + cadence + the brightness formula convention
   against canonical sources (both flagged above) — this is the "no guessing" gate
   before any code gets written.
2. Bob picks a magnitude cutoff and a time-window rule.
3. Prototype stage 1+2 as a standalone script that just prints a candidate list —
   verify it against the current hand-picked `comets.yaml` (does it agree on today's
   5 comets, roughly?) before wiring it into the pipeline.
4. Only then integrate into `fetch_comet_ephemerides.py` as the new input source,
   with the YAML surviving as an optional override file if Bob wants that.
