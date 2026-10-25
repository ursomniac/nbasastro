---
title: "Parsecs vs. Light Years"
date: 2026-12-18
description: "A parsec is easy to define and hard to feel. Where the unit came from, why a 1902 choice still hides in the distance formula as a −5, and a scale bar of real stars to carry it."
byline: "Two rulers for the same sky, and how to get a feel for the stranger one"
authors: ["bob-donahue"]
series: ["astronomical-frameworks"]
thumbnail: "thumbnail.jpg"
banner: "banner.webp"
miniseries: "measuring-astronomical-distances"
miniseries-sequence: 6
---

## Introduction

{{< nbas-image src="banner.webp" fullwidth="true"
caption="One patch of the winter sky, with distances. Left: Canis Major, Orion, Taurus and Canis Minor as they appear (north up, east left). Right: the same six objects sorted by distance. Aldebaran sits in front of the Hyades, not in them. Star positions: HYG database v4.1 (CC BY-SA 4.0)."
alt="Star chart of the winter sky around Orion, with gold circles and distance labels: Sirius 2.6 parsecs, Procyon 3.5, Aldebaran 20, the Hyades 47 (a dashed circle around the cluster, with Aldebaran's smaller circle inside it), the Pleiades 136 and the Orion Nebula 389. To the right, the same six names on a logarithmic distance axis from 1 to 1,000 parsecs, from Sirius nearest to the Orion Nebula farthest." >}}

At the end of the [article on parallax](/articles/2026/12/parallax/) we had a number: Proxima
Centauri, the nearest star after the Sun, has a parallax of 768.07 milliarcseconds. Turn that
upside down and you get its distance: 1.302 parsecs. Or, if you prefer, 4.246 light-years.

Two answers, two units, one star. Back in [the first article of this series](/articles/2026/10/measuring-distance/)
we asked why astronomy bothers with two units for the same job. This article is the answer --
and an attempt at something harder: trying to *feel* a parsec, since it's the unit most of the
measurements still to come are given in.

Over the last five articles we've built up a feel for light-travel time. Light takes a little
over a second to reach the Moon, eight minutes to reach us from the Sun, and hours to cross the
outer solar system. So "4.2 light-years" means something: the same kind of trip, just longer.

The parsec is different. Its definition is easy to picture -- a tiny angle, a long triangle --
but most of us have no *scale bar* for it. Proxima is 1.3 parsecs away. Then what? What's at 10
parsecs, or 50, or 400? By the end of this article you should have one: a handful of real stars
and clusters, most of them in the winter evening sky, that turn "parsecs" from a definition into
a distance.

---

## What a Parallax Actually Gives You

### 206,265

Start with what the telescope measures. A parallax is an angle: half of the tiny back-and-forth
shift a nearby star makes against the background over a year -- the angle the Earth–Sun distance
would span, seen from the star.

{{< nbas-image src="fig-parsec-geometry.svg" width="450" align="right"
caption="The definition of the parsec: the distance at which the Earth–Sun distance (1 AU) spans one arcsecond. Not to scale -- the real triangle is 206,265 times longer than it is tall."
alt="Diagram: the Sun and Earth one astronomical unit apart on the left, with two long lines meeting at a distant star on the right. The tiny angle at the star is labeled one arcsecond, and the distance is labeled 1 parsec equals 206,265 AU equals 3.26 light-years." >}}
Turn that angle into a distance and you don't get kilometers or light-years. You get a distance
in units of the Earth–Sun distance -- the astronomical unit we spent
[a whole article measuring](/articles/2026/11/measuring-the-astronomical-unit/). A star with a
parallax of one arcsecond is 206,265 AU away. A star with a parallax of half an arcsecond is
twice that. (206,265 is just the number of arcseconds in a radian; it falls out of the geometry.)

So every distance measured by parallax in the nineteenth century came out of the calculation in
AU, and turning it into any other unit meant multiplying by something:

- **kilometers or leagues** needed the size of the AU, which was itself still uncertain;
- **light-years** needed the size of the AU *and* the speed of light.

Every conversion carried along the errors of its conversion factors.

### Light-time came first

People converted anyway, and the unit they reached for most often was light-travel time. That
habit is older than any measured distance to a star. In 1694 an English writer, Francis Roberts,
remarked that "Light takes up more time in Travelling from the Stars to us, than we in making a
West-India Voyage (which is ordinarily performed in six Weeks)."

