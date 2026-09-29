# Research: The Speed of Light (speed-of-light)

(INTERNAL -- not reader-facing. Sourcing, disputes, and verification status that
 support index-d3. The notes file carries one-line pointers here.
 Started in d3 v3; split out in v4.)

---

## Rømer

(STATUS: REWORKED in v3 around the method. Sources consulted are listed per point.
 "CONFIRMED" = checked against a source this session; still re-check the primary
 before prose. Computed values use astropy's built-in ephemeris; 1676 positions are
 outside its designed range (1900-2100), so treat 1676 distances as approximate
 (accuracy there is unknown -- VERIFY against JPL Horizons).)

(THE ONE IDEA -- say this before any geometry:
 Io is a clock that ticks every 42½ hours: each tick is Io vanishing into (or coming
 out of) Jupiter's shadow. The ticks HAPPEN evenly, at Jupiter. Nobody anywhere else
 receives them evenly, because Jupiter itself is moving: from any point in space
 the distance to Jupiter changes. For Earth it changes a lot, because Earth is moving
 too (mostly Earth's motion, plus Jupiter's). Don't use "seen from a fixed point"
 or "an observer at constant distance" -- the first is false, the second is an
 abstraction that doesn't help the reader. The clock lives at Jupiter; every
 receiver gets a distorted copy.
 Moving away, each tick's light has a little farther to travel than the last, so it
 arrives a little late -- and the lateness piles up. Moving closer, the reverse.
 Only the change in DISTANCE matters, not motion as such: at opposition Earth moves
 almost sideways relative to Jupiter, the distance barely changes, and the clock
 looks honest. That's why the curve is flat there.
 (Fine print: the tick rate is set by Io and the Sun-Jupiter shadow line, which turns
 slowly as Jupiter orbits -- why the eclipse period, 42 h 28.6 m, is a little longer
 than Io's orbit relative to the stars (~62 s longer, computed). Jupiter's orbit is
 eccentric (e ≈ 0.049, VERIFY), so the shadow line turns at a varying rate and even
 the ticks AT Jupiter drift by roughly ±6 s per orbit (computed estimate: 62 s x 2e)
 -- but over Jupiter's ~12-year orbit, so within one apparition it's effectively
 constant. That's why calibrating the clock near each opposition works. Io's
 resonance with Europa and Ganymede also perturbs its timing (part of Cassini's
 objection) -- magnitude unknown to us; VERIFY before mentioning.
 Footnote material, not main text.)
 Total lateness between two dates = (how much farther Jupiter got) ÷ (speed of light).
 KEY SENTENCE for prose: "shift = change in your distance to Jupiter ÷ c." Nothing
 else about the observer's position or motion matters. Keep the two non-light-time
 effects separate: source drift (eccentricity, resonance -- calibrated out near
 opposition) and measurement noise (clock, seeing, which moment of the fade).
 That is the whole method. Everything else is bookkeeping.
 Analogy candidates (pick one): a friend who mails a letter every Monday while you
 move farther away each week; a lighthouse flashing on schedule seen from a ship
 sailing off. The letters are always sent on time; they just arrive later and later.)

