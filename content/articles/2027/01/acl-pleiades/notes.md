# A Closer Look: The Pleiades — notes

Status (2026-11-08, end of session): Bob's v7 (banner caption added; based on v6). Step 6 (Bob's
rewrite / editorial passes) next. Planned date: 2027-01-16.
Framing: naked-eye object, so "closer" = deeper, not more magnification. Weight: experience +
history carry the piece; distance dispute = the one big story; age/brown dwarfs = a paragraph that
returns to the eyepiece (keep AWV-depth physics out).
CONSISTENCY RULE: before stating anything also covered in an earlier article (esp. C07
building-the-ladder, C09 galactic-tour), check that article's notes and match it.
WORKFLOW NOTE: Bob's versions may start from an earlier Claude copy — diff against the latest
Claude version and re-apply any lost fixes (v5 had lost the v4 Hipparcos correction).

## v6 changes (2026-11-08)
- Hipparcos paragraph restored to the correlated-errors explanation (Makarov 129 pc).
- Typo: "since long before there were records."
- Occultations → "our Astronomical Events calendar" (TODO link for site v1.3) + one sentence:
  closest approaches shrink from ~1° (Jan 2027) to ~0.5° (late 2027).
- Smart Scopes: "field rotation" wording (alt-az; corners clipped in long stacks; margin/EQ/mosaic).
- Alt text for Vedder (1885), Galileo plate, four Stellarium views. [^stellarium] marker added
  in the Binoculars paragraph (definition had no reference).
- Dinosaur paragraph kept (age comparison stands) + twist (Bob): 125 Myr ago the Sun and the
  Pleiades were in different parts of the Galaxy; everything is in orbit. No distance given —
  an orbit integration (galpy, Gaia UVW) would be needed to quantify.
- CMD figure placed by Bob in How Far Away? (main-sequence fitting context).
- Remaining NOTE: stream extent on the sky — arctan(40/136) = 16.4° max from center
  (computed); optional text "a patch of sky more than 30 degrees across".

## For v7 (2026-11-08, after v7) — Gaia row CHANGED
- Table row → | 2020 | Gaia DR2 parallaxes (952 members) | 136.1 |  (no ± — see below)
- Figure re-rendered: Gaia point at 2020, 136.1 pc, no error bar.
- Source: OUR median (= weighted mean) of the Plx column of Cantat-Gaudin+ 2020 members
  (J/A+A/640/A1/nodup, Melotte_22; same paper C09 used) → 7.349 mas → 136.1 pc. Statistical
  error of the mean ±0.006 mas (~0.1 pc); a +0.029 mas DR2 zero-point correction would give
  135.5 pc → calibration dominates; "± 0.1" was overstated.
- Do NOT use Cantat-Gaudin 2020 table1 DistPc (128 pc) — that's a photometric (neural-net)
  distance, not the parallax.
