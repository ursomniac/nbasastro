# What's Up: The Smart Scope Gift — Notes (started 2026-10-25; updated 2026-10-27)

Series: Smart Scopes (`smart-scopes`). Publication: 2026-12-24 (Thu).
Workflow step: 5 — v1 drafted 2026-10-27 (index-ssx-v1.md, ~2,875 words body, 35 [TK]s).
Bob has 28 gallery images; scope/integration come from filenames when galleries are built.
Skeleton: index-ssx-v0.md (Bob). [verify] = check before prose.
Date swap 2026-10-25: `first-asteroids` now 2026-12-21 (before this → can link back);
`christmas-tree-cluster` now 2026-12-27 (after this → no link).

## Decisions (Bob, 2026-10-27)
- THRUST: get people excited about their new smart scope; mostly discuss realistic
  expectations and what a little effort buys. Short descriptions only for gallery objects.
- NOT a Watch piece. DSO galleries stay as Bob chose them (capability showcase, any season).
- Front matter: Bob undecided whether to tag gallery objects; v1 tags only discussed objects
  (M101, PG 1634+706, Q0957+561); sso_* keys for Pluto/Eris etc. left for Bob.
- Supernova section: SN 2023ixf in M101 (Bob's image). NGC 7331 SN — Bob to identify.
- Bob owns: S30, two S50s, eQuinox 2. Draco on order; Dwarf Mini possible (likely not in time).
- Product-agnostic prose, EXCEPT the spec table (in v1 as "What Your Scope Actually Sees",
  an added subsection under the Introduction — Bob to confirm placement).
- Structure: Bob's skeleton (SSO / DSO / Citizen Science / Tips / Wrapup).
- Exotic objects: Bob has PG 1634+706 (no 3C 273 image).

## v1 open items (main [TK]s)
- Links: Pluto, Haumea, Makemake, M 20, C 55, M 92 pages; first-asteroids; observing
  challenges; Members' Skies. aerith.net and Rochester "Latest Supernovae" URLs.
- Facts: SN 2023ixf (Itagaki, 19 May 2023, Type II, peak ~10.8, ~21 Mly) — all unverified;
  bright-SN frequency; Haumea/Makemake mags; manufacturer QE figure; Jupiter 45″;
  planetary/video modes per model; solar filters per model; comet-stacking modes;
  coordinate entry per app; COBS; occultation timing needs; Seestar variable-star mode;
  ISS feasibility; first-four-asteroid visibility in the publication window.
- Media: banner/thumbnail, PG 1634+706 and SN 2023ixf filenames/captions, galleries, Eris
  image if any, comet/asteroid/lunar images, eclipse video.

## Stories — verified material (2026-10-27)
1. Planets disappoint — Jupiter pixel counts from the spec table (11–37 px; Draco native ~62).
2. Eris vs Pluto/Tombaugh: Pluto ~15th mag at discovery (Astronomy 2002); Lowell 13-inch,
   14×17 in plates, ~1 h exposures (Lowell); found 18 Feb 1930 on plates of Jan 21–29.
   Plate limiting mag NOT FOUND. Eris ~18.7, in Cetus (2026). 3.7 mag = ~30× (computed).
   Emulsion QE "seldom greater than 1%" (Keel). Modern sensor QE [verify manufacturer].
3. MPChecker (minorplanetcenter.org/cgi-bin/checkmp.cgi): UT date, J2000 RA/Dec, radius
   5–300′ (default 15), limiting V (default 20), obs code (default 500). VERIFIED.
4. Comets grainy — stacking modes [verify].
5. Dual-band filter vs moonlight — physics standard.
6. HD 209458 b: V 7.65, Pegasus (22h03m, +18°53′), 157 ly; transit depth 1.5%
   (0.0162 mag), duration 184 min, period 3.5247 d (Exoplanet Transit Database,
   var.astro.cz — amateur light-curve archive; use as "who wants the data"). STARE 10 cm,
   Charbonneau, transits 9 and 16 Sep 1999; Henry et al. independently.
7. Quasars:
   - PG 1634+706 (lead): Draco, ~+70°, circumpolar; ~5.3° SSE of η UMi; V 14.2–14.7;
     z = 1.337. Lookback 9.09 Gyr (Planck18) / 9.00 (WMAP9); universe 4.7 Gyr old at
     emission (computed). Astronomy "~9 Gyr" correct; S&T's 11.5 Gyr / 21 Gly WRONG — don't use.
   - 3C 273 (context only): V 12.9, z 0.158; "2.4 Gly" = luminosity distance; lookback
     ~2.0 Gyr (computed).
   - Twin Quasar Q0957+561: A 16.7, B 16.5; 6″; z 1.41; lens z 0.355; delay 417 ± 3 d;
     1979; UMa. Separation S30 Pro 1.6 px, S50 Pro 2.6, Draco 4.1, eQuinox 2 4.5,
     Origin 4.9. AAVSO A/B monitoring request.
8. Save raw stacks — 16-bit file-size fact.
SAFETY: solar filter before pointing near the Sun [verify per model].

## Citizen science approach
"Doors I haven't walked through yet" — what it is / can a smart scope do it / who wants the
data / one link. Occultations: OccultWatcher Cloud (cloud.occultwatcher.net); predictions
from asteroidoccultation.com (Preston; Herald's Occult).

## Spec table (settled 2026-10-27)
Plate scale = 206.265 × pixel (µm) / focal length (mm). Jupiter at 45″ [verify].
| Scope | Ap mm | FL mm | Sensor | Pixel µm | Output px | ″/px | FOV | Jupiter px |
|---|---|---|---|---|---|---|---|---|
| Seestar S30 Pro | 30 | 160 | Sony IMX585 | 2.9 | 3840×2160 | 3.74 | 4.0°×2.2° | 12 |
| Seestar S50 Pro | 50 | 260 | OmniVision OS08B10 | 2.9 | 3840×2160 | 2.30 | 2.45°×1.38° | 20 |
| Dwarf Mini | 30 | 150 | Sony IMX662 | 2.9 | 1920×1080 | 3.99 | 2.13°×1.20° | 11 |
| Dwarf Draco (2×2 bin) | 90 | 340 | OmniVision OV50Q40 | 2.394 (1.197) | 4096×3072 | 1.45 (0.73) | 1.65°×1.24° | 31 (62) |
| Unistellar eQuinox 2 | 114 | 450 | Sony IMX347 | 2.9 [verify] | raw 2088×1536; stack 2048×1536 | 1.33 | 45.4′×34.0′ landscape | ~34 |
| Celestron Origin Mk II | 152 | 335 | Sony IMX678 | 2.0 | 3856×2180 | 1.23 | 1.32°×0.75° | 37 |
| Vaonis Vespera 3 | 50 | 245 | Sony IMX585 | 2.9 | 3840×2160 | 2.44 | 2.60°×1.46° | 18 |
| Vaonis Vespera Pro 2 | 50 | 245 | Sony IMX676 | 2.0 | 3536×3536 | 1.68 | 1.65°×1.65° | 27 |
- Draco's 1.87°×1.05° = pre-launch IMX585 guess (dwarfastro.com) — superseded.
- eQuinox 2 from Bob's files; raw FITS 6.4 MB = 2088×1536×2 bytes. Unistellar's 6.2 MP and
  47′×34′ don't match the files — not used.
- Bob's images: original S30 (150 mm, 3.99″/px) and S50 (250 mm, 2.39″/px).
- Replace retailer/review sources with manufacturer pages (done: Vespera Pro 2).
- Vaonis Atlas (Oct 2026): not in table.

## Resource box
Comets: aerith.net (Yoshida) [verify URL], COBS. Ephemerides: JPL Horizons. Asteroid ID:
MPChecker ✓. Variable stars: AAVSO ✓. Supernovae: Rochester "Latest Supernovae" [verify URL].
Occultations: OccultWatcher Cloud ✓, asteroidoccultation.com ✓. Exoplanets: ETD
(var.astro.cz) ✓. Twin Quasar: AAVSO forum request ✓. Club: NBAS meetings / Members' Skies.

## Figures / media (candidates)
- 28 gallery images (Bob).
- Optional: field-of-view footprints of the table's scopes over one real target (astropy).
- SN 2023ixf before/after if a "before" exists.

## Cross-references
Back-links: `first-asteroids` (Dec 21), Pluto/Haumea/Makemake pages, NGC 253 ACL (Hα
experiment), smart-scope challenge articles. Later (no links): `christmas-tree-cluster`
(Dec 27), `jupiter-returns` (Jan 10), `mars-returns` (Feb 7), `winter-variable-stars`.
