---
title: "The Local Group: A Distance That Changed the Universe"
date: 2027-01-25
description: "In 1923 one faint variable star in Andromeda settled whether the spiral nebulae were other galaxies. How we measure the distances to our nearest galactic neighbors, how far the old rungs of the distance ladder reach, and what those distances reveal about the Local Group."
byline: "One star in Andromeda, and the neighborhood it revealed"
authors: ["bob-donahue"]
series: ["astronomical-frameworks"]
tags: ["Local Group"]
thumbnail: "thumbnail.webp"
banner: "banner.webp"
miniseries: "measuring-astronomical-distances"
miniseries-sequence: 10

dso_messier: ["31", "32", "33", "110"]
dso_ngc: ["147", "185", "6822"]
dso_caldwell: ["17", "18", "51", "57"]
dso_other: ["IC 10", "IC 1613", "Leo I", "LMC", "SMC", "WLM"]

---
<!-- v21 FINAL (2026-11-11): Bob's final read (v20) + Claude's final editorial pass. Every remaining item is marked OPEN or BOOK. Nothing else is pending. Ledger (what's in, out, waiting): claude/local-group-ledger.md. -->

## Introduction
{{< nbas-image src="banner.webp" fullwidth="true"
caption="M 31, M 32, and M 110 -- Bob Donahue, NBAS, Seestar S50, 82 min" alt="The Andromeda Galaxy with its companions M 32 and M 110" >}}

A hundred years ago, nobody knew what the Andromeda "nebula" actually was. It might have been a
cloud of gas and young stars inside our own Milky Way. It might have been a whole other
Milky Way, seen from very far away. Good astronomers argued both sides.

What settled it wasn't winning an argument. It was a distance -- one number, measured from one faint star. 
Once that number was in hand, the universe was a different place: no longer one galaxy with some
fuzzy clouds in it, but a universe full of galaxies, with the Milky Way just one among them.

This chapter doesn't add any new rungs to the ladder. Everything here uses the rungs we've already built -- 
Cepheids and RR Lyrae, from [Building the Distance Ladder](/articles/2026/12/building-the-distance-ladder/) -- 
stretched outward to the nearest galaxies. What's new is what those distances *revealed*: 
that the nearest galaxies form a family of their own, how that family is held together, and how much mass it contains.

---

## The Question

{{< article-table align="right" >}}

| | Shapley | Curtis |
|---|---|---|
| Milky Way's size | ~300,000 ly | ~30,000 ly |
| The Sun | far from the center | near the center |
| Spiral nebulae | not galaxies like ours | galaxies like ours |

{{< /article-table >}}

On the evening of April 26, 1920, at the National Academy of Sciences in Washington, Harlow
Shapley and Heber Curtis gave back-to-back talks on "the scale of the universe." History calls
it the Great Debate, though it was really two lectures, each about forty minutes, and no
transcript survives. Shapley argued for a huge Milky Way -- about 300,000 light-years across,
with the Sun far from its center. Curtis argued for a smaller Galaxy, with the spiral nebulae
as separate "island universes," galaxies in their own right.

Each was partly right. Shapley was right about the Sun's off-center position; Curtis was right
about the spirals. But that's all hindsight. In 1920, the honest answer was that nobody could
measure the distance to a spiral nebula, and every argument made about their nature rested on 
an assumption about how bright something *really* was. In the language of this series: they 
needed a rung, and the only candidates were shaky ones.

### Three clues

Three pieces of evidence bore on the question, and each one implied a distance scale.

{{< nbas-image src="c_12-equ-39m.webp" width="300" align="right"
caption="NGC 6946/C 12 -- the Fireworks Galaxy. Bob Donahue, NBAS, eQuinox 2, 39 min" alt="A face-on spiral galaxy with loose, knotty arms, seen through a field of Milky Way stars." >}}

**Faint novae.** The most promising candidate was the nova. In 1917, George Ritchey caught a "new star" flaring
in the spiral NGC 6946 (the "[Fireworks Galaxy](/articles/2026/07/ngc-6946-the-fireworks-galaxy/)"),
and a search of old photographic plates turned up more of them in other
spirals -- eleven by the end of that year. The novae in the spirals were *faint*, far fainter
than the novae seen in our own Galaxy. If they were the same kind of event, the spirals had to
be very far away.


{{< nbas-image src="fig-s-and-light-curve.webp" width="500" align="right"
caption="S Andromedae as observers saw it in 1885 and 1886: one point per night, averaged over all the observers and corrected for each one's habits, from August until it faded out of reach in January. At its peak it was near the naked-eye limit -- about eleven magnitudes, or 25,000 times, brighter than an ordinary nova in Andromeda. Data: de Vaucouleurs & Corwin (1985), Tables 1 and 4."
alt="Graph of magnitude against days after the August 1885 peak: about 90 gold dots fall steadily from magnitude 7 to magnitude 14 over five months, with a few open circles near magnitude 6 for the earliest reports, an arrow marking that nothing was seen on August 16, and a blue dashed line near magnitude 17 for an ordinary nova in Andromeda." >}}
<!-- Data transcribed from the ADS scan of de Vaucouleurs & Corwin 1985 (Table 4 <Vc>; Table 1 early
     reports, with the published erratum applied). Observations are facts; the plot is ours. -->
**S Andromedae.** Another observation pointed in the other direction. In August 1885, 
what was thought to be another "nova" had appeared near the center of the Andromeda nebula itself, 
bright enough to approach naked-eye visibility at its peak (magnitude 5.85). 
It was named S Andromedae. If Andromeda were a distant galaxy, that one
star would have had to be impossibly luminous -- Shapley put its absolute magnitude near −16
and called that out of the question. Curtis could only suggest that S Andromedae was an outlier,
perhaps a different kind of nova altogether.

**Spinning spirals.** A third line of evidence seemed to settle things for the "nearby" side. 
Adriaan van Maanen at Mount Wilson reported that he could see spiral nebulae *rotating* on plates 
taken a few years apart. If they were as large as galaxies, their outer parts would have to be 
moving faster than the speed of light. Shapley trusted the measurements; van Maanen was a respected 
colleague and a friend.

| Evidence | Pointed toward | What became of it |
|---|---|---|
| Faint novae in spirals (1917) | Spirals are far away | Correct: they were ordinary novae, seen at great distance |
| S Andromedae (1885) | Andromeda is nearby | It was a *supernova* -- a different, far brighter kind of explosion |
| Van Maanen's "rotating" spirals | Spirals are small and nearby | Measurement error; Hubble's remeasurement (1935) found no rotation |

<!-- BOOK: footnote on Ritchey vs Curtis credit for the first M 31 novae (sources disagree; prose avoids assigning it). -->

So the evidence split, and each side could explain away the other's best case. What the
question needed was a distance that didn't depend on assuming what kind of explosion you were
looking at. It needed a star whose true brightness could be *read* unequivocally -- and the distance ladder already gave us one.

---

## A Cepheid in Andromeda

On the night of October 5–6, 1923, Edwin Hubble exposed a 4-by-5-inch glass plate on the
Andromeda nebula for 45 minutes, using the 100-inch Hooker telescope on Mount Wilson -- the
largest telescope in the world at the time. He was hunting novae, and on the plate he marked
three suspects with an "N." A nova appears suddenly, so it isn't there on earlier plates.

When he compared this plate with those taken earlier, one of the three turned out not to be a nova at
all. It had been there before, but fainter; now it was brightening again. Hubble crossed out its "N"
and wrote "VAR!" -- variable -- beside it. The plate, catalogued as H335H, is one of the most
famous photographs in astronomy, and the exclamation point is earned.

{{< nbas-image src="hubble1929-plateVI-v1.webp" fullwidth="true"
caption="V1 on another of Hubble's 100-inch plates, taken August 4, 1924, when the star was near its faintest; Hubble's label and tick marks point to it. At its brightest, he noted, it matched the brighter of the two stars just above and to the left. North is to the left. Edwin Hubble, Astrophysical Journal 69, 103 (1929), Plate VI; public domain. Scan: NASA Astrophysics Data System."
alt="A grainy black-and-white photographic plate of a star field in Andromeda's outer disk, with the label V1 and two short tick marks pointing to a faint star near the top; two novae elsewhere in the field are marked with crosses numbered 77 and 78." >}}
<!-- OPEN (ledger D2): only if Carnegie grants the "VAR!" plate -- it goes here, beside this one. -->

{{< nbas-image src="hubble1929-fig1-v1.webp" width="450" align="right"
caption="Hubble's own light curve of V1, from his measurements on the Mount Wilson plates: brightness (up is brighter) against days through one 31.4-day cycle. Edwin Hubble, Astrophysical Journal 69, 103 (1929), Fig. 1; public domain. Scan: NASA ADS."
alt="A hand-drawn graph of brightness against days from 0 to 30, with dots and a smooth curve rising steeply near day 0 and day 31 and fading slowly in between, between magnitudes 18.2 and 19.5." >}}
The star, now called V1, rose and fell with a period of 31.4 days in the lopsided rhythm of a
Cepheid -- a quick rise, a long, slow fade. That was the whole game. A Cepheid's period tells
you its true brightness; Henrietta Leavitt had found that law in the Small Magellanic Cloud,
and it is the rung we built in [Building the Distance Ladder](/articles/2026/12/building-the-distance-ladder/). 
Compare the true brightness with how faint V1 looks, and the distance follows.

Hubble's answer, read on his behalf by Henry Norris Russell at the American Astronomical Society
meeting on New Year's Day 1925, put Andromeda roughly a million light-years away. (His fuller
1929 analysis gave about 900,000.) Shapley had already seen the result in a letter from Hubble.
"Here is the letter that destroyed my universe," he is said to have told a colleague.

