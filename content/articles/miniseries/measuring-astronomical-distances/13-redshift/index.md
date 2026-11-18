---
title: "Velocities and the Hubble Tension"
date: 2027-02-27
description: "Far enough out, redshift is the only distance ruler left. Follow one galaxy in the Coma Cluster from a shifted spectrum line to a distance: what else hides in its measured velocity, how the expansion rate H0 has to be measured, why the methods still disagree, and what that does to the age of the universe."
byline: "One galaxy, one spectrum, and a constant that won't settle."
authors: ["bob-donahue"]
series: ["astronomical-frameworks"]
tags: ["Hubble Tension"]
thumbnail: "thumbnail.webp"
banner: "banner-h0-tension.webp"
miniseries: "measuring-astronomical-distances"
miniseries-sequence: 13

---
<!-- NOTE: can't have [^refs] in captions - they come out verbatim -->
<!--
D13 v16 (2026-11-18, Claude): Coma CMB correction now "about 220 km/s" (the published difference,
  which is what the article actually uses via 7,085); our 268 check moved into the footnote, labeled.
  D12 URL confirmed by Bob.
D13 v15 (2026-11-18, Claude): "favorite size" -> "characteristic size"; stickman citation
  VERIFIED by Bob (SciX: ApJL 302, L1, 1986/03).
