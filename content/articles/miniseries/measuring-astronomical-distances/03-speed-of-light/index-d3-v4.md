---
title: "The Speed of Light"
date: 2026-11-08
description: ""
byline: ""
authors: ["bob-donahue"]
series: ["historical-perspectives"]
thumbnail: "thumbnail.jpg"
banner: "banner.png"
miniseries: "measuring-astronomical-distances"
miniseries-sequence: 3
---

(WORKING NOTES -- d3 v5. RESTRUCTURED 2026-09-28 from chronology to argument.
 Conventions as in d2: NOTES / TODO / FIGURE / IMAGE / TABLE / EXERCISE / ROLE blocks.
 EVERY historical number, date, and name below is RECALLED, NOT VERIFIED unless
 marked CONFIRMED. Sourcing lives in research-d3; the DIY version in companion-romer.
 Material from v4 is carried over verbatim; new framing blocks are marked NEW.)

(SPINE -- NEW -- test every section against it:
 "This is not the history of the speed of light. It's how astronomical distances rely
 on the speed of light, and how the speed of light came to calibrate them.
 Nobody measures c directly at first: every experiment times light over some distance,
 in whatever unit that distance comes in. Step by step the other unknowns drop away,
 until we ARE measuring c -- then measuring it better -- then using it as the ruler.")

(METHOD NOTE -- NEW: same moves as the rest of the series: shift the perspective, turn
 the question inside out, lean on metaphor. Each method gets one paragraph on what it
 MEASURED and one on what else it NEEDED. One new idea per step. Deep detail goes to
 the companion (Rømer) or the next article (the AU).)

(FRONT MATTER FLAGS:
 [ ] banner: "banner.png" in front matter vs. banner.webp in the shortcode -- pick one.
 [ ] thumbnail .jpg vs. the sample article's .webp convention -- intentional?)

## Introduction

{{< nbas-image src="banner.webp" fullwidth="true"
caption=""
alt="" >}}

{{< nbas-image src="earth-moon-c.gif" fullwidth="true"
caption="Animation with the moving dot taking exactly the time between the Earth and Moon, James O'Donoghue, CC BY 3.0, via Wikimedia Commons" >}}

A ruler is only as good as its calibration.   So far, we've looked at 
[distances in the solar system](/articles/2026/10/distance-at-solar-system-scale/) 
using light time as a unit:  the Sun and the Moon are 8.3 light-minutes, 
and 1.28 light-seconds from Earth on average, respectively; Voyager 1 is nearly one light *day* from us.    
But of course that conversion requires knowing the fundamental quantity:  the speed of light.

{{< clear >}}
---

## The Number

The speed of light, _c_ (as in the famous equation _E = m c<sup>2</sup>_) is
exactly 299,792,458 meters per second -- hardcoded since 1983.  We typically
round that out to 300,000 km/s or 186,000 miles per second: you can use any
velocity units of distane of time -- 1.2 trillion furlongs per fortnight, 
~1 foot/nanosecond, or going back to Earth-sized measurements, just under 7.5 trips
around the Earth per second.

But *exact* is a strong word -- aren't measured scientific numbers always being
refined?  Yes, but the twist here is that we've also defined the meter "exactly"
too -- this becomes clear further down.

---

## Too Fast to Catch

At first, it wasn't even clear that there was a speed of light. Was light something that travels, or just something that happens? The ancient Greeks argued about it, and tangled up in that argument was another question: does seeing work by something going out from our eyes to the object, or by something coming in from the object to us?

Empedocles (c. 494 – c. 434 BCE) had it both ways: our eyes shine out like lanterns to meet what we look at, and light takes time to get from one place to another. Aristotle would have none of it. Light, he argued, doesn't move at all; it's a state of the transparent air, present everywhere at once. Over a short distance, he allowed, light's travel might go unnoticed, but from one end of the sky to the other? That strained belief.

Heron of Alexandria offered a proof. Open your eyes at night, and the stars are there at once. If sight travels out from the eye to the stars, it must get there instantly, so its speed must be infinite.  Of course, if light is coming _in_, then it's already
been traveling to us, so seeing the stars should be instantaneous.


(NOTES -- NEW framing: the question, before any measurement. And the first lesson in
 miniature: every early attempt failed because the DISTANCE was too small for the
 clock. To see light take time you need a big distance -- which means astronomy.)

### Light as Something That Simply Is

(NOTES: The older default: light doesn't travel, it's a state that appears everywhere
 at once. Aristotle as the headline. Worth noting there were dissenters early:
 Empedocles (finite, per later sources); Ibn al-Haytham (Alhazen) argued for a finite
 speed and that it is slower in denser media -- which Foucault confirms ~800 years
 later (nice rhyme, if it holds). Kepler: infinite.
 Keep it to a paragraph or two -- the point is that "instant" was a reasonable
 conclusion from everyday experience, not stupidity.)

(PINNED -- POSSIBLE REPLACEMENT for this subsection; not yet agreed:
 "You can't time something until you know which way it's going."
 Organize the ancient material around the VISION debate, not a roll call of names
 (a roll call just retells Wikipedia's history section).
 - Extramission (eye sends out rays/"fire": Empedocles in some form, Euclid, Ptolemy)
   vs. intromission (something travels from object to eye). If seeing is the eye
   reaching out, "how fast is light?" = "how fast is seeing?" -> points to "instant."
 - The stars argument (attributed to Heron of Alexandria -- UNCERTAIN, may be someone
   else): open your eyes at night and the stars appear at once, so the eye's rays
   must reach them instantly. Fails because it assumes rays go OUT; if light comes
   IN, it was already arriving. EXERCISE candidate: readers can try it on a clear night.
 - Empedocles: "light moves, we just don't notice." Aristotle answers him directly:
   light is a state of the transparent medium, not a thing that moves, so "speed"
   doesn't apply. A real exchange, not two opinions.
 - Ibn al-Haytham as the turning point: vision is light ENTERING the eye, which makes a
   finite speed a sensible question; also slower in denser media (-> Foucault).
 - Length: two or three paragraphs. Descartes and Galileo then follow as the first to
   treat it as testable.
 TODO:
 [ ] Verify every attribution above. Empedocles survives mostly via Aristotle's
     criticism (De Anima / De Sensu?) -- source from a scholarly secondary, not
     Wikipedia.
 [ ] Confirm who made the stars argument (Heron? Ptolemy? Hero's Catoptrica?).
 [ ] Confirm Ibn al-Haytham's finite-speed and denser-media claims (Book of Optics).)

### Descartes Bets on a Lunar Eclipse

(CANDIDATE STORY -- recalled, verify:
 Descartes staked a lot on infinite speed (reportedly said that if light took time,
 his whole philosophy would be overturned). His argument: during a lunar eclipse,
 if light took time to travel Earth-Moon-Earth, we'd see the Moon's eclipse offset
 from where the Sun-Earth-Moon alignment says it should be. No offset observed ->
 light is instant.
 The lovely part: his LOGIC was fine. It only ruled out slow speeds. The effect at
 the true c is ~2.5 s of delay -- invisible to 17th-century timing. A good lesson
 in "absence of evidence at the precision you have.")

(EXERCISE candidate: how fast would light have to be for Descartes to have seen the
 effect, given naked-eye timing good to, say, a few minutes?)

(TODO:
 [ ] Verify the Descartes lunar-eclipse argument and the "philosophy overturned"
     statement (letter to Beeckman, 1634?) from a reliable history source.
 [ ] Verify Ibn al-Haytham's position; verify Empedocles attribution.)

### Galileo's Lanterns

(NOTES: Two New Sciences (1638): two observers with shuttered lanterns on distant
 hills; A uncovers, B uncovers on seeing it, A times the return. Galileo reported
 he tried it at under a mile and saw no delay -- "if not instantaneous, extraordinarily
 rapid." (Paraphrase only; don't quote from memory.)
 The Accademia del Cimento reportedly repeated it later at longer range, also null.
 The real lesson: the experiment was measuring human reaction time, not light.)

(EXERCISE -- strong candidate, "Galileo's Hills":
 Human reaction time ~0.2 s. Light's round trip over 1.6 km: ~11 microseconds.
 How far apart would the hills need to be for light's round trip to equal just ONE
 reaction time? Answer ~30,000 km each way -- more than twice Earth's diameter.
 Takeaway: Galileo's idea wasn't wrong; the planet wasn't big enough.)

(TODO:
 [ ] Verify Galileo's reported distance and the Accademia del Cimento repeat (date,
     distance).
 [ ] Compute the exercise numbers exactly at drafting.)

(IMAGE: Galileo portrait (Sustermans, PD, Wikimedia) -- or skip; he's over-illustrated.
 Better: a period woodcut/illustration of the lantern experiment IF a genuine one
 exists. Don't use modern stock "recreations".)

---

## What You Can Actually Measure

(NOTES -- NEW, short, plain; sets up everything after it:
 - You can't measure a speed; you measure a time over a distance.
 - So c always arrives tied to the unit the distance was in. If the distance is
   "the size of Earth's orbit," you get c in AU per minute -- real, but only as good
   in km as your AU.
 - The story from here: what each method MEASURED, what else it NEEDED, and how the
   "needed" column empties out.)

(TABLE -- NEW -- the spine of the article, full-width Markdown:
 | Year | Who | What they actually measured | What else they needed | Result |
 Rows: Rømer, Bradley, Fizeau, Foucault, (Weber-Kohlrausch/Maxwell), Michelson,
 Essen/Froome, Evenson, 1983. Values from the fact pass only.
 Could appear once here, filling in as the reader goes, or once at the end as the
 recap. Decide at prose.)

(CANDIDATE ORGANIZING IDEA -- "move the bottleneck" (2026-09-28):
 Accuracy does NOT improve steadily before ~1860 (Bradley 1729 at ~+0.4% beats
 Fizeau 1849 at ~+5%, per Wikipedia's table -- unverified). The real progression is
 in WHAT LIMITS each measurement:
   human reaction time (Galileo) -> the size of the AU (Rømer, Bradley: they measure
   c in AU per time) -> mechanical timing over a known baseline (Fizeau, Foucault,
   Michelson: km/s directly, no AU needed) -> frequency and length standards
   (Evenson 1972: limited by the meter itself) -> 1983 definition.
 Stated uncertainties only exist from Foucault (1862) on; after 1907 they shrink
 steadily (±30 km/s -> ±4 -> ±3 -> ±0.1 -> ±0.0011). Electrical methods (Siemens
 1875, Hertz 1893) were far off before becoming competitive (Rosa & Dorsey 1907,
 Essen 1950).
 TODO: verify the table against a real history (Froome & Essen, "The Velocity of
 Light and Radio Waves", 1969?); find what AU the Bradley row assumes; Rømer row
 says 1675 -- should be 1676.
 FIGURE: fig-c-measurement-history -- OPTIONAL; author finds it too bespoke. The
 TABLE carries this idea instead.)

---

## c in the Solar System's Own Units

(NOTES -- NEW: two real, solid results that settle "finite" -- both scaled by an AU
 nobody knew well in km. Huygens' ~220,000 km/s is a good measurement times a bad
 ruler. The finite-vs-infinite dispute (Cassini vs. Rømer) lives here and ends with
 Bradley.)

### Rømer: A Clock Orbiting Jupiter

(ROLE -- MEASURED: light-time per AU (minutes of delay per AU of extra distance).
        NEEDED: the AU in km, to get km/s. Huygens used the 1672 value -> ~220,000 km/s (verify).)

(Sourcing, the 22-minute dispute, and verification status: research-d3, "Rømer".
 The do-it-yourself version: companion-romer.)

(THE ONE IDEA -- say this before any geometry:
 Io is a clock that ticks every 42½ hours: each tick is Io vanishing into (or coming
 out of) Jupiter's shadow. The ticks HAPPEN evenly, at Jupiter; every receiver gets
 a distorted copy, because the distance to Jupiter keeps changing. Moving away, each
 tick's light has farther to travel than the last, so the lateness piles up.
 KEY SENTENCE: "shift = change in your distance to Jupiter ÷ c." Nothing else about
 the observer matters. At opposition Earth moves nearly sideways, the distance barely
 changes, and the clock looks honest -- the flat bottom of the curve.
 Analogy candidates: a friend who mails a letter every Monday while you keep moving
 away; a lighthouse flashing on schedule seen from a ship sailing off.
 Lead with the months-long pile-up (minutes), not the per-orbit effect (~14 s);
 the per-orbit version is why Wikipedia's account is hard to follow.)

(READER STEPS:
 1. Near opposition, time the clock.  2. Predict ahead by adding whole periods.
 3. Months later, an eclipse arrives late.  4. Lateness ÷ extra distance (in AU) =
 light-time per AU. No km needed until you want km/s -- the bootstrapping beat.)

(STORY BEATS (details in research-d3):
 - Why anyone was timing Io: the longitude problem; Io as a sky clock.
 - Cassini wrote it down first (Aug 1676) and then spent decades rejecting it.
 - The 9 Nov 1676 emersion: ~10 min late, as predicted. Our check: ~1.12 AU farther
   since ~23 Aug -> ~9.3 min. This is what Rømer DEMONSTRATED.
 - 11 minutes per AU (22 for the orbit's diameter) is what he STATED; how he got it
   is unclear -- don't rebuild his arithmetic in prose.
 - Huygens turns it into a speed using the orbit's size in Earth diameters.)

(EXERCISE pointer: short paragraph + link to companion-romer ("Jupiter reaches
 opposition in February 2027; here's how to catch Io running late").)

(FIGURE: fig-romer-ticks (TikZ) -- a "sent" row of evenly spaced ticks, a "received"
 row stretched as the distance grows, with the accumulated lag labeled. No orbits.
 fig-romer-delay-curve -- shared with the companion.)
(IMAGE: Rømer's own figure from the 1676 paper (PD scan), shown as the historical
 artifact, captioned toward our clearer version.)

### Bradley: The Star That Moved the Wrong Way

(ROLE -- MEASURED: the ratio (Earth's orbital speed) / c, as a ~20" tilt.
        NEEDED: Earth's orbital speed in km/s = 2 pi AU per year -> the AU again.)

(NOTES -- a better story than "second method":
 - Bradley (with Molyneux, 1725) was NOT looking for the speed of light. He was hunting
   STELLAR PARALLAX in Gamma Draconis (chosen because it passes near the zenith at
   London, minimizing refraction) to prove Earth orbits the Sun.
 - He found a shift of ~20 arcsec -- but with the wrong timing: maximum when parallax
   should be zero, a quarter-year out of phase. Not parallax.
 - Explanation: aberration. Earth's orbital velocity tilts the apparent direction of
   incoming starlight. The rain-and-umbrella picture. (Famous anecdote: insight from
   a wind vane on a boat on the Thames changing direction with the boat's heading --
   flag as possibly embellished.)
 - Published 1729. Two results in one: light is finite (settling the dispute), AND
   the first direct evidence that Earth moves around the Sun.
 - The parallax he was actually looking for took until 1838 (Bessel, 61 Cygni) --
   ~100x smaller. Forward hook to parallax.
 - Aberration gives the RATIO v_Earth / c ≈ 1/10,000. Getting c in km/s again needs
   the AU -- bootstrapping, part 2.)

(EXERCISE -- strong candidate, "The Umbrella":
 Walking through vertical rain, tilt the umbrella forward. Tilt angle ≈ your speed /
 rain speed. Earth: ~30 km/s through "rain" falling at 300,000 km/s ->
 ratio 1/10,000 rad -> ~20.6 arcsec. Readers can do this with a calculator and get
 Bradley's number. Then: 20 arcsec is ~1/90 of the Moon's diameter -- tiny, but
 Bradley's zenith sector could see it.)

(FIGURE: fig-aberration-umbrella -- two panels: (a) person walking in vertical rain,
 apparent rain slant; (b) Earth moving in orbit, starlight tilt. TikZ or matplotlib.)
(FIGURE: fig-aberration-vs-parallax -- the "wrong timing" plot: expected parallax
 displacement vs. observed aberration displacement over a year, 90° out of phase.
 matplotlib. This is THE figure for "the star moved the wrong way.")
(IMAGE: Bradley portrait (PD); Bradley's zenith sector (PD engraving? check
 Royal Museums Greenwich licensing).)

(TODO:
 [ ] Verify: Gamma Draconis, Molyneux/Kew, 1725 start, 1729 publication.
 [ ] Verify Bradley's value (light-time Sun-Earth ~8m 12s? or 8m 13s?).
 [ ] Modern aberration constant (~20.5 arcsec) from IAU/USNO.
 [ ] Thames boat anecdote: source it or label as traditional.)

---

## Cutting the AU Out

(NOTES -- NEW: bring the distance down to Earth, where you can survey it. Now c is
 measured, not scaled. The catch: a short distance needs a very fast clock -- the
 answer to Galileo's problem is a machine, not a better human.
 Bootstrap tease: with c known in km/s, the dependency can run BACKWARDS -- c fixes
 the AU. How that played out is the next article.)

### Fizeau: A Toothed Wheel Between Two Hills of Paris

(ROLE -- MEASURED: round-trip time over a surveyed baseline on the ground.
        NEEDED: only the baseline length. FIRST km/s with no AU in it.)

(NOTES -- first Earth-bound measurement (1849):
 - Light passes through a gap in a spinning toothed wheel, travels ~8.6 km to a mirror
   (Suresnes to Montmartre), returns. Spin the wheel fast enough and the returning
   light hits the next TOOTH instead of the gap -- the light goes dark.
 - Recalled: 720 teeth, ~12.6 rev/s, result ~313,000 km/s.
 - The trick in one sentence: the wheel is a stopwatch that ticks in microseconds.
 - Nice callback: this is Galileo's lanterns with the human replaced by a machine.
   Same geometry, a clock ~10,000x faster than a reaction.)

(EXERCISE candidate: "Run Fizeau's numbers" -- given teeth, distance, and rotation
 rate, compute c. Short, satisfying, and shows how a gear can time light.)

(FIGURE: fig-fizeau-wheel -- schematic of the apparatus: source, half-silvered mirror,
 wheel, long path, distant mirror; inset: gap vs. tooth. TikZ is the natural tool.)
(IMAGE: 19th-c. engraving of Fizeau's apparatus (PD, Wikimedia); Fizeau portrait.)

(TODO:
 [ ] Verify all Fizeau numbers (distance, teeth, rotation rate, result, year).)

### Foucault: Spinning Mirrors, and Light in Water

(ROLE -- MEASURED: round-trip time over a short lab path (rotating mirror).
        NEEDED: only the path length. Result can now be turned AROUND to fix the AU -- tease only.)

(NOTES -- two stories:
 1. Precision: a rotating mirror instead of a wheel. Light bounces off a spinning mirror
    to a fixed mirror and back; in the round-trip time the mirror has turned slightly,
    so the returned beam is displaced. Measure the displacement -> time. Short path
    (tens of meters, fits in a lab). Recalled: 1862, ~298,000 km/s -- within ~0.5%.
 2. The crucial experiment (1850): Newton's particle theory predicted light moves
    FASTER in water; the wave theory predicted SLOWER. Arago proposed the test;
    Fizeau and Foucault raced; Foucault published first (verify). Slower. A clean
    verdict between two rival theories of what light is.
    (Rhyme with Ibn al-Haytham, if verified.)

 CANDIDATE BEAT -- bootstrapping, part 3 (UNVERIFIED): Foucault's lab value for c,
 combined with Bradley's aberration constant, was used to REVISE the solar parallax
 (i.e., the AU) -- recalled ~8.86 arcsec. If true, the dependency ran backward: a
 tabletop measurement corrected the size of the solar system. This is the pivot of
 the whole c/AU story and should be verified carefully.)

(FIGURE: fig-foucault-mirror -- schematic, rotating mirror + fixed mirror + displaced
 return. TikZ. Could share a style with fig-fizeau-wheel as a matched pair.)
(IMAGE: Foucault portrait (PD); apparatus engraving (PD). Link to the site's pendulum
 content if any exists -- Foucault is better known for that.)

(TODO:
 [ ] Verify 1850 water/air experiment details and priority; Arago's role.
 [ ] Verify 1862 value and path length.
 [ ] Verify Foucault -> solar parallax revision and the value.)

---

## A Different Road: Electricity

(NOTES -- NEW: a parallel track that never looks at light and gets the same number.
 Explains the electrical rows in the table (Weber-Kohlrausch; Siemens, Hertz far off;
 Rosa & Dorsey, Essen later competitive). Keep short.)

### Maxwell: The Speed Nobody Measured

(ROLE -- MEASURED: a ratio of electrical units that comes out as a speed.
        NEEDED: no light at all -- electrical standards. A parallel road to the same number.)

(NEW STORY -- not in the original notes; "wait, why is that true?":
 - Weber and Kohlrausch (1856) measured the ratio between electrostatic and
   electromagnetic units of charge -- a pure electricity experiment with capacitors
   and galvanometers. The ratio came out with units of velocity, ~3.1 x 10^8 m/s
   (verify).
 - Maxwell (1860s) noticed it matched the measured speed of light and concluded light
   IS an electromagnetic wave. c was predicted by people who never looked at light.
 - Why this belongs here: it changes c from "the speed of a thing" to a property of
   space itself -- which is exactly what sets up "The Same for Everyone" and the 1983
   definition. It also answers the reader's unspoken "why THIS number?" as far as
   physics can: it falls out of electricity and magnetism.
 - Keep it light on math. The equation is optional; if used, only
   c = 1/sqrt(mu0 eps0), with a plain-language gloss.)

(TODO:
 [ ] Verify Weber-Kohlrausch date and value; Maxwell's 1862/1865 papers and his
     stated comparison.
 [ ] Decide: include, footnote, or park for an AF piece. (Recommend include, short.))

---

## Beating Down the Error

(NOTES -- NEW: the "needed" column is now empty; from here it IS "here's my value of
 c, beat down my error." The error bars shrink every time (±30 km/s in 1907 ->
 ±0.0011 in 1972, per Wikipedia's table -- verify) until the limit is the meter.)

### Michelson: A Mile of Empty Pipe

(ROLE -- MEASURED: c directly, over ever-better baselines, then in vacuum.
        NEEDED: nothing else -- from here it is "beat down the error" (air correction -> the pipe).)

(NOTES:
 - Michelson refined Foucault's rotating-mirror method over ~50 years (first ~1879 as
   a young naval officer, verify).
 - 1920s: Mount Wilson to Mount San Antonio (~35 km), with a rotating octagonal mirror;
   the baseline was surveyed to high precision (by the Coast and Geodetic Survey?).
 - Last experiment: a ~1-mile evacuated pipe (Irvine Ranch, Santa Ana) to remove air;
   he died in 1931 before it finished; colleagues completed it. (verify)
 - First American Nobel in the sciences, 1907. (verify)
 - Aside, not a speed measurement but central to section 4: Michelson-Morley (1887) --
   the null result that light's speed doesn't depend on Earth's motion. One or two
   sentences here; payoff in "The Same for Everyone.")

(IMAGE: Michelson portrait (PD); photo of the evacuated-pipe apparatus or the Mount
 Wilson setup (check source/licensing -- Caltech archives? AIP?).)

(TODO:
 [ ] Verify all Michelson dates, distances, results, Nobel year.)

### Measured Better Than the Meter: 1983

(ROLE -- MEASURED: frequency x wavelength of a laser line.
        NEEDED: the meter itself, which became the limit -> so the meter was redefined by c.)

(NOTES -- the inversion, the payoff of the whole history:
 - Post-WWII: microwave cavities, radar, then lasers (frequency x wavelength).
 - Recalled: 1972 NBS measurement (Evenson et al.) using a laser, with most of its
   remaining uncertainty coming from the definition of the METER itself (the krypton-86
   line). c was now known better than the ruler used to measure it.
 - 1983: the CGPM fixes c at exactly 299,792,458 m/s and defines the meter as the
   distance light travels in 1/299,792,458 s. We stopped measuring c; we measure
   length with it.
 - Say plainly what that means for the reader: "the speed of light is exact" is not
   a claim about nature being tidy -- it's a choice of units. Any improvement in
   measurement now changes our knowledge of the meter, not of c.
 - Parallel ending with measuring-the-au (AU fixed by definition in 2012) -- tease only.)

(EXERCISE -- strong candidate, "The Light-Foot" / Grace Hopper's nanoseconds:
 Grace Hopper famously handed out ~11.8-inch wires: the distance light travels in a
 nanosecond, to explain why computers can't be arbitrarily large and fast.
 Reader exercise: a 5 GHz processor -- how far does light get in one clock tick?
 (~6 cm.) GPS: 1 ns of clock error ≈ 30 cm of position error.
 Everyday proof that c constrains the device in your pocket.)

(IMAGE: Hopper holding a "nanosecond" -- check licensing (may be US Navy PD, or not).)

(TODO:
 [ ] Verify 1972 NBS value, uncertainty, and the krypton-limited claim.
 [ ] Verify 1983 CGPM resolution wording (BIPM).
 [ ] Verify Hopper wire length and story source.)

---

## What Else Changes the Travel Time

(NOTES -- NEW framing for the old "How c Behaves": travel time is not just
 distance / c. Every light-time distance -- including the radar ranging in the next
 article -- has to correct for these. That's the bridge forward.
 - Air: why Michelson built the vacuum pipe.
 - Gravity: radar echoes from Mercury and Venus at superior conjunction, grazing the
   Sun, come back late (Shapiro delay -- verify).
 Still may want to become its own AF companion; measure length after drafting.)

### Slower in Stuff

(NOTES:
 - c is the vacuum speed. In a medium, v = c/n.
 - Numbers readers can hold: air (~99.97% c), water (~75%), glass (~65-67%),
   diamond (~41%). Pull indices at drafting.
 - Modern hook: optical fiber carries the internet at ~2/3 c (~5 microseconds per km).
   Trading firms reportedly built microwave tower links because signals through AIR
   beat signals through GLASS. (Verify; widely reported, get one solid source.)
 - Cherenkov radiation: particles can exceed light's speed IN WATER (never in vacuum),
   producing the blue glow in reactor pools -- a "sonic boom" of light. Good image;
   also a neat clarification of what "nothing is faster than light" actually means.
 - Optional extreme: "slow light" experiments (Hau et al., 1999, ~17 m/s in a
   Bose-Einstein condensate). One sentence at most, if verified.
 - Keep the "why does light slow in glass?" explanation honest and brief -- the
   popular "photons bounce between atoms" story is misleading; the absorb-and-reemit
   story is also not right as usually told. Either say it carefully or say it's
   subtle and move on. Flag for fact pass.)

(TABLE candidate -- thin, right-aligned article-table:
 | Medium | n | Speed (% of c) |  -- air, water, glass, diamond, fiber.)
(IMAGE: Cherenkov glow in a reactor pool -- Idaho National Laboratory ATR photo
 (US gov, check license) or similar PD.)

(TODO:
 [ ] Refractive indices from a reference (specify wavelength, e.g. ~589 nm).
 [ ] Fiber group index / latency figure.
 [ ] Microwave vs. fiber trading links: one solid source.
 [ ] Cherenkov: verify phrasing.)

### The Same for Everyone

(NOTES -- short bridge; possibly merge into the gravity subsection:
 - Michelson-Morley null result; Einstein 1905 makes it a postulate: every observer
   measures the same c regardless of their own motion.
 - Callback: Maxwell's c belongs to space, not to the source.
 - DO NOT drift into a special-relativity tutorial. One paragraph: this is why c can
   serve as the definition of the meter -- it's the one speed everyone agrees on.
 - Astronomical evidence line (optional sidebar): GW170817 -- gravitational waves and
   gamma rays from a neutron-star merger ~130 million light-years away arrived ~1.7 s
   apart, showing gravity travels at c to extraordinary precision. (verify all numbers)
   Might belong in AF instead.)

### Near Strong Gravity

(NOTES -- keep the notes' careful framing verbatim as the guardrail:
 - Locally, c is always c, for any observer anywhere.
 - A distant observer sees light delayed and bent near mass: Shapiro delay, lensing.
   A consequence of curved spacetime (longer paths / clock rates), not c changing
   where the light actually is.
 - Avoid both "c is always c, full stop" and "c slows near black holes."
 Astronomy hook for Shapiro delay: radar echoes from Venus/Mercury near superior
 conjunction took measurably longer (Shapiro, 1960s); Cassini spacecraft (2002-03)
 gave a precise test. That ALSO links to measuring-the-au: the same planetary radar
 that measured the AU tested relativity. Verify.
 Lensing: pair with any existing site content (see cross-links TODO).)

(FIGURE: fig-shapiro-delay -- schematic, Earth, Sun, planet near superior conjunction,
 radar path grazing the Sun. Optional -- only if the section survives.)
(IMAGE: a well-known lensing image (Einstein ring / cluster lensing) from HST or
 JWST -- NASA/ESA, check license and credit line format.)

(TODO:
 [ ] Verify Shapiro 1964 proposal and first measurements; Cassini 2003 result.
 [ ] Careful editing pass on this subsection specifically (per original notes).)

---

## Wrapup

(NOTES -- REVISED for the new spine:
 - Look BACK: solar-system-scale used the light-time ruler on credit; this is the
   calibration certificate.
 - The arc in one breath: minutes per AU (Rømer, Bradley) -> km/s with no AU
   (Fizeau, Foucault) -> the same number from electricity (Maxwell) -> better and
   better (Michelson -> lasers) -> so good it became the ruler (1983).
 - Hand off FORWARD to measuring-the-au: now run it backwards -- with c in hand,
   time a radar echo and you have the AU. Tease the loop; let the next article close it.
 - Point at the sky: Io is still keeping time, still running late when Jupiter is
   far away -- link to companion-romer.
 Keep short.)

---
#### Footnotes

(TODO: sources for every date and value in the history section; c definition (BIPM);
 refractive indices; aberration constant; Weber-Kohlrausch; Shapiro/Cassini.)

---

(CROSS-LINKS -- no links until live; "a later article" until then:
 - Back: measuring-distance (light-time teased as a ruler).
 - Back: solar-system-scale (light-time units used; Sun "8 minutes ago"; Voyager light-day).
 - Forward: measuring-the-au (radar; bootstrapping; parallel "measured -> defined"
   endings, 1983 meter / 2012 AU).
 - Forward: parallax (Bradley was hunting it; Bessel 1838).
 - Companion: companion-romer (reader-facing "measure it yourself" page).
   HUGO -- DECIDED 2026-09-28 (tested on Hugo 0.160.0, mock site):
   - Companion lives in a SIBLING folder next to the article (a leaf bundle "may not
     contain another bundle" -- anything inside the article's folder never becomes a
     page). Naming convention: <article-folder>--<suffix>, e.g. the-speed-of-light--diy,
     so it sorts next to its article.
   - Front matter: url: "/articles/2026/11/the-speed-of-light/diy/" plus
     build: {list: never}. Published at that URL; excluded from lists, sitemap, RSS
     in the mock test. Restart hugo server after adding the folder.
   - Real folder nesting would require articles to become sections (_index.md):
     rejected (breaks dated URLs, drops out of RegularPages/RSS, template rewrites).
   - STILL TO CHECK in the real site: home/series/miniseries templates don't pick it
     up; images in the companion folder publish correctly under the url override.
   - research-d3 never goes in the Hugo repo (like figure sources).
 - Existing site content: check nbasastro.org for HSW/AF pieces on lensing, black
   holes, or the Foucault pendulum before drafting section 4.)

(FIGURE SUMMARY:
 - fig-c-measurement-history: OPTIONAL (too bespoke?) -- the measured/needed TABLE
   is the preferred carrier for the progression.
 - fig-romer-ticks (TikZ), fig-romer-geometry-2027, fig-romer-delay-curve (matplotlib+astropy)
 - fig-aberration-umbrella (TikZ)
 - fig-aberration-vs-parallax (matplotlib) -- strongest "story" figure
 - fig-fizeau-wheel, fig-foucault-mirror (TikZ, matched pair)
 - fig-shapiro-delay (optional)
 IMAGE SUMMARY (all to license-check): Rømer 1676 paper scan; portraits (Rømer,
 Bradley, Fizeau, Foucault, Michelson); Fizeau/Foucault engravings; Michelson
 apparatus; Cherenkov glow; lensing image; Hopper nanosecond; author's own Jupiter/Io.)

(OPEN QUESTIONS:
 - STRUCTURE: DECIDED 2026-09-28 -- organized by argument (what was measured /
   what else was needed), not by date. HP fit: author to confirm against series def.
 - "What Else Changes the Travel Time": keep, trim, or spin off as an AF companion?
   Decide after first draft.
 - Table placement: once up front filling in, or as the closing recap?
 - Maxwell: include (recommended) or park?
 - "Be Rømer": DECIDED -- short pointer here; full version in companion-romer
   (web page linked from the article; book semi-chapter).
 - Descartes: story beat or cut for length?
 - Ancient section: adopt the PINNED "which way does light go?" version, or keep the
   short Aristotle paragraph?
 - Bradley gets real space (agreed in notes' leaning) -- confirm.)