He was working from the only estimate of the speed of light there was: Rømer's, from the timing
of Jupiter's moons in 1676, which said light takes about ten or eleven minutes to reach us from
the Sun. (Not everyone believed it yet; that took Bradley, half a century later.)

Once real parallaxes arrived in 1838, the habit continued. A French astronomer lecturing on the
first handful of measured distances gave them in astronomical units and in leagues -- and then
added a table in "years of light."

The word itself came in 1851, from a German writer, Otto Ule: *Lichtjahr*. He knew it sounded
odd for a distance to end in "year," and compared it to the *Wegstunde*, the "hour's walk," a
distance named for the time it takes to cover. (English does the same thing: "the station is ten
minutes away.") By 1868 an English journal was describing the light-year as a unit "used by the
Germans."

So the light-year was never a simplified version of the parsec, invented for the public. It came
first. The parsec is the latecomer -- and its one great virtue is that it's the unit in which the
conversion factor is exactly 1.

{{< nbas-image src="fig-unit-timeline.svg" fullwidth="true"
caption="Two threads, 1694–2015. Light-travel time (left) is older than any measured stellar distance; the angle-based units (right) arrive in a rush between 1898 and 1913. Rows are in order, not to a time scale."
alt="A vertical timeline with a central spine. On the left, in gold, light-travel-time milestones: Roberts 1694, Bode 1768, Ule coins Lichtjahr 1851, an English journal calls it a German unit 1868, Curtis 1913, IAU recommends the light-year for popular use 1919. On the right, in blue, angle-based units: Herschel's distance of Sirius 1785, Bessel's first parallax 1838, Seeliger's Siriusweite 1898, Kapteyn's 10-parsec absolute magnitude 1902, Kobold's Sternweite 1906, Charlier's siriometer 1911, the name parsec 1913, IAU adoption 1922, Charlier's proposal rejected 1928, and the exact IAU definition 2015." >}}

---

## A Zoo of Units

{{< article-table align="right" >}}

| Unit | Who, when | One unit is… |
|------|-----------|--------------|
| distance of Sirius | Herschel, 1785 | Sirius's distance, then unknown |
| *Siriusweite* | Seeliger, 1898 | a 0.2″ parallax (5 pc) |
| *Sternweite* | Kobold, 1906 | a 1″ parallax (1 pc) |
| *siriometer* | Charlier, 1911 | 1,000,000 AU (4.85 pc) |
| *parsec* | Turner, 1913 | a 1″ parallax (1 pc) |

{{< /article-table >}}
By 1900, the astronomers studying the structure of the Milky Way were handling thousands of
stars at once, and converting every parallax by hand was a nuisance. So several of them made up
their own unit, tied directly to the measured angle -- or to something close to it.
Even before any parallax had been measured, William Herschel had used the distance of Sirius as
his yardstick, as a stand-in for the average distance of the brightest stars. The *Siriusweite*
borrowed the name, but not the number: 0.2 arcseconds isn't Sirius's actual parallax (about
0.38). It's just a round number that sets the scale.

The *Sternweite* is the one to notice. It's exactly the parsec, defined seven years before
anyone called it that.

{{< clear >}}

### The name

{{< nbas-image src="fig-unit-zoo.svg" width="500" align="right"
caption="One idea, many names: the competing star-distance units of 1785–1913, converted to parsecs. Kobold's Sternweite and Turner's parsec are the same length."
alt="Dot plot on a logarithmic scale of the length of one unit in parsecs: light-year 0.31, parsec 1, Sternweite 1, Herschel's distance of Sirius 2.64 (shown at Sirius's modern distance), siriometer 4.848, Siriusweite 5." >}}

The name we use came out of a 1913 paper by the Astronomer Royal, Frank Dyson. In a footnote he
suggested calling the 1-arcsecond unit an *astron*, and noted that his colleague H.H. Turner had
suggested *parsec* -- PARallax of one SECond.

When Dyson presented the paper to the Royal Astronomical Society, the naming question took over
the discussion. "Astron" sounded too much like "astronomical unit." Turner floated *macron*,
which might be confused with *micron*. "Siriometer," Dyson said, "suggests a machine for
measuring." An American astronomer even proposed a unit equal to the distance of the Andromeda
nebula -- whose distance nobody knew to better than about 50%, and that turned out to be
optimistic.

"Parsec" is the name that stuck. Its zero-conversion convenience certainly helped. But to be
honest about the record, what survives from 1913 is an argument about *names*: the quantity had
been defined for years, and Turner gave it the name people kept using.

---

## A Measured Unit, or a Physical One?

Underneath the naming argument was a real difference of opinion. The American astronomer Heber
Curtis argued for a unit built on a constant of nature, like the speed of light, instead of on
the size of Earth's orbit -- which in 1913 was still known to only about one part in a thousand:

> "...whether the Milky Way is three thousand, or several million light-years across, the
> light-year is still a usable unit."

Arthur Eddington took the opposite side, complaining about "the light-year which,
notwithstanding its inconvenience and irrelevance, has sometimes crept from popular use into
technical investigations."

Both had a point, and they still do:

- The parsec is the **observational** unit: it's what a parallax measurement naturally produces.
- The light-year is a **physical** unit: it measures distance against the one speed everything
  in the universe agrees on.

Curtis's precision complaint, at least, has gone away. Both units are now defined exactly. Since
2015 the International Astronomical Union (IAU) has defined the parsec as exactly 648,000/π =
206,264.8 astronomical units, and the light-year is exactly 9,460,730,472,580,800 meters -- the
distance light travels in a vacuum in one year of 365.25 days.

And the parsec's tie to measurement is anything but historical. The Gaia spacecraft has now
measured parallaxes for more than a billion stars, and every one of them comes out, naturally,
in parsecs.

---

## The −5: Why Standard Candles Speak Parsec

There's one more reason the parsec runs all through professional astronomy, and it was set
before the word "parsec" existed.

The [magnitude article](/articles/2026/10/measuring-brightness-the-magnitude-system/) introduced
*absolute magnitude*: how bright a star would look if it were placed at a standard distance of
10 parsecs. That standard came from the Dutch astronomer Jacobus Kapteyn. In 1902 he defined it --
not in parsecs, since there was no such word yet, but as the brightness a star would have at a
parallax of 0.1 arcseconds. He defined it in the raw measurement, the angle.

There was nothing inevitable about 10 parsecs. Other astronomers used 100 parsecs, or 1. By 1920
even Kapteyn had accepted the parsec -- "very convenient (though very ugly)," he called it -- and
proposed moving absolute magnitude to 1 parsec. But in 1922 the young IAU settled on the letters
*m* and *M* and on the parsec as the unit, and Kapteyn's 10 parsecs stayed.

### Where the −5 comes from

The relationship between apparent magnitude *m*, absolute magnitude *M*, and distance *d* is:

> *m* − *M* = 5 log₁₀ (*d* / 10 pc)

Every factor of 10 in distance adds 5 magnitudes, and at exactly 10 parsecs the two magnitudes
are equal. Pull the 10 out of the logarithm, and you get the version in most textbooks:

> *m* − *M* = 5 log₁₀ *d* − 5   (with *d* in parsecs)

{{< nbas-image src="fig-distance-modulus.svg" width="500" align="right"
caption="Where the −5 comes from. With absolute magnitude defined at 10 parsecs (Kapteyn, gold), the formula needs a −5; with the 1-parsec standard some astronomers used instead (blue dashed), it wouldn't. Same slope, offset by exactly 5 magnitudes."
alt="Graph of how many magnitudes fainter a star looks against its distance from 1 to 1,000 parsecs, on a logarithmic scale. Two parallel straight lines: a solid gold line crossing zero at 10 parsecs, labeled Kapteyn, m minus M equals 5 log d minus 5, adopted; and a dashed blue line crossing zero at 1 parsec, labeled Hertzsprung. An arrow marks the constant 5-magnitude gap between them." >}}

That −5 is nothing but Kapteyn's 10. It isn't physics; it's a fossil of a 1902 decision. Had the
standard been 1 parsec instead, the formula would simply be *m* − *M* = 5 log₁₀ *d*.

People noticed the oddity even then. At the IAU meeting in 1928, one astronomer pointed out how
strange it was to use the parsec as the unit while defining absolute magnitude at *ten* parsecs.
Eddington's reply: physics defines the liter as a cubic decimeter, and nobody minds.

{{< clear >}}
### Why it reaches so far

But parallax -- even with Hipparcos and Gaia -- only reaches stars within our own Galaxy. So what
carries the parsec farther? Most ways of finding distances to faraway stars and galaxies work by figuring out how bright 
an object is intrinsically -- its absolute magnitude -- and comparing that with how bright it 
looks. Those objects are called *standard candles*, and we'll meet them properly later in the series.

Every one of them runs its answer through the magnitude formula, so every one of them comes out in
parsecs. Not because they have anything to do with parallax, but because the magnitude system
they plug into was built around parsecs before any of them were discovered.

It's the same thing that happened with the astronomical unit: Kepler's third law made the AU the
natural unit for the solar system, and every later measurement inherited it. A framework built
early sets the unit for everything that plugs into it later.

{{< clear >}}
---

## A Scale Bar for the Parsec

Now for the part that's been elusive. Light-years are already a unit we can feel, so let's use
them as the bridge, and calibrate our sense of the parsec using real objects.

One rule of thumb first: **a parsec is about three and a quarter light-years.** I'll admit
something: after decades of doing astronomy, I _still_ don't think natively in parsecs. When I see one, 
something in my head immediately tries to multiply by three (or by 3.26, with a calculator). 
Maybe this table will finally retrain me. It's not so different from the mental leap someone used
to miles makes when driving somewhere that uses kilometers: practice brings familiarity. So here
goes.

| Distance | Light-years | What's there |
|----------|-------------|--------------|
| 1.3 pc | 4.2 ly | Proxima Centauri and Alpha Centauri, the nearest stars |
| 2.6 pc | 8.6 ly | Sirius, the brightest star in the night sky |
| 3.5 pc | 11.4 ly | Procyon; and 61 Cygni, Bessel's first parallax star |
| 7.7 pc | 25 ly | Vega |
| **10 pc** | **32.6 ly** | **Kapteyn's distance -- where absolute magnitude is defined** |
| 20 pc | 65 ly | Aldebaran, the red eye of Taurus |
| 47 pc | 153 ly | The Hyades, the V-shaped cluster around Aldebaran |
| 136 pc | 443 ly | The Pleiades |
| 389 pc | 1,270 ly | The Orion Nebula |
| 0.9 kpc | 3,000 ly | M35, the bright open cluster in Gemini |
| 7.4 kpc | 24,000 ly | M13, the Great Globular Cluster in Hercules |
| 8.2 kpc | 26,700 ly | The center of the Milky Way |
| 50 kpc | 162,000 ly | The Large Magellanic Cloud |
| 770 kpc | 2.5 million ly | The Andromeda Galaxy |

*Distances: Reylé et al. (2021, updated 2023) for the nearest stars; Hipparcos for Aldebaran and the
Hyades; Gaia DR3 for the Pleiades; VLBA radio parallaxes (Kounkel et al. 2017) for the Orion Nebula;
Wu et al. (2009) for M35; GRAVITY Collaboration (2019) for the Galactic center; Pietrzyński et al.
(2019) for the LMC; the average of several methods for Andromeda.*

The last five rows are a preview. Past a few hundred parsecs, the numbers stop describing our
neighbors and start describing the Galaxy and what lies beyond it, so the natural unit grows to
the kiloparsec (a thousand parsecs) and beyond. And most of those distances weren't measured by
parallax at all. Each comes from a different method, and those methods are what the rest of this
series is about.

{{< nbas-image src="fig-scale-bar.svg" fullwidth="true"
caption="A scale bar for the parsec, with light-years along the top. The shaded band marks where the Sun itself would sit among the faint backyard stars (10 parsecs) and where it would drop out of naked-eye view (about 17 parsecs)."
alt="A horizontal logarithmic distance axis from 1 to about 500 parsecs, with light-years on a second axis above. Landmarks marked with dots: Proxima and Alpha Centauri at 1.3 parsecs, Sirius 2.6, Procyon and 61 Cygni 3.5, Vega 7.7, Aldebaran 20, the Hyades 47, the Pleiades 136, the Orion Nebula 389. A blue band from 10 to 17 parsecs is labeled: the Sun from here would be a faint backyard star, and invisible past about 17 parsecs." >}}

Finally, the row in bold (at 10 pc) is the one worth stopping on, because there's another way it can be *felt*: the 
Sun's absolute magnitude is about 4.8. So if you moved the Sun out to Kapteyn's 10 parsecs, it would shine at
that magnitude -- becoming another of the faint stars you can just make out from a suburban backyard on a
clear night. Move it out to about 17 parsecs and it fades past magnitude 6, the usual naked-eye
limit under a good dark sky. (Under a truly pristine sky, sharp eyes can follow it a little
farther.)


{{< article-table align="right" >}}

| Sun-like star | Distance | Magnitude |
|---------------|----------|-----------|
| ξ Boötis A | 6.8 pc | 4.7 |
| χ¹ Orionis | 8.7 pc | 4.4 |
| κ¹ Ceti | 9.3 pc | 4.85 |
| *the Sun, moved to 10 pc* | *10 pc* | *4.8* |
| δ Trianguli | 10.8 pc | 4.8 |
| 18 Scorpii | 13.9 pc | 5.5 |

{{< /article-table >}}

So the next time you're out, look for the faintest stars you can see without trying hard. Any one of
them could be the Sun at 10 parsecs. And a few real Sun-like stars sit right around that distance
(see the table), similar to the Sun though at different ages. Most are naked-eye stars from
mid-northern latitudes. χ¹ Orionis, for example, is the western of the two stars at the top of
Orion's "club." The last one, 18 Scorpii, is one of the closest known "solar twins" in overall
properties, and it sits about midway between our 10-parsec reference point and where the Sun would
fade from view.

*Solar analog distances: Reylé et al. 2021/2023 (ξ Boo, χ¹ Ori, κ¹ Cet); Hipparcos via the HYG database
(δ Tri, 18 Sco). All are G-type dwarfs like the Sun (G0–G7).*



---

## The Neighborhood

The stars in the first few rows of the scale-bar table are our neighbors, and the idea of a "solar
neighborhood" has a long history. In 1937 a Yale astronomer published a list of the 127 stars
then known within 10 parsecs, with their companions. Twenty years later, Wilhelm Gliese's
*Catalogue of Nearby Stars* listed 915 stars within 20 parsecs, and its "GJ" numbers are still how
many of these stars are known today.

The most complete census now is built largely on Gaia parallaxes: every known star, brown dwarf,
and planet within 10 parsecs (Reylé et al. 2021, updated 2023). It lists 336 systems, holding 456
stars, brown dwarfs and white dwarfs, plus 85 known planets. Some of the names are famous well beyond astronomy:

- **Alpha Centauri** (1.3 pc): three stars including Proxima, and the target of every "nearest
  star" story.
- **Barnard's Star** (1.8 pc): the fastest-moving star across our sky.
- **Wolf 359** (2.4 pc): a dim red dwarf that science fiction has made far more famous than its
  magnitude 13.5 would suggest.
- **Sirius** (2.6 pc): with its white-dwarf companion.
- **Epsilon Eridani** (3.2 pc) and **Tau Ceti** (3.7 pc): two fairly Sun-like stars, and the
  targets of the first radio search for signals from other civilizations, Project Ozma, in 1960.
- **61 Cygni** (3.5 pc): Bessel's star.
- **40 Eridani** (5.0 pc): also famous in certain science fiction circles[^startrek].

Most of the neighborhood, though, consists of objects with names or catalog identifiers that nobody would recognize:

- **350 stars**, about 280 of them small, dim red dwarfs. Only about 50 objects in the whole
  catalog are bright enough to see without a telescope, even from a dark site; Proxima itself, at
  magnitude 11, is not one of them.
- **85 brown dwarfs** -- objects that form like stars but are too small to ever sustain hydrogen
  fusion. Most of them (73) are on their own: 68 of the 336 systems are a lone brown dwarf or a
  pair of them, with no hydrogen-burning star. The other 12 orbit stars.
- **21 white dwarfs**, the cooling cores of stars that have finished their lives.

{{< nbas-image src="fig-10pc-neighborhood.svg" fullwidth="true"
caption="The 336 star systems within 10 parsecs of the Sun, each plotted in its direction around the plane of the Galaxy at its true distance (height above or below the plane isn't shown). Rings every 2.5 parsecs. Notice the empty space around the Sun: nothing is closer than Alpha Centauri. Data: Reylé et al. 2021, 2023 update (CDS J/A+A/650/A201)."
alt="Map centered on the Sun with rings at 2.5, 5, 7.5 and 10 parsecs, each marker at its true distance from the Sun, leaving an empty region around the Sun out to Alpha Centauri at 1.3 parsecs. 336 markers: gold dots for star systems (255), blue squares for lone white dwarfs (13), gray triangles for brown-dwarf-only systems (68). Labeled: Alpha Centauri, Barnard's Star, Wolf 359, Sirius, Procyon, Epsilon Eridani, Tau Ceti, 61 Cygni, Altair and Vega. An arrow on the right points toward the Galactic center." >}}

### How far to the next star?

Spread 336 systems through a sphere 10 parsecs in radius and you get about one system for every
12.5 cubic parsecs. But the more useful question is: from any one star, how far is the *nearest*
other one?

{{< nbas-image src="fig-nn-histogram.svg" width="450" align="right"
caption="How far is the next star? For each of the 111 systems within 6.5 parsecs (the Sun included), the distance to its nearest neighbor. The median is 1.26 parsecs; the Sun's nearest neighbor, Proxima, is at 1.30."
alt="Histogram of nearest-neighbor distances from 0.2 to 2.6 parsecs, peaking between 1.0 and 1.4 parsecs. A dashed line marks the median at 1.26 parsecs, and an arrow marks the Sun-to-Proxima distance of 1.30 parsecs, in the tallest part of the histogram." >}}

For systems near the middle of the census, the answer is remarkably consistent. The median is
1.26 parsecs, and four out of five fall between about 0.7 and 1.8 parsecs. Our own nearest
neighbor, Proxima at 1.30 parsecs, is about as typical as it gets. The Sun lives in an entirely
ordinary part of town.  Why is the nearest neighbor closer than the average spacing? Because stars 
aren’t laid out on a grid. Scattered at random, someone is almost always closer than average.

So here's the second rule of thumb worth carrying around: **in our part of the Galaxy, the next
star is about a parsec and a bit away.** That's about 30 million times the width of the Sun. At
Voyager 1's speed of 17 kilometers per second, a trip to Proxima would take about 75,000 years.
Light makes it in a little over four.

{{< clear >}}
---

## Two Units, by Design

So did the parsec win? Among professional astronomers, yes. Everywhere else, no -- and it was
never really supposed to.

That split wasn't an accident of popularity; it was written down at the start. In 1919 the
IAU's committee on notation recommended the light-year "especially in popular articles," and the
parsec -- "or preferably a unit 10 times as great" -- for technical work. Dyson had said much the
same at that 1913 meeting: light-years, he felt, had been introduced "for lecture purposes, not
for operations when your lecturer is working with the star."

Both units earn their place:

- The **light-year** is built from two ideas everyone already has, a year and the speed of light,
  and it carries a story no angle can: the light you see from Vega left it about 25 years ago.
- The **parsec** is the unit the measurements come out in, and the one the whole magnitude system
  is built on.

The prefixes work the same way for both. A kiloparsec is a thousand parsecs, about 3,260
light-years; a megaparsec is a million, about 3.26 million light-years. And the kiloparsec keeps
the parsec's original trick, one scale up: a parallax of 1 *milli*arcsecond means 1 kiloparsec.

---

## Wrapup

So why two units? Not out of redundancy, and not because one of them is right. The parsec is the
unit of measurement: it comes straight out of the parallax, and the magnitude system made it the
native unit of everything built on top. The light-year is the unit of experience: it was there
first, it's built from things everyone understands, and it tells you how long the light has been
on its way.

And now the parsec has a scale bar -- one you can find in a single patch of the December sky. By
late evening, Sirius is up in the southeast: 2.6 parsecs. Procyon is above and to its left: 3.5 pc.
Follow Orion's belt up to the right and you reach Aldebaran at 20 parsecs, sitting in front of the
Hyades at 47 pc, which have nothing to do with it. Keep going and you reach the Pleiades at 136 pc.

Back down in Orion's sword, the faint glow of the Orion Nebula is at about 390 pc. That's most of the
table, in one winter view -- and the faintest stars you can see between them stand in for the
Sun, moved out to 10 parsecs.

### Footnotes

[^startrek]: "Vulcan's Sun", Letter to the Editor, *Sky & Telescope*, July 1991.