D13 v14 (2026-11-18, Claude): from Bob's v13. Bob's four NOTEs:
  - Correction callout: terms renamed so "ours" vs "the galaxy's" is unmistakable.
  - Fingers of God, "where can I see this?": the CfA "stickman" (1986) -- Coma IS the torso. One sentence +
    footnote. Figure option (not done): our own cone plot from public CfA2 catalog data.
  - CMB ripples: what they are (mottling, ~1 part in 100,000), and why COBE didn't show them (7° beam).
  - "H0 varying over time?": yes -- one sentence in the CMB section; "constant" = same everywhere, now.
  Also: comment moved out of mid-paragraph (it split the dipole paragraph in two); hard line break removed
  (trailing double space); "the methods' error bars don't overlap" fixed (CCHP's do); typos.
D13 v12 (2026-11-17, Claude): from Bob's v11 (uploaded as index-d14-v11-bob.md).
  - One name for the example: defined once in the intro as a typical, not a particular, Coma member;
    "our sample galaxy" everywhere after.
  - NEW subsection "Redshift as a distance" (end of "Close, But Not There Yet"): z is the unit astronomers
    quote; table z -> Mpc for 67.4 and 73, stopping at z = 0.15 (the far end of the supernova tier), where
    the simple division is still within a few percent. The "limit to the ruler" paragraph moved here from
    the Clock section. D14 (how-far-can-we-see) owns which distance and what z = 7 means (topic map:
    lookback vs comoving distance).
  - CMB dipole: one clause on WHY motion shows up as temperature (Bob's NOTE).
  - Age paragraph turned inside out (Bob's NOTE): the 13.8 is a model result, not a free measurement.
D13 v10 (2026-11-17, Claude): REBUILT on Bob's five-beat spine (20:36), carrying one example -- a galaxy
  in Coma -- through every step:
  1. From Redshift to Velocity (measure the shift; take out our motion, the region's flow, the galaxy's own
     motion; table of what has to be accounted for; noise wins nearby)
  2. Measuring the Expansion (Hubble's law; H0 has to be MEASURED, far away, with a two-tier ladder)
  3. Many Ladders, Many Slopes (1929 -> Baade -> Sandage -> 50 vs 100 -> Key Project -> SH0ES/CCHP/H0DN;
     it's the DISTANCES that disagree, not the redshifts)
  4. Close, But Not There Yet (CMB's second job: a predicted H0; table of current values; sirens;
     the asterisk on our Coma galaxy)
  5. The Clock in the Constant (Hubble time; 1931 age-of-the-Earth; the tension in the clock; handoff to D14)
  SCIENCE FIX vs v9: the CMB-frame correction removes ALL of our motion at once (whatever causes it).
  Virgo/GA/Shapley explain WHY we move -- and are examples of the regional flows that also move the
  target galaxy. v9's correction formula subtracted Virgo/GA/Shapley as if they were extra corrections
  for us; the callout now separates our motion from the target's flow and its own motion.
  FACT FIX vs v9: Scolnic et al.'s 111.8 Mpc is NOT Coma's velocity / 67.4; it is DESI's fundamental-plane
  relation calibrated to 67.4. Prose now uses our own v/H0 arithmetic (97 vs 105 Mpc); 98.5 and 111.8 in
  the footnote.
  CUT: fig-virgo-projection, fig-pec-error (-> a small table), Hercules, Dipole Repeller, the 2006/2017
  splits, the "declined to participate" sentence. Flock-of-birds metaphor adopted, with callbacks.
Facts: claude/hubble-tension-facts.md. Notes: claude/hubble-tension-notes.md.
-->

## Introduction

{{< nbas-image src="banner-h0-tension.webp" fullwidth="true"
caption="The expansion rate of the universe, measured two different ways over the last dozen years. Gold: measured nearby, with the distance ladder (filled: calibrated with Cepheids; open: calibrated with red giants, CCHP). Blue: predicted from the early universe (WMAP: an earlier satellite). The bands are each series' error bars; they have narrowed, and they have not met."
alt="A chart of the Hubble constant from 2012 to 2027, between 65 and 75 kilometers per second per megaparsec. A gold band labeled measured nearby, the distance ladder, runs near 73; a blue band labeled predicted from the early universe runs near 67; open gold circles labeled red giants (CCHP) sit between them near 70, and a blue point labeled WMAP sits at 70 in 2013. Both bands narrow toward the right without touching." >}}
<!-- CHECK: banner caption reworded to answer "three clusters -- how is it two ways?": the red-giant
points are still the ladder. Banner art unchanged. -->

Beyond the Local Group, distances are counted in megaparsecs, and the ladder starts to run out of
rungs. Cepheids and red giants give star-by-star distances only out to about 40 Mpc. Type Ia supernovae
reach much farther, but only where and when one happens to go off. For almost every galaxy in the
universe, we need another tool.

That tool is **redshift**: the shift of the lines in a galaxy's spectrum caused by its motion -- "red"
because, for a galaxy moving away from us, the lines move toward longer, redder wavelengths. Vesto
Slipher measured the first galaxy velocities this way in 1912, and by 1929 Edwin Hubble had shown that
the farther a galaxy is, the faster it recedes.

{{< nbas-callout kind="definition" title="Redshift: from a shift on a spectrum to a speed" >}}
The **redshift**, *z*, is the shift in a line's wavelength, Δλ, divided by the line's laboratory
wavelength:

{{< nbas-equation >}}
z = \frac{\Delta\lambda}{\lambda_{\text{lab}}}
{{< /nbas-equation >}}

For speeds small compared with light, the velocity, *v*, is the redshift times the speed of light, *c*
(about 300,000 km/s):

{{< nbas-equation >}}
v \approx c\,z
{{< /nbas-equation >}}

Because every line shifts by the same fraction, every line gives the same *z* -- a built-in check.
{{< /nbas-callout >}}

Any galaxy whose light can be spread into a spectrum has a redshift, so for almost every galaxy, redshift
is the *only* distance we will ever have. The recipe sounds simple: distance is velocity divided by the
rate at which the universe expands. Both halves of that division have a catch, and this article takes
them one at a time, following a galaxy in the Coma Cluster from its spectrum to its distance. It
isn't any particular galaxy -- just a typical member, one like hundreds of others there. Call it our
**sample galaxy**.  First, what's really in the velocity. Then, where the expansion rate comes from -- why the methods for
measuring it disagree, and what that does to the age of the universe.

---

## From Redshift to Velocity

Spread a galaxy's light into a spectrum and you see the fingerprints of its atoms: dark lines at
wavelengths fixed by physics. Calcium, hydrogen, magnesium and sodium make the same lines in a galaxy
as in a laboratory. But in a galaxy moving away from us, every line is shifted toward longer, redder
wavelengths -- and all by the same *fraction*, so the red lines move farther in nanometres than the blue
ones. A galaxy moving toward us shows a blueshift instead.

{{< nbas-image src="fig-spectrum-shift.webp" fullwidth="true"
caption="What a redshift looks like. Top: absorption lines at their laboratory wavelengths. Bottom: the same lines in a galaxy receding at about 6,900 km/s, like a galaxy in the Coma Cluster. Every line moves by the same fraction, 2.3 percent, so the shift in nanometres grows toward the red: about 9 nm for calcium, about 15 nm for hydrogen-alpha. Schematic; a real galaxy spectrum has many more lines."
alt="Two horizontal rainbow strips from violet at 380 nanometres to red at 700. The top strip, labeled laboratory, has dark lines marked Ca II H and K near 395, H-beta near 486, Mg near 517, Na near 589 and H-alpha near 656. The lower strip, labeled galaxy, has the same pattern of lines, each shifted to the right; gold arrows connect each line to its shifted position, and the H-alpha arrow is labeled delta lambda about 15 nanometres." >}}

Let's make that our sample galaxy. Its hydrogen-alpha line, at 656.3 nm in the lab, shows up at about
671.4 nm. That's Δλ ≈ 15.1 nm, so *z* ≈ 15.1 ÷ 656.3 ≈ 0.023, and its velocity is
about 0.023 × 300,000 ≈ 6,900 km/s. A ruler-measured shift on a spectrum has become a speed.
<!-- COMPUTED: 656.28 x 1.023 = 671.37; 15.09/656.28 = 0.0230; x 299,792 = 6,895 km/s. Coma's main
cluster: heliocentric 6,863 km/s (Colless & Dunn 1996), so 6,900 is a fair member. -->

But that 6,900 km/s isn't one motion. It's several, added together, and only one of them tells us the
distance.

### What's in a measured velocity

Imagine being one of a flock of birds in flight. The flock is carried along as a whole, but
every bird also darts and weaves on its own, and a gust of wind can push one whole section of the flock
to the side. All you can see is how the other birds move relative to you.

A galaxy's measured velocity is the same kind of sum. There is the expansion of space, the **Hubble
flow** -- the part we want. There is our own motion and drift. And there is the galaxy's own motion through space,
its **peculiar velocity**, which comes in two parts: the gust that moves its whole region, and its own
darting within its group or cluster.

The metaphor breaks in one place, and it's the important part. A flock moves together. But the universe's
flow has everything moving apart, and moving faster the farther away it is. The other motions stay about the same size
at any distance, so they swamp the signal nearby and fade to almost nothing far away.

Here is everything we have to account for, and what we can do about each:

| Motion | Typical size | Same in every direction? | What we do |
|---|---|---|---|
| Our own motion | 370 km/s (the Sun) | No: one arrow, measured precisely | Remove it exactly |
| The galaxy's regional flow (the gust) | A few hundred km/s | No: differs region by region | Model it with flow maps; what the maps miss remains in as error |
| The galaxy's darting within its group | A few hundred km/s; about 1,000 in a rich cluster | Yes: random | Can't remove it for one galaxy; average many, or go far |

The first two are *arrows*: each adds to a galaxy's redshift or subtracts from it, depending on where the
galaxy sits on the sky. A galaxy in the direction we're heading gets one correction, and a galaxy behind
us gets the opposite one. Only the third is random.

### Our own motion

{{< nbas-image src="fig-cmb-dipole.webp" fullwidth="true"
caption="The cosmic microwave background is about 3.36 thousandths of a degree warmer in the direction we're heading and that much cooler behind us. This map is drawn from the measured pattern (Planck 2018), not a photograph of the sky. Stars: the motion of the Sun and of the Local Group. Circles: the Virgo Cluster, the Shapley Supercluster, and the Norma cluster at the heart of the Great Attractor."
alt="An oval all-sky map in galactic coordinates, with the Milky Way's plane across the middle. One half of the sky is shaded gold, warmest near the upper right; the other half blue, coolest at the lower left. Stars mark the Sun's motion, 370 km/s, and the Local Group's, 627 km/s, both in the gold half. Open circles mark Virgo near the top, Shapley near the Local Group's star, and the Norma cluster, labeled Great Attractor, just below the plane." >}}

A bird in the flock can't judge its own speed from the other birds. It has to look down at the ground.
But we also have a "ground" to look at: the **cosmic microwave background** (CMB), the faint glow left over from
when the universe was young and hot, filling all of space. Move through it, and the glow ahead of you is
Doppler-shifted slightly toward shorter wavelengths, the glow behind toward longer ones. For a glow like
this, shorter wavelengths mean warmer, so the sky ahead looks warmer by a few thousandths of a degree,
and the sky behind cooler. After hints
in 1969 and 1971, a detector flown on a U-2 spy plane saw it clearly in 1977.[^dipolehistory] Planck has
since measured it to a few parts in ten thousand: the Sun moves at about 370 km/s relative to the CMB,
toward the little constellation of Crater.[^dipole]
<!-- Certain: a Doppler-shifted blackbody is a blackbody at T(1 + (v/c)cos θ) to first order. -->

That makes our own motion the easy one. Its direction and size are known, so for any galaxy we take the
part of our motion that points toward it and remove it. Catalogs call the raw value "heliocentric" (as
seen from the Sun) and the corrected one "in the CMB frame." Coma lies about 44 degrees from the
direction we're heading, so we are partly moving toward it, and that hides some of its recession. Put
it back -- about 220 km/s, in Coma's direction -- and our sample galaxy's 6,900 km/s becomes about
7,100.[^comav]
<!-- 222 = published CMB-frame minus heliocentric (7,085 - 6,863). Our own check: Sun's vector (264.0°, 48.3°)
vs Coma (~58°, ~88°) = 43.6° apart; 369.8 cos 43.6° = 268 km/s. Difference not traced; footnote says so. -->

### The gust: regional flows

Removing our motion is exact. *Explaining* it is another matter, and the search for an explanation is
how astronomers learned that whole regions of the universe flow together.

The Sun's 370 km/s includes its orbit around the Milky Way; the Local Group as a whole moves at about
627 km/s.[^dipole] The obvious suspect for why is the Virgo Cluster, 16.5 Mpc away, which we are falling toward
at something like 200 to 240 km/s.[^virgoinfall] But Virgo sits about 45 degrees off our direction of
motion, and arrows only help each other in proportion to how well they line up. So, Virgo supplies only
about a quarter of our speed.[^projection] In the late 1980s, seven astronomers nicknamed the "Seven
Samurai" compared the distances and redshifts of about 400 elliptical galaxies and found a large region
of sky -- us included -- streaming generally toward the constellations of Hydra and Centaurus, beyond the Virgo Cluster. 
They named the cause the **Great Attractor**.[^samurai] Its heart is the Norma cluster, comparable to Coma in mass but dimmed by
the Milky Way's dust. Beyond it, in the same broad direction, the **Shapley Supercluster**, about 200 Mpc
away, adds its own pull.[^shapley]

That's the gust. Birds inside it can't feel it; you only see it by comparing with distant birds, which
is what the Samurai did. And every other galaxy sits in a gust of its own. Today astronomers map these
flows in three dimensions from thousands of galaxies with measured distances, and subtract each galaxy's
regional flow from the map. Our home supercluster,
[Laniakea](/articles/2027/02/beyond-the-local-group-the-universe-in-megaparsecs/), is defined that way:
by where its galaxies are going.[^laniakea]

The maps aren't finished. A 2026 study argues that everything within about 220 Mpc accounts for only
about 72 percent of our own speed.[^stiskalek] Different maps give somewhat different corrections, and
that spread is part of every redshift distance's error bar.  We're being pushed and pulled in a variety
of directions by different structures, and we still don't know what (and where) all of them are.

For Coma, the gust turns out to be small. Studies of the cluster as a whole find it nearly at rest
relative to the CMB; others find a few hundred km/s.[^comarest]

{{< nbas-callout title="The correction, written out" >}}
A galaxy's "cosmic" velocity -- the part that is pure expansion -- is its measured velocity, corrected
layer by layer:

{{< nbas-equation >}}
\begin{aligned}
V(\text{cosmic}) = {} & V(\text{measured}) \\
 & + V(\text{us, toward it}) \\
 & - V(\text{its region's flow}) \\
 & - V(\text{its own darting})
\end{aligned}
{{< /nbas-equation >}}

One term is ours; the other two belong to the galaxy. Each is an arrow, projected onto the line of sight
to that particular galaxy, so its size depends on the direction. Our motion is known exactly; the
galaxy's regional flow comes from a map; its darting is unknown for any single galaxy, and averages away
over many.
{{< /nbas-callout >}}

### The darting: a galaxy's own motion

The last term is the one we can't remove. Every galaxy is tugged by its neighbors, which gives it a
peculiar velocity of a few hundred km/s in ordinary surroundings. Inside a rich cluster it's much more:
Coma's galaxies swarm around their common center at about 1,000 km/s. Fritz Zwicky measured that spread
in 1933 and realized the visible galaxies at those speeds weren't nearly massive enough to hold onto 
each other -- the first evidence for dark matter.[^zwicky]

For our sample galaxy, that means its 7,100 km/s could be anywhere from about 6,100 to 8,100 km/s of real
expansion, and there's no way to tell from its spectrum alone. Divided by an expansion rate of 70 (we'll
see where that comes from in the next section), our sample galaxy could be anywhere from about 87 to 116 Mpc
away.[^fingers] Every galaxy in a rich cluster has this problem. On a redshift map, the whole cluster
stretches into a spike pointing back at us -- astronomers call these "fingers of God." The most famous
one is Coma's own. In 1986 a slice of the sky mapped by Valérie de Lapparent, Margaret Geller and John
Huchra showed a pattern shaped like a stick figure, and the stick man's torso was the Coma Cluster,
stretched out along our line of sight.[^stickman]
<!-- FIGURE OPTION (not done): our own cone plot from the public CfA2 catalog (Bob downloads the data;
the workspace can't reach it). The published 1986 figure is copyrighted; don't reuse. -->

The cure is numbers. Measure hundreds of Coma's galaxies and average: the dartings cancel each other out, 
and the cluster's velocity in the CMB frame comes out at 7,085 ± 95 km/s.[^comav] Our sample galaxy's best distance is
the cluster's.
<!-- COMPUTED: (7,085 ± 1,000)/70 = 86.9 to 115.5 Mpc. -->

### Noise wins nearby

How much the leftover motions _matter_ (i.e., their contribution to the uncertainty)
depends entirely on distance, because the expansion grows and they don't. 
Take a typical leftover of 300 km/s:

| Distance | Expansion velocity (at 70) | 300 km/s is… |
|---|---|---|
| 15 Mpc (about Virgo) | 1,050 km/s | 29 percent |
| 43 Mpc | 3,000 km/s | 10 percent |
| 100 Mpc (about Coma) | 7,000 km/s | 4 percent |
| 600 Mpc | 42,000 km/s | under 1 percent |
<!-- COMPUTED: 300/(70 d). At 600 Mpc, v ≈ cz is already approximate (z ≈ 0.14); fine for a ratio. -->

Therefore, nearby, redshift is actually a poor ruler - peculiar velocities contribute significantly to the uncertainty. 
Far away, it's an excellent one -- *provided* we know the expansion rate.

---

## Measuring the Expansion

That expansion rate has to come from somewhere, and the history of the idea starts with speeds. By 1917
Slipher had velocities for 25 spirals: four approaching, the rest receding, some at more than 1,000
km/s.[^slipher] Nobody knew how far away any of them were until 1925, when [Hubble found Cepheids in
Andromeda](/articles/2027/01/the-local-group-a-distance-that-changed-the-universe/). The speeds came a
decade before the distances.

When the distances came, they scaled with the speeds. In 1927 Georges Lemaître showed that an expanding
universe makes speed grow in proportion to distance, and estimated the rate; he published in French, in a
Belgian journal, and when he translated the paper into English in 1931 he left his estimate
out.[^lemaitre] The version that caught on was Hubble's, in 1929: 24 galaxies with distances, most of
their velocities Slipher's, and a straight line through them.[^hubble1929] Two years later Hubble and
Milton Humason pushed the same line out to a cluster in Leo receding at 19,600 km/s, and the doubt was
gone.[^hh1931]

That straight line is **Hubble's law**: a galaxy's speed, *v*, is its distance, *d*, times a constant.

{{< nbas-equation >}}
v = H_0\, d
{{< /nbas-equation >}}

The constant, H<sub>0</sub>, is the **Hubble constant**, the expansion rate. Why should speed be
*proportional* to distance? Because that is the only rule that looks the same from every galaxy. If every
distance in the universe grows by the same small fraction each year, a galaxy twice as far away recedes
twice as fast -- and an observer in any other galaxy sees exactly the same thing. Any other rule would
imply some kind of "center" exists. The straight line says there isn't one.

Turn the law around and it's the ruler we've been using:

{{< nbas-equation >}}
d = \frac{v}{H_0}
{{< /nbas-equation >}}

But H<sub>0</sub> isn't given to us. It has to be *measured*, the only way a slope can be: find galaxies
with _both_ a velocity and a distance (from some other method), and fit the line. The table above says where
to do it. However, there's a conundrum.  Nearby, where we can get distances star by star, the velocities 
are too noisy. Far away, where the velocities are cleaner, single stars are too faint.

So the modern ladder has two tiers that never meet. Within about 40 Mpc, Cepheids and red giants give
distances to a few dozen galaxies that have hosted Type Ia supernovae. That tells us how bright those
supernovae really are -- the rung built 
in [Extending the Ladder](/articles/2027/02/extending-the-ladder-beyond-the-cepheids/). 
Then a separate set of supernovae, far enough away that the leftover motions hardly matter, 
gives the slope: in the most-cited recent analysis, 277 of them, with distances ranging between  about 100 and 640 Mpc.[^tiers] 
The nearby galaxies hold the calibration; the distant ones hold the clean velocities; every rung 
from parallax up sits underneath.

---

## Many Ladders, Many Slopes

The redshifts were never the problem. Slipher's velocities were good in 1912, and the same velocities
still fit today. Every disagreement about H<sub>0</sub> has been about the *distances* -- which means
about the ladder.

{{< nbas-image src="fig-hubble-1929-today.webp" fullwidth="true"
caption="Hubble's 24 galaxies, with the same velocities, at the distances he gave them in 1929 (faint circles, on his steep dashed line of 500 km/s per Mpc) and at today's distances (gold dots), around a modern line of 70. The scatter that remains is the galaxies' own motions. Distances: earlier articles in this series, the NASA/IPAC Extragalactic Database, and two recent measurements."
alt="Velocity against distance from 0 to 20 million parsecs. Open circles crowd the left edge within 2 Mpc along a steep dashed line; horizontal arrows carry each to a gold dot between about 3 and 19 Mpc, scattered around a much shallower solid line. Labels mark M 31, M 81, the Virgo cluster, NGC 7331 and M 85." >}}

Hubble's first slope was 500. This figure shows his 24 galaxies twice: where he put them in 1929, and
where we put them today.[^d1929] 
Every galaxy moves outward, by a factor of about seven on average, and
the slope flattens from 500 to about 70. The law was right; the distances weren't. Notice, too, what
doesn't change: the scatter. Eleven of his 24 galaxies are within about 5 Mpc, the top row of the noise
table, where the expansion is no bigger than the galaxies' own motions. Andromeda and M 81 are still
approaching. Hubble found a real law in data dominated by noise.
<!-- COMPUTED: 11 of 24 have modern d < 5 Mpc; 70 x 5 = 350 km/s. Median modern/Hubble ratio 7.4. -->

The repairs came rung by rung, and earlier articles in this series tell those stories. In 1952 Walter
Baade found that the Cepheids in other galaxies were a brighter kind than the ones they'd been calibrated
on ([Building the Distance Ladder](/articles/2026/12/building-the-distance-ladder/)); distances roughly
doubled, and H<sub>0</sub> roughly halved.[^baade] In 1958 Allan Sandage found that Hubble's "brightest
stars" were often glowing gas clouds ([Extending the
Ladder](/articles/2027/02/extending-the-ladder-beyond-the-cepheids/)), and brought H<sub>0</sub> down to
about 75, "with a possible uncertainty of a factor of 2."[^sandage1958]

{{< nbas-image src="fig-h0-history.webp" fullwidth="true"
caption="Almost a century of one number. Each point is a published value of the Hubble constant, with its stated uncertainty where there is one (Sandage's 1958 bar is his own \"factor of 2\"). The right-hand scale reads each value as a Hubble time. At this scale the modern values look like agreement; the inset zooms in on 2012–2027, where they split into two groups -- the ladder near 73 and the early universe near 67 -- with the red-giant ladder between. Sources in the notes."
alt="Hubble constant against year on a logarithmic scale from 30 to 800, with a right-hand scale of Hubble time in billions of years. Points fall from Hubble at 500 in 1929 (2 billion years), through the Baade era near 280 in 1952 and a point near 180, to Sandage near 75 in 1958 with a bar from about 38 to 150. In the 1970s and 80s, Sandage and Tammann sit near 50 and 55 while de Vaucouleurs sits near 100 and 95. The Key Project is at 72 in 2001. A box around the tight cluster of modern points near 70 leads to an inset, zoom 2012 to 2027, in which gold ladder points sit near 73, blue early-universe points near 67, and open gold red-giant points near 70." >}}

Through the 1970s and 1980s Sandage and Gustav Tammann found
values near 50 to 55, while Gérard de Vaucouleurs found values near 95 to 100, from the same kinds of
galaxies but with differently built ladders. Each side quoted about 10 percent uncertainty, so each side's
error bars excluded the other's value.[^fiftyhundred] The "factor of 2" had become a feud.  The Hubble Space 
Telescope was built in part to settle it, and in 2001 its Key Project announced 
H<sub>0</sub> = 72 ± 8.[^h0data] The answer was in between.

Yet, the argument didn't end; it just shrank. The SH0ES team, led by Adam Riess, has used Hubble and now the James
Webb Space Telescope to measure Cepheids in 37 supernova host galaxies, anchored to geometric distances.
Their value has stayed near 73 while the uncertainty shrank to about 1.4 percent.[^shoes] Wendy Freedman,
who led the Key Project, now leads the Chicago-Carnegie Hubble Program (CCHP), which calibrates the
supernovae with red giants -- the [tip of the red giant
branch](/articles/2027/02/extending-the-ladder-beyond-the-cepheids/) -- instead of Cepheids. Their latest
value is about 70.4.[^cchp] In 2026 a large collaboration tried replacing the ladder with a network: many
overlapping methods linked at once, so that no single rung carries the whole weight. They found 73.5,
uncertain by about 1 percent.[^network]

Fifty years ago, two ladders disagreed by a factor of two. Today the ladders disagree by about 4 percent.
That's progress by any measure -- and we'd expect that over time, things would converge at a single value, 
if there weren't a completely different way to get the answer.

---

## Close, But Not There Yet

The CMB has a second job. The same glow that showed us our own motion *also* provides a value for 
H<sub>0</sub>, and it does it without using a single rung of the ladder.

The CMB is a snapshot of the universe at about 380,000 years old, when it first became transparent. Its
temperature isn't perfectly even. Take away our motion, and the sky is mottled with slightly warmer and
cooler spots, differing by about one part in 100,000. COBE first detected them in 1992, but its view was
blurred to about 7 degrees, too coarse to show their pattern; WMAP and Planck saw much finer
detail.[^cobe] That mottling is the imprint of sound waves that rang through the hot gas before the
universe became transparent. The physics of that gas sets how far a sound wave could travel in that
time, so the spots have a characteristic size: about 144 Mpc, as the expansion has stretched it since. On the sky, Planck measures that size as an angle
of about 0.6 degrees, to three parts in ten thousand.[^acoustic] A known size and a measured angle give a
distance -- the same step we used to work out the [Virgo Cluster's
width](/articles/2027/02/beyond-the-local-group-the-universe-in-megaparsecs/), run the other way.

But that's the distance out to light that has been travelling for nearly all of cosmic history. And the
expansion rate itself changes with time. The "constant" in Hubble constant means the same everywhere at
one moment, not the same forever; H<sub>0</sub> is its value *today*. To get from the CMB's distance to
today's rate, you need the rate at every moment in between, added up along the light's whole journey. That history comes
from the **standard model of cosmology**: a universe of ordinary matter, dark matter and "dark energy,"
in amounts that are themselves fitted to the same CMB data. The model isn't handed down; it's the
simplest recipe that fits what we see. Run it all forward, and the ripples say H<sub>0</sub> should be 67.4,
pinned to well under 1 percent.[^cmb]

That's why it's called a *prediction*. The ladder measures today's expansion directly. The CMB value is
what today's expansion should be, if the standard model is right about the 13.8 billion years in between.
Here they are side by side:

| Measurement | Method | H<sub>0</sub> (km/s per Mpc) | Uncertainty |
|---|---|---|---|
| SH0ES (2022) | Ladder: Cepheids → supernovae | 73.0 | ± 1.0 (1.4%) |
| Distance network (2026) | Ladder: many methods linked | 73.5 | ± 0.8 (1.1%) |
| CCHP (2025) | Ladder: red giants → supernovae | 70.4 | ± 1.9 (2.8%) |
| Gravitational waves (2026) | No ladder, no model | 71 | +9 / −7 (about 11%) |
| Planck (2018) | Early universe + standard model | 67.4 | ± 0.5 (0.7%) |

In the 1980s, 10 percent error bars made a 10 percent disagreement in H<sub>0</sub> estimates an argument. 
Now the error bars are around 1 percent, and the Cepheid ladder's and the early universe's no longer overlap.
The "gap" between the Cepheid ladder and the early universe is about 8 percent -- about five times the combined uncertainty. 
That's the **Hubble tension**. The red-giant ladder, with wider error bars, sits within about one and a half of 
its own uncertainties of *both* camps, which is why it's the subject of so much argument.[^sigma] 
While that gap doesn't *seem* like much, it's enough to shift distances noticeably.
So, either the ladder has an error nobody has found, or the early-universe measurement does, 
or the standard model that connects then to now is missing something.
<!-- COMPUTED: 73.04/67.4 = +8.4%; (73.04-67.4)/sqrt(1.04²+0.5²) = 4.9σ; CCHP vs Planck 1.5σ, vs SH0ES 1.2σ.
H0DN quotes 7.1σ vs 67.24 ± 0.35. -->

One row in that table needs neither a ladder nor a model. When two neutron stars collided on 17 August
2017, gravitational-wave detectors recorded the event, GW170817, and the shape of the signal gave its
distance directly. Telescopes found the flash related to the event in the galaxy NGC 4993, which gave the redshift. 
One event, one H<sub>0</sub>: 70, with error bars from about 62 to 82.[^gw170817] By 2026, with more than 200
events, the value was 71, still uncertain by about 11 percent.[^gwtc5] These "standard sirens" can't
settle the question yet, but they're the one ruler that shares nobody's assumptions, and they sharpen
every year with each new event detected.

Now back to our sample galaxy in Coma. Its cluster recedes at 7,085 km/s. With the ladder's 73, that's 97 Mpc;
with the early universe's 67.4, it's 105 Mpc.[^coma] That difference, 8 Mpc, is about 26 million
light-years -- half the distance to the Virgo Cluster! The supernovae that have gone off in Coma itself
put it at 98.5 Mpc, on the ladder's side, as they must: they're calibrated by the same ladder. Same
galaxy, same light, and two answers about 8 percent apart that won't agree until H<sub>0</sub> does. 
So, every galaxy distance measurement that starts with an observation of its redshift has an asterisk: "your mileage may vary".
<!-- COMPUTED: 7,085/73 = 97.1; /67.4 = 105.1; 8 Mpc x 3.2616 = 26 Mly; 8/16.5 = 48%. -->

### Redshift as a distance

Because a redshift is the one thing measured directly, astronomers usually quote it instead of converting to a
distance: e.g., "a galaxy has *z* = 0.05" because it avoids having to assign a particular value of H<sub>0</sub>.
Within the range this article covers, turning redshift into megaparsecs
is the division we've been doing all along, d = c*z* ÷ H<sub>0</sub>, and the two values of
H<sub>0</sub> give two columns:

| Redshift, *z* | c*z* (km/s) | Distance at 73 | Distance at 67.4 |
|---|---|---|---|
| 0.01 | 3,000 | 41 Mpc | 44 Mpc |
| 0.023 (about Coma) | 6,900 | 95 Mpc | 102 Mpc |
| 0.05 | 15,000 | 205 Mpc | 222 Mpc |
| 0.1 | 30,000 | 411 Mpc | 445 Mpc |
| 0.15 (the far end of the supernova tier) | 45,000 | 616 Mpc | 667 Mpc |
<!-- COMPUTED: c = 299,792 km/s; cz/73 and cz/67.4. Coma row uses the spectrum figure's z (heliocentric),
so it differs slightly from the 97/105 above (CMB-frame 7,085 km/s). -->

That's where the simple division runs out. It assumes that the universe barely changed while the light
was on its way, and that "speed = redshift × the speed of light" still holds. By *z* = 0.15 those
assumptions are already off by a few percent, and by *z* = 0.5 by more than 10.[^zlimit] Light that left a
galaxy billions of years ago was stretched by the expansion all along its trip, the galaxy has moved on
since, and "how far away is it?" no longer has one answer. Past this point, astronomers keep the
redshift itself as the label -- which is why a galaxy is reported "at redshift 7," with no distance
attached.  

---

## The Clock in the Constant

H<sub>0</sub> has one more thing to tell us. Its units, kilometers per second per megaparsec, hide a
time: a megaparsec is also a number of kilometers, so the units cancel to one over a time. Run the
expansion backward at today's rate, and 1/H<sub>0</sub> -- the **Hubble time** -- is how long ago
everything was together. At H<sub>0</sub> = 70, space stretches by about one part in 14,000 every million years, and the
Hubble time is about 14 billion years.[^clock]

The clock has caused trouble before. Hubble's 500 gave 2 billion years. In 1931 a National Research
Council committee concluded from radioactive dating that the Earth was _at least_ two billion years
old.[^earthage] The universe was no older than Earth's own rocks -- one more sign, if anyone needed it, that
the ladder was broken.

Today the clock carries the tension with it. Using the ladder's 73, the Hubble time is about 13.4 billion
years; at the early universe's 67.4, about 14.5. Neither is the age of the universe, because the
expansion hasn't run at today's rate the whole time: it slowed for its first 9 billion years or so, and
has sped up since. To turn a Hubble time into an age you need that whole history, and the history comes
from the standard model. Run the model, and the age comes out at 13.8 billion years -- the most familiar
number in cosmology, and a product of the very model the tension calls into question. (A curiosity: at
today's rate, the Hubble time comes within a few percent of that age. Nobody knows whether that means
anything.[^coincidence])
<!-- COMPUTED: 978/73.04 = 13.39; 978/67.4 = 14.51 Gyr. -->

---

## Wrapup

We followed our sample galaxy in the Coma Cluster from a line on a spectrum to a distance. The line gave a
velocity, 6,900 km/s. Our own motion, read off the CMB, came out exactly. Its region's flow came from a
map, and was small. Its own darting couldn't be removed at all, so we borrowed the whole cluster's
average. That left one division: velocity over H<sub>0</sub>.

H<sub>0</sub> has to be measured the same way, with clean velocities from far away and distances from
the ladder. Hubble's first try was off by a factor of seven, because the ladder under it was broken.
Every repair since brought the ladders closer together, until they now agree to within a few percent.
But they still disagree, by about 8 percent, with the value the early universe predicts. For our sample galaxy,
that's the difference between 97 and 105 Mpc, with the underlying issues an asterisk on every redshift distance 
as well as on the clock of the universe itself.

That isn't a failure of the ladder. A ruler precise enough to disagree with the universe's own prediction
is a ruler worth arguing about.

There's one question left. Redshift carries us out to light that left its galaxies billions of years ago,
from places that the expansion has moved on since. How far can we see?

## Footnotes

[^slipher]: C. O'Raifeartaigh 2013, in *Origins of the Expanding Universe: 1912–1932*, ASP Conf. Ser. 471 (arXiv:1212.5499): first clear spectrum of Andromeda in September 1912, approaching at 300 km/s (V. M. Slipher 1913, *Lowell Obs. Bull.* 2, 56); 25 spirals by 1917, four approaching.

[^dipolehistory]: E. K. Conklin 1969, *Nature* 222, 971; P. S. Henry 1971, *Nature* 231, 516; G. F. Smoot, M. V. Gorenstein & R. A. Muller 1977, *PRL* 39, 898.

[^dipole]: Planck Collaboration 2020, *A&A* 641, A1 and A3: dipole amplitude 3362.08 ± 0.99 μK toward galactic (l, b) = (264.021°, 48.253°), the Sun moving at 369.82 ± 0.11 km/s. Local Group: 627 ± 22 km/s toward (276°, 30°) (A. Kogut et al. 1993, as given in the Particle Data Group's CMB review). The map is our drawing of that measured pattern, not a Planck image. Norma cluster at (325.3°, −7.2°): P. A. Woudt et al.; Shapley at (312°, 31°): T. Mutabazi et al. 2014, arXiv:1401.7478.

[^comav]: Main Coma cluster, heliocentric 6,863 km/s with a velocity dispersion of 1,082 km/s (M. Colless & A. M. Dunn 1996); in the CMB frame, 7,085 ± 95 km/s (Smith et al. 2004); both as quoted in arXiv:1601.03047. The correction used here, about 220 km/s, is the difference between those two published values. Our own check, projecting the Sun's 370 km/s onto Coma's direction (about 44° away), gives about 270 km/s; we have not traced the difference.

[^virgoinfall]: The range of published values; direction from D. A. Dale et al. 1999, arXiv:astro-ph/9808158.

[^projection]: Our calculation with astropy: the Local Group's motion toward (276°, 30°) and M 87 at (283.8°, 74.5°) are 44.7° apart; 220 km/s × cos 44.7° = 156 km/s, about a quarter of 627.

[^samurai]: D. Burstein, R. L. Davies, A. Dressler, S. M. Faber, D. Lynden-Bell, R. J. Terlevich & G. Wegner: A. Dressler et al. 1987, *ApJ* 313, L37; D. Lynden-Bell et al. 1988, *ApJ* 326, 19.

[^shapley]: Distance about 200 Mpc (redshift 0.046), as in [Beyond the Local Group](/articles/2027/02/beyond-the-local-group-the-universe-in-megaparsecs/); position from Mutabazi et al. 2014.

[^laniakea]: R. B. Tully et al. 2014, *Nature* 513, 71.

[^stiskalek]: R. Stiskalek et al. 2026, arXiv:2601.08524 (preprint): mass within 155 h⁻¹ Mpc accounts for about 72% of the Local Group's speed.

[^comarest]: Nearly at rest: e.g., arXiv:astro-ph/9903380 (fundamental-plane peculiar velocities of 20 clusters); a few hundred km/s, depending on the method: arXiv:2409.16871.

[^zwicky]: F. Zwicky 1933, *Helvetica Physica Acta* 6, 110 (English translation: H. Andernach & F. Zwicky 2017, arXiv:1711.01693), with velocity differences in Coma of "at least 1500 to 2000 km/s." Today's figure of about 1,000 km/s for the spread: e.g., M. A. Strauss & J. A. Willick 1995, arXiv:astro-ph/9502079.

[^fingers]: Strauss & Willick 1995. The 87–116 Mpc range is our arithmetic for 7,085 ± 1,000 km/s at 70 km/s per Mpc.

[^stickman]: V. de Lapparent, M. J. Geller & J. P. Huchra 1986, *ApJL* 302, L1 ("A Slice of the Universe"); the torso as Coma's finger: M. J. Geller et al. 2011, the 2010 Russell Lecture, arXiv:1110.1380.

[^lemaitre]: G. Lemaître 1927, *Annales de la Société Scientifique de Bruxelles* A47, 49; the omitted passage and Lemaître's own letter about the translation: M. Livio 2011, *Nature* 479, 171. In 2018 the International Astronomical Union recommended calling the relation the Hubble–Lemaître law (IAU Resolution B4).

[^hubble1929]: E. Hubble 1929, *PNAS* 15, 168: velocities for 46 nebulae, distances for 24; four of the velocities were new measurements by Humason. His slope: about 500 km/s per Mpc.

[^hh1931]: E. Hubble & M. L. Humason 1931, *ApJ* 74, 43; the Leo cluster at 19,600 km/s as summarized by S. van den Bergh 2011, arXiv:1108.0709.

[^tiers]: A. G. Riess et al. 2022, *ApJL* 934, L7; D. Brout et al. 2022: 277 Hubble-flow supernovae at redshifts 0.0233 to 0.15; calibrator hosts up to about 40 Mpc (Riess et al. 2019). Distances in Mpc are redshift velocity divided by 70 (our arithmetic, approximate at the far end).

[^d1929]: Modern distances use the value already given in an earlier article of this series where there is one; otherwise the median of the distances measured with Cepheids, red giants, surface brightness fluctuations or masers in the NASA/IPAC Extragalactic Database (NED), queried November 2026; for NGC 4151, Cepheids (W. Yuan et al. 2020, *ApJ* 902, 26); for M 77, red giants (N. A. Tikhonov & O. A. Galazutdinova 2021, *Astrophys. Bull.* 76, 255). Velocities are Hubble's, as printed. The median ratio of modern to 1929 distance, 7.4, is our calculation.

[^baade]: W. Baade, International Astronomical Union General Assembly, Rome, 1952. Published values of H0 just after his revision range from about 180 to 280.

[^sandage1958]: A. Sandage 1958, *ApJ* 127, 513.

[^fiftyhundred]: Summary in *Nature Physics* 13, 2017 (doi:10.1038/nphys4055); A. Sandage & G. A. Tammann, "Steps Toward the Hubble Constant" I–X (1974–1995); G. de Vaucouleurs 1982, *Nature* 299, 303.

[^h0data]: Hubble 1929; Baade era 280 ± 28 (1952) from the compilation of P. Bethapudi & S. Desai 2017 (arXiv:1701.01789), unlabeled point 180 (Humason, Mayall & Sandage 1956); A. Sandage 1958, *ApJ* 127, 513; Sandage & Tammann 50 (1974) and 55 ± 5 (1996, arXiv:astro-ph/9611170); G. de Vaucouleurs 100 ± 10 (1979, via the same compilation) and 95 ± 10 (1982, *Nature* 299, 303); Key Project: W. L. Freedman et al. 2001, *ApJ* 553, 47. Modern: SH0ES (A. G. Riess et al. 2016, 2019, 2021, 2022); CCHP (W. L. Freedman et al. 2019, *ApJ* 882, 34; 2021, *ApJ* 919, 16; 2025, *ApJ*); WMAP 2013, Planck 2015 and 2018, and the combined Planck, SPT and ACT value 67.24 ± 0.35; the 2026 network (H0DN 2026).

[^shoes]: Riess et al. 2022: 73.04 ± 1.04 km/s per Mpc, from 42 supernovae in 37 host galaxies. JWST photometry of Cepheids agrees with Hubble's (Riess et al. 2023–2024).

[^cchp]: W. L. Freedman et al. 2025, *ApJ*: 70.39 ± 1.22 (stat) ± 1.33 (sys) ± 0.70 (supernovae) km/s per Mpc, from red giants with Hubble and Webb; 1.94 combined (our arithmetic).

[^network]: H0DN Collaboration (S. Casertano et al.) 2026, *A&A* 708, A166: 73.50 ± 0.81 km/s per Mpc, 7.1 standard deviations from the early-universe value with the standard model.

[^acoustic]: Planck Collaboration 2020, *A&A* 641, A6: angular acoustic scale 100θ* = 1.0411 ± 0.0003 (0.03 percent), sound horizon at last scattering 144.4 Mpc; last scattering at redshift about 1,090. The age at that time, about 380,000 years, is the standard-model value. The angle in degrees is our conversion.

[^cobe]: COBE's Differential Microwave Radiometer: beam about 7°; fluctuations of about 30 μK announced in 1992 (*Physics Today* 50, no. 11, 1997; the Berkeley Lab COBE pages). One part in 100,000 is our arithmetic for 30 μK against 2.7 K.

[^cmb]: Planck Collaboration 2020, *A&A* 641, A6: 67.4 ± 0.5, "assuming the base-ΛCDM cosmology"; combined with the South Pole Telescope and the Atacama Cosmology Telescope, 67.24 ± 0.35 (as quoted by the 2026 network).

[^sigma]: Our arithmetic, combining each pair's uncertainties: SH0ES vs Planck about 4.9 standard deviations; CCHP vs Planck about 1.5; CCHP vs SH0ES about 1.2.

[^gw170817]: B. P. Abbott et al. (LIGO Scientific Collaboration, Virgo Collaboration and others) 2017, *Nature* 551, 85: 70.0 +12.0/−8.0 km/s per Mpc.

[^gwtc5]: LIGO–Virgo–KAGRA Collaboration 2026, arXiv:2605.27227 (GWTC-5.0, 236 events, combined with GW170817): 71.0 +9.0/−7.1 km/s per Mpc.

[^coma]: Distances at 73 and 67.4 km/s per Mpc are our arithmetic from Coma's CMB-frame velocity. Supernova distance: D. Scolnic et al. 2025, *ApJL* 979: 98.5 ± 2.2 Mpc from 13 Type Ia supernovae calibrated with the Hubble Space Telescope distance ladder. The same paper finds that a galaxy-based distance relation from the DESI survey, calibrated instead to 67.4, puts Coma at 111.8 ± 1.8 Mpc.

[^zlimit]: Our comparison, with astropy's Planck 2018 cosmology: c*z* ÷ H<sub>0</sub> against the standard model's comoving distance is about 4 percent high at *z* = 0.15 and about 14 percent high at *z* = 0.5. Which distance to compare against is the subject of the next article.

[^clock]: Our arithmetic: 1 Mpc = 3.086 × 10^19 km, so 1/H0 = 978 billion years divided by H0 in km/s per Mpc.

[^earthage]: The National Research Council's report on the age of the Earth (1931), with the radioactive-dating survey by Arthur Holmes, as reported in the press that year: "at least 2,000,000,000 years," from a mineral dated at 1.85 billion years.

[^coincidence]: A. Avelino & R. P. Kirshner 2016, *ApJ* 828, 35: H0 times the age of the universe = 0.96 ± 0.01.