{{< clear >}}

### Wrong, and right anyway

{{< article-table align="right" >}}

| Year | Andromeda's distance |
|---|---|
| 1920 | (Shapley's whole Galaxy: 300,000 ly across) |
| 1922 | ~1.5 Mly (Öpik, from its rotation) |
| 1925 | ~1 Mly (Hubble) |
| 1929 | ~0.9 Mly (Hubble) |
| 1952 | roughly doubled (Baade) |
| 2021 | 2.48 Mly (HST Cepheids) |

{{< /article-table >}}

Even so -- extreme as it seemed at the time, Hubble's number was wrong. 
In 1952 Walter Baade found that the Cepheid scale Hubble had used
was calibrated with the wrong kind of Cepheid, making the distance to Andromeda roughly double --
that story is told in [Building the Distance Ladder](/articles/2026/12/building-the-distance-ladder/). 
Later refinements pushed it even further. Today's best Cepheid distance, from the Hubble Space Telescope, 
is 761,000 parsecs: about 2.5 million light-years, close to three times Hubble's figure.

So why did a distance that was wrong by almost a factor of three settle the question at all?
Because of the margin. Shapley's size of the Galaxy, the biggest anyone proposed, was 300,000 light-years
across. Hubble's too-small distance of 900,000 light-years _already_ put Andromeda about three times farther away than
that; it *had* to be outside the Milky Way. Every later correction made the answer *more* true, not less. 
The measurement didn't have to be precise to be decisive -- it just had to be far enough from the dividing line.

The greater distance also solved the puzzle of S Andromedae. Once Andromeda's distance was known more accurately, 
its ordinary novae turned out to be just as bright as those observed within the Milky Way Galaxy -- with S Andromedae about 
eleven magnitudes brighter than the rest. It wasn't an "impossible nova" -- it was a different kind of event
entirely, the kind we now call a supernova. The newly corrected rung repaired the old, broken one. (At
today's distance, S Andromedae's peak works out to an absolute magnitude of about −18.6 before
any correction for dust -- even brighter than the value Shapley rejected.)

<!-- BOOK: the "out of the question" −16 is Shapley's 1919 figure (via arXiv 1801.00598); the
     −18.6 is ours, V = 5.85 at μ = 24.41, no extinction. -->

### Andromeda by light

At 2&frac12; million light-years, Andromeda is the first object in this series whose distance is
naturally measured in *millions* of light-years -- the first rung of a new size. The light
reaching your eye from it tonight left around the time the human family tree was branching
toward our own genus.

And V1 itself? It is still there, still pulsing every 31.4 days, but it is faint: about
magnitude 19.4 on average. The gold circle in the smart scope image below marks its exact position. 
There's nothing to see there: at magnitude 19, and against the glow of Andromeda's own disk, the star is
lost in the smart scope's 2.6-arcsecond pixels. Hubble needed the biggest telescope on Earth to catch it; the Hubble Space Telescope, below, shows it as an ordinary star. 
It _is_ within reach of a large amateur telescope with a good camera today -- members of the AAVSO tracked 
its light curve in 2010 -- but generally beyond what a smart scope image will show. Some distances you can
measure; some stars you can only point to.

{{< nbas-image src="fig-v1-location.webp" fullwidth="true"
caption="Where V1 is today: inside the gold circle -- and far too faint to show. At about magnitude 19, against the glow of Andromeda's disk, it is lost in a smart scope's 2.6-arcsecond pixels. Right: the boxed area, enlarged and stretched; the circle is 20 arcseconds in radius. Bob Donahue, NBAS, Seestar S50, 82 min; V1 position from Templeton et al. (2011)."
alt="Wide image of the Andromeda Galaxy with a small box on its outer disk, and an enlarged grayscale close-up of that box showing scattered stars and an empty gold circle where the variable star V1 is located." >}}

{{< nbas-image src="ann1110a-v1.webp" fullwidth="true"
caption="The same star through the Hubble Space Telescope, which was pointed at V1 in 2011 as a tribute to Edwin Hubble's discovery. V1 is the star in the gold circle -- an ordinary-looking point among thousands of Andromeda's stars. NASA, ESA and the Hubble Heritage Team (STScI/AURA), CC BY 4.0; circle added by NBAS."
alt="A dense Hubble Space Telescope star field in Andromeda's disk, crossed by dark dust lanes, with a gold circle around one moderately bright star in the lower left." >}}


---

## Leavitt's Clouds, Revisited

There's a detail in Hubble's 1929 paper that's easy to miss. He didn't measure Andromeda's
distance directly. He compared its Cepheids with the Cepheids in the Small Magellanic Cloud --
the same cloud where Leavitt had found her law -- and found Andromeda to be about 8.5 times 
farther away. Then he multiplied by the accepted distance to the Cloud at the time. Hubble
was using a distance ladder that was not yet accurately calibrated.

The comparison was the strong part: two sets of Cepheids, same kind of star, side by side on
the period–luminosity diagram. The weak part was the Cloud's own distance, which rested on the
Galactic Cepheid calibration -- exactly where Baade later found the problem. Today the SMC is
measured at 62,400 parsecs (about 204,000 light-years), from pairs of stars that eclipse each
other. Multiply that by Hubble's own ratio and you get about 530,000 parsecs -- *most* of the way
to the modern value but still not quite there. Hubble's ruler was sound. Its zero point wasn't.

{{< nbas-image src="lmc-smc-stellarium-default.webp" fullwidth="true"
caption="The Large and Small Magellanic Clouds in a dark southern sky, simulated in Stellarium. From New England, neither one ever rises."
alt="A simulated southern night sky with two hazy patches of light, the Large and Small Magellanic Clouds, among the stars." >}}

The Large Magellanic Cloud, the SMC's bigger neighbor, is now one of the best-measured galaxies beyond our own: 49,590 parsecs (about 162,000 light-years), good to about 1 percent, also from
eclipsing binaries. The LMC in particular is where much of the modern distance ladder gets anchored -- which is
why its number is worth getting right.


### When the rulers disagree

One measurement of a distance is a number. Several measurements, made different ways, are an
honest error bar. The Local Group is where you can actually see that, because its galaxies are
close enough to be measured with nearly every method we have. Some of those methods are the
Cepheids and RR Lyrae stars; others -- the tip of the red giant branch (the brightest red giants 
a galaxy's old stars can reach) and eclipsing binaries (pairs of stars whose eclipses give 
their true size) -- get their own treatment later in the series. Here's how they compare for Andromeda:

| Method | Distance (kpc) | Distance (Mly) | Source |
|---|---|---|---|
| Cepheids (Hubble Space Telescope) | 761 ± 11 | 2.48 | Li et al. 2021 |
| RR Lyrae stars | 776 ± 22 | 2.53 | Savino et al. 2022 |
| Tip of the red giant branch | ~780 | 2.54 | Conn et al. 2012 |
| Eclipsing binary #1 | 772 ± 44 | 2.52 | Ribas et al. 2005 |
| Eclipsing binary #2 | 724 ± 37 | 2.36 | Vilardell et al. 2010 |

Five different methods, five different kinds of star, all within a few percent of each other.
That's what a settled distance looks like.

M 33, the Triangulum Galaxy, is a better story, because it wasn't settled -- not for a long time:

{{< nbas-image src="m_33-s30-62m-full.webp" fullwidth="true"
caption="M 33 -- the Triangulum Galaxy. Bob Donahue, NBAS, Seestar S30, 62 min" alt="The Triangulum Galaxy, a face-on spiral with loose, patchy arms." >}}

| Method | Distance (kpc) | Distance (Mly) | Source |
|---|---|---|---|
| Tip of the red giant branch (2002) | 916 ± 17 | 2.99 | Kim et al. 2002 |
| Eclipsing binary (2006) | 960 ± 54 | 3.13 | Bonanos et al. 2006 |
| Blue supergiants (2009) | ~970 | 3.16 | U et al. 2009 |
| Tip of the red giant branch (compiled) | ~809 | 2.64 | McConnachie catalog |
| Cepheids (Hubble Space Telescope, 2023) | 840 ± 11 | 2.74 | Breuval et al. 2023 |
| Tip of the red giant branch (2025) | ~842 | 2.75 | A&A 697, L6 (2025) |

<!-- 2025 row: A&A 697, L6, Vilnius group (corresponding author V. Vansevičius); 24.626 mag, ~842 kpc. Cited by journal because the full author list wasn't confirmed. -->

For about twenty years, careful measurements of M 33 ranged over roughly 20 percent. Only
recently have Cepheids and red giants converged near 840 kiloparsecs. Nobody was being sloppy;
each method has its own corrections for dust, crowding, and the chemistry of the stars, and
until those were understood, the methods disagreed.

The LMC teaches the opposite lesson. By 2013, astronomers had published 233 separate distance
determinations for it, and they clustered suspiciously tightly around one value. A study of
that clustering concluded that much of the agreement came from the measurements not being
independent -- the same calibrations and the same samples, reused several times. Agreement is
only as good as the independence behind it. (In that case the consensus was right: the 2019
geometric distance landed within about 1 percent of it. But nobody could have known that from
the agreement alone.)

{{< clear >}}

### The neighbors

The Local Group has more than a hundred known members, and the count keeps growing. Here are the most prominent: the
big ones, plus many of the smaller ones you can catch with a smart scope (see the observing notes below).
Most of the rest are faint dwarfs, found only in deep surveys. A standard reference list is the
[catalog kept by the astronomer Alan McConnachie](https://www.cadc.hia.nrc-cnrc.gc.ca/en/community/nearby) (2012, updated 2021).

| Galaxy | Distance (kpc) | Distance (Mly) | Diameter (kpc) |
|:---|---:|---:|---:|
| Milky Way (ours)            | ----- | ---- | ~28    |
| Large Magellanic Cloud      |  49.6 | 0.16 |   9.9  |
| Small Magellanic Cloud      |  62.4 | 0.20 |   5.8  |
| Leo I                       | 254   | 0.83 |   0.5* |
| NGC 6822 (Barnard's Galaxy) | 459   | 1.50 |   0.7* |
| NGC 185                     | 617   | 2.01 |   0.9* |
| NGC 147                     | 676   | 2.20 |   1.3* |
| IC 1613                     | 755   | 2.46 |   3.0* |
| M 31 (Andromeda)            | 761   | 2.48 |  46.6  |
| IC 10                       | 794   | 2.59 |   1.2* |
| M 32                        | 805   | 2.63 |   0.2* |
| M 110 (NGC 205)             | 824   | 2.69 |   1.2* |
| M 33 (Triangulum)           | 840   | 2.74 |  18.7  |
| WLM (Wolf–Lundmark–Melotte) | 933   | 3.04 |   4.7* |

*Distances for the LMC, SMC, M 31 and M 33 are the measurements discussed above; all others are
from the compilation of McConnachie (2012, updated 2021). Diameters are the standard optical
size (D25) for the four big galaxies; those marked * are the diameter holding half the galaxy's
light (McConnachie), so their faint outskirts reach well beyond. The Milky Way's size is
approximate, since we can't see it from outside.*


---

## The Local Group as a Place

With distances in hand for dozens of galaxies, the nearest part of the universe stops being a
list and becomes a place. It has a shape, an edge, and a mass -- and every one of those comes
from combining distances with something else.

### One ruler that fails here

Andromeda is famous for being one of the few galaxies in the sky that is coming *toward* us. Its
light is blueshifted: it is approaching at about 300 km/s. Surely that motion tells us something
about how far away it is?

{{< nbas-image src="fig-velocity-distance.webp" width="500" align="right"
caption="Inside the Local Group (left of the dashed line), velocity tells you nothing about distance: galaxies at the same distance from the group's center move toward and away from it at up to 300 km/s. Just outside, every member of the NGC 3109 group is receding. A few dwarfs just past the edge, such as SagDIG, are barely moving at all: the edge is fuzzy. Velocities are line-of-sight, corrected for the Sun's motion relative to the group (Karachentsev & Makarov 1996). Data: McConnachie (2012, updated 2021)."
alt="Scatter plot of velocity against distance from the middle of the Local Group: dozens of galaxies within 1 Mpc spread both above and below zero velocity, while six galaxies of the NGC 3109 group near 1.6–1.8 Mpc all have positive velocities of about 70 to 140 km/s." >}}

It doesn't, and the reason is worth noting. Most of that 300 km/s isn't _Andromeda's_ motion at
all -- it's ours. The Sun is carried around the center of the Milky Way, and right now that
orbit is taking us toward Andromeda at about 190 km/s. Take that out, and Andromeda approaches
the Milky Way at about 110 km/s. Measure it instead against the Local Group as a whole, and
what's left is a few tens of km/s.

Meanwhile, the expansion of the universe -- the effect that makes distant galaxies recede faster
the farther away they are -- would contribute only a few tens of km/s at Andromeda's distance.
Inside the Local Group, that small signal is swamped by the galaxies' own motions as they fall
toward each other and swing around. Velocity can't be a ruler here. Distance has to come first.


### Who belongs

So what *is* the Local Group? It isn't simply "the galaxies near us." It's the galaxies that are
held together by each other's gravity -- falling inward or orbiting, instead of being carried
away by the expansion. Between those two behaviors there is a boundary, the place where a galaxy
neither falls in nor drifts away. For the Local Group it sits about a million parsecs (some
3 million light-years) from the group's center.

You can't find that boundary with distance alone, or with velocity alone. You need both, for
the same galaxy. Plot them together and the edge shows up: inside it, galaxies scatter toward
and away from the center; outside it, they recede.

{{< nbas-image src="fig-local-group-map.webp" fullwidth="true"
caption="The Local Group from measured distances, drawn on the plane that contains the Milky Way, Andromeda and M 33. Two big galaxies, each with its own swarm of dwarfs, and a few loners in between. Dots mark positions only, not sizes; the faintest dwarfs are dimmed. The dashed circle marks the edge of the group -- about 1 million parsecs, where galaxies stop falling inward -- centered halfway between the two giants (an approximation). The NGC 3109 group (blue) lies just beyond it; one of its members sits right on the circle. Because the map flattens a 3D arrangement, SagDIG, really just outside the edge, lands inside it. The dots at the top belong to the Sculptor group, about 2 million parsecs away. Data: McConnachie (2012, updated 2021); Andromeda at 761 kpc (Li et al. 2021)."
alt="Map of the Local Group: the Milky Way and Andromeda as two gold dots about 0.77 Mpc apart, each surrounded by small dots for dwarf galaxies, M 33 near Andromeda, a dashed circle about 1 Mpc in radius around both, a few blue dots for the NGC 3109 group to the left, SagDIG labeled inside the circle below center, and a few dots at the top labeled Sculptor group." >}}
The best example sits right at the line. A little clump of small galaxies around NGC 3109 (located in Hydra), 
about 1.3 to 1.6 million parsecs from us, was long counted as part of the Local Group -- and you'll
still find them listed that way. But once their distances and velocities were measured better, all
of them turned out to be moving away from the group. They're our nearest neighbors *outside* the
family. Membership, it turns out, is a measurement, and it can change when the measurement does.

And the edge itself is fuzzy. The Sagittarius Dwarf Irregular Galaxy (SagDIG), about 1.07 million
parsecs from us, sits just past the line -- roughly 1.15 million parsecs from the group's center.
Yet it is barely moving relative to the group: not clearly falling in, not clearly drifting away.
Some lists call it the Local Group's most distant member; others leave it out. It isn't alone,
either -- a few other faint dwarfs sit at similar distances, moving just as slowly. Where you draw
the line depends on how you read those measurements.
<!-- SagDIG (McConnachie catalog): 1,067 kpc from the Sun, ~1,148 kpc from the MW-M31 midpoint,
     v_LG ~ +21 km/s. Similar: Tucana (~1,067 kpc from midpoint, v_LG ~ +73) and Aquarius
     (~1,047, ~ +13). Labeled on fig-velocity-distance. -->

The map shows the group's shape: not an even cloud but a dumbbell. Two big galaxies, the Milky
Way and Andromeda, each sit amidst a swarm of their own satellites. M 33 is most likely bound to
Andromeda. A handful of small galaxies, like NGC 6822 and IC 1613, drift on their own in between.

{{< nbas-image src="fig-local-group-subgroups.webp" fullwidth="true"
caption="Zooming in on the two swarms, with the big galaxies drawn as circles of their true diameter (their tilts aren't shown). Most satellites are dwarfs far smaller than their dots. The map is flat, so some distances look shorter than they are: Leo I appears about 100 kpc from the Milky Way but is really about 257 kpc away. M 32 and M 110 plot behind Andromeda because their distances were measured differently; how far behind, if at all, isn't settled. Data: McConnachie (2012, updated 2021)."
alt="Two square panels, each 700 kiloparsecs across, with a dashed 300-kiloparsec circle. Left: the Milky Way as a small gold disk with the Magellanic Clouds just beside it and dozens of small dots for dwarf galaxies, labeled Sagittarius dwarf, Leo I and Fornax. Right: Andromeda as a larger gold disk with M 32 and M 110 next to it, NGC 147, NGC 185 and IC 10 below, and M 33 as a small gold disk about 200 kiloparsecs above." >}}

### Galaxies are crowded

Distance alone doesn't tell you whether a neighborhood is crowded. Size does: how far apart
things are compared with how big they are. Measure each gap in the widths of the objects
themselves, and the scales we assembled from earlier chapters line up in a surprising way.

{{< article-table align="right" >}}

| Pair | Apart, in their own widths |
|---|---|
| Earth and Moon | ~30 Earth widths |
| Sun and Earth | ~107 Sun widths |
| Milky Way and Andromeda | ~27 Milky Way widths |
| Sun and Proxima Centauri | ~29 million Sun widths |

{{< /article-table >}}

The Moon sits about 30 Earth widths from us. Andromeda sits about 27 Milky Way widths away --
nearly the same proportion. Stars are another matter entirely: the Sun's nearest neighbor is about
29 million Sun widths away. Looking at things this way, galaxies live close together, and stars live
almost alone.

That difference suggests what could happen when galaxies meet. The Milky Way and Andromeda are
approaching each other; whether they will actually merge is the subject of debate
(see "[The Andromeda Family of Galaxies](/articles/2026/09/the-andromeda-family-of-galaxies/)"). If they
do, the galaxies will run into each other, but their stars -- millions of their own widths
apart -- will almost never touch. The Sun's neighborhood might see noticeably more "visitor" stars
passing through, like the halo tourists of the previous chapter, but at the scale of the stars
themselves, a merger is surprisingly calm. (To get a feel for these proportions with your own
hands, try the scale model at the end of this chapter.)

{{< clear >}}
{{< nbas-image src="fig-crowding-strip.webp" fullwidth="true"
caption="The Milky Way and Andromeda to scale, 761,000 parsecs apart: about 27 Milky Way widths. Milky Way disk ~28 kpc across; Andromeda 46.6 kpc (standard optical diameter)."
alt="A strip showing a small gold disk labeled Milky Way and a larger gold disk labeled Andromeda, with a row of outlined circles the size of the Milky Way filling the gap between them, under the caption 'about 27 Milky Way widths apart'." >}}

### The mass of the group

Distances don't just place things. Combined with motion, they can measure mass -- how much matter
something contains. (Astronomers often call this "weighing" a galaxy, but weight depends on the
gravity where you stand; mass doesn't. Mass is what's being measured here.)

The idea goes back to the debate years. In 1922, before Hubble's Cepheids, the Estonian
astronomer Ernst Öpik estimated Andromeda's distance from how fast it rotates: the rotation told
him its mass, and if its stars were like ours, that mass implied how bright it should be. His
answer, about 450,000 parsecs, was closer to the truth than Hubble's. Motion plus an assumption
about mass gave a distance.

In 1959, Franz Kahn and Lodewijk Woltjer ran the same kind of reasoning the other way. Early in
the universe's history, everything was moving apart -- the Milky Way and Andromeda included.
Today, they are approaching each other. So something turned them around, and the only candidate is
their own gravity. Three numbers pin the orbit down: how far apart they are now, how fast they
are closing, and how long they've had. Only one total mass fits all three.

{{< nbas-image src="fig-timing-argument.webp" width="450" align="left"
caption="Measuring the Local Group's mass with a distance. If the Milky Way and Andromeda started together and are now approaching at 110 km/s, their separation must have followed a curve like one of these -- and only one total mass fits each distance. Today's distance requires about 4.6 trillion solar masses; Hubble's 1929 distance would have required only 0.8 trillion. A simplified head-on model (published values, including sideways motion, are about 5 trillion); curves stop at today and are not a forecast."
alt="Graph of Milky Way–Andromeda separation against time since the Big Bang: two arching curves rise and then fall toward today, a gold solid curve peaking near 1 Mpc labeled 4.6 trillion solar masses and a blue dashed curve peaking near 0.55 Mpc labeled 0.8 trillion solar masses." >}}

The answer was startling. Kahn and Woltjer found that the pair had to contain at least ten
times more mass than anyone could see -- one of the earliest hints of what we now call dark
matter. Modern versions of the calculation, which include Andromeda's small sideways motion,
give about 5 trillion solar masses for the Milky Way and Andromeda together. Since the two giants
dominate the group, that is close to the mass of the whole Local Group. (Timing estimates tend to
run high compared with other methods; "several trillion" is the honest summary.)

And here the distance matters directly. Run the same calculation with Hubble's 1929 distance
and the pair comes out at less than a trillion solar masses. Today's more accurate distance makes
it more than five times as massive. Fixing the ruler changed how much matter we think the
neighborhood holds.

{{< clear >}}

---

<!-- BOOK (ledger D3, decided 2026-11-11): trim to the sky map plus one short paragraph; no carousel.
     Article keeps the full section. Apply at the LaTeX conversion. -->
## Observing Hooks

Most of the Local Group is within reach of a small telescope or a smart scope, and a few of its
members don't need a telescope at all.

{{< nbas-image src="fig-local-group-sky.webp" fullwidth="true"
caption="Where the neighbors are on the sky. Andromeda's family bunches together in Andromeda and Cassiopeia, just off the Milky Way; the rest are scattered all over the sky. The Magellanic Clouds sit below the dashed line, which marks the declination that never rises from latitude 40° north (New England is slightly farther north still). Solid blue line: the plane of the Milky Way; dotted lines: 10° either side."
alt="All-sky map in right ascension and declination. The Milky Way plane arches across it. A cluster of gold dots near 0h and +40 to +60 degrees is labeled Andromeda and its satellites, with M 33 just below. Leo I sits alone near 10h, IC 1613 near the celestial equator at 1h, NGC 6822 at 20h in Sagittarius, and the two Magellanic Clouds near -70 degrees, below a dashed line marked never rises from 40 degrees north." >}}

### The big ones

**Andromeda (M 31)** is visible to the naked eye from a reasonably dark site, as an elongated
smudge in the constellation that gives it its name -- the most distant thing most people will
ever see without optical aid. Its two bright companions, **M 32** and **M 110**, show in any image, and
so does **NGC 206**, a great cloud of young stars in Andromeda's disk.

**M 33**, in Triangulum, is a harder naked-eye catch -- a few observers manage it under truly
dark skies -- but an easy and rewarding smart-scope target. **The Magellanic Clouds** are
naked-eye showpieces, but only from far enough south; from New England they never rise above the horizon.

### The hunt

The small ones are the real hunt. **NGC 147** and **NGC 185** are a pair of Andromeda's
satellites near the Cassiopeia border, about a degree apart on the sky. **IC 10**, a starburst
dwarf, sits only 3° from the plane of our own Galaxy, behind a veil of its dust. **IC 1613** is
about as alone as a Local Group galaxy gets: some 500,000 parsecs from Andromeda and 750,000 from
us. **NGC 6822** (Barnard's Galaxy) is a loner on our side of the group, about 450,000 parsecs
away. And **Leo I**, a faint smudge close to Regulus, whose glare is part of the challenge, is one
of the Milky Way's most distant satellites -- about 250,000 parsecs out, and moving away from us at
nearly 300 km/s. **WLM** (the Wolf–Lundmark–Melotte galaxy), in Cetus, is a lone dwarf out near
the group's edge: about 930,000 parsecs from us, and about 800,000 from the group's center --
still inside the line.

Faint is the point: these are entire galaxies, and they look like almost nothing.

{{< nbas-gallery style="carousel" size="300px" title="Smaller members of the Local Group" >}}
c_17-equ-32m.webp    | NGC 147/C 17                        | eQuinox 2, 32 min
c_18-equ-32m.webp    | NGC 185/C 18                        | eQuinox 2, 32 min
ic_10-s50-272m.webp  | IC 10                               | Seestar S50, 272 min
c_51-s50-92m.webp    | IC 1613/C 51                        | Seestar S50, 92 min
pgc_143-s50-98m.webp | Wolf–Lundmark–Melotte (WLM)/PGC 143 | Seestar S50, 98 min
c_57-equ-27m.webp    | NGC 6822/C 57 = Barnard's Galaxy    |  eQuinox 2, 27 min
reg_dw-equ-47m.webp  | Leo I = the Regulus Dwarf           |  eQuinox 2, 47 min
{{< /nbas-gallery >}}

{{< clear >}}
---

## The Fence

In their own era, these rungs -- Cepheids and RR Lyrae, calibrated in our own Galaxy and the
Magellanic Clouds -- reached the Local Group and only a little beyond. A few million parsecs out, individual stars in
other galaxies became too faint and too crowded for the telescopes of the time to pick out.

Space telescopes have since found Cepheids in galaxies much farther away. But that doesn't change the shape of
the problem: every rung so far is a kind of star, and observable stars run out. To measure the distances to
the thousands of galaxies beyond our neighborhood, astronomers needed brighter rungs -- objects
that can be seen when individual stars can't.

That is the Local Group's other job. Its galaxies are close enough to measure in nearly every
way we know, so they became the test bench: the place where each new, brighter rung was checked
against the old ones before anyone trusted it farther out. The neighborhood we've just mapped is
where the next part of the ladder gets built.

---

{{< nbas-callout title="Try It: Build the Local Group to Scale" >}}
Numbers like "761 kiloparsecs" don't feel like anything, so build them. Shrink the Local Group
until 1,000 light-years is 1 millimeter, and lay it out on a kitchen table with things from the
fruit bowl and the spice rack.

| Galaxy | At this scale | About the size of | Distance from the Milky Way |
|---|---|---|---|
| Milky Way | ~10 cm | an orange | -- |
| Andromeda (M 31) | 15 cm | a big grapefruit | 2.5 m |
| Triangulum (M 33) | 6 cm | a lime | 2.7 m (0.7 m from the grapefruit) |
| Large Magellanic Cloud | 3 cm | a walnut | 16 cm |
| Small Magellanic Cloud | 2 cm | a grape | 20 cm |
| M 32 and M 110 | 1–4 mm | grains of sand to a peppercorn | 2–3 cm from the grapefruit's center, as seen from the orange |
| Smaller dwarfs | 2–10 mm | peppercorns to a pea | 0.8 to 2.5 m |

*Galaxy sizes: standard optical diameters (the "D25" size) for the large galaxies; the Milky
Way's is approximate, since we can't measure it from outside. Dwarf sizes are the diameters that
hold half their light -- their faint outskirts extend farther. Distances from the measurements
above.*

Hold the Milky Way orange in one hand. The walnut and the grape -- the Magellanic Clouds -- sit a hand's
width away. Across the room, about 2.5 meters off, is our Andromeda grapefruit, with a couple of
peppercorns sitting right against its skin (as seen from the orange, they overlap it). The lime representing M 33 is a few steps beyond. 
All of the major members fit in an ordinary room: the edge of the Local Group, where 
galaxies stop falling inward, is about 3 meters from its center. The nearest galaxies *outside* it, 
the NGC 3109 group, are just over in the next room.

Now try the stars at the same scale. The Sun would be about a thousand times smaller than an
atom, and its nearest neighbor, Proxima Centauri, would be 4 micrometers away -- the length of a
bacterium. Galaxies are fruit a couple of meters apart; stars are specks smaller than atoms, a
microbe's width apart.

<!-- OPEN (ledger O3): Bob's photo of the model goes here (kitchen-table.jpg, fullwidth):
{{< nbas-image src="kitchen-table.jpg" fullwidth="true" caption="The Local Group at 1 mm = 1,000 light-years. Positions are only approximate: the real arrangement is 3D. Bob Donahue, NBAS" alt="A tabletop scale model of the Local Group: an orange, a grapefruit, a lime, a walnut, a grape and scattered peppercorns laid out across a kitchen table." >}} 
-->

{{< clear >}}
{{< /nbas-callout >}}
<!-- BOOK (ledger D4): keep or drop depending on the page count at layout time. -->

<!-- CROSS-LINKS used: building-the-distance-ladder; ngc-6946-the-fireworks-galaxy;
     the-andromeda-family-of-galaxies. Still optional: parsecs-vs-light-years (star spacing,
     Curtis); galactic-scale (Milky Way size); galactic-tour (LMC merger). -->


