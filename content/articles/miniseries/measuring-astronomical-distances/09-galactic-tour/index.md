---
title: "A Tour of the Milky Way Galaxy"
date: 2027-01-13
description: "A traveler's tour of the Milky Way: skies that never get dark, a sky full of glowing gas, a Galaxy hanging overhead, and neighborhoods where planets can't keep their comets. What the familiar sky becomes when you go there."
byline: "Postcards from inside our Galaxy"
authors: ["bob-donahue"]
series: ["wider-view"]
thumbnail: "thumbnail.webp"
banner: "fig-band-labels.webp"
miniseries: "measuring-astronomical-distances"
miniseries-sequence: 9

dso_messier: ["13", "15", "16", "45"]
dso_ngc: ["5466", "6522"]
dso_other: ["Barnard 68-72"]
stars_bright: ["Arcturus"]
stars_nearby: ["Arcturus", "Kapteyn's Star", "Gmb 1830"]
stars_other: ["Gmb 1830", "HD 140283", "Kapteyn's Star", "S5-HVS1"]

---

<!-- v18 = Bob's v17 + copyedits (typos, the kpc paragraph, M 7/M 11 sentence, callout comment moved).
     v16 = Bob's v15 + UNITS: galactic distances in kpc (C08's ruler); pc kept for spacings and
     local objects (B 68, M 7, open clusters, neighbor distances).
     v14 (Claude, 2026-11-07, from Bob's v13):
  - FIGURES: You Are Here insets and the 4-panel globular vista REMOVED. Replaced by a set of
    full-width "window" views from the same model and ONE shared brightness scale
    (fig-views/fig-view-from.py): halo (Bob's spot) and M 13; the LMC view re-plotted on the same
    scale. Home's member of the set is the real-sky band figure. Inner Galaxy: no model view (see
    the CHECK there). The set is named once, in the first view's caption; the others say "same model".
  - FOOTNOTES: every paper cited in the text now has a footnote (list at the end). Inline
    "(Author year)" removed from the prose; numbers marked "our calculation" keep that wording.
  - HALO rewritten around Bob's stop (16 kpc from the center, 12 kpc up): the density gradient,
    the transition to the disk, and the Gaia-Enceladus "river that carved the canyon".
  - Bob's v13 NOTEs answered in place and removed: HD 140283's orbit, Arcturus lag vs pass,
    B 68 identification, M 16's arm, open-cluster spacing of ALL stars, gallery size, NGC 891,
    NGC 6522's orbit, the GHZ callout (now a short paragraph), the intro itinerary paragraph. -->

## Introduction

A map tells you a country is there. It doesn't tell you what it's like to live there.

Over the last eight articles we've built a map of the Milky Way using parallax for our neighbors,
standard candles for the far side of the Galaxy, and with both, a rough idea of where the disk, the bulge,
and the halo sit. Every place on that map has a distance we know how to measure. This time
we're going to go there, and imagine what it's actually like.

Every traveler knows the moment when the familiar turns strange: the same sun, the same rain,
the same kind of people, and yet everything feels different. The Milky Way is like that. Wherever
you go, it's still the same kinds of stars, the same physics, the same Galaxy. But go to the right
places and the night sky never gets dark. Or the whole sky glows with gas. Or the Milky Way isn't
a band at all, but a spiral hanging over your head. Or your nearest neighbor is so close that
no star could hold on to a cloud of comets the way the Sun does.

Our trip starts at home and works outward: a dark cloud, a stellar nursery and a young star
cluster, all close by; then up into the halo, into a globular cluster, and finally down into
the crowded heart of the Galaxy. Along the way we'll meet a few tourists who are passing through
our own neighborhood right now. And from some of the stops, we'll turn around and look back at
the Milky Way itself, because the same Galaxy looks completely different depending on where you
stand.

Back at [the very beginning](/articles/2026/10/measuring-distance/) of this series, "near" and "far"
were everyday distances measured in miles or kilometers. Here, near is a few hundred parsecs, and far is
the other side of the Galaxy. And distance turns out to shape what each place is like: how far it is
to the next star decides how bright your neighbors are, how dark your nights get, and whether a star can
keep its comets and planets.

At this scale our standard unit is the kiloparsec (kpc): 1 kpc is 1,000 pc, about 3,260 light-years,
the distance at which a star's parallax is 1 milliarcsecond. Anything farther away has a smaller
parallax still, which is why the distance ladder needed its standard-candle rungs. We started out
getting a feel for distances in our own Solar System; now we're crossing the entire Galaxy.

---

## The View from Home

Before we leave on this galactic journey, look up. Every place on the itinerary is already in your night sky, stacked on
top of one another: things a few hundred parsecs away sit in front of things thousands of parsecs farther on, all in the same patch of sky.

{{< nbas-image src="fig-band-labels.webp" fullwidth="true"
caption="The whole Milky Way band, with the center of the Galaxy in the middle. Almost every star you can pick out by eye is local. The glow behind them comes from much farther away. Open clusters (squares) are strung along the band at every distance. The 28 brightest globular clusters (circles), 2-12 kpc away, bunch toward Sagittarius. The part inside the dashed line never rises from New England. The Milky Way's brightness is enhanced for visibility.[^stellarium]"
alt="A panorama of the Milky Way band stretching across a starry sky, with labels. Squares mark open clusters along the band, with distances: h and chi Persei and M 11 at 2,200 parsecs, M 7 at 280, M 6 at 460, and NGC 3532 at 500. Circles mark globular clusters, crowded around the bright, yellowish center. Labels point to dark dust rifts, the hidden Galactic center, and the Large Sagittarius Star Cloud, where the bulge shows through a gap in the dust. At lower right, inside a dashed loop marking the sky that never rises from New England, are the two Magellanic Clouds." >}}

<!-- BOOK: use fig-band-labels-print (no New England loop, Bob 2026-11-06); drop the caption's
     sentence "The part inside the dashed line...".
     NOTES (Bob): might replace the banner as well. M 24 ("a window into an arm") left off the
     figure for now: its only source so far is an observatory web page. -->

### Glow, Not Stars

Nearly every star you can see by eye is basically a neighbor. Of the roughly 5,000 stars brighter than
magnitude 6, half lie within about 100 pc (about 330 ly) and nearly all within 500 pc.
The Milky Way's glow comes from behind them: stars thousands of parsecs away, too faint and too
crowded together to see one at a time.

{{< nbas-image src="fig-naked-eye-distances.webp" fullwidth="true"
caption="How far away are the stars you can see? For the roughly 5,000 stars brighter than magnitude 6 in the HYG catalog, half are within about 100 pc and nearly all within 500. A few distant, very luminous stars make up the long tail."
alt="A chart of the distances to naked-eye stars, showing most of them within a few hundred parsecs, with a thin tail of distant stars beyond 1,000 parsecs." >}}

### Along the Band, and Bunched Toward Sagittarius

Open clusters sit on the band because they live in the disk, and they sit at every distance:
M 7 (in Scorpius) is about 280 pc away; M 11 (in Scutum) is about 2.2 kpc, nearly eight times
farther. In the sky they look like neighbors in the summer constellations.

Globular clusters don't follow the band. They crowd toward Sagittarius, Scorpius and Ophiuchus,
because they swarm around the center of the Galaxy rather than around us. That lopsided
crowding is the clue Harlow Shapley used to find the center (see
[Building the Ladder](/articles/2026/12/building-the-distance-ladder/)). Under dark skies a few
are even visible without optical aid. M 13, in Hercules, is about 7.4 kpc (24,000 light-years) away:
representing the halo, already in your sky.

### Windows in the Dust

Toward the center, the band breaks up into bright clouds and dark lanes. The dark lanes of the
Great Rift are clouds of dust much closer to us than the stars behind them, the same kind of
dark cloud we'll step into later. The bright patches appear where the dust is thinner. The Large
Sagittarius Star Cloud, the brightest part of the whole Milky Way, is a piece of the Galaxy's
bulge seen through one of these gaps, Baade's Window, a hole about 1° wide centered on the
globular cluster NGC 6522.

{{< nbas-image src="m_24-s30-36m.webp" fullwidth="true"
caption="M 24, the Small Sagittarius Star Cloud: a dense field of distant stars seen through a gap in the dust. Seestar S30, 36 min."
alt="A crowded field of thousands of faint stars, broken by a few dark patches of dust." >}}

The center itself is about 8.2 kpc (27,000 light-years) away, a couple of degrees west of that
star cloud. You can _point_ right at it, but you can't _see_ it: about 30 magnitudes of dust lie
in between, which lets through less than one photon in a trillion. In winter you face the other
way, out of the Galaxy and toward the [anticenter](/articles/2026/12/the-view-out-the-back-door-the-galactic-anticenter/).

{{< clear >}}

---

## Home

Home is the yardstick for everything that follows, so it's worth considering what's normal here.

Our neighbors are mostly red dwarfs. Near the Sun there's about one star system for every 12
cubic parsecs,[^reyle2021] so your nearest neighbor is about 1.3 pc away. Only about one neighbor in ten is a
star like the Sun; the rest are dimmer and redder, which is why so few of our nearest neighbors
are visible without a telescope. (The Sun-like ones within 10 pc are listed in
[Parsecs vs. Light-Years](/articles/2026/12/parsecs-vs.-light-years/).) This sky is the one you
know: about 16 stars of first magnitude or brighter, some 5,000 in all visible on a dark night, the band
of the Milky Way, and real darkness between the stars.

And change is almost imperceptible. Our bright neighbors drift past at 15 to 35 km/s on average, so the
constellations reshape themselves only over tens of thousands of years. The Sun itself bobs gently up and down
through the plane of the Galaxy, about 50 to 100 pc to either side, over tens of millions of
years. It's currently about 20 pc above the midplane, heading up.

### We Live in a Bubble

{{< nbas-image src="fig-bubbles.webp" width="450" align="right"
caption="Our Local Bubble and its neighbor, the Per-Tau Shell, seen from above the Galaxy's plane. The Per-Tau Shell is drawn at its measured position and size. The Local Bubble's real shape is irregular, so its outline here is only a sketch. But the two bubbles do touch."
alt="A diagram seen from above. A large dashed circle about 300 parsecs across, the Local Bubble, has the Sun near its middle. To its left, partly overlapping, is a smaller circle 156 parsecs across, the Per-Tau Shell, with the Taurus clouds marked on its edge and the Perseus clouds on its far side. An arrow points toward the Galactic center, and a scale bar shows 100 parsecs." >}}
Even the empty space here has a story. The Sun sits near the middle of the Local Bubble, a
cavity about 300 pc (1,000 light-years) across, blown out by roughly 15 supernovae starting about
14 million years ago.[^zucker2022] The Sun drifted into it about 5 million years ago. The bubble is empty of
gas, not of stars: the gas inside is at least ten times thinner than the Galaxy's average, while
stars are as common here as anywhere nearby. The gas the explosions swept up piled into a shell,
and nearly every star-forming cloud near us sits on its surface.

Bubbles like this are everywhere. The Perseus-Taurus Shell, about 156 pc (500 light-years) across and 6 to
22 million years old, touches ours;[^bialy2021] the Taurus clouds sit where the two meet. Farther off, the
James Webb Space Telescope found 1,694 bubbles in the galaxy M 74 alone,[^watkins2023] from 6 to 552 pc in
radius. Ours is an ordinary size. Our neighborhood isn't special, and that's a finding in
itself. The places we're about to visit are the ones that are comparatively more exotic.

{{< clear >}}

---

## Tourists in Our Midst

But even our ordinary neighborhood gets tourists. Stars from the halo, the thin cloud of old stars
that surrounds the whole Galaxy, follow their own orbits, and those orbits carry some of them
straight through the disk. Roughly one star in 500 near the Sun is a halo visitor,[^bird2026]
enough that the nearest one at any moment is about 10 pc away. Groombridge 1830, in Ursa Major, is
9.2 pc away; Kapteyn's Star, in Pictor, is an unusually close 3.9 pc.

### What Gives Them Away?

Not their looks -- at a quick glance. Groombridge 1830 is a faint yellow star, magnitude 6.4, right at the edge of
what the eye can see on a very dark night. Nothing about it stands out.  Look more carefully, though, and you'll notice two
important differences. The first is its chemistry. Groombridge 1830 has only about 6% of the Sun's share of
elements heavier than helium, the mark of a star born long ago, before stellar evolution had time to produce those
heavier elements. The second is how it moves.

| Star | Constellation | Magnitude | Distance (pc) | Drift across the sky (″/year) | Toward us (−) or away (+), km/s | Speed relative to the Sun, km/s |
|:--|:--|:-:|--:|--:|--:|--:|
| Vega             | Lyra       |  0.0  |  7.7 | 0.35 |  −12 |   18 |
| Altair           | Aquila     |  0.8  |  5.1 | 0.66 |  −26 |   31 |
| Arcturus         | Boötes     | −0.05 | 11.3 | 2.28 |   −5 |  122 |
| Groombridge 1830 | Ursa Major |  6.4  |  9.2 | 7.06 |  −98 |  322 |
| Kapteyn's Star   | Pictor     |  8.8  |  3.9 | 8.64 | +245 |  293 |
| HD 140283        | Libra      |  7.2  | 61.5 | 1.16 | −169 | ~370 |

*Vega and Altair are ordinary neighbors, for comparison. Speeds are our calculations, from Gaia
and HYG positions and motions.[^hyg] HD 140283's radial velocity is from Bond et al.[^bond2013]*

<!-- TABLE CHECKS (Claude):
     - Vega, Altair, Arcturus: HYG v4.1 (pm, dist, rv). Groombridge 1830, Kapteyn's Star: Wikipedia
       infobox (Gaia astrometry; Kapteyn RV 245.05). HD 140283: Gaia pm/parallax via Wikipedia (notes),
       RV −169.0 (Bond et al. 2013). Speeds = sqrt(v_tan² + RV²), our calc.
     - HD 140283: our 377 km/s (Gaia 61.5 pc) vs Bond et al. 361 (58 pc) → "~370".
     - Magnitudes: Kapteyn 8.80–8.85 (variable) → 8.8. Arcturus −0.05 (as in the drift figure). -->

The visitors move ten or more times faster than our ordinary neighbors. But look at HD 140283: it
barely drifts across the sky, yet it's the fastest of all. It's simply farther away. A drift
across the sky only becomes a speed once you know the distance, which is why it took the whole
distance ladder to spot these tourists.

### Going Their Own Way

The stars of the disk, the Sun included, go around the Galaxy mostly in the same direction at
about the same speed. The visitors don't.

Groombridge 1830 goes the right way, but slowly: it lags the Sun by about 160 km/s, on a long,
stretched orbit that plunges it in toward the center and back out again. HD 140283, an easy
binocular star, is stranger still. It's moving fast, about 370 km/s relative to us, but almost
none of that motion carries it _around_ the Galaxy. It falls in toward the center and climbs back
out, and rises and dives through the disk, while drifting slowly around in the wrong direction
(our calculation). Picture a ball thrown almost straight at the center rather than a car on the
ring road. Kapteyn's Star, too far south to observe from New England, is another wrong-way
driver.[^guinan2016]

Their visits are short, by the Galaxy's clock. Groombridge 1830 will cross the 10 pc stretch of
our neighborhood in about 30,000 years, and then it's back out into the halo.

{{< nbas-callout title="The Most Extreme Traveler" >}}

The current record belongs to a star called S5-HVS1.[^koposov2020] About 4.8 million years ago it was half of a pair of
stars that strayed too close to the black hole at the Galaxy's center. The black hole captured
its partner, and flung S5-HVS1 away. We don't know anything about the partner; it's the
leftover star that tells the story. S5-HVS1 is now about 29,000 light-years from us, in the
southern constellation Grus, moving at about 1,700 km/s. It isn't passing through; it's *leaving*.
Nothing in the Galaxy can hold it, and it will never come back.

{{< /nbas-callout >}}
<!-- CHECK (Claude): Koposov et al. 2020 — the Hills mechanism: a binary disrupted by Sgr A*, one star
     captured, the other ejected. (Comment moved outside the callout: the callout re-renders its
     contents as Markdown.) -->

### Arcturus: a Visitor, but Not from the Halo

The halo isn't the only place visitors come from. Arcturus belongs
to the Galaxy's _thick disk_: an older, puffier layer of stars that rise and fall much farther
above and below the plane than the Sun does. One leading explanation is a collision. About ten
billion years ago the young Milky Way swallowed a smaller galaxy, now called Gaia-Enceladus, and
the impact stirred up the disk it had at the time.[^helmi2018] Arcturus goes around the Galaxy the
same way we do, but about 120 km/s slower, and it bobs up and down through the disk as it goes. So
the Sun is overtaking it, and from here it seems to slide past us at 122 km/s.
We see that as a drift across the sky: in about 21,000 years Arcturus will have crossed out of Boötes
into Virgo, as the constellation boundaries are drawn today.

{{< nbas-image src="fig-arcturus-drift.webp" fullwidth="true"
caption="Arcturus's straight-line path over 100,000 years, against the modern constellation boundaries. It crosses from Boötes into Virgo about 21,000 years from now, and it stays about as bright as today the whole time (magnitude −0.05 now; +0.28 fifty thousand years ago, +0.20 fifty thousand years ahead). The gray lines show that other bright stars also drift, just more slowly; the long one in Serpens is γ Serpentis, a fast local. Positions are calculated, not photographed.[^d3celestial]"
alt="A star chart of Boötes, Virgo, and their neighbors, with constellation boundaries. A gold line runs from upper left to lower right, with dots for 50,000 years ago, today, 25,000 years from now, and 50,000 years from now, each labelled with Arcturus's magnitude. An X marks where the line crosses into Virgo, about 21,000 years from now. Short gray lines through the other stars show their own, smaller drifts." >}}

{{< clear >}}

<!-- CHECKS (Claude):
     - Thick disk origin: Helmi et al. 2018 (Nature 563, 85): the Gaia-Enceladus merger (~4:1 mass ratio)
       "must have led to the dynamical heating of the precursor of the Galactic thick disk and therefore
       contributed to the formation of this component approximately 10 Gyr ago." Written as "one leading
       explanation" because other thick-disk formation pictures exist (not sourced here).
     - Do NOT say Arcturus came from Gaia-Enceladus (its group's origin is unresolved; notes).
     - γ Ser caption line: Bob's addition, reworded; "long one in Serpens" — check that it IS the
       longest gray track in Serpens on the chart.
     - "nearly all" (Bob's question about counter-examples): runaway stars exist but no source on
       their orbit directions here; "nearly all" keeps it safe. Runaways → backlog AWV (Bob). -->

---

## Destinations Under Construction

Our first trips are short ones, a few hundred to a couple of thousand parsecs, to places where
stars are still being built: a cloud that hasn't started, a nursery in full swing, and a young
cluster that has just cleared away its gas.

### Inside a Dark Cloud

{{< nbas-image src="b_68-72-s30-78m.webp" width="400" align="right"
caption="Dark clouds against the crowded star fields toward the center of the Galaxy. Barnard 68 is the small, round dark spot at the bottom center; the S-shaped cloud is B 72, the Snake; the other dark spots are its neighbors in the same group. Seestar S30, 78 min."
alt="A dense field of faint stars with several dark, starless patches: an S-shaped dark lane, a few small dark spots, and at the bottom center a small round one, Barnard 68, that looks like a hole in the sky." >}}

Barnard 68, the small round spot at the bottom of the photo, looks like a hole in the sky, and
from inside, it would seem like one.[^alves2001] It's a cloud of cold
gas and dust about 125 pc (410 light-years) away, twice the Sun's mass, only 16 degrees above
absolute zero, and about 12,500 AU in radius. From its center the dust would blot out nearly
everything: no Milky Way, few or none of the stars we know. It's the darkest place on our tour,
and the emptiest. There are no stars inside yet.

But it may not stay that way. B 68 is on the verge of collapse, and if it falls in on itself it
could make a single star something like the Sun. With its neighbors, including the Snake, it may
one day become a small, sparse group of young stars.

<!-- CHECKS (Claude):
     - B68: Alves, Lada & Lada 2001 (Nature 409, 159); ESO eso0102: 2.1 M☉, 16 K, radius 12,500 AU,
       ~125 pc, "marginally stable and on the verge of collapse"; B68 + B69/70/72 may be the precursor
       of a sparse association of low-mass stars.
     - "There are no stars inside yet": B68 is described as starless in our sources (Bob asked about
       HH objects in Bok globules — those belong to globules that already have young stars; I found
       nothing saying B68 has one). "Starless" CONFIRMED: Burkert & Alves 2009 ("The Inevitable Future of the
       Starless Core Barnard 68"), Nielbock et al. 2012 ("prototypical starless core").
     - "From its center the dust would blot out nearly everything": qualitative. B68's dust hides the
       stars behind it from us; from the center you look through half the cloud in every direction.
       Not computed. -->

### The Nursery

{{< nbas-image src="m_16-equ-35m-LP.webp" width="400" align="right"
caption="The Eagle Nebula (M 16), with its young star cluster and, near the center, the Pillars of Creation. Bob Donahue, NBAS, eQuinox 2, 35 min."
alt="A reddish glowing cloud with dark columns of dust rising into its center and a scattering of bright young stars." >}}

The Eagle Nebula, M 16, is about 5,700 light-years (1.7 kpc) away,[^kuhn2019] one spiral arm closer to the center than
we are. It's star formation at full tilt. Its cluster is only a few million years old, and its
brightest stars are hot, blue, and tens of times the Sun's mass. Some stars are still forming
inside the dark columns of dust, the Pillars of Creation; the tallest is 4 to 5 light-years from
base to tip.

Live here and the sky would be ruled by those few blue stars. The brightest, a pair of stars
about 80 times the Sun's mass, would shine many times brighter than Venus from a parsec away
(our calculation). Around them,
glowing gas would fill much of the sky, with the dark pillars and dust lanes cutting across it.

But here's a surprise: the glow wouldn't be any brighter than it looks to us through a
telescope. A glowing cloud has the same brightness per patch of sky whether you're near it or
far away; getting closer only makes it bigger. So from inside, the nebula would be a faint glow
spread across the sky, too dim for the eye to see its red color, and stronger near the brilliant
stars. It's the stars, not the nebula, that would steal the show.

None of it lasts. The light and winds from the young stars that make the cloud glow are also
wearing it away, pillars included. Eventually the gas will be blown clear, and what's left is
our next stop: a young open cluster.

{{< clear >}}

<!-- CHECKS (Claude):
     - Brightest star: HD 168076, an O3.5 V + O7.5 V pair, ~80 M☉, V = 8.24 (Wikipedia, citing Sana et al. 2009).
       Text softened from "magnitude −10" to "many times brighter than Venus": at 1 pc, m = M_V − 5, so any
       M_V brighter than about 0 beats Venus (−4.9 max) — an O3.5 V star is far brighter than that. The exact
       M_V needs the extinction to NGC 6611, which I did not look up.
     - Surface brightness doesn't change with distance (for a resolved, uniform source, ignoring dust):
       standard optics. "Too dim to see its red color": the eye loses color vision at low light — say so
       only if Bob agrees; M16's surface brightness not computed.
     - Bob asked how bright, and what it would do to the rest of the sky: the honest answer is a faint
       veil, not a blaze. Whether it would hide the Milky Way behind it is not established. -->

### Inside an Open Cluster

The stars of a young open cluster were all born at the same time, out of the same cloud, and they
are still close together. In the core of an open cluster, the stars as bright as the Sun or
brighter are packed 100 to 1,100 times more tightly than around us. (We count those because
they're the ones we can count reliably; the faint red dwarfs are much harder to find in a cluster
hundreds of parsecs away.) If a cluster has the same mix of bright and faint stars as our
neighborhood, the faint ones are packed just as tightly, and your nearest neighbor of any kind
would be 0.1 to 0.3 pc away, roughly 25,000 to 60,000 AU, instead of 1.3 pc.

<!-- GALLERY (Bob asked: do we need 7?): trimmed to four, in order of AGE (young → coming apart),
     which is the story the paragraph above tells. The table keeps all seven. Restore M 41, M 35,
     M 37 if wanted (files: m_41-s50-12m.webp, m_35-s50-5m.webp, m_37-s30-8m.webp); if dropped from
     the article entirely, also drop "35", "37", "41" from dso_messier. -->
{{< nbas-gallery style="carousel" size="300px" >}}
m_36-s30-10m.webp   | M 36, 28 million years | Seestar S30, 10 min
m_45-s30-69m.webp   | M 45, 78 million years | Seestar S30, 69 min
m_11-s30-41m.webp   | M 11, 309 million years | Seestar S30, 41 min
m_44-s30-36m.webp   | M 44, 676 million years | Seestar S30, 36 min
{{< /nbas-gallery >}}

So the sky in an open cluster is similar to our home's sky with the cluster stars added. You'd still see the ordinary
background of stars and the band of the Milky Way. But from the middle of the Pleiades you'd add
about 64 stars brighter than first magnitude, where home has 16, and a couple of them would be far
brighter than Venus. Imagine a sky with four times as many bright stars, many of them blue-white.

| Cluster | Age (million years) | Sun-or-brighter stars, × home | Their spacing (pc) | Nearest neighbor of any kind (pc) | Stars brighter than magnitude 1, seen from the center |
|---|---|---|---|---|---|
| Home | — | 1× | 5.7 | 1.3 | 16 |
| M 41 | 170 | ~100× | 1.2 | ~0.3 | ~105 |
| M 45 (Pleiades) | 78 | ~125× | 1.1 | ~0.3 | ~64 |
| M 35 | 148 | ~115× | 1.2 | ~0.3 | ~210 |
| M 44 (Beehive) | 676 | ~115× | 1.2 | ~0.3 | ~75 |
| M 37 | 447 | ~400× | 0.8 | ~0.2 | ~480 |
| M 36 | 28 | ~900× | 0.6 | ~0.14 | ~145 |
| M 11 | 309 | ~1,100× | 0.5 | ~0.13 | ~750 |

*Our calculations, from Gaia cluster members[^cantatgaudin2020] inside the radius that holds half
of each cluster's members. "Nearest neighbor of any kind" assumes each cluster has the same mix of
bright and faint stars as our neighborhood. Counts are lower limits: the brightest few members of
every cluster but the Pleiades may be missing from the lists.*

<!-- TABLE CHECKS (Claude):
     - Pleiades spacing 1.1 pc is SCALED from the corrected count (58 → 65); the notes give 1.2 for the
       uncorrected 58. Keep 1.1 or round back to 1.2 — Bob's call.
     - "many of them blue-white": the Pleiades' bright members are B stars (Seven Sisters); true for the
       Pleiades, not checked for every cluster in the table.
     - NEW column (Bob's question): nearest neighbor of any kind = 1.3 pc / (× home)^(1/3), our calc,
       ASSUMING the cluster's mass function matches the field near the Sun. Older clusters lose faint
       stars preferentially (mass segregation + evaporation; not sourced here), so for M 44 the real
       spacing of faint stars may be larger. 0.13 pc = 26,800 AU; 0.28 pc = 57,800 AU. -->

The Pleiades has nebulosity too, but a different kind from M 16's. The Eagle's gas glows with its
own light, energized by its hot young stars. The Pleiades' blue haze is dust, reflecting the
light of the stars. And it isn't left over from the cluster's birth. The
cluster just happens to be passing through an unrelated cloud of interstellar dust, at about
11 km/s.[^nasa2000] From inside, the same rule holds as in M 16: the haze would be no brighter per patch
than it looks from here, a faint glow gathered around the brightest stars, not a blue sky.

Open clusters don't last. M 36 is 28 million years old; M 44, the Beehive, is 676 million and
coming apart. The Galaxy's pull slowly strips members away, one at a time. Eventually the cluster is gone, and
its stars become ordinary field stars, like our neighbors. The Sun probably started out in a cluster
like these, but its birth siblings scattered long ago.[^adams2010]
<!-- CHECK (Claude): "Sun born in a cluster" — Bob's addition. Mainstream view (e.g. Adams 2010, "The Birth
     Environment of the Solar System", Annual Review of Astronomy & Astrophysics 48, 47 — citation from memory,
     verify on ADS). Footnote it if kept. -->

{{< clear >}}

<!-- CHECKS (Claude):
     - Pleiades dust: NASA/Hubble IC 349 release (2000): unrelated cloud, relative speed ~11 km/s. Bob's
       note: describe the CLUSTER passing through the cloud — done.
     - "No brighter per patch than from here": surface-brightness invariance (as M 16). IC 349, the
       brightest patch, ~18.5 V mag/arcsec² (NASA); a full calculation of the haze from the center was
       never done (notes) — keep it qualitative.
     - Emission vs reflection: standard. -->

---

## The Halo

Now let's leave the disk altogether, and check out the place our tourists come from. We'll stop
in the halo about 16 kpc from the center: 11 kpc out from the center along the plane of the
Galaxy, a little beyond the Sun's distance, and 12 kpc above it.

This is the emptiest place on the tour. Halo stars are old and short on heavy elements, and
there are no young, hot blue stars at all. Most are dim dwarfs. Near the Sun, halo stars are
about 18 pc apart, but the halo has no single density. It thins out steadily the farther you go
from the center, and it's squashed: it thins out faster going up than going out along the
plane.[^juric2008] At our stop, halo stars are about 45 pc apart, and your nearest neighbor is
about 25 pc (80 light-years) away (our extrapolation). Most of them are dimmer than the Sun, and
even a star like the Sun would be too faint to see by eye from there. Turn away from the Galaxy
and the sky is almost black, with only a handful of stars, nearly all of them rare giants.

Where you stop in the halo matters. Drop to 5 kpc above the Sun and the halo is about seven times more
crowded: neighbors about 24 pc apart, and a Sun-like nearest neighbor would be a faint naked-eye
star. Go out past about 25 kpc and the halo empties much faster than before.[^deason2011]

That change of pace has a cause. Many of the halo's stars are wreckage from Gaia-Enceladus, the
galaxy the Milky Way swallowed ten billion years ago. Their long, plunging orbits all turn around
at about the same distance from the center, so the stars pile up there, and beyond it the halo
thins out fast.[^deason2018] The same collision puffed up the thick disk that Arcturus belongs to.
The halo's shape, its edge, and the thick disk are all scars of one event.

There's no wall between the halo and the disk, either. At the Sun's distance from the center,
halo stars start to outnumber disk stars about 3.3 kpc above the plane (our calculation, from
the measurements of Jurić and colleagues). Below that, the thick disk takes over gradually. You
tell the two apart not by where they are, but by how they move and what they're made of: disk
stars circle the Galaxy together, while halo stars go every which way and are short on heavy
elements, just like our tourists.

{{< nbas-image src="fig-view-from-halo.webp" fullwidth="true"
caption="Our Galaxy from the halo, 16 kpc from the center and 12 kpc above the disk. The dashed ring is the Sun's orbit. This is one of a set of views of the Galaxy from stops on our tour, all made from the same model and on the same brightness scale; they are not photographs."
alt="A huge spiral galaxy seen at a slant from above against a black sky, filling most of the view: a bright, elongated center, pale spiral arms winding outward, and the nearest part of the disk running off the bottom of the frame. A dashed gold oval marks the Sun's orbit, with the Sun's position labelled at its lower left." >}}

Now turn around and look in. The Galaxy fills half your sky, about 90° from edge to edge. It's
like looking down from a mountaintop: the part of the disk nearest you, below, shows its spiral arms
in detail, and farther off it all blends into the larger spiral, until everything runs
together in the glow of the bulge. Every star we've ever seen by eye is in there, in one small
patch of the disk.

And the halo hardly changes. Nothing new is being built here, and there's so much room between
stars that nothing ever runs into anything. Even when a halo star dives through the crowded disk,
as Groombridge 1830 is doing, it never encounters another star; it feels the disk only as a
smooth pull. It's just "passing through".

<!-- CHECKS (Claude):
     - Stop = Bob's: xyz (9.53, −5.50, 12.0) kpc; 16.3 kpc from the GC; 13.3 kpc from the Sun.
     - Halo numbers (our calc): Bird et al. local halo density 1.7e-4 /pc³ × Jurić et al. 2008 flattened
       profile (c/a = 0.64, r^−2.8); nearest neighbor = 0.554 × spacing. Stop: effective radius 21.7 kpc →
       spacing 45 pc, nearest 25 pc (Sun-like V ≈ 6.8). 5 kpc above the Sun: 24 pc, 14 pc (V ≈ 5.5).
       "About seven times more crowded": (45/24)³ = 6.6.
     - Break: ~25 kpc (review arXiv 1602.07702: 25 ± 10 kpc; Deason et al. 2011: ~27 kpc).
     - Pile-up cause: Deason et al. 2013 (break ↔ one early massive accretion) and Deason et al. 2018
       (apocenter pile-up of the "Sausage" = Gaia-Enceladus stars). Thick disk: Helmi et al. 2018.
     - Halo/disk crossover 3.3 kpc: our calc with Jurić's thin 300 pc / thick 900 pc / 12% / halo 0.5%.
     - "about 90° from edge to edge": disk to 15 kpc spans ~93° from this stop (our calc).
     - Text now says "spiral arms" (not "arms and dust") to match the render, whose dust is smooth.
     - NGC 891 image dropped (Bob: why is it here?). Also removed from dso_ngc / dso_caldwell. -->

{{< clear >}}

---

## A Globular Cluster

From the emptiest place in the Galaxy to one of the most crowded. The globular clusters swarm
around the center, mostly well above or below the disk. M 13 holds about
half a million Suns' worth of stars, half of them inside a ball only about 10 pc
across.[^baumgardt2018] Their residents are old, short on heavy elements like the halo's stars,
but packed together.

### A Sky That Never Gets Dark

{{< nbas-gallery style="carousel" size="300px" >}}
ngc_5466-s50-26m.webp | NGC 5466 | Seestar S50, 26 min
m_71-equ-19m.webp     | M 71     | eQuinox 2, 19 min
m_13-s30-40m.webp     | M 13     | Seestar S30, 40 min
m_3-s30-60m.webp      | M 3      | Seestar S30, 60 min
m_92-equ-16m.webp     | M 92     | eQuinox 2, 16 min
m_15-s30-33m.webp     | M 15     | Seestar S30, 33 min
{{< /nbas-gallery >}}

At the center of M 13 your nearest neighbor would be roughly 7,000 AU away. A star like the Sun
at that distance would outshine Venus, and you'd have many neighbors like that. Add up all the
starlight and the sky at the center of M 13 would be about 80 times brighter than our darkest
skies; at the center of M 15, several hundred times brighter (our calculation, from the
clusters' measured brightness[^harris1996]). There would be no real night. But not every globular is
like that: the center of a looser globular cluster like NGC 5466 would be about as dark as home.

{{< article-table align="right" >}}
| Cluster | Center vs. home | Nearest neighbor at the center |
|---|---|---|
| Home (Sun) | 1× | ~1.3 pc (~260,000 AU) |
| NGC 5466 | ~200× | ~46,000 AU |
| M 71 | ~12,000× | ~11,000 AU |
| M 13 | ~50,000× | ~7,000 AU |
| M 3 | ~140,000× | ~5,000 AU |
| M 92 | ~50 million× | ~700 AU |
| M 15 | ~100 million× | ~550 AU (~3 light-days) |
{{< /article-table >}}
<!-- TABLE NOTES: central mass density from Baumgardt et al. catalogue v4 (log rho_c) vs ~0.043 Msun/pc3
     near the Sun (McKee et al. 2015, footnote); nearest neighbor scaled from home's 1.3 pc ASSUMING the
     same average mass per star — mass segregation puts heavier stars and remnants in cores, so real core
     spacings are somewhat larger. Say "roughly". The table's density basis is in the mckee2015 footnote. -->

### No Room for Comets

Here's where a globular really stops being like home. At the very center of M 15 your nearest
neighbor would be roughly 550 AU away: about 3 light-*days*. That's closer than Sedna, the distant
dwarf planet, gets from the Sun at the far end of its orbit, 937 AU. Our Sun is wrapped in a cloud
of comets, the Oort cloud, that reaches out tens of thousands of AU. No star in a globular core
could keep one. Even in M 13, the neighbors live inside that range.

Planets may have a hard time too. When the Hubble Space Telescope watched about 34,000 stars in
the globular cluster 47 Tucanae for eight days in 1999, astronomers expected to catch about 17
giant planets passing in front of their stars. They found none.[^gilliland2000] That could be
because these old stars had too little of the heavy elements that planets are made of, or
because passing neighbors pulled their planets away, or both; a later look using what Kepler
taught us about planets concluded more sensitive searches are still needed.[^masuda2017] Either
way, a planet in a globular core lives in a very different neighborhood from ours.

### The Galaxy from the Front Yard

What you'd see of the Milky Way depends on where your cluster sits. From M 13, about 5 kpc
above the disk, the Galaxy spreads across the whole lower half of the sky, its near side so close
that it swells and runs off past the horizon. Nobody draws a galaxy that way, because nobody has
seen one from its own galactic front yard: it's the difference between the view from a hilltop and the
view from an airplane.

{{< nbas-image src="fig-view-from-m13.webp" fullwidth="true"
caption="Our Galaxy from M 13, 5 kpc above the disk, looking toward the center. The dashed arc is the Sun's orbit; the Sun itself is behind us, out of the frame. Same model and brightness scale as the other views."
alt="A black sky above a vast, glowing spiral disk that fills the lower half of the view like a landscape seen from a hill. The bright, elongated center sits just below the middle, spiral arms sweep out to both sides and run past the edges, and a dashed gold arc, the Sun's orbit, curves across the disk." >}}

From NGC 5466, three times farther out, it's a smaller spiral hanging in a dark sky, and our own
neighborhood is out in its dim outskirts. From NGC 288, almost straight below the Sun, our
neighborhood would be overhead. Some of these views look strange, even wrong. That strangeness is
real: it's what our Galaxy looks like from there.

{{< clear >}}

<!-- CHECKS (Claude):
     - fig-view-from-m13: M 13 at (l 59.01, b 40.91, d 7.42 kpc, Baumgardt) → xyz (5.29, 4.81, 4.88) kpc.
       View centered 16° ABOVE the direction to the GC (PITCH −16) so the sky shows above the disk.
     - Sky brightness: our calc (sky ≈ central surface brightness + 0.75 mag; Harris mu_V; A_V = 3.1 E(B−V)).
       Dark-sky reference 22.0 V mag/arcsec² VERIFIED (astropix: "widely accepted value"; ING La Palma 21.9).
       Harris mu_V dereddening: still not confirmed either way. M15 is ~870× (A_V removed) or ~650× (if Harris
       already dereddened) → text now says "several hundred times", true either way. M13 ~80×, NGC 5466 ~0.7×.
     - Sedna aphelion 937 AU (Wikipedia, JPL-based). Oort cloud ~50,000–100,000 AU (EBSCO); text says
       "tens of thousands of AU". Not footnoted (encyclopedic) — add if Bob wants.
     - 47 Tuc: Gilliland et al. 2000; Masuda & Winn 2017. The stars watched were ~1′ from the core.
     - "Among the oldest things": globulars as old populations (NGC 6522 papers). "but very slowly": no source.
     - The 4-panel fig-globular-vista is retired (Bob, 2026-11-07). NGC 5466 and NGC 288 keep their prose
       lines without a figure. -->

---

## The Inner Galaxy

The last stop is the inner Galaxy, about 1 kpc from the center, in the bar and bulge. It's
crowded in every direction.  Averaged over the whole bar, there's about
ten times as much mass in stars per cubic parsec as around the Sun (our calculation[^portail2015]),
and it gets denser toward the middle.

{{< nbas-image src="ngc_6522-s50-17m.webp" width="400" align="right"
caption="NGC 6522, an ancient globular cluster about 1 kpc from the center of the Galaxy, seen through Baade's Window. Its center is roughly a million times denser than our neighborhood. Seestar S50, 17 min."
alt="A compact globular cluster in a field crowded with faint stars." >}}
<!-- CHECK: filename as given (ngc_6522-50-17m.jpg — "s50" missing?). Numbers: R_GC 1.04 kpc and
     log rho_c 4.62 (Baumgardt v4) → ~970,000× home. -->

Our base is NGC 6522, the globular cluster at the center of Baade's Window. It isn't a tourist
passing through; it's one of the oldest residents. Most globulars swing far out into the halo
and back, but NGC 6522's orbit is small: it never leaves the inner Galaxy, and it moves along with
the rotating bar. It formed here, not in a swallowed galaxy.[^barbuy2021] Its stars are 12 to 14
billion years old, older than the bar itself.[^kerber2018]

### A Sky Turned Inside Out

At home, the Milky Way is a bright band across a dark sky. Here it's the other way around. The
bulge's stars light up the sky almost everywhere, above and below you. There's no dark sky to set
a band against: the whole sky _is_ the Milky Way.

### The Center: Where Time Runs Fast

Everywhere else on this tour, the sky holds still. Stars take millions of years to go around the
Galaxy, and a lifetime of watching shows almost nothing moving. At the very center, that changes.
The center holds a black hole about four million times the Sun's mass, and the stars closest to
it orbit in years. The star S2 goes around it once every 16 years, swinging within 120 AU at
7,650 km/s.[^gravity2018] A local there could watch the brightest stars in the sky visibly move,
and even watch one complete its orbit, in a single lifetime, much like we follow the motion of the
planets in our own sky. (S2's orbit, drawn to scale beside Sedna's, is in
[Distance at Galactic Scale](/articles/2027/01/distance-at-galactic-scale/).)

Could anyone live here? Planets aren't missing from the inner Galaxy: microlensing surveys, which
can find planets thousands of parsecs away, find cold planets toward the bulge about as often as
nearer home.[^koshimoto2021] Life might have a harder time. Closer to the center there are more
exploding stars, and one well-known estimate put the best place for complex life in a ring about
7 to 9 kpc from the center.[^lineweaver2004] The Sun sits inside that ring. Home may be
ordinary, but it's also in a good spot.

{{< clear >}}

<!-- CHECKS (Claude):
     - Bar density: Portail et al. 2015 box average 0.42–0.54 M☉/pc³ (our calc) vs 0.043 near the Sun →
       ~10–12×. Box average, not the value at 1 kpc.
     - NGC 6522 orbit (Bob asked): Barbuy et al. 2021 — bulge member (99.8%); orbits computed by
       Pérez-Villegas et al. 2020 stay in the bar region and mostly follow the bar's shape; inner-bulge
       clusters have lower space velocities than halo clusters (Rossi et al. 2015, quoted there); formed in
       the main bulge, not Gaia-Enceladus (Massari et al. 2019). "Most globulars swing far out into the
       halo": general; no single source here — soften to "Many" if Bob wants.
     - "A Sky Turned Inside Out" SOFTENED: v12's "the dust would cut a dark band; the Milky Way would be
       the dark stripe" is DROPPED. I rendered the view from NGC 6522 with its own brightness scale: the model
       shows a sky bright almost everywhere, brightest toward the center, but no clear dark stripe (the
       model's dust is smooth, so it can't settle the question either way). No model figure for this stop:
       on the shared scale it is pure white, and on its own scale it's a featureless gradient.
     - S2: GRAVITY 2018 (A&A 615, L15). Linked to C08 (/articles/2027/01/distance-at-galactic-scale/, URL from Bob),
       which has fig-s2-orbit (S2 vs Sedna to scale).
     - GHZ callout → paragraph (Bob). Penny et al. 2016 ("fewer planets?") dropped for brevity; restore as
       a clause if wanted. Koshimoto: "no large dependence"; doesn't fully rule out rarity. -->

---

## Beyond the Border

{{< nbas-image src="fig-view-from-lmc.webp" width="400" align="right"
caption="Our Galaxy from the Large Magellanic Cloud, about 50 kpc away: a tilted spiral roughly 30° across, three fists at arm's length, seen from below the plane. The circle marks the Sun's neighborhood. Same model and brightness scale as the other views."
alt="A spiral galaxy, tilted, glowing against a black sky: a bright center with arms winding around it. A small gold circle partway out in the disk is labelled as the Sun's location. A scale bar shows 10 degrees." >}}

Some of our tourists came from farther than the halo. Many of the halo stars near the Sun are
the wreckage of Gaia-Enceladus, the galaxy the Milky Way swallowed about ten billion years
ago.[^helmi2018] And more are on the way. The Large Magellanic Cloud, our biggest satellite
galaxy, is expected to fall in and merge with the Milky Way in about 2½ billion
years,[^cautun2019] bringing a whole new crowd of foreign stars. Andromeda may join us after that;
we covered that in [The Andromeda Family of Galaxies](/articles/2026/09/the-andromeda-family-of-galaxies/).
Even then, the stars themselves won't collide. There's too much room between them.

From the LMC, our Galaxy would look like this: a large spiral, much like the ones we photograph.
Is it a typical one? We've now seen how much one galaxy can hold, from dark clouds to clusters with
no night. To know whether it's ordinary, we have to go abroad, to the other galaxies. And that
means asking whether the distance ladder we've built will reach that far.

{{< clear >}}

<!-- CHECKS (Claude):
     - fig-view-from-lmc re-plotted on the set's shared scale (white point 5× Home reference, was 2×);
       the render itself is unchanged.
     - Gaia-Enceladus: Helmi et al. 2018. LMC: Cautun et al. 2019 (~2.4 Gyr). Don't name our tourists as
       G-E members. -->

### Footnotes

[^stellarium]: This article made use of the Stellarium planetarium (stellarium.org), v26.2 (2026), doi:10.5281/zenodo.23020615. Zotti, G., Hoffmann, S. M., Wolf, A., Chéreau, F., & Chéreau, G. (2021). The Simulated Sky: Stellarium for Cultural Astronomy Research. *Journal of Skyscape Archaeology*, 6(2), 221–258. https://doi.org/10.1558/jsa.17822

[^d3celestial]: Constellation boundaries from d3-celestial, © 2015 Olaf Frohn, BSD 3-Clause License (github.com/ofrohn/d3-celestial).

[^reyle2021]: Reylé, C., et al. (2021). The 10 parsec sample in the Gaia era. *Astronomy & Astrophysics*, 650, A201. doi:10.1051/0004-6361/202140985

[^zucker2022]: Zucker, C., et al. (2022). Star formation near the Sun is driven by expansion of the Local Bubble. *Nature*, 601, 334–337. doi:10.1038/s41586-021-04286-5

[^bialy2021]: Bialy, S., et al. (2021). The Per-Tau Shell: A Giant Star-forming Spherical Shell Revealed by 3D Dust Observations. *The Astrophysical Journal Letters*, 919, L5. doi:10.3847/2041-8213/ac1f95

[^watkins2023]: Watkins, E. J., et al. (2023). PHANGS–JWST First Results: A Statistical View on Bubble Evolution in NGC 628. *The Astrophysical Journal Letters*, 944, L24. doi:10.3847/2041-8213/aca6e4. (NGC 628 is M 74.)

[^bird2026]: Bird, S. A., Flynn, C., Sekhri, R., et al. (2026). Galactic Stellar Halo Luminosity Function. arXiv:2603.11354. Local density of halo stars: 1.7 × 10⁻⁴ per cubic parsec; disk-to-halo ratio 480:1.

[^hyg]: Positions, distances and motions for Vega, Altair and Arcturus from the HYG database, v4.1 (astronexus.com). Groombridge 1830, Kapteyn's Star and HD 140283 from Gaia astrometry as listed on their Wikipedia pages.

[^bond2013]: Bond, H. E., et al. (2013). HD 140283: A Star in the Solar Neighborhood that Formed Shortly after the Big Bang. *The Astrophysical Journal Letters*, 765, L12. arXiv:1302.3180

[^guinan2016]: Guinan, E. F., Engle, S. G., & Durbin, A. (2016). Living with a Red Dwarf: Rotation and X-Ray and Ultraviolet Properties of the Halo Population Kapteyn's Star. *The Astrophysical Journal*, 821, 81. doi:10.3847/0004-637X/821/2/81

[^koposov2020]: Koposov, S. E., et al. (2020). Discovery of a nearby 1700 km/s star ejected from the Milky Way by Sgr A*. *Monthly Notices of the Royal Astronomical Society*, 491, 2465–2480. doi:10.1093/mnras/stz3081

[^helmi2018]: Helmi, A., Babusiaux, C., Koppelman, H. H., Massari, D., Veljanoski, J., & Brown, A. G. A. (2018). The merger that led to the formation of the Milky Way's inner stellar halo and thick disk. *Nature*, 563, 85–88. doi:10.1038/s41586-018-0625-x

[^alves2001]: Alves, J. F., Lada, C. J., & Lada, E. A. (2001). Internal structure of a cold dark molecular cloud inferred from the extinction of background starlight. *Nature*, 409, 159–161. See also ESO press release eso0102, and Burkert, A., & Alves, J. (2009), The Inevitable Future of the Starless Core Barnard 68, *The Astrophysical Journal*, 695, 1308.

[^cantatgaudin2020]: Cantat-Gaudin, T., et al. (2020). Painting a portrait of the Galactic disc with its stellar clusters. *Astronomy & Astrophysics*, 640, A1. doi:10.1051/0004-6361/202038192

[^nasa2000]: NASA / Space Telescope Science Institute (2000). Hubble image of IC 349, a cloud of interstellar dust passing through the Pleiades.

[^juric2008]: Jurić, M., et al. (2008). The Milky Way Tomography with SDSS. I. Stellar Number Density Distribution. *The Astrophysical Journal*, 673, 864–914. doi:10.1086/523619. The halo is squashed (axis ratio 0.64) and its density falls off as distance^−2.8. Our halo spacings combine this with the local density from Bird et al.

[^deason2011]: Deason, A. J., Belokurov, V., & Evans, N. W. (2011). The Milky Way stellar halo out to 40 kpc: squashed, broken but smooth. *Monthly Notices of the Royal Astronomical Society*. arXiv:1104.3220. Break at about 27 kpc; other studies put it between about 15 and 35 kpc.

[^deason2018]: Deason, A. J., et al. (2018). Apocenter Pile-Up: Origin of the Stellar Halo Density Break. *The Astrophysical Journal Letters*. arXiv:1805.10288. See also Deason, A. J., et al. (2013), Broken and unbroken: the Milky Way and M31 stellar haloes, arXiv:1210.4929.

[^baumgardt2018]: Baumgardt, H., & Hilker, M. (2018). A catalogue of masses, structural parameters, and velocity dispersion profiles of 112 Milky Way globular clusters. *Monthly Notices of the Royal Astronomical Society*, 478, 1520–1557. doi:10.1093/mnras/sty1057. We used the online catalogue, version 4 (2023): people.smp.uq.edu.au/HolgerBaumgardt/globular/. Central densities are compared with 0.043 solar masses per cubic parsec near the Sun (McKee, C. F., Parravano, A., & Hollenbach, D. J. 2015, Stars, Gas, and Dark Matter in the Solar Neighborhood, *The Astrophysical Journal*, 814, 13).

[^harris1996]: Harris, W. E. (1996, 2010 edition). A Catalog of Parameters for Globular Clusters in the Milky Way. *The Astronomical Journal*, 112, 1487. Central surface brightnesses from the 2010 edition.

[^gilliland2000]: Gilliland, R. L., et al. (2000). A Lack of Planets in 47 Tucanae from a Hubble Space Telescope Search. *The Astrophysical Journal Letters*, 545, L47–L51. doi:10.1086/317334

[^masuda2017]: Masuda, K., & Winn, J. N. (2017). Reassessment of the Null Result of the HST Search for Planets in 47 Tucanae. arXiv:1703.06136

[^portail2015]: Portail, M., Wegg, C., Gerhard, O., & Martinez-Valpuesta, I. (2015). Made-to-measure models of the Galactic box/peanut bulge: stellar and total mass in the bulge region. *Monthly Notices of the Royal Astronomical Society*, 448, 713–731. doi:10.1093/mnras/stv058. Bar mass 1.25–1.6 × 10¹⁰ solar masses; we averaged it over their model's volume.

[^barbuy2021]: Barbuy, B., et al. (2021). UVES analysis of red giants in the bulge globular cluster NGC 6522. *Astronomy & Astrophysics*, 654, A29. doi:10.1051/0004-6361/202140815. Summarizes the orbit calculations of Pérez-Villegas et al. (2020) and the origin study of Massari et al. (2019).

[^kerber2018]: Kerber, L. O., et al. (2018). Ages of the Bulge Globular Clusters NGC 6522 and NGC 6626 (M28) from HST Proper-motion-cleaned Color-Magnitude Diagrams. *The Astrophysical Journal*. doi:10.3847/1538-4357/aaa3fc

[^gravity2018]: GRAVITY Collaboration (2018). Detection of the gravitational redshift in the orbit of the star S2 near the Galactic centre massive black hole. *Astronomy & Astrophysics*, 615, L15.

[^koshimoto2021]: Koshimoto, N., Bennett, D. P., Suzuki, D., & Bond, I. A. (2021). No Large Dependence of Planet Frequency on Galactocentric Distance. *The Astrophysical Journal Letters*, 918, L8. doi:10.3847/2041-8213/ac17ec. An earlier study suggested the bulge might have fewer planets: Penny, M. T., et al. (2016), *The Astrophysical Journal*, 830, 150.

[^lineweaver2004]: Lineweaver, C. H., Fenner, Y., & Gibson, B. K. (2004). The Galactic Habitable Zone and the Age Distribution of Complex Life in the Milky Way. *Science*, 303, 59–62. arXiv:astro-ph/0401024

[^kuhn2019]: Kuhn, M. A., et al. (2019). Kinematics in Young Star Clusters and Associations with Gaia DR2. *The Astrophysical Journal*, 870, 32. Distance 1,740 ± 130 pc. Older sources give about 7,000 light-years.

[^adams2010]: Adams, F. C. (2010). The Birth Environment of the Solar System. *Annual Review of Astronomy and Astrophysics*, 48, 47–85. doi:10.1146/annurev-astro-081309-130830

[^cautun2019]: Cautun, M., et al. (2019). The aftermath of the Great Collision between our Galaxy and the Large Magellanic Cloud. *Monthly Notices of the Royal Astronomical Society*, 483, 2185–2196. doi:10.1093/mnras/sty3084

<!-- FOOTNOTE CHECKS (Claude, 2026-11-07 pass):
     - VERIFIED this pass (title, volume, pages or DOI): reyle2021, zucker2022, bialy2021, watkins2023, bird2026,
       guinan2016, koposov2020, cantatgaudin2020, mckee2015 (in baumgardt2018), portail2015, cautun2019,
       adams2010, kuhn2019, Burkert & Alves 2009 (in alves2001). Earlier: helmi2018, juric2008, deason2011/2013/2018,
       barbuy2021, kerber2018, gilliland2000, masuda2017, koshimoto2021.
     - NOT re-checked (from memory): bond2013 (title/volume), alves2001 (title), gravity2018 (title),
       lineweaver2004 (title), baumgardt2018 (title), harris1996 (AJ 112, 1487 — confirmed by the catalog's
       own readme; title not re-checked). Check on ADS: https://ui.adsabs.harvard.edu
     - nasa2000: add the release number/URL (hubblesite.org) — not looked up.
     - helmi2018 is referenced twice (Arcturus section and Beyond the Border): check the site renders it. -->