(WHY WIKIPEDIA'S VERSION IS HARD -- so we don't repeat it:
 Its diagram (after Rømer's own figure) packs Earth's orbit, Jupiter, Io's orbit and
 the shadow into one picture at wildly different scales, and it explains the effect
 PER ORBIT near quadrature (Earth moves L->K during one 42.5-h orbit). The per-orbit
 effect is real but tiny -- ~14 s at most (computed: max Earth-Jupiter range rate
 ~27.6 km/s x 42.48 h / c = 14.1 s; Shea 1998 gives "about 14 s", CONFIRMED match).
 Readers can't see 14 seconds. They CAN see ten minutes. So lead with the
 ACCUMULATED delay over months, and treat the per-orbit version as a footnote.)

(WORKED EXAMPLE, 1676 (the historical demonstration):
 - Io eclipse period: 42 h 28.6 m computed (synodic, from sidereal 1.769137786 d and
   Jupiter 4332.589 d -- VERIFY inputs vs JPL). Rømer's 1672 measurement, 42 h 28 m
   31¼ s (Wikipedia, citing Rømer's data -- CONFIRMED as reported there).
 - 1676 opposition ~10 July (computed, approximate).
 - The Nov 9, 1676 emersion, observed 5h35m45s in the evening at Paris, came ~10 min
   later than expected (Rømer 1676, trans. Rabounski 2008 -- CONFIRMED in translation).
   Per Shea 1998, the reckoning ran over 44 orbits; he models ~9.5 min expected.
 - Our check: 44 orbits before 9 Nov = ~23 Aug 1676. Earth-Jupiter distance grew
   ~1.12 AU (computed) x 8.317 light-min/AU = ~9.3 min. Agrees with Shea and with
   Rømer's 10.
 - "Wait, why?" item: 10 min / 1.12 AU ≈ 9 min per AU -- closer to the truth (8.3)
   than the published 11. Don't claim this in prose; Shea reports Rømer's baseline
   time was ~2 min off, and we don't know what distance change Rømer assumed.)

(HOW DID HE GET 11 MINUTES? -- honest version:
 - Cassini's 22 Aug 1676 announcement: "ten or eleven minutes [to cross] a distance
   equal to the half-diameter of the annual orbit" (Bobis & Lequeux 2008, CONFIRMED).
 - Rømer's Dec 1676 paper: 40 revolutions on the approaching side "sensibly shorter"
   than 40 on the receding side, "22 minutes for the entire distance HE" -- HE being
   the diameter of Earth's orbit (Rømer 1676 trans.; Shea 1998 quotes it; CONFIRMED).
   22 min / 2 AU = 11 min per AU. Modern: 8.317 min (499.005 s, computed from exact c
   and exact AU).
 - HOW he got 22 from the 40-orbit sets is NOT clear from surviving records. Shea
   argues his surviving data don't contain clean matching 40-orbit sets, and reads the
   comparison differently (difference should be ~33 min, so Rømer was ~1/3 LOW, not
   high). Most sources compare 22 with 16.6. This is a live interpretive dispute --
   present the 11-min figure as what he STATED, and the Nov 9 prediction as what he
   DEMONSTRATED. Don't reconstruct his arithmetic in prose.
 - Recommendation: our reader recreation uses modern positions and shows how the
   method yields ~8.3 min/AU; the history reports 11 honestly, with the reason for
   the gap left as "17th-century clocks and tables" (Shea: pendulum clocks good to
   10-15 s/day at best, not routinely achieved).)

(STORY BEATS, now sourced:
 - Longitude problem; Io as a sky clock (Galileo's proposal) -- still VERIFY.
 - CASSINI FIRST: "The first written account of the discovery is thus undeniably by
   Cassini" (Bobis & Lequeux 2008). Cassini announced the light-delay explanation in
   Aug 1676, then backed away (other moons didn't obviously show it) and in his 1693
   tables used empirical corrections, different for each moon -- which contradicts
   the idea (Wikipedia, citing B&L). Great irony: the man who first wrote it down
   spent the rest of his life rejecting it.
 - Who made the Nov prediction: Wikipedia says Rømer (for 16 Nov); B&L quote the
   22 Aug announcement as predicting it. No record the 16 Nov emersion was observed;
   the 9 Nov one was (B&L). RESOLVE at fact pass -- matters for "Rømer's prediction".
 - Huygens' conversion (Traité de la lumière): "16-2/3 diameters in one second"
   [Earth diameters], from 22 min and ~22,000 Earth diameters for the orbit
   (Wikipedia quoting Huygens, CONFIRMED as quoted there; check the Traité itself).
   Wikipedia notes it was an order-of-magnitude illustration. Bootstrapping beat
   survives: the speed needed the orbit's size in Earth diameters.
 - Wikipedia: Rømer's 22 min with modern orbit values implies ~226,663 km/s, 24.4%
   low. Use only if we adopt the standard reading (see dispute above).)

(TODO:
 [ ] Read Rømer 1676 in full (Rabounski translation + original Journal des Sçavans).
 [ ] Resolve who predicted the Nov emersion (Rømer vs. Cassini's Aug announcement).
 [ ] Decide how to present the 22-min dispute (Shea vs. standard reading); read
     Cohen 1940 and Kristensen 2012 (Centaurus) -- the latter unreachable this session.
 [ ] Read arXiv:2607.28512 directly.
 [ ] Verify Io and Jupiter periods (JPL/NASA fact sheets); 2027 opposition date.
 [ ] Re-run 1676 distances with JPL Horizons.
 [ ] Longitude-problem background; Rømer/Picard/Uraniborg.
 [ ] Minor trivia, footnote-only if at all: Rømer's temperature scale -> Fahrenheit.)

---

## Hugo: companion pages (decided 2026-09-28, tested on Hugo 0.160.0, mock site)

(Not needed for romer-yourself any more (it's an article), kept for future companions.
 - A leaf bundle "may not contain another bundle" (gohugo.io page-bundles). Anything
   inside an article's folder is a resource: .md and .html are not published at all;
   .txt and other non-content files are copied as-is.
 - Working pattern: SIBLING folder (<article>--<suffix>) with front matter
   url: "/articles/YYYY/MM/<slug>/<child>/" and build: {list: never}. Published at
   that URL; excluded from lists, sitemap, RSS in the mock test.
 - Rejected: article as section (_index.md) -- breaks dated URLs, drops out of
   RegularPages/RSS; rendering companion .md from the article template -- works in
   the mock, but brittle custom machinery.
 - Unchecked in the real site: theme templates, images under a url override.)
