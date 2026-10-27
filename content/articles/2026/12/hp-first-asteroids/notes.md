# The First Asteroids — Framework Notes (2026-10-25)

Series: Historical Perspectives (HP). Publication: 2026-12-21 (Mon) — swapped with
`christmas-tree-cluster` 2026-10-25 (day-of-week slots no longer apply). Bob keeps the working
copy as notes-v0.md; this file is the project summary.
Workflow step: 3 → 5. Fact pass 1 done 2026-10-25 (results at the end; they supersede the
[verify] tags in the story list). Next: index-ast-v1.md.
Overlap: the fall asteroid challenge covered Pallas and Vesta as observing targets. This piece is
about the people and circumstances; observing gets one closing paragraph + a link. The asteroid
challenge does NOT tell Olbers' broken-planet theory (Bob) — story 5 stays in full.

## Central picture
Four "planets" in six years, then nothing for 38. The search was organized and theory-driven,
and the theory was wrong — but it found two of the four. (Bob: confirmed angle.)

## Stories (as framed before fact pass 1)

0. **Titius–Bode as setup (two paragraphs, before story 1).** The rule left an empty slot at
   2.8 AU; Uranus (1781) near the predicted 19.6 AU made it a search target → Zach's search.
   Ceres at ~2.77 AU fit. Pays off in story 5 (Olbers' broken planet = the Bode planet) and
   story 11 (Neptune 1846 broke it). One clause: no physical basis established.

1. **The search party that arrived second.** Zach's "celestial police," 1800: 24 astronomers,
   the zodiac divided into zones. Harding was one of the 24. Piazzi was on the list but found
   Ceres on 1 Jan 1801 independently.

2. **Piazzi wasn't looking for a planet.** He was building a star catalogue (begun 1792 because
   Wollaston's catalogue had errors), timing meridian transits with his assistant Niccolò
   Cacciatore recording. Night 2: a "star" out of place — Piazzi blamed a recording error,
   Cacciatore blamed the observation. Night 4: it had moved again. He announced it cautiously
   as a comet in an unsigned Journal de Paris notice; Lalande learned of it from the newspaper.
   Privately he suspected "something better than a comet." His letter to Oriani was delayed by
   Napoleon's occupation. (MacTutor.) Gauss's recovery: one paragraph only.

3. **Hegel and the empty gap (short aside, or skip).**

4. **Pallas: found while looking at Ceres.** 28 March 1802, Olbers relocating Ceres. Orbit
   tilted ~35°.

5. **Olbers' broken-planet theory — wrong, and productive.** Letter to Herschel, 17 May 1802.
   Search where the orbits cross, Virgo and Cetus. Vesta, 29 March 1807, in Virgo.

6. **Juno and the atlas.** Harding, 1 Sept 1804, Lilienthal. Atlas novus coelestis.

7. **The observatory that burned.** 1813, Vandamme.

8. **Asteroids in the periodic table (sidebar — keep, Bob).** Palladium (ceresium first);
   cerium.

9. **Vesta: the one you can see.** Gauss named it, designed the symbol; orbit in 10 hours.

10. **38 years of nothing — then a postmaster.** Hencke, Astraea 8 Dec 1845, Hebe 1 Jul 1847.

11. **What to call them.** Herschel, "asteroid," 1802; reclassified in the 1850s.

## Possible spine
Titius–Bode setup (0) → search party (1) → Piazzi's accident (2; 3 as an aside) → Pallas and
the broken-planet idea (4–5) → Juno and Lilienthal (6–7) → Vesta (9) → elements sidebar (8) →
the 38-year silence and Hencke (10) → what they became (11) → go look.

## Go look (closing paragraph) — all four are up in late December
Positions (Bob, late December 2026): Ceres 7h28m +29° (Gem, V 7.1); Pallas 0h59m −20° (Cet,
V 9.3); Juno 21h32m −12° (Aqr, V 10.3); Vesta 1h07m −01° (Cet, V 7.5).
Altitudes at end of astronomical twilight, North Adams (astropy, positions held fixed — date
effect only):
| Date | Moon at dusk | Ceres | Pallas | Juno | Vesta |
|---|---|---|---|---|---|
| Dec 21 | 93%, up | 7° E | 27° S | 24° SW | 45° S |
| Dec 30 | 48%, not risen | 13° E | 27° S | 19° SW | 46° S |
| Jan 7 | new | 20° E | 27° S | 13° SW | 46° S |
- Juno: sinking into the SW at dusk; catch it early in the evening, before ~New Year.
- Pallas, Vesta: well placed in the south at dusk either way.
- Ceres: rising at dusk; a later-evening target; ~12–21° from the Moon Dec 21–30.
- Full Moon Dec 23 → publication week moonlit; rest of the four best in the first week of
  January (new Moon Jan 7).
- Smart scopes: all four easy; small telescopes: Pallas and Juno findable (Bob).
[verify with Horizons before prose: positions for the actual dates, magnitudes]

## Figures / media
- Portraits: Piazzi, Olbers, Harding, Hencke, Wollaston. Not a book chapter, so Wikimedia Commons
  is fine (Bob); check each file page's licence (PD-old).
- A page from Harding's Atlas novus coelestis (PD) — shows the "no mythology" point.
- fig-four-orbits (code): Ceres, Pallas, Juno, Vesta orbits, top-down and edge-on, showing
  Pallas' tilt and where Ceres' and Pallas' orbits cross. Makes story 5 visible. Orbits may
  exist from Gareth (meteors article) — need full elements (i, node, epoch) for the edge-on
  panel; else JPL small-body pages.
- Wollaston's handbill [verify an image source and its status].

## Cross-references
fall asteroid challenge (Pallas, Vesta), `smart-scope-gift`, parallax article (Bessel at
Lilienthal). NOTE: with the date swap, `christmas-tree-cluster` and `smart-scope-gift` publish
AFTER this article — no links to them (house rule: no forward links); they can link back here.

---

## Fact pass 1 (2026-10-25)

### Confirmed (source)
- Titius inserted two paragraphs into his 1766 German translation of Bonnet's Contemplation de
  la Nature (not in the French original). Bode published it in 1772 in his compendium, in a
  footnote, first unsourced, later crediting Titius. Precursor: David Gregory 1702. (Wikipedia,
  Titius–Bode law.) CORRECTION: it was inserted text, not a footnote, in Titius; Bode's was the
  footnote.
- Rule vs actual (AU): Ceres 2.8 vs 2.77; Uranus 19.6 vs 19.22; Neptune ~38.8 vs 30.07.
  Bode used Uranus's fit to urge a search. No accepted physical explanation; Icarus no longer
  accepts papers proposing improved versions. (Wikipedia.)
- Celestial police: founded 20 Sept 1800 at Lilienthal (Schröter's observatory); six present
  (Schröter president, Zach secretary, von Ende, Gildemeister, Olbers, Harding). Formal name
  Vereinigte Astronomische Gesellschaft. Ecliptic split into 24 zones of 15° in longitude,
  ~7–8° either side. Piazzi is on the "canonical" list of 24; Lalande invited, declined; some
  invitations late or never arrived. Zach's motive: the Bode-law planet. (Wikipedia, Celestial
  police; Wikipedia, Zach.)
- Piazzi invitation: Sky at Night says he found Ceres "before receiving his invitation";
  Wikipedia only says some invitations arrived late or never. → Prose: "had not yet heard
  from them" level is OK as commonly told; don't dramatize. Safer: "He was on their list, but
  he wasn't searching — and he got there first."
- Ceres Ferdinandea: after Ceres (patron goddess of Sicily) and King Ferdinand IV of Naples
  and Sicily; "Ferdinandea" dropped for political reasons. (Wikipedia, Piazzi; Kirkwood 1888.)
- Journal de Paris notice dated 15 Jan 1801, appeared February; no name; said "19th star of
  Mayer," a misprint for 109th. Letters 24 Jan 1801: Bode received 20 March; Oriani 5 April
  (Napoleon). To Bode "comet"; to Oriani "something better than a comet." Cacciatore's account
  told to Captain Basil Hall, 1841 (so: a story told 40 years later). (MacTutor.)
  What the misprint affected: NOT found. Drop that question; at most mention the misprint as
  one more obstacle.
- Ceres recovered by Zach 31 Dec 1801 / 1 Jan 1802 from Gauss's prediction; Olbers one night
  later. (Wikipedia, Zach.)
- Hegel: his number row (from Plato's Timaeus, altered) left no room between Mars and Jupiter,
  *if* Timaeus was right; he did not apodictically claim only seven planets (Neuser commentary,
  hegel.net). Same year as Ceres; whether he knew of it isn't established. Later he said he was
  no longer satisfied with what he'd written on the gaps. → Recommend a 2–3 sentence aside or
  cut; it's a myth-correction, and the correction is subtle.
- Olbers: physician in Bremen; observatory in the upper story of his house. Pallas 28 Mar 1802
  while relocating Ceres. Hypothesis letter to Herschel, 17 May 1802 (Wikipedia, Phaeton).
  Sky at Night attributes a letter to Gauss in 1802 — both may exist; cite Herschel.
  Pallas inclination 34.9° (infobox; body text 34.8°) → "about 35°".
- Search regions: Whewell (1858) — Olbers thought the break-up happened in Virgo or in Cetus,
  opposite constellations through which all fragment orbits must pass, and planned to survey
  both three times a year. EB1911: "near the common node." Kirkwood: two opposite regions the
  orbits must cross; Olbers gave up in 1816. Vesta in Virgo (Wikipedia, 4 Vesta).
- Juno: 1 Sept 1804, Lilienthal. Harding was preparing star charts of the small stars near the
  orbits of Ceres and Pallas; noticed an 8th-mag star not in Lalande's catalogue (Kirkwood).
  2-inch (5 cm) refractor (Astronomy.com — secondary; [verify] or omit). Orbit by Gauss and
  Burckhardt (Whewell). Albedo ~0.2–0.24, unusually reflective for an S-type; ~mag 7.5 at
  favorable oppositions, ~8.7 typical; diameter ~250 km (Wikipedia, 3 Juno).
- Harding: came 1796 as tutor to Schröter's son; observer/inspector; Atlas novus coelestis
  1808–1823, ~120,000 stars, first atlas without mythological figures; left 1805 for Göttingen;
  Bessel succeeded him (Wikipedia). Bessel as Schröter's assistant 1806–1810 (Wikipedia,
  Schröter).
- Schröter: French under Vandamme destroyed books, writings and observatory, 1813; died
  29 Aug 1816 in Lilienthal (Wikipedia). Kirkwood/RocketSTEM: the society effectively ended with
  it.
- Palladium: isolated 1802; "ceresium" first; sold as "Palladium, or New Silver" at 26 Gerrard
  Street, Soho (Mrs Forster's shop) at 5 shillings / half a guinea / a guinea; Chenevix bought
  the stock, called it a platinum–mercury alloy, published in Phil. Trans. and got the Copley
  medal; anonymous letter Dec 1803 offered £20 for making it in public; nobody did; Wollaston's
  full paper 1805. (Chemistry World, Griffith.)
- Cerium: 1803, Hisinger & Berzelius; Klaproth independently; named for Ceres (vanderkrogt).
- Vesta: Gauss named it and designed the altar-and-fire symbol; computed the orbit "in the
  remarkably short time of 10 hours"; ~mag 5.1 at best, faintly naked-eye (Wikipedia, 4 Vesta).
- Astraea: 8 Dec 1845, Hencke at Driesen, comparing star charts with the sky from his dormer
  window (Deutsche Biographie); used the Berlin Academy charts plus his own (Kirkwood). Search
  "resumed about 1831" (Kirkwood) — so "about 15 years," not "since 1830." Profession: postal
  official, retired as Postsekretär ~1845 (Deutsche Biographie) — "postmaster" is loose; use
  "retired postal official." Reward: pension from the King of Prussia (1,200 marks per
  Wikipedia; DB says "increase in his pension") → say "a royal pension." Encke named Astraea.
  Hebe 1 Jul 1847, named by Gauss at Hencke's request.
- Asteroid count: 15 by 1851 (each with its own symbol); Gould proposed circled numbers (1852)
  (Wikipedia, 4 Vesta). 38-year gap = Vesta 1807 → Astraea 1845. ✔
- "Asteroid": introduced by Herschel at the Royal Society, May 1802; Cunningham argues the word
  came from Charles Burney Jr. (S&T). Herschel's sizes: Ceres ~162 mi, Pallas ~147 mi (S&T).
  Widely rejected at first. Reclassification "in the 1850s" (Astronomy.com) — no formal date;
  keep "by the 1850s."

### Not confirmed → don't use as stated
- "Piazzi's invitation hadn't arrived" as a dramatic fact (see above).
- What the Mayer misprint affected.
- "Hencke searched since 1830" → "about 15 years."
- Juno's discoverer telescope (5 cm) — secondary only.

## Sources (fact pass 0–1)
Wikipedia: Titius–Bode law; Celestial police; Giuseppe Piazzi; Franz Xaver von Zach; Heinrich
Wilhelm Matthias Olbers; Phaeton (hypothetical planet); 2 Pallas; 3 Juno; 4 Vesta; 5 Astraea;
6 Hebe; Karl Ludwig Harding; Johann Hieronymus Schröter. MacTutor: Giuseppe Piazzi. hegel.net
(Neuser commentary). Sky & Telescope, "Why do we call them asteroids?". Sky at Night, Vesta /
celestial police. Chemistry World: Griffith, "Two men, two centuries, four metals."
vanderkrogt Elementymology (cerium). Deutsche Biographie: Hencke. Kirkwood, The Asteroids (1888,
Gutenberg 41570). Whewell, History of the Inductive Sciences (1858). EB1911 vol. 21.