- The old 136.0 ± 0.1 came from a different CDS dataset ("Likely Pleiades members with Gaia
  DR2", ML study, 1,454 members) — no longer used for the table.

## Bob's 2027 Moon–M45 conjunctions (from his calendar; geocentric closest approach)
2027-01-18 09:11 1°07′ · 02-14 16:39 1°09′ · 03-13 22:12 1°04′ · 04-10 04:02 0°54.4′ ·
07-01 07:37 0°53.1′ · 07-28 16:52 0°57.5′ · 08-24 00:10 0°55.2′ · 09-21 05:49 0°46.3′ ·
10-18 11:29 0°35.6′ · 11-14 18:56 0°29.8′ · 12-11 04:36 0°31.7′
(Times as given; time zone per Bob's calendar. Occultation visibility is location-dependent.)

## Front matter — sources
- Coordinates RA 03h47m24s, Dec +24°07′00″: Wikipedia infobox, cited to SIMBAD (Bob to spot-check).
- Magnitude 1.6, size 110′: SEDS M45 page.
- Distance ~444 ly (136 pc): Melis et al. 2014 VLBI 136.2 ± 1.2 pc; Gaia DR2 members 136.1.
- Age ~125 Myr: lithium depletion boundary (Stauffer, Schultz & Kirkpatrick 1998, 125 ± 8).
  Turnoff without overshoot 78 Myr (Mermilliod 1981; Cantat-Gaudin uses 78 — galactic-tour);
  overshoot isochrones ~100 Myr (Oliveira+ 2003). Bob's old ~70 Myr = no-overshoot turnoff era.
- Gyrochronology: discussed, left out (Bob). Pleiades is a CALIBRATOR (Rebull+ 2016 K2: slow
  sequence F5–K8, periods 2–11 d; cooler stars rapid/disorganized).
- Lithium figure: considered, left out (Bouvier+ 2018 = Li–rotation in K dwarfs, AWV depth).

## FACT PASS — verified material
### Why seven? (HYG v4.1, computed)
- Six bright: Alcyone 2.85, Atlas 3.62, Electra 3.72, Maia 3.87, Merope 4.14, Taygeta 4.30.
- 0.75-mag gap → Pleione 5.05 (variable) → HD 23753 5.44, Celaeno 5.45, 18 Tau 5.66, Asterope 5.76.
- Pleione 5.0′ from Atlas, 1.4 mag fainter (~3.6×). Aratus (3rd c. BC): only six visible.
  Galileo: seventh "scarcely ever visible."
- Norris & Norris 100,000-yr hypothesis: speculative, criticized; omitted.
### Pleione
- GCVS Gamma Cas, 4.77–5.50 V; B / Be / Be-shell phases; ~34-yr cycle (Marr+ 2022). 3.4 M☉, 184 L☉.
### Names
- IAU WGSN (21 Aug 2016): Asterope = 21 Tau only; 22 Tau = traditional Sterope II. 2.82′ apart.
- Giants (HYG): Alcyone B7III, Atlas B8III, Electra B6III, Maia B8III.
### Cultures
- Hen and chicks (Fiastyúk; Freyja's hens; Thai tale); Subaru ("coming together"; six-star
  logo); sieve (Sitechko); Matariki (mother + six daughters; NZ holiday since 24 June 2022);
  Krittika; Aboriginal + Greek pursuit by Orion. Majority image = young women (Norris 2021,
  citing Krupp 1994; not cited in the article — no citation needed).
### Telescope history
- Galileo (1610, Carlos 1880 tr.): "more than forty others invisible to the naked eye"; 36 drawn.
  Plate: pleiades-3.jpg, BnF via Wikimedia Commons, PD.
- Messier M45, 4 March 1769 (Alcyone's position); Lacaille-42 = suggestion only.
### Nebula
- Tempel 19 Oct 1859, 4-inch; Auwers quote; photography 1880s settled it.
- Barnard 1890, IC 349, 36″ from Merope. Visual: 6-inch at 25–100×, Merope outside field.
- Unrelated cloud passing at ~11 km/s (NASA 2000). Plate solve confirms NGC 1435 in Bob's images.
- Infant Pleiades (Bob's question, open): LB 1497 white dwarf member → once had more massive
  stars; whether it ever had O stars (Orion-like HII region) is UNVERIFIED — needs a source.
  Surface brightness independent of distance.
### Distance dispute — VERIFIED TABLE
| Year | Method | Distance (pc) | Source |
| 1998 | Main-sequence fitting (Pinsonneault+) | 131.9 ± 2.4 | Melis+ 2012 Table 1 |
| 1999 | Hipparcos (van Leeuwen) | 118.3 ± 3.5 | Melis+ 2012 Table 1 |
| 2000 | Allegheny ground parallaxes (Gatewood+) | 130.9 ± 7.4 | Melis+ 2012 Table 1 |
| 2004 | Interferometric orbit of Atlas (Pan+) | 135.0 ± 2.0 | Melis+ 2012 Table 1 |
| 2004 | Eclipsing binary HD 23642 (Munari+) | 132 ± 2 | A&A 418, L31 abstract |
| 2005 | HST FGS, 3 stars (Soderblom+) | 134.6 ± 3.1 | AJ 129, 1616 abstract |
| 2009 | Hipparcos new reduction (van Leeuwen) | 120.2 ± 1.9 | A&A 497, 209 |
| 2014 | VLBI (Melis+) | 136.2 ± 1.2 | Science 345, 1029 abstract |
| 2020 | Gaia DR2 parallaxes, 952 members | 136.1 | Cantat-Gaudin+ 2020 members; our median |
- Soderblom's 133.5 ± 1.2 = combined best estimate, not the HST result.
- CAUSE: leading explanation = errors correlated over stars sharing Hipparcos's ~0.9° field
  (Pinsonneault+ 1998; van Leeuwen & Evans 1998; An+ 2007); Makarov 2002: 129 ± 3 pc.
  Hipparcos team never accepted it. DON'T say "never pinned down."
### Age / brown dwarfs / dinosaurs
- LDB at 125 Myr: 0.075 ± 0.005 M☉ → fainter members are brown dwarfs.
- ICS: Cretaceous 145.0–66.0; Early/Late 100.5; Aptian base ≈125.0; Campanian 83.6–72.1.
### Members / motion
- Lodieu+ 2019: 1,248 members; stream to 40 pc. Gaia DR2 ML study: 1,454; four ejected;
  PM 49.7 mas/yr → full Moon in ~36,000 yr; RV +5.8 km/s. White dwarf LB 1497 is a member.

## Fields of view
- Cluster 110′ = 1.83°. Nikon Aculon A211 7×35 9.3° / 10×50 6.5°. S50 0.73° × 1.29° (named
  stars fit); S30 1.2° × 2.4°. Stellarium renders (measured): 7×35 9.2°, 15×80 4.3°, 80 mm f/5
  + 25 mm 3.3°, + 17 mm 2.2°.

## Occultations (computed, PRELIMINARY)
- Series 5 Sep 2023 – 7 Jul 2029; next 2042. 2026-12-21 ~3:48–5:06 PM EST twilight event from
  North Adams (confirm with IOTA/Occult before any publication).

## Still open
- Events-calendar link (site v1.3).
- Stream extent sentence (optional). Infant-Pleiades thread (orbit integration + O-star
  question) — Bob's call whether to pursue.

## MEDIA (status end of session)
- banner-m45.png (caption added in v7), thumbnail.jpg (Bob); vedder-1885.jpg (PD, Wikimedia).
- m_45-s50-21m-annotated.jpg — star key (labels verified against plate solve).
- m_45-s30-69m.webp — Smart Scopes.
- pleiades-3.jpg — Galileo plate (BnF, PD).
- fig-pleiades-distance-history — done (Gaia point updated 2026-11-08). fig-pleiades-cmd — done
  (Cantat-Gaudin 2020 nodup, 952 members + 7 bright stars from HYG via Evans+ 2018 Table A.2;
  G within 0.01, colors ~0.05 bluer). Scripts in Claude's workspace; Bob has copies.
- Stellarium views: binoc-7x35-v2.png, binoc-15x80.png, ep-80mm-25mm-16x.png, ep-80mm-17mm-23.5x.png.
- fig-pleiades-why-six — optional, not built. Finder chart — dropped.
