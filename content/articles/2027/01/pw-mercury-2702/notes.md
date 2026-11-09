# Planet Watch!: Finding Mercury — notes (started 2026-11-08)

Publication: 2027-01-22. Apparition: evening, greatest eastern elongation 2027-02-03 (18.3°).
Workflow step: 6 — Claude's v6 (index-pwmer-v6.md = v4 structure + Bob's v5 additions) is the
ship candidate (2026-11-08). Remaining = pre-publication checks below.
SERIES: Planet Watch + How the Sky Works (dual) — Bob MAY DROP the dual series now that the
ecliptic-angle topic is spinning off into its own HSW article (see below).
All numbers = Claude's calculation (astropy builtin ephemeris; North Adams 42.70 N, 73.11 W),
PRELIMINARY — cross-check with Stellarium or JPL Horizons before quoting.

## PRE-PUBLICATION CHECKS (before 2027-01-22)
- BepiColombo: did orbit insertion (planned Nov 21, 2026) happen? Update Closing tense.
- Stellarium/Horizons spot-check: six elongations table, Feb 7 Moon/Mercury altitude table,
  Moon Feb 7/8 positions, Sun ~1° S of equator on Sep 25.
- New Moon ~16:00 UT Feb 6 (astropy) → Moon ~31 h old at 6:00 PM EST Feb 7 (text: "about a day
  and a quarter"; Bob's software 1.2 d).
- MESSENGER credit wording (PIA11364). Alt text on rad-mercury.jpg and the 7×35 render written
  from captions — Bob to check against the images. thumbnail.jpg present?

## v6 STRUCTURE
- Intro (banner fig-mercury-horizon-track) → When and Where to Look → Observing: Naked Eye (Bob's
  phone photo rad-mercury.jpg + phone-app para), Binoculars (safety; Stellarium 7×35 render
  mer-moon-070227-2300-7x35.png; Feb 7 young-Moon challenge + altitude table, best 5:45–6:00 PM
  EST), Telescopes (fig-mercury-phases; 100× → 7″ looks ~12′, ~1/3 full Moon) → Why Some
  Elongations Are Better (eastern-elongation "backwards" para; six-row Evening/Morning table;
  season w/ fig-mercury-ecliptic-seasons + morning mirror; eccentric orbit; tilt; perihelion
  brightness) → Closing (MESSENGER image, BepiColombo).
- Bob tried telescope renditions of the phase: magnifications unreasonable — dropped.
- Feb 7 table (EST, Sun / Mercury / Moon alt): 5:30 −3.7/12.2/8.6 · 5:40 −5.5/10.5/7.0 ·
  5:50 −7.2/8.7/5.3 · 6:00 −9.0/7.0/3.7 · 6:15 −11.7/4.3/1.1; separation 3.2–3.6°.
- Six elongations: Feb 3 E 18.3°/10.9° · Mar 17 M 27.6°/4.5° · May 28 E 22.9°/12.5° ·
  Jul 15 M 20.7°/7.6° · Sep 25 E 26.3°/2.2° · Nov 4 M 18.8°/11.8° (altitude at Sun −6°).

## ECLIPTIC ANGLE — how to explain (Bob, 2026-11-08)
- Combination of the Sun's ecliptic longitude (season), observer latitude, and where the
  ecliptic sits relative to the equator. Constellation labels STAY in the figure — valid for our
  latitude (~42–43° N).
- At the horizon on Feb 3 the ecliptic is still SOUTH of the celestial equator (Sun in
  Capricornus); it climbs steeply and crosses the equator at the March equinox point in Pisces
  (~35° up). Don't say "above the equator" at the horizon.
- Shortcut (90° − φ) ± 23.4° is exact only with the Sun at an equinox.

## FUTURE: How the Sky Works — ecliptic angle article (Bob's idea, 2026-11-08)
- Standalone HSW article; possibly 12 panels (one per month) because e.g. March differs a lot
  from February. Reuse fig-mercury-ecliptic-seasons.py machinery.

## MAGNITUDES (Bob, from his software)
- Phase data: Jan 18 93% 5.2″ −1.04; Jan 25 82% 5.8″ −0.97; Feb 3 50% 7.2″ −0.44; Feb 10 18%
  8.9″ +1.02; Feb 12 10% 9.5″ +1.95. (Bob's earlier "Feb 4 0.0" conflicts; text uses these.)
- Fades through the apparition because of PHASE. Perihelion effect is a comparison BETWEEN
  apparitions — (0.448/0.309)² ≈ 2.1× sunlight vs Sept.

## THREE FACTORS — the 2027 evening elongations compared (computed)
| Elongation | Angle | Mercury–Sun dist | Ecliptic vs horizon at sunset | Merc. ecl. lat | Alt (Sun −6°) |
| Feb 3 | 18.3° | 0.309 AU (perihelion Feb 6) | ~62° | +0.6° | 10.9° |
| May 28 | 22.9° | 0.412 AU | ~51° | +1.9° | 12.5° |
| Sep 25 | 26.3° | 0.448 AU (aphelion Sep 14) | ~24° | −2.9° | 2.2° |

## FIGURES (web + print + .py)
- fig-mercury-horizon-track (banner) · fig-mercury-three-elongations ·
  fig-mercury-orbit-elongations · fig-mercury-phases (Telescopes) ·
  fig-mercury-ecliptic-seasons (Feb 3 vs Sep 25 western sky, zodiac labels, March equinox point,
  Ecliptic/Equator key).
