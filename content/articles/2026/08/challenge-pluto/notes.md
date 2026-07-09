# Smart Scope Challenge Plan: Pluto

Working notes only — not the article draft. Slug: `challenge-pluto`. Window: late August through mid-October 2026.

## Direct predecessor found: this article is already teased

`content/articles/2026/05/dwarf-planet-challenge/index.md` ("Smart Scope Challenge: Haumea and Makemake", published 2026-05-28) contains this line in its own Introduction: *"Pluto is actually an easy target for these scopes (and we'll get to it later in the summer)."* This new article is that payoff — worth an opening nod back to it, and it sets the established conventions to match:

- **Frontmatter**: `series: ["observing-challenges", "smart-scopes"]` (dual-tagged, not just one), `challenge: { skill, mode: ["imaging"], duration, target, window }`. Note `mode` used `"imaging"` in practice, not `"imaging-telescope"` as the series `_index.md` technically defines — an existing inconsistency in the codebase, not something to fix unilaterally here, just match the working precedent.
- **Structure that precedent uses**: Introduction → background section on the object class → "How to Observe" (equipment/exposure guidance) → "The Lucky Shot" (enter RA/Dec directly into the smart scope app — Seestar via custom object entry, eQuinox2 via the Move/crosshairs coordinate entry) → "The Confirmation" (repeat imaging days/weeks later, blink-compare for motion) → "Ephemeris Predictions" (a plain table of Horizons positions with a citation link, sorted by date, one table per object).
- **No finder chart was used in that article at all** — just direct coordinate entry plus the ephemeris table. Given Pluto is much brighter (mag ~14.5) than Haumea/Makemake (mag ~17.2), there's more field-star clutter at comparable brightness, so an actual visual chart may earn its keep here in a way it didn't for the fainter pair — this matches what you asked for, just worth knowing the precedent skipped it entirely.

## The hook

Pluto is "frighteningly easy" not because it's bright (it isn't — mag ~14.5) but because you don't need to identify it by looking, you need to identify it by *motion*. Take two smart-scope exposures of the same star field a night or more apart, blink-compare them, and the one dot that moved is Pluto. No resolving a disk, no distinguishing it from a field star by eye in a single frame — the technique does the work. That's the article's whole premise and probably its title angle: "the hardest-to-see, easiest-to-find object in the solar system."

## Positions — computed locally, not from Horizons

**Important technical note**: JPL Horizons (`ssd.jpl.nasa.gov/api/horizons.api`) is unreachable from this sandbox — confirmed via direct request, HTTP code 000, same network restriction that's blocked ESA/VizieR/SIMBAD all session. I could not poll it as planned.

Workaround: the repo already bundles a JPL DE421 ephemeris kernel (`scripts/assets/de421.bsp`), which includes the Pluto system barycenter as a target body. Pluto's own offset from that barycenter (due to Charon) is on the order of 2,000 km, which at ~35 AU works out to roughly 0.08 arcsec — completely negligible for finder-chart purposes. So I computed positions locally with `skyfield` against this kernel instead of Horizons. Same underlying JPL data family, no network required, and DE421 is valid through 2053 so 2026 is well within its accurate range.

Computed geocentric positions, 6:00 UTC, every 5 days:

| Date | RA (J2000) | Dec (J2000) | Distance | Approx. Mag | Solar Elong. |
|---|---|---|---|---|---|
| 2026-08-25 | 20h 26m 34.5s | −23° 36.2′ | 34.70 AU | ~14.46 | 151.3° |
| 2026-08-30 | 20h 26m 10.1s | −23° 37.6′ | 34.74 AU | ~14.46 | 146.4° |
| 2026-09-04 | 20h 25m 47.4s | −23° 38.9′ | 34.80 AU | ~14.46 | 141.5° |
| 2026-09-09 | 20h 25m 26.6s | −23° 40.1′ | 34.86 AU | ~14.47 | 136.6° |
| 2026-09-14 | 20h 25m 07.9s | −23° 41.1′ | 34.92 AU | ~14.47 | 131.7° |
| 2026-09-19 | 20h 24m 51.5s | −23° 41.9′ | 34.99 AU | ~14.48 | 126.8° |
| 2026-09-24 | 20h 24m 37.6s | −23° 42.6′ | 35.07 AU | ~14.48 | 121.9° |
| 2026-09-29 | 20h 24m 26.3s | −23° 43.1′ | 35.14 AU | ~14.49 | 116.9° |
| 2026-10-04 | 20h 24m 17.8s | −23° 43.4′ | 35.23 AU | ~14.49 | 112.0° |
| 2026-10-09 | 20h 24m 12.0s | −23° 43.5′ | 35.31 AU | ~14.50 | 107.1° |
| 2026-10-14 | 20h 24m 09.3s | −23° 43.4′ | 35.40 AU | ~14.50 | 102.1° |

