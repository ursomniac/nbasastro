---
title: "Extending the Ladder: Beyond the Cepheids"
date: 2027-02-03
description: "Cepheids fade out a few tens of millions of light-years away. How astronomers built brighter rungs on the distance ladder -- the tip of the red giant branch, Tully-Fisher, Type Ia supernovae -- and the geometric anchors that hold them all up."
byline: "Brighter rungs, built on the ones below"
authors: ["bob-donahue"]
series: ["astronomical-frameworks"]
tags: []
thumbnail: "thumbnail.webp"
banner: "banner.webp"
miniseries: "measuring-astronomical-distances"
miniseries-sequence: 11

dso_messier: ["101", "106", "33"]
dso_ngc: ["4248", "5461", "5462", "5471", "604"]
dso_other: ["UGC 7356"] 
stars_variable: ["SN 2011fe", "SN 2023ixf"]

---
<!-- v19 (2026-11-14): Bob v18 (credits trimmed, full M 33 added) + M 33 caption punctuation and alt fix (Bob's image order kept). v17: Bob v16 + Claude editorial pass. v15: footnotes added. v14: Bob's v13 + Claude editorial pass: units (Mpc/Mly defined once), Bob's NOTEs
     answered, intro and anchors openings tightened, TRGB halo paragraph moved up. F7 (Phillips relation) dropped.
     PNG/JPG now; WEBP conversion at the end. -->

## Introduction

<!-- NOTE using hero.webp = banner.webp but I'm annotating the banner for SEO/FB purposes.  Keeping the hero.webp copy because it's cleaner. -->
{{< nbas-image src="hero.webp" fullwidth="true"
caption="M 101, the Pinwheel Galaxy -- Seestar S30, 67 min" alt="The face-on spiral galaxy M 101, with loose arms dotted with pink knots of star formation." >}}

Edwin Hubble's distance scale put the Pinwheel Galaxy, M 101, about 2 million light-years away. 
Today the best measurements put it between 21 and 24 million light-years -- roughly ten times farther.
It's not that he was careless: the distance ladder Hubble had to work with had two broken rungs. 
The story of how they broke, and how they were replaced, is the story of how astronomers 
learned to measure the universe beyond our own neighborhood, the Local Group.

The last chapter, [The Local Group](/articles/2027/01/the-local-group-a-distance-that-changed-the-universe/), 
ended at a fence. The rungs we built in [Building the Distance Ladder](/articles/2026/12/building-the-distance-ladder/) --
parallaxes, Cepheids, RR Lyrae stars -- all depend on picking out individual stars in another galaxy.
From the ground, Cepheids can be found in galaxies out to roughly 7 million parsecs -- 7 Mpc, or about 23 million
light-years (Mly). (For nearer galaxies we'll use kpc, thousands of parsecs.) The Hubble Space Telescope 
stretches that to about 40 or 50 Mpc.[^reach] Past that, the problem isn't only faintness: a distant galaxy's 
stars crowd together, and a Cepheid's light blends with its neighbors' until it can't be measured cleanly.

In order to go farther, you need something brighter -- except nothing that bright is close enough to calibrate
directly with parallax. The trick is to find a new kind of object in galaxies whose distances the lower
rungs can already provide, measure how bright it really is there, and then go looking for it farther
out. **The upper rungs were discovered by standing on the lower ones.** Each new rung is something you
can measure *without* knowing the distance -- a sharp edge in a crowd of stars, the width of a radio
line, how fast a supernova fades. Each one tells you how bright, or how big, the object truly is. Compare
that with how bright or big it *looks*, and the distance follows. But each rung is only as good as the
galaxies it was calibrated in -- and one of the first broke spectacularly.

---

## The Brightest Stars, and a Mistake

The first attempt to go beyond the Cepheids used a very simple assumption: the brightest stars in
any big galaxy ought to be about equally bright. Harlow Shapley tried it in 1917; Hubble put it on a
firmer footing in 1926, calibrating the brightest stars against galaxies whose Cepheids he had
already measured, and applying it to 32 galaxies.

{{< article-table >}}

| Hubble's step | Galaxies | Hubble's distance | Today |
|---|---|---|---|
| Cepheids | NGC 6822, M 33, M 31 | ~0.27 Mpc | 0.46–0.84 Mpc |
| "Brightest stars" | M 101 group | ~0.63 Mpc | ~6.5–7.2 Mpc |

{{< /article-table >}}
<!-- Sources: Hubble's chain via Sandage & Tammann (arXiv 0712.2346); modern values from C10 tables and
     extending-the-ladder-facts (M 101 range 6.52 CCHP TRGB to 7.24 Lee & Jang). -->

The chain went like this: Cepheids gave Hubble the distances to three Local Group galaxies -- NGC 6822,
M 33 and M 31 -- coming out at about 0.27 Mpc. In those galaxies he also measured how bright the brightest
"stars" were. Next, he found the brightest stars in galaxies too far for Cepheids -- including the M 101
group -- setting their distance at about 0.63 Mpc. From there he went on to the great cluster of galaxies 
in Virgo.[^chain]

But two things were wrong with those distances, and they stacked. The first was the Cepheid calibration itself,
which Walter Baade showed in 1952 had been built on the wrong kind of Cepheid -- that story is told in
[Building the Distance Ladder](/articles/2026/12/building-the-distance-ladder/). The second mistake was worse:
many of Hubble's "brightest stars" weren't actually stars at all.

{{< nbas-image src="m_101-annotated.webp" 
caption="M 101 with its brightest knots labeled -- the same galaxy as the banner at the top of this chapter. The NGC numbers date from the 1800s, when these looked like separate nebulae; they are H II regions, giant clouds of glowing hydrogen lit by clusters of young stars. The largest, NGC 5471 at right, is about a hundred times larger and brighter than the biggest such region in the Milky Way. Seestar S30, 67 min."
alt="The spiral galaxy M 101 with a coordinate grid, a yellow circle around its disk, and yellow labels on star-forming knots: NGC 5447, 5449, 5450, 5451, 5453 and 5455 on the left side, NGC 5461 and 5462 on the right, and NGC 5471 in a small circle beyond the disk's edge at right." >}}

The labeled knots in M 101 are **H II regions** (pronounced "H-two"): clouds of hydrogen set glowing
by clusters of hot young stars inside them. The Orion Nebula is the most famous example in our own
Galaxy. The giant ones in other galaxies dwarf it: NGC 604 in M 33 is about 1,500 light-years wide,
dozens of times the size of Orion. Seen from far enough away, on a photographic plate, even a large cloud 
like that shrinks to a point of light -- one that's far brighter than any single star. Mistake one for 
a star in a distant galaxy, assume it's only as bright as a star, and your distance comes out far too small.

The clue to recognizing them was in their color. Glowing hydrogen gas gives off its strongest visible 
light in one deep-red line, hydrogen-alpha (H&alpha;), and on photographic plates sensitive to red light 
these "stars" came out far too red. Milton Humason and his colleagues first noticed this in 1956, 
and Allan Sandage made the correction stick in 1958. With Baade's Cepheid fix folded in, Sandage's 
revision multiplied Hubble's distances by a factor of 5 to 10.[^sandage1958]

{{< nbas-image src="m_33-annotated-ngc604.webp" width="360" align="right"
caption="NGC 604, the biggest H II region in the Triangulum Galaxy: about 1,500 light-years across, and unmistakably pink. Detail of the image at left."
alt="Close-up of part of M 33's disk: a bright pink knot circled in yellow and labeled NGC 604 at lower left, and a fainter knot labeled IC 143 above and to the right, among bluish stars and a faint coordinate grid." >}}
{{< nbas-image src="m_33-annotated.webp" width="400" align="right"
caption="M 33, annotated with features that have their own NGC/IC designations -- mostly H II regions. Seestar S30, 62 min." 
alt="The spiral galaxy M 33 with a coordinate grid, a yellow ellipse around its disk, and yellow labels on star-forming knots." >}}

You can see the same clue yourself. In almost any color image of a nearby spiral, the H II regions are
the pinkish knots in the arms -- that pink is hydrogen-alpha. Look for them in the banner image of
M 101 at the top of this chapter, or at NGC 604 in M 33. A smart scope or a camera on a small telescope 
picks them out in the bigger, brighter galaxies, given enough exposure time. Hubble's plates couldn't 
show color the way your camera does.

There was one more twist. In the 1970s, Sandage and Gustav Tammann recalibrated both the brightest
stars *and* the sizes of the largest H II regions against galaxies with well-known Cepheid distances.
Both turned out to depend on how big and bright the host galaxy was. The rung hadn't just been misread; it
was never really a useful standard at all. Big galaxies have brighter "brightest stars." The lesson stuck: 
a new rung has to be something whose brightness is set by _physics_, not by the luck of which galaxy you look at.

{{< clear >}}

---

## The Tip of the Red Giant Branch

The next rung grew out of examining the old stars, not the young ones. That turned out to be its great
strength: a galaxy's brightest young stars depend on how much star formation it happens to be doing,
but almost every galaxy has a population of old stars, and old stars *follow rules*.
<!-- Source: Tammann & Reindl (arXiv 1208.5054), on Baade 1944a,b. -->
Walter Baade saw it first, in 1944. On red-sensitive plates of several nearby galaxies made of old
stars, the galaxy suddenly "resolved" into individual stars at one fixed maximum brightness -- nothing above it,
crowds of stars below. He recognized that edge, later called "Baade's sheet," as the top of the red
giant branch, already familiar from globular clusters. Why the red giants should all stop there took
another decade to work out.[^baade1944]

{{< nbas-image src="fig-trgb-track.webp" width="380" align="right"
caption="One star's life, computed: a star of the Sun's mass, poor in heavy elements like an old halo star. As it climbs the red giant branch its helium core grows (dots), and its brightness grows with it. When the core reaches 0.48 solar masses, helium ignites and the star drops to the helium-burning branch (the drop is drawn simplified). Every such star stops at nearly the same core mass, and so at nearly the same peak brightness. Model: MIST stellar tracks (Choi et al. 2016; Dotter 2016)."
alt="Diagram of luminosity against surface temperature: a gold track runs from the main sequence near 1 solar luminosity up the red giant branch, with dots labeled core 0.2, 0.3 and 0.4, to a circled tip near 2,000 solar luminosities labeled helium ignites; a dashed arrow labeled helium flash drops to a blue dot labeled helium burning near 70 solar luminosities." >}}

Here is the reasoning, worked out by Fred Hoyle and Martin Schwarzschild in 1955. A star
like the Sun -- and any up to about twice its mass -- eventually runs out of hydrogen in its core.
What remains is a core of helium "ash," not (yet) hot enough to burn. This core is squeezed so tightly
it behaves like a white dwarf: its size is set by its mass alone. Meanwhile hydrogen keeps burning in a
thin shell around it, and the shell's output depends only on the mass of the core underneath. As the
shell dumps fresh helium onto the core, the core grows, causing the star to get brighter, and it climbs 
the red giant branch.

But that climb ends at a fixed point. When the core itself reaches about half the Sun's mass, it finally gets hot
enough to burn helium, all at once -- the "helium flash" -- and the star settles down onto the
horizontal branch, becoming fainter and hotter. That's the same horizontal branch where the RR Lyrae stars of
[Building the Distance Ladder](/articles/2026/12/building-the-distance-ladder/) live. Every star that
takes this path stops at nearly the same core mass, and so at nearly the same peak brightness: about
2,000 times the Sun's.

{{< nbas-image src="fig-trgb-edge.webp" width="380" align="left"
caption="How the tip is found: not from one star but from thousands. In an old population, red giants pile up below a sharp ceiling, and above it only a few rarer, later-stage stars remain. Counting stars by brightness (right) shows a sudden step at the tip. This is a simulated population for illustration; the tip's true brightness, an I-band magnitude of about −4.05, is the measured value."
alt="Two-panel chart. Left: thousands of gold dots form a diagonal band of red giants rising from lower left to upper right and stopping at a dashed line labeled the tip near magnitude −4; a few scattered dots lie above it. Right: a blue histogram of star counts that grows toward fainter magnitudes and drops abruptly to nearly zero at the dashed line." >}}

You can't pick out the one star sitting exactly at the tip, but you don't need to. Photograph a few
thousand red giants in another galaxy's halo and count them by their observed brightness. 
The star counts decrease with brightness, but stop abruptly at the tip, because no red giant can be brighter than that.  
Find that limit, and you've found a star population of known brightness. In near-infrared light (the I
band), this tip lands at an absolute magnitude of about −4.05 for old stars
poorer in heavy elements ("metals") than the Sun -- and for those, it barely depends on exactly how poor.
The modern version of the method dates from 1993 (Lee, Freedman and Madore).[^tipcal]

The best place to look is a galaxy's outskirts. In the busy disk, younger bright red stars can sit
above the tip and fool the count, and dust dims everything. In the quiet halo there's little dust,
little crowding, and mostly old stars -- exactly the kind we want to find.

Here is the whole method in three lines. Measure where the step appears in a galaxy's halo, subtract
the tip's absolute magnitude of −4.05, and you have the distance modulus from
[Parsecs vs. Light-Years](/articles/2026/12/parsecs-vs.-light-years/) -- apparent minus absolute
magnitude, which equals 5 log₁₀(distance in parsecs) − 5. Then turn the modulus into a distance:[^tiptable]
<!-- Tip magnitudes are dust-corrected I-band values:
     LMC 14.485 (Jang & Lee 2017); M 106 25.347 (Jang et al. 2021); M 101 25.02 = CCHP mu 29.07 minus 4.05
     (Beaton et al. 2019). Distances computed here. M 101 Cepheid value: Kelson et al. 1996, mu 29.34.
     Virgo: Hatt et al. 2018 (ApJ 861, 104) give NGC 4424/4526/4536 tips 27.03/27.01/27.02 and
     mu 31.00/30.98/30.99 with M = -4.00. Rescaled here to M = -4.05: dust-corrected tip ~27.0 (mu - 4.00;
     Hatt et al. used 0.03 mag foreground extinction -- confirmed by Bob), mu ~31.04, D ~16.1 Mpc.
     13-19 Mpc = Tully & Fisher 1977 (30.6) vs Sandage & Tammann as compared by Fisher & Tully (31.4). -->

{{< article-table >}}

| Galaxy | Tip seen at (I) | Distance modulus | Red giant tip says | Another method says |
|---|---|---|---|---|
| Large Magellanic Cloud | 14.49 | 18.54 | 51 kpc | 49.6 kpc (eclipsing binaries) |
| M 106 | 25.35 | 29.40 | 7.58 Mpc | 7.58 Mpc (masers) |
| M 101 | 25.02 | 29.07 | 6.52 Mpc | 7.4 Mpc (Cepheids, 1996) |
| Virgo cluster (3 galaxies) | 27.0 | 31.04 | 16.1 Mpc | 13–19 Mpc (Tully–Fisher, 1970s) |

{{< /article-table >}}

The LMC comes out within about 3 percent of its eclipsing-binary distance. M 106 matches its maser
distance exactly -- but that's no test, because M 106 is where the −4.05 was calibrated in the first
place. M 101 is the interesting one: red giants in its halo, measured by the Carnegie-Chicago Hubble
Program, put it at 6.5 Mpc, while the Hubble Key
Project's Cepheids in 1996 said 7.4 Mpc. Which galaxy you calibrate on, and which stars you use, still
matters at the level of a few percent -- and sometimes even more.

The last row reaches the Virgo cluster itself. Three of its galaxies, measured the same way, agree
with each other to within 1 percent, at about 16 Mpc (52 Mly). Keep that number in mind for the
next section, where two teams in the 1970s fought over whether Virgo was 13 or 19 Mpc away.

One thing to understand: the tip is *not* brighter than the brightest Cepheids, so this rung doesn't
reach farther. With the Hubble Space Telescope it works out to about 20 Mpc; the Webb telescope is
pushing it past that. Its value to the distance ladder is that it's an **independent** check. 
Cepheids are young, massive, pulsating stars; red giants are old, quiet ones. They share nothing but 
the anchors at the bottom of the ladder, so when the two methods agree on a galaxy's distance, that 
agreement carries some weight. And the tip works in galaxies with no young stars
at all, like the elliptical companions of big spirals, where there are no Cepheids to find.

{{< clear >}}

---

## Tully–Fisher: Weighing a Galaxy by Its Spin

With Tully–Fisher, the standard candle stops being a star. It's the entire galaxy.

The basic idea was already in the last chapter. In 1922, Ernst Öpik estimated the distance to Andromeda from
how fast it rotates: rotation gave him its mass, and its mass told him how bright it ought to be
([The Local Group](/articles/2027/01/the-local-group-a-distance-that-changed-the-universe/)). 
Tully–Fisher is Öpik's idea made empirical -- turned from one clever estimate into a calibrated rung.

{{< nbas-image src="fig-21cm-profile.webp" width="500" align="right"
caption="Why a radio line measures a galaxy's spin. Hydrogen on the side turning toward us is shifted to negative velocities, on the far side to positive ones, so a rotating disk spreads its 21-cm line into two horns. Seen edge-on, the horns sit at plus and minus the rotation speed; tilted, the line narrows; face-on, the rotation is invisible. Computed from a model disk spinning at 200 km/s."
alt="Graph of signal strength against velocity: a gold edge-on profile with two sharp horns at about −200 and +200 km/s, a narrower blue dashed tilted profile with horns near ±130 km/s, and a single narrow dotted face-on peak at zero; an arrow across the top marks the edge-on width as twice the rotation speed." >}}

The measurement comes from radio wavelengths, not visible light. Cold hydrogen gas gives off a faint 
radio signal at a wavelength of 21 centimeters (1,420.4 MHz), and a spiral galaxy is full of that gas. 
The gas on the side turning toward us is Doppler-shifted one way, the gas on the far side the other, so the galaxy's 21-cm
line is smeared into a broad, two-horned shape. Its width is twice the rotation speed. No individual
star has to be seen, and the width doesn't depend on distance at all.

There's one correction, and it matters. The width only shows the part of the rotation along our line
of sight. A galaxy seen edge-on shows all of it; a tilted one shows less, and a face-on galaxy shows
none. So the tilt has to be measured from the galaxy's shape on the sky: it won't work with face-on galaxies.

Why should spin predict brightness? A galaxy that spins faster has to have more mass to hold itself
together, and more mass means more stars to shine. Work through the physics with a few simple
assumptions, and brightness should go as the rotation speed to the fourth power: spin twice as fast,
and you're about sixteen times brighter. In practice the relation works best in infrared light, where
dust in the galaxy dims things least. (There's a puzzle buried here that's still argued about -- the
relation holds even for galaxies whose stars are spread very thin -- better than the simple story says
it should. The answer involves dark matter, which gets its own discussion later.)

R. Brent Tully and J. Richard Fisher published the relation in 1977. They calibrated it on galaxies
whose distances were already known from Cepheids -- M 31, M 33, and the groups around M 81 and
M 101 -- and applied it to the Virgo cluster. Tully expected it to be useful out to about 100 Mpc.[^tf1977]
Today it, together with its cousin for elliptical galaxies (below), supplies most of the distances in
the largest catalogs: tens of thousands of galaxies, out to a few hundred Mpc, each to within
roughly 20 percent.[^cf4]

Here's where the chapter's other lesson shows up: the corrections decide the answer. Tully and Fisher put
Virgo at a distance modulus of 30.6. Sandage and Tammann, using the same kind of measurements, got 31.4 --
0.8 magnitudes larger, which puts Virgo about 45 percent farther away. 
The difference came from which galaxies were in each sample and how each team corrected for dust and for tilt. 
Both answers also rested on the distance to the Hyades star cluster -- the fragile foundation from
[Building the Distance Ladder](/articles/2026/12/building-the-distance-ladder/) -- and correcting
for a revised Hyades distance moves *both* answers by another 0.2 magnitudes. A shaky rung at the bottom of the
ladder reached all the way to Virgo.[^virgo1970s]

Elliptical galaxies don't have orderly rotating disks, so they needed their own method. In 1976 Sandra
Faber and Robert Jackson found that an elliptical's brightness tracks how fast its stars move around
inside it. In 1987, two groups independently sharpened that into the **fundamental plane**: an
elliptical's internal star speeds and its surface brightness together predict its true *size* -- a
standard ruler instead of a standard candle.[^fp]

{{< clear >}}

---

## Type Ia Supernovae

For the farthest rung, you need something that can outshine a whole galaxy.  A Type Ia
supernova does. SN 2011fe in M 101 peaked at an absolute magnitude of about −19.45 -- over 13
magnitudes brighter than a bright Cepheid.[^ia2011fe] 
That means it can be seen in galaxies hundreds of times farther away.

Supernovae looked like standard candles from the start, though at first for the wrong reasons. In the
1930s Fritz Zwicky ran a systematic search for supernovae in other galaxies, and his colleague Walter
Baade studied what he found. In 1938 Baade compiled 18 of them and found that their peak brightnesses
scattered by only about a magnitude, far less than ordinary novae. That was partly luck: the
supernovae Zwicky had been finding happened to all be the same kind.[^baade1938] 
In 1941 Rudolph Minkowski split supernovae into two types by their spectra -- Type I without hydrogen, 
Type II with it -- and later work split Type I further into other subtypes.  
The Type Ia's turned out to be the uniform ones most useful to the distance ladder.

Why should they be? The usual description is that a white dwarf in a close pair of stars gains material
until it reaches a limiting mass -- about 1.4 times the Sun's -- causing it to burn through in a single
thermonuclear runaway. Same fuel, same trigger, same explosion. That picture is still debated: some
Type Ia's seem to come from lighter white dwarfs, especially the fainter ones. But the explosions are
alike enough to work with, *if* you correct for one thing.

The supernovae aren't _quite_ identical. Some are brighter than others by more than a magnitude -- and the
brighter ones are seen to fade more slowly. A supernova's light after the first few days is powered by radioactive
nickel decaying to cobalt and then to iron. A higher nickel abundance means a brighter explosion; and the iron-group
elements trap light, so it takes longer to leak out, making the light curve broader. (How much
of the relation that explains is still argued about.) The point for a distance-measurer is simple:
measure how fast a Type Ia fades, and you know how bright it really was.

That relation was found independently in the 1970s by Bert Rust and Yuri Pskovskii -- and then
doubted for about sixteen years.[^rust] Dust could make a supernova look fainter, and some supernovae lumped
in as "Type I" were really a different kind of explosion. What settled it was better data: in 1993 Mark
Phillips used nine well-observed supernovae measured with electronic cameras and showed that how much
a Type Ia fades in the 15 days after its peak tracks how bright it was. Larger samples confirmed it.
Notice where Phillips's distances came from: Tully–Fisher and other secondary methods. The top rung was
first calibrated on the rung below it. Once corrected, Type Ia peaks agree to about 0.14 magnitudes --
about 7 percent in distance.[^phillips1993]

{{< nbas-image src="m_101-sn2023ixf-equ-20m.webp" width="400" align="right"
caption="M 101 on July 30, 2023, about ten weeks after SN 2023ixf was discovered. The supernova, still near magnitude 12.5, is the bright point at the arrow. eQuinox 2, 20 min."
alt="A circular smart-scope view of the spiral galaxy M 101 dated July 30, 2023, with a white arrow labeled SN 2023ixf pointing to a bright point in the galaxy's upper-left arm." >}}
M 101 has had two bright supernovae in recent years, and they make the point better than any
textbook. SN 2011fe was a Type Ia, caught by the Palomar Transient Factory on August 24, 2011, less than
a day after it exploded, in a part of the galaxy with almost no dust. It reached magnitude 9.9 -- within
reach of binoculars -- and amateur observers recorded its whole light curve for the AAVSO.

More recently, SN 2023ixf was a Type II: the collapse of a massive star, discovered at magnitude 14.9 by the Japanese
amateur Koichi Itagaki on May 19, 2023, right beside the H II region NGC 5461. More than a hundred
smart-scope owners in the Unistellar network followed it, starting even before its first known
detection. It peaked at about magnitude 11.[^sn2023ixf]

{{< nbas-image src="fig-sn-light-curves.webp" fullwidth="true"
caption="Two supernovae in the same galaxy, measured by amateur observers. SN 2011fe (gold) was a Type Ia, the explosion of a white dwarf; SN 2023ixf (blue, dashed) was a Type II, the collapse of a massive star. Both are in M 101, at the same distance, so their brightnesses compare directly. Lines are daily medians of V-band camera measurements; day 0 is discovery. Data: AAVSO International Database (2026)."
alt="Graph of brightness against days after discovery. A gold curve for SN 2011fe rises to magnitude 10 at about day 19 and fades steadily to about 13.8 by day 130. A blue dashed curve for SN 2023ixf rises within days to about magnitude 11, declines slowly to 12.6 by day 75, drops steeply to about 14.3 by day 90, then fades slowly to 15.2 by day 158." >}}

Same galaxy, same distance -- but very different supernova light curves. A Type II's brightness depends on properties of the star
that died: its mass, its outer layers, what it had shed beforehand. Astronomers can coax distances out
of Type II supernovae too, but less precisely. The Type Ia is the one with nearly the same fuel every time.

{{< clear >}}

But there's a catch, and it shapes the whole ladder. To calibrate Type Ia's, you need them in galaxies close
enough for Cepheids or red giants, and they're rare: you can't schedule one; they happen when they happen. 
The SH0ES team's calibration uses 42 Type Ia supernovae in 37 galaxies -- essentially every suitable one seen 
nearby in four decades, about one a year. A supernova like SN 2011fe, in a nearby galaxy with good Cepheid and 
red-giant distances, is exactly what that calibration depends on.[^shoes]


---

## Better Anchors

In [Building the Distance Ladder](/articles/2026/12/building-the-distance-ladder/), the bottom of the
ladder was a single cluster, the Hyades -- and we just saw its shifting distance reach all the way to
Virgo. The modern answer is not one better anchor but several, each of which can fail in a completely
different way. If they agree, it isn't because they share a mistake. Here are three.

**Eclipsing binaries in the Large Magellanic Cloud.** When two stars orbit each other edge-on, they take
turns blocking each other's light. How long each eclipse lasts, combined with how fast the stars move
(from their spectra), gives each star's true size in kilometers. Separately, a star's color tells you
how bright each patch of its surface is -- a direct consequence of how hot things glow -- and with its
apparent brightness that gives its size as an angle on the sky. Kilometers divided by angle is the
distance -- the "skinny triangle" formula, _distance = size ÷ &theta;_ (with &theta; in radians). 
The one ingredient that isn't pure geometry, the link between color and surface brightness,
was calibrated by measuring the actual angular sizes of 41 nearby red giants with interferometers.[^pietrzynski2019]

{{< nbas-image src="fig-eclipsing-binary.webp" fullwidth="true"
caption="How a pair of eclipsing stars gives a distance. The eclipses and the stars' speeds give their true sizes in kilometers; their color and brightness give their sizes as angles on the sky. Schematic curves, not real data. The method behind the 1-percent distance to the Large Magellanic Cloud (Pietrzyński et al. 2019)."
alt="Three panels. Left: a brightness curve over one orbit with two dips, one deep and one shallow. Middle: two velocity curves, gold and blue dashed, swinging in opposite directions and crossing zero at the eclipses. Right: text reading speed times time gives each star's true size in kilometers; color plus brightness gives its size as an angle on the sky; kilometers divided by angle equals distance." >}}

The systems that work best are rare: pairs of aging giant stars on long, wide orbits. Astronomers in
the OGLE survey watched about 35 million stars in the LMC for 20 years to find only 20 good ones. The result,
published in 2019, put the LMC at 49.6 kpc, good to about 1 percent -- the number quoted in
[The Local Group](/articles/2027/01/the-local-group-a-distance-that-changed-the-universe/).

{{< nbas-image src="m_106-equ-30m-full.webp" fullwidth="true"
caption="M 106 (NGC 4258). Its small companions, the edge-on NGC 4248 and the faint UGC 7356, lie at the same distance. The disk of water masers that gives M 106 its geometric distance orbits the galaxy's central black hole, deep inside the bright core -- far smaller than a single pixel of this image. eQuinox 2, 30 min."
alt="The spiral galaxy M 106, tilted to show a bright core and long, faint spiral arms, with a small edge-on galaxy and a faint round smudge nearby in the field." >}}

**The masers in M 106.** Deep in the core of M 106 (NGC 4258), a thin disk of gas orbits a black hole
of about 40 million Suns, and that disk is oriented almost exactly edge-on to us. Water molecules in the disk act
as natural masers -- the microwave version of a laser -- producing sharp radio beacons. M 33 has
masers too: the first water maser ever found outside our Galaxy, in 1977, was in its H II region
IC 133. But M 106's disk is special.[^churchwell1977]

{{< nbas-image src="fig-maser-disk.webp" fullwidth="true"
caption="How the maser disk in M 106 gives a distance with no standard candle at all. Schematic, not to scale. The 9 km/s-per-year figure is computed from the black hole's mass and the masers' orbit."
alt="Diagram of a disk seen from above, with a black hole at the center. Blue dots at the left and right edges carry arrows showing one side coming toward us and the other moving away; a gold dot on the near side moves sideways while an arrow labeled gravity points toward the black hole. Text at left gives three steps: the near-side masers' changing speed gives the orbit's radius in kilometers, radio telescopes measure the same radius as an angle, and kilometers divided by angle gives the distance." >}}

The masers on the near side of the disk, directly in front of the black hole, are moving across our
line of sight. Gravity keeps bending their path around the black hole, so their speed *toward or away
from us* slowly changes: by about 9 km/s every year.[^masercalc] Speed squared divided by that change gives the
radius of their orbit in kilometers. Radio telescopes spread across the Earth, linked together, measure
the same radius as an angle -- a few thousandths of an arcsecond. Kilometers divided by angle again -- another "skinny triangle".
And no assumption about how bright anything is.

Still, it took decades to get right. The first estimate, in 1995, was 6.4 ± 0.9 Mpc; by 1999 it was
7.2, after it turned out the masers' orbit had been taken to be about 10 percent too large. The 2019
analysis gave 7.58 Mpc, to about 1.5 percent. The measurement is so fine that even the slow
drift of the continents _carrying_ the radio telescopes has to be corrected for. And the efforts continue: 
a 2026 reanalysis that tracked individual maser clumps got answers anywhere from 6.7 to 8.1 Mpc
depending on which ones it used, and argued that the precision is overstated; another 2026
analysis recovered 7.56 Mpc. The anchor itself is solid; exactly how solid is still being argued, which is how it
should be. Only a handful of galaxies have maser disks this well-behaved.[^maserhistory]

{{< article-table align="right" >}}

| A star at | 0.02-milliarcsecond offset = |
|---|---|
| 250 pc | 0.5% distance error |
| 1,000 pc | 2% |
| 2,000 pc | 4% |

{{< /article-table >}}

**Parallaxes of Cepheids in our own Galaxy.** The Gaia spacecraft has measured parallaxes for the
Milky Way's own Cepheids, and in 2021 a study of 75 of them, combined with Hubble Space Telescope
brightness measurements, calibrated the Cepheid scale to about 1 percent -- better than any other
single anchor.[^riess2021] The catch is a tiny zero-point error. Quasars, which are so far away their parallax
should be exactly zero, show a small nonzero average in Gaia's data, and that error depends on a star's
apparent brightness, color and position on the sky. For bright stars like Cepheids, the standard correction
turned out to overshoot by about 0.014 milliarcseconds, so astronomers now solve for it along with
everything else. A shift of 0.02 milliarcseconds sounds like nothing, but it is 2 percent of the
distance to a star 1,000 parsecs away.

This is the same lesson the Hipparcos satellite taught us with the Pleiades in
[Building the Distance Ladder](/articles/2026/12/building-the-distance-ladder/): the hardest errors in a
space mission are the small ones that affect every star the same way.

Three anchors -- stars eclipsing each other in a neighboring galaxy, gas orbiting a black hole in a
more distant one, and parallaxes in our own -- each with its own way to go wrong. But today they agree to
within a few percent.

{{< clear >}}

---

## The Full Ladder

Here is the whole ladder, from the bottom up. Each rung measures something that doesn't depend on
distance, and each one was calibrated where it overlaps the rung below.

| Rung | What you measure | Why it works | Reach (roughly) | Calibrated on |
|---|---|---|---|---|
| Parallax | a star's yearly shift | geometry | within our Galaxy | nothing: it's the foundation |
| Cepheids | pulsation period | bigger, brighter stars pulse more slowly | ~7 Mpc from the ground; ~50 Mpc with the Hubble telescope | parallaxes, LMC, M 106 |
| Red giant tip | brightness of the brightest red giants | helium ignites at the same core mass | ~20 Mpc with the Hubble telescope; farther with Webb | the same anchors |
| Tully–Fisher | width of the 21-cm line | spin → mass → light | ~200 Mpc today | Cepheid and red-giant-tip galaxies |
| Type Ia supernovae | how fast the light fades | more nickel: brighter and slower | billions of light-years | Cepheid and red-giant-tip galaxies |

{{< nbas-image src="fig-ladder-reach.webp" fullwidth="true"
caption="How far each rung reaches. Bars are approximate; hatched sections are reach added later -- by space telescopes for Cepheids (Hubble) and the red giant tip (Webb), and by large modern surveys for Tully–Fisher. Each rung overlaps the one below it -- that overlap is where it gets calibrated."
alt="Horizontal bar chart on a logarithmic distance scale from 10 parsecs to beyond 1 gigaparsec: parallax covers our Galaxy; Cepheids run from within the Galaxy to about 7 Mpc, extended to about 50 Mpc; the red giant tip from about 30 kpc to about 20 Mpc, extended to 50; Tully–Fisher from about 1 to 100 Mpc, extended to about 200; Type Ia supernovae from about 5 Mpc to billions of light-years. Dotted lines mark the LMC, M 31, and M 101 and M 106." >}}

Look back at M 101. Hubble's broken rungs put it about 2 million light-years away. Today the red
giants in its halo and its Cepheids put it at about 21 to 24 million. Every number in that chain
rests on the anchors at the bottom -- and the top rung, the Type Ia supernovae, reaches far enough to
measure how fast the universe itself is expanding. Beyond a few hundred Mpc, a galaxy gets a direct
distance only if a supernova happens to go off in it. For everything else, the supernovae
calibrate a different ruler entirely: redshift. That's where the next chapter begins.

<!-- FOOTNOTES (v15). Only verified bibliographic details are given; "via" = where we checked the claim. -->

[^reach]: Ground-based Cepheid reach of about 7 Mpc: G. A. Tammann, "The cosmic distance scale" (IAU review). Hubble Space Telescope: the SH0ES Cepheid hosts reach about 40–50 Mpc (arXiv:2408.11770; arXiv:2401.04773). Crowding and blending as the main limit beyond about 20 Mpc: Freedman et al. (2019), as quoted in Riess et al. (2024), arXiv:2401.04773.

[^chain]: Hubble's chain of distances (Cepheids at distance modulus 22.2, "brightest stars" to the M 81 and M 101 groups at 24.0, Virgo at 26.8): A. Sandage & G. A. Tammann, arXiv:0712.2346. Modern M 101 range: 6.52 Mpc (Beaton et al. 2019, *ApJ* 885, 141, doi:10.3847/1538-4357/ab4263) to 7.24 Mpc (Lee & Jang 2012).

[^sandage1958]: Humason and colleagues (1956) and Sandage (1958), and the overall factor of 5 to 10, as summarized by G. A. Tammann & B. Reindl, arXiv:1211.4655, and Tammann's IAU review "The Hubble constant and the deceleration parameter." The red-plate clue: arXiv:1504.03606.

[^baade1944]: W. Baade (1944a,b), as described by G. A. Tammann & B. Reindl, arXiv:1208.5054, which also credits the physical explanation to Hoyle & Schwarzschild (1955).

[^tipcal]: Lee, Freedman & Madore (1993) is cited as the origin of the modern method in arXiv:1210.6040. Tip absolute magnitude M_I ≈ −4.05: Madore, Mager & Freedman (2009), arXiv:0809.2598; and, calibrated on the M 106 maser distance, −4.050 ± 0.028 ± 0.048 (Jang et al. 2021, *ApJ* 906, 125). Near-independence from metallicity holds for [Fe/H] below about −0.7.

[^tiptable]: Dust-corrected tip magnitudes: LMC 14.485 (Jang & Lee 2017); M 106 25.347 (Jang et al. 2021, *ApJ* 906, 125); M 101 from the published distance modulus 29.07 (Beaton et al. 2019, *ApJ* 885, 141); Virgo galaxies NGC 4424, 4526 and 4536 from Hatt et al. (2018, *ApJ* 861, 104, doi:10.3847/1538-4357/aac9cc), who used M = −4.00 and 0.03 mag of foreground extinction; rescaled here to M = −4.05. M 101 Cepheids: Kelson et al. (1996), distance modulus 29.34 ± 0.17. Distances in the table are our calculations from these values.

[^tf1977]: R. B. Tully & J. R. Fisher 1977, *A&A* 54, 661. Calibrators (M 31, M 33, and the NGC 2403/M 81 and M 101 groups) as listed by Sandage (2006), arXiv:astro-ph/0608677. Reach "say to 100 Mpc": Tully, IAU Colloquium 37.

[^virgo1970s]: Distance moduli 30.6 ± 0.2 (Tully & Fisher 1977) and 31.4 ± 0.2 (Sandage & Tammann 1976), and the 0.2-mag Hyades shift, from the comparison in Jacoby et al. (1992), NED Level 5 review, section 7.1. Other sources give the 1976 Sandage & Tammann value as 31.70 ± 0.08 (Federspiel, Tammann & Sandage 1998, arXiv:astro-ph/9709040).

[^cf4]: Cosmicflows-4: distances to 55,877 galaxies, mostly from Tully–Fisher and the fundamental plane, with about 0.4 mag (≈20%) uncertainty each (Tully et al. 2023, arXiv:2209.11238; arXiv:2507.22236). Tully–Fisher sample: 9,792 spirals within 15,000 km/s (Kourkchi et al. 2020, *ApJ* 902, 145, doi:10.3847/1538-4357/abb66b); fundamental-plane distances from SDSS reach z = 0.1.

[^fp]: Faber & Jackson (1976); the fundamental plane: Djorgovski & Davis (1987, *ApJ* 313, 59) and Dressler et al. (1987).

[^ia2011fe]: SN 2011fe peak M_B ≈ −19.45 and the 0.14-mag scatter after correction: G. A. Tammann & B. Reindl, arXiv:1112.0439.

[^baade1938]: Baade (1938): 18 supernovae, mean peak −14.3 with 1.1 mag scatter (B. Leibundgut, arXiv:1311.5099); the single-type luck (R. P. Kirshner, arXiv:0910.0257). Minkowski (1941), *PASP* 53, 224.

[^rust]: Rust (1974, thesis) and Pskovskii (1977, 1984), via arXiv:1608.04192.

[^phillips1993]: M. M. Phillips 1993, *ApJ* 413, L105, doi:10.1086/186970: nine supernovae, host distances from surface-brightness fluctuations and Tully–Fisher. Confirmed by Hamuy et al. (1996) with 29 supernovae.

[^sn2023ixf]: Discovery: Itagaki, 2023 May 19.727 UT, magnitude 14.9 (Hiramatsu et al. 2023, arXiv:2307.03165). Unistellar network: L. A. Sgro et al. 2023, *Research Notes of the AAS* 7, 141 (252 observations from 115 telescopes).

[^shoes]: 42 Type Ia supernovae in 37 host galaxies: Riess et al. (2022), arXiv:2112.04510.

[^pietrzynski2019]: G. Pietrzyński et al. 2019, *Nature* 567, 200, doi:10.1038/s41586-019-0999-4: 20 eclipsing binaries; 49.59 ± 0.09 (statistical) ± 0.54 (systematic) kpc.

[^churchwell1977]: E. Churchwell et al. 1977, *A&A* 54, 969.

[^masercalc]: Our calculation: for a 4 × 10⁷ solar-mass black hole and an orbit of about 0.14 pc (3.9 milliarcseconds at 7.58 Mpc), orbital speed v = √(GM/r) ≈ 1,100 km/s and acceleration v²/r ≈ 9 km/s per year.

[^maserhistory]: 6.4 ± 0.9 Mpc (Miyoshi et al. 1995); 7.2 Mpc (Herrnstein et al. 1999); 7.60 Mpc (Humphreys et al. 2013); 7.576 ± 0.082 ± 0.076 Mpc (Reid, Pesce & Riess 2019, arXiv:1908.05625). 2026 reanalyses: D. van der Boom & D. Kushnir, arXiv:2601.14374; R. Stiskalek & H. Desmond, arXiv:2609.17684. Usable disk galaxies and continental drift: arXiv:2109.01161.

[^riess2021]: A. G. Riess et al. 2021, *ApJ Letters* 908, L6, arXiv:2012.08534. Parallax zero-point offsets: Lindegren et al. (2021); Freedman's review, arXiv:2309.05618.