Notes on this table:
- Position: RA/Dec are solid — straightforward geometric ephemeris, not sensitive to the approximations below.
- Magnitude: approximate. Computed from a standard absolute magnitude H ≈ −1.0 and the standard distance formula (heliocentric × geocentric distance), without a full phase-integral correction. Phase angle at these distances is small (~1.6°) so the correction would be minor, but treat ~14.5 as "close enough to plan an exposure," not a citable precise value. If you want a tighter number, MPC or Horizons (run from your own machine, outside this sandbox) would give a properly phase-corrected value.
- Motion: only about 2.5 arcmin of RA drift over these 5-day steps — slow, as expected this far out, but very detectable against a fixed star field over a night or two.
- Location: RA ~20h24-27m, Dec ~−23.6° to −23.7° puts Pluto right at the Sagittarius/Capricornus border — consistent with its known real-world drift out of Sagittarius in recent years.
- Solar elongation drops from 151° to 102° over the window — still well-placed for evening observing (getting closer to the Sun for imaging purposes as fall goes on but not yet a problem by mid-October).

## The finder chart problem — real blocker, needs your input

This is the part I can't finish here. The article needs a chart showing Pluto's position against a field dense enough to include mag 15-16 stars (per your note), and the site's existing `scripts/finder_charts/finder_charts.py` genuinely can't do that in this sandbox:

- Its primary star source is a VizieR NOMAD query (reaches well past mag 16), but VizieR is one of the blocked domains here (same as Horizons above).
- Its local fallback catalog (`stars.bigksy.0.1.3.mag11.parquet`) is hard-capped at magnitude 11 — nowhere near deep enough for this.

Two ways forward, your call:
1. **You run it locally.** On your own machine, with real network access, `python finder_charts.py --objects "Pluto" --fov <whatever> --mag-limit 16` should work fine via the VizieR path — the script already supports this, it's just this sandbox's network that's the problem, not the script.
2. **You supply a chart or deep catalog export** and I annotate/finish it from there.

Either way, flagging this now rather than guessing at a workaround.

## Proposed structure

1. **Introduction** — the "frighteningly easy" hook, set expectations (you will not see a disk, you will not "recognize" Pluto by eye)
2. **The Technique** — blink comparison, two nights minimum, ideally a few days apart given the slow motion above; note what separation is actually detectable given typical smart-scope plate scale
3. **Where and When** — the position table above, window through mid-October, elongation/altitude framing
4. **The Chart** — pending the blocker above
5. **What You're Actually Looking At** — brief, since this is a challenge piece not an ACL: mention it's tracked here via its Pluto-Charon barycenter for the ephemeris (small aside, not a deep dive), maybe one line on why it's this faint (35 AU, small albedo-limited body) — keep this short, the challenge is the point, not the astrophysics

## Frontmatter draft (matched to the dwarf-planet-challenge precedent)

```
series: ["observing-challenges", "smart-scopes"]
sso_planets: ["Pluto"]   # confirmed -- this is the correct key, same one dwarf-planet-challenge used for Haumea/Makemake
challenge:
  skill: "beginner"      # or "intermediate" -- Haumea/Makemake used "advanced" for a much fainter/harder pair; Pluto at mag ~14.5 is easier
  mode: ["imaging"]      # matches precedent's actual usage, not the series _index.md's "imaging-telescope"
  duration: "weeks"      # matches precedent's value style
  target: "Pluto"
  window: "Aug-Oct 2026"
```

## Open items

- Resolve the finder chart blocker (see above) — this is the main thing standing between notes and draft
- Decide skill level (beginner vs intermediate) once technique section is drafted — leaning beginner given the precedent used "advanced" for a harder pair of targets
- Decide title — matching the precedent's plain style would be "Smart Scope Challenge: Pluto"
- Decide whether to open with an explicit callback line to the May Haumea/Makemake article (recommend yes — nice continuity, and that article already promised this one)
