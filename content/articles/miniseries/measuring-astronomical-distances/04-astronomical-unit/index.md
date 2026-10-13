---
title: "Measuring the Astronomical Unit"
date: 2026-11-23
description: "The Earth-Sun distance is 93 million miles – but nobody could measure it directly. How Mars, Venus, an asteroid, and radar put a scale bar on a map astronomers had drawn centuries earlier."
byline: "It's a fundamental value – 93 million miles – but how was it determined?"
authors: ["bob-donahue"]
series: ["historical-perspectives"]
thumbnail: "thumbnail.webp"
banner: "banner.webp"
miniseries: "measuring-astronomical-distances"
miniseries-sequence: 4
---

## Introduction

{{< nbas-image src="banner.webp" fullwidth="true" caption="" >}}

At the end of [the last article](/articles/2026/11/the-speed-of-light/)
in the "Measuring Astronomical Distances" series,
we had the speed of light in hand and a promise: bounce a radar
signal off a planet, time the echo, and you have its distance – and
from that, the size of the astronomical unit itself.

That works, and this is where the story ends: the first radar
echo from Venus came back in 1961. But for three centuries before that,
astronomers were in a strange position. They had an excellent map
of the Solar System – every planet's orbit drawn in the right
proportions – and no scale bar.  Everything was measured relative
to the distance between the Earth and the Sun.

This article is about that scale bar. The rest of this series – from 
the first distance to a star to the parsec itself – is measured with it.

{{< clear >}}
---

## The Number: How Far Away is the Sun?

{{< article-table align="right" >}}

| Unit | Value |
| :--- | :--- |
| Meters | 149,597,870,700 (exact) |
| Kilometers | about 149.6 million |
| Miles | about 92.96 million |
| Light time | 499.0 s (8 min 19 s) |
| Solar parallax | 8.794″ |

{{< /article-table >}}

The astronomical unit – 1 AU – is *exactly* 149,597,870,700 meters.
That's not a measurement; since 2012 it has been the explicit definition.[^iau2012]
The table gives it in more familiar terms: about 93 million miles – a number
we all memorized in school – or the 8.3 light-minutes we've been using since the start of this series.

But that value has the same twist as the speed of light: "exact" is a strong word for
something that was a hard-won measurement for three centuries.  How it got that way is 
what this article unveils.

For most of that time, though, nobody quoted the AU in kilometers
or miles. Instead, they quoted an angle: the **solar parallax**, the size
of Earth's equatorial radius as it would look from the Sun – about
8.8 arcseconds. Smaller angle, more distant Sun. It's the natural
unit, because an angle is what astronomers could actually measure;
turning it into kilometers also needs the size of the Earth. (In
principle, two observers on opposite sides of the Earth would see
the Sun shifted by twice that, about 17.6″ – but only with the Sun
sitting on both their horizons, the worst place to measure anything.
Real pairs of observers get a fraction of that maximum value depending on where 
each of them is located.)

{{< clear >}}
---

## A Map With No Scale Bar

### Aristarchus: Right Geometry, Impossible Measurement

The first serious attempt is about 2,300 years old. Aristarchus of
Samos (c. 310 – c. 230 BCE) realized that at the exact moment of
half Moon, the Sun, Moon and Earth make a right triangle, with the
right angle at the Moon. Measure the angle between the Moon and the
Sun in the sky at that moment, and the shape of the triangle – and
so the ratio of the Sun's distance to the Moon's – follows.

{{< nbas-image src="fig-aristarchus-triangle.svg" fullwidth="true"
caption="At the moment of exact half Moon, our line of sight runs along the Moon's day/night line, so the right angle is at the Moon. Not to scale."
alt="Schematic of the Sun, Moon and Earth at half Moon. Sunlight lights the near half of the Moon; Earth’s line of sight runs along the Moon’s day/night line, so the Moon appears exactly half lit. The right angle is at the Moon, and the angle φ is measured at Earth. Not to scale." >}}
He took the angle to be 87°, "a quadrant less a thirtieth," proving
that the Sun is more than 18 but less than 20 times as far
away as the Moon.[^aristarchus]  The geometry of this method is flawless.  But the angle
he estimated isn't: the true value is about 89°51′, putting the Sun about 389
times farther than the Moon. Aristarchus was off by nearly three degrees – but the deeper 
problem is the target. The true angle falls only nine arcminutes short of a right angle, 
less than a third of the Moon's width, and the whole method depends on telling that sliver 
apart from nothing at all. With a measurement of 89°51′ you get 389; at 90° the Sun is infinitely 
far away.

{{< nbas-image src="fig-aristarchus-sky.svg" fullwidth="true"
caption="At the moment of exact half Moon, how far is the Moon from the Sun on the sky? Drawn to scale. The true answer is 89°51′, so the half Moon sits 9 arcminutes short of 90° – the line falls inside the Moon's own disk. Aristarchus put it at 87°."
alt="Two half Moons drawn to scale against a line marking 90° from the Sun. The real half Moon sits 9 arcminutes short of the line, overlapping it; Aristarchus's half Moon sits 3 degrees short, about six Moon-widths away." >}}

{{< nbas-callout title="Imagining the Scale" >}}
Every diagram of Aristarchus's triangle, including ours, cheats: the Sun is drawn far too close.
To draw it honestly, put the Earth and Moon one inch apart. The Sun then goes 389 inches away –
32 feet 5 inches – and is about 3.6 inches across. The Earth is a dot a thirtieth of an inch wide,
and the Moon less than a hundredth of an inch. From the Earth-dot, the lines to the Moon and to the
Sun make an angle just nine arcminutes short of a right angle.

But you don't need to build it. The next time you see a half Moon in the daytime sky with the Sun
still up, you're standing in the full-size model.
{{< /nbas-callout >}}

It's Galileo's hills from the last article all over again: the idea is right, only the measurement is out of reach.

Later Greek astronomers fared no better.[^eratosthenes] Hipparchus couldn't detect
_any_ parallax of the Sun at all, and just worked from an upper limit instead. 
Ptolemy arrived at 1,210 Earth radii, using the Moon's distance and the size of 
Earth's shadow during lunar eclipses[^ptolemy] – about 7.7 million km, off by a factor of nearly 20. 
Versions of that figure lasted into the 1600s: as late as the 1630s, the most
respected tables put the solar parallax at more than two arcminutes;
even Kepler's own estimate was about one.[^hornsby1763]

Others went back to Aristarchus's method. In the 1600s, Wendelin, timing the half Moon again and again, worked his way up to 89°45′ or
more; Riccioli, taking the middle of the few minutes during which the Moon looked exactly half lit, got about
89½°.[^kutrovatz] Closer – but at 89°45′ the triangle puts the Sun about 229 times as far as the Moon, and at
89½° only about 115. The method itself is the problem: near a right angle, the tiniest error in the angle
becomes an enormous error in the distance.

### Copernicus and Kepler: Every Distance But One

{{< article-table align="right" >}}

| Planet | Copernicus | Modern |
| :--- | ---: | ---: |
| Mercury | 0.376 | 0.387 |
| Venus | 0.719 | 0.723 |
| Mars | 1.520 | 1.524 |
| Jupiter | 5.219 | 5.203 |
| Saturn | 9.175 | 9.539 |

{{< /article-table >}}

Then the problem changed shape. In 1543, Copernicus worked out the
distance of every planet from the Sun – not in miles, but as multiples
of Earth's distance – from geometry alone.[^copernicus] For Venus,
it's one line: at its greatest angle from the Sun, the Sun–Venus–Earth
angle is a right angle, and the sine of that angle (about 46°) gives
0.72. The outer planets take one more step: time how long a planet
takes to go from opposition (opposite the Sun in our sky) to quadrature
(90° from the Sun). Knowing how fast Earth and the planet each circle
the Sun, that time gives the angle between them at the Sun – and at
quadrature the Sun–Earth–planet angle is a right angle, so the triangle
gives the planet's distance.[^spitz]

{{< nbas-image src="fig-copernicus-method.svg" fullwidth="true"
caption="How Copernicus measured the Solar System in units of Earth’s distance. Left: when Venus is farthest from the Sun in our sky, the angle at Venus is a right angle, so its distance from the Sun is the sine of that 46° angle: 0.72. Right: when Mars is 90° from the Sun in our sky, the right angle is at Earth; the angle θ at the Sun follows from how long it has been since opposition, and Mars’s distance is 1 / cos θ: 1.52."
alt="Two diagrams of circular orbits. Left: Sun, Venus and Earth form a right triangle with the right angle at Venus; the 46-degree angle at Earth gives Venus’s distance as 0.72. Right: Sun, Earth and Mars form a right triangle with the right angle at Earth; the angle θ at the Sun gives Mars’s distance as 1.52." >}}

In 1619, Kepler made it sharper still: his third law ties every
planet's orbital period to the size of its orbit.[^kepler] Periods
are easy to measure precisely, so by the late 1600s the _proportions_
of the Solar System were known well.

{{< nbas-image src="fig-au-map.svg" fullwidth="true"
caption="The Solar System to scale – with the length of the AU still unknown." 
alt="Two panels of circular planetary orbits around the Sun, drawn to scale in AU from Copernicus's values. Left: all six known planets out to Saturn at 9.175 AU. Right: Mercury, Venus, Earth and Mars enlarged. Each panel has a 1 AU scale bar labelled '1 AU = ? km'." >}}

That's the map with no scale bar. Every distance on it is known as
a multiple of one unknown – the AU. Which means the whole problem
collapses to a single measurement: if you can find **any one** distance in the
Solar System in miles or kilometers independently, every other one follows.

Not knowing the distance from the Earth to the Sun was more than
one missing number; it left a string of other unknowns behind it.
The planets’ angular sizes could be measured, but without their
real distances, their real sizes – and the Sun’s – couldn’t be
worked out. When Isaac Newton published his law of universal
gravitation in 1687, he could weigh Jupiter and Saturn against the
Sun from the orbits of their moons, because the unknown scale cancels
out of those comparisons. It doesn’t cancel for the Earth: comparing
the Moon’s orbit, measured in Earth radii, with Earth’s own orbit
needs exactly the number nobody had. The Solar System had a working
model, but much of its physical detail hung on that one value.

{{< clear >}}
---

## What You Can Actually Measure

As in the last article, we'll ask each measurement two questions:
what did it actually measure, and what else did it need to know?
Last time, the "what else" column emptied out. This time, watch it change:
first the size of the Earth, then the speed of light – and then
nothing at all.

| Year | Who | What they measured | What else they needed | Result |
| :--- | :--- | :--- | :--- | :--- |
| 1672 | Cassini & Richer | Mars's shift against the stars, Paris vs. Cayenne | The size of the Earth; Mars's distance in AU | 9.5″ (about 138 million km) |
| 1771 | Hornsby, from the 1769 transit | Timing of Venus crossing the Sun from five stations | The size of the Earth; the stations' longitudes | 8.78″ (about 150 million km) |
| 1822–24 | Encke, reanalysing 1761 and 1769 | The same timings, all stations | The same | 8.58″ (about 153 million km) |
| 1862 | Foucault, for Le Verrier | The speed of light, in the lab | Bradley's aberration; the size of the Earth | 8.86″ (about 148 million km) |
| 1877 | Gill | Mars's shift from one site, evening vs. morning | The size of the Earth | 8.78″ (about 150 million km) |
| 1941 | Spencer Jones, from Eros in 1931 | Eros's shift against the stars | The size of the Earth; Eros's orbit | 8.790″ ± 0.001″ |
| 1961 | JPL, Goldstone | Radar echo time, Earth to Venus and back | The speed of light | 149,598,500 ± 500 km |
| 2012 | IAU | – | – | 149,597,870.700 km, exact by definition |

---

## Mars: The First Real Number

The obvious way to measure a distance is the surveyor's way. Look
at the same object from two places a known distance apart, measure
how much it shifts against the background stars, and the triangle gives
the distance. Your thumb against a far wall, viewed with one eye
and then the other, is the same trick.

The Sun is a poor target for this – there are no stars behind it to measure against, 
and the shift is tiny. But the map says any distance will do. 
So, pick something closer (where the angle is larger).

{{< nbas-image src="fig-two-station-parallax.svg" fullwidth="true"
caption="Two observers at once: Cassini in Paris and Richer in Cayenne, 1672. From two places thousands of kilometers apart, Mars appears in slightly different positions against the distant stars. Side view, north up; the two sites also differ in longitude, which this view can’t show. Not to scale."
alt="Side view of Earth with Paris and Cayenne marked. Sight lines from each cross at Mars and continue to different points among distant stars, showing Mars’s apparent shift between the two observers." >}}

In 1672 Mars came to a close opposition, and the new Paris Observatory
was ready. Giovanni Cassini (with Jean Picard) observed from Paris;
Jean Richer had been sent to Cayenne, in French Guiana in South America, thousands
of kilometers away. Each measured Mars against nearby stars, and
the difference gave Mars's parallax: about 25″, putting Mars about
53 million km away. The map already said Mars was 0.381 AU away, so
one AU came out at about 138 million km – a solar parallax of
9.5″.[^britannica] That's about 7% short of the truth, and yet enormously larger than anything most
astronomers had imagined.

That same year, John Flamsteed in England did it without a second
observer. He measured Mars in the evening and again before dawn,
letting Earth's rotation carry him across thousands of kilometers
overnight, and concluded the solar parallax was no more than
10″.[^hornsby1763] Hold onto that; it comes back two centuries later.

{{< nbas-image src="fig-diurnal-parallax.svg" fullwidth="true"
caption="The one-observer method, seen from above the North Pole. Earth’s rotation carries the observer nearly a full Earth diameter between evening and dawn, so Mars appears in a slightly different place against the distant stars. Not to scale, and the planets’ own motions overnight are left out."
alt="Diagram of Earth seen from above the North Pole, with the Sun to the left and Mars to the right. An observer is marked at two points on Earth's edge, evening and before dawn. Sight lines from both cross at Mars and continue to different points among distant stars, showing Mars's apparent shift." >}}

There’s a catch the diagram leaves out. Between the evening sighting
and the one before dawn, the Earth doesn’t just turn – it also
travels more than a million kilometers along its orbit, while Mars
moves along its own. The combined effect is that Mars drifts against
the background stars overnight, and near opposition that drift is
roughly ten times larger than the shift the method is trying to
measure. What saves the method is that the drift is smooth and
predictable, while the parallax shift repeats every night as the
Earth turns. Measure Mars over several nights, and the two can be
pulled apart.

Eighty years later, Nicolas-Louis de Lacaille tried again from the
Cape of Good Hope, measuring Mars and Venus against the stars while
astronomers in Europe did the same.[^lacaille] His result, around
10″, was _worse_ than Cassini's. Better instruments didn't automatically
mean a better number – a theme this story will return to.

{{< clear >}}
---

## Venus: Halley's Plan

### The First Transit

{{< nbas-image src="Horrocks_observing_the_1639_transit_of_Venus_by_Eyre_Crowe.webp" width="300" align="right" 
caption="Eyre Crowe, *The Founder of English Astronomy* (1891), Walker Art Gallery, Liverpool. No portrait of Horrocks made in his lifetime survives; this Victorian painting imagines the scene. Public domain, via Wikimedia Commons."
alt="Victorian painting of Jeremiah Horrocks in a darkened room, watching the image of the Sun projected from a small telescope onto a sheet of paper." >}}

Venus passes directly between the Earth and the Sun – a **transit**
– in pairs eight years apart, and then more than a century between
pairs: the next two are in December 2117 and December 2125. 
The first one anyone observed was in 1639, by Jeremiah Horrocks, a
young English curate who had worked out that it would happen and
watched it projected through a small telescope onto a sheet of paper.

Horrocks also gave an estimate for the solar parallax, 14″, far
smaller than anyone before him.[^horrocks] It came from an assumption
rather than a measurement: he supposed every planet would look the
same size seen from the Sun – 28″ across – and applied that to the
Earth.[^imcce99] It put the Sun at about 94 million km: 63% of the
true distance, but a value closer than anyone had managed until then.

{{< clear >}}
### The Idea

{{< nbas-image src="halley-1716.webp" fullwidth="true"
caption="“Dr. Halley’s Dissertation on the Method of Determining the Parallax of the Sun by the Transit of Venus, June 6, 1761,” with its engraved plate of the transit geometry. Public domain, via Wikimedia Commons."
alt="Two facing pages of an old printed book. Left: the title page of Dr. Halley's Dissertation on determining the parallax of the Sun by the transit of Venus of June 6, 1761, noting that it was delivered to the Royal Society and published in its Transactions, No. 348. Right: an engraved plate titled The Theory of Venus's Motion, Parallax and other Phenomena, with geometric diagrams of Venus's path across the Sun's disk." >}}

In 1716, Edmond Halley published a way to turn the next pair of transits, 
in 1761 and 1769, into a measurement of the solar parallax "to within its 
five hundredth part."[^halley] He died in 1742, nineteen years before the first of them.

The idea itself wasn't Halley's. The Scottish mathematician James Gregory had pointed out in 1663 
that a transit of an inner planet could give the solar parallax. Halley made the idea practical: he had 
timed a complete transit of Mercury himself from St Helena in 1677, described a working method 
to the Royal Society in 1691, and published the full plan in 1716.[^vangent]

Halley's insight was to trade an angle for a clock.  Observers at widely separated latitudes see 
Venus at slightly different locations against the Sun's disk, so it crosses on slightly different paths – different 
chords of the circle.  A chord nearer the middle is longer and takes more time to cross. So instead of measuring 
a tiny angle, each observer times how long the transit lasts, and the difference 
in durations between stations gives the shift between their chords. That shift is the parallax – Venus's 
against the Sun's – and the map turns it into the AU.

{{< nbas-image src="fig-transit-chords.svg" fullwidth="true"
caption="Two observers, two chords: the farther Venus's path lies from the Sun's center, the shorter the crossing. Illustrative numbers, not a real transit; the gap between the paths is drawn five times larger than it is."
alt="The Sun's disk with two parallel paths of Venus across its lower part. Path A, 600 arcseconds from the center, takes 6 hours 7 minutes; path B, 20 arcseconds farther out, takes 5 hours 59 minutes, a difference of about 8 minutes." >}}

{{< nbas-callout title="From a clock to an angle" >}}
(using illustrative numbers, not a real transit)

The Sun's disk is about 1,900″ across, and Venus creeps over it at about 4 arcminutes an hour. 
If, for one observer, Venus's path lies 600″ from the Sun's center, the crossing takes a little over six hours.

Now let a second observer, far to the north or south, see Venus's path shifted by 20″. Their transit is 
about **8 minutes** longer or shorter. Eight minutes is easy to measure; 20″ against the blazing face 
of the Sun is not.

Working backward: a timing error of 1 second becomes an error of about 0.04″ in that 20″ – one part 
in 500, Halley's figure. A 10-second error makes it one part in 50.
{{< /nbas-callout >}}

Halley's method has one drawback: each station has to see the whole transit, start and finish. Joseph-Nicolas Delisle proposed 
a variant that needed only one contact – the moment Venus touches the edge, say – timed at each station, 
then compared. The problem is that the stations must agree on the **absolute** time, which means knowing 
their longitudes precisely – the same longitude problem that had astronomers timing Io's eclipses in the last article.[^vt2004]

### 1761 and 1769

{{< nbas-image src="Venus_Drawing-1769.webp" width="400" align="right"
caption="Venus at the edge of the Sun, 1769, as drawn by Captain James Cook (top) and Charles Green (bottom), observing side by side at Tahiti. *Philosophical Transactions* 61 (1771), Table XIV. Public domain, via Wikimedia Commons."
alt="Engraved plate of two sets of numbered drawings, one by Cook and one by Green, showing Venus at successive stages of crossing the Sun's edge. Several stages show a hazy ring around Venus and a dark neck joining it to the Sun's edge." >}}
The 1761 transit drew observers across Europe and beyond, and the results disappointed: depending on who reduced the observations, the solar parallax came out anywhere from about 8.5″ to 10.5″. Two things were blamed – poorly known 
longitudes at many stations, and something odd happening at the edge of the Sun.[^vt2004b]

For 1769, Britain sent parties to the North Cape, Hudson Bay, and
Tahiti, where James Cook's expedition set up Fort Venus and two
outlying stations. The sky on June 3 was clear, and every observer
recorded the transit.[^orchiston] And then the odd thing happened
again. Cook wrote that "we very distinctly saw an Atmosphere or
dusky shade round the body of the Planet which very much disturbed
the times of the contacts," and that the observers "differ'd from
one another in observeing the times of the Contacts much more than
could be expected."[^cook]

{{< nbas-image src="Venus_Transit_Black_Drop_extreme_(7350314908).webp" width="250" align="right" 
caption="The black drop. Jeff Barton from Richardson, TX, USA, CC BY 2.0, via Wikimedia Commons" 
alt="Photograph of Venus as a dark disk just inside the Sun's edge, still joined to the edge by a short dark neck: the black-drop effect." >}}
That's the **black drop**. Just as Venus's disk comes fully onto the Sun, instead of a clean break 
between the two edges, a dark neck seems to tie Venus to the Sun's edge, then snaps. When exactly 
did the contact happen? Observers standing side by side disagreed; in 1761 they couldn't fix 
the moment of contact to better than 30 seconds, or even a minute.[^pasachoff] Go back to the box above: on 
those numbers, 30 seconds of uncertainty is a 6% error in the answer, and a full minute is 12%.

For two centuries the usual explanation was Venus's atmosphere. It isn't. In 1999 a spacecraft above 
Earth's air photographed a transit of **Mercury** – a planet with no atmosphere to speak of – and _also_ saw 
a black drop. The real cause is the telescope's own slight blurring combined with the way the Sun's disk darkens 
toward its edge; Earth's turbulent air makes it worse.[^schneider]

{{< clear >}}
### The Right Answer, Then the Wrong One

In 1771, Thomas Hornsby at Oxford combined the Tahiti timings with those from four other stations and got a solar parallax of 8.78″[^hornsby1771] – within a fifth of a percent of the modern value.
Hornsby's own distance came out a little long: 93,726,900 miles, largely because he took Earth's radius to be 3,985 miles. 
Right parallax, slightly wrong Earth – the "what else they needed" column at work.

{{< nbas-image src="max-hell-varda-sammi.webp" width="200" align="right"
caption="Maximilian Hell (Hell Miksa) in Sámi clothing at Vardø for the 1769 transit of Venus. Credit unknown, possibly W. Pohl, Vienna, 1771. Public domain, via Wikimedia Commons."
alt="Portrait of Maximilian Hell wearing Sámi clothing." >}}
Fifty years later, Johann Encke, in Berlin, reanalysed everything from both transits, carefully and comprehensively. 
His answer, 8.58″, became the standard; the British *Nautical Almanac* used it from 1834 to 1869.[^eb1911] But 
it was 2.5% too small, putting the Sun about 4 million km too far away. His more thorough analysis gave the worse answer.

Why? A large part of the answer is one observer. Maximilian Hell, a Jesuit astronomer, had observed the 1769 
transit from Vardø, in the far north of Norway – one of the most valuable stations, because of its latitude. 
He was slow to publish, and Encke distrusted him. In the 1830s the Vienna astronomer Karl Ludwig von Littrow 
examined Hell's notebook and concluded that the timings had been altered after the fact, in a different ink. 
Encke accepted the charge.[^aspaas]

In the early 1880s, Simon Newcomb examined the same notebook. There was no different ink – the odd-looking
marks came from a defective pen – and von Littrow, it turned out, was color-blind. Newcomb published the
vindication in 1883.[^aspaas] And when he reworked both eighteenth-century transits himself, Hell included,
he got 8.79″.[^hudon] The data had held the right answer all along.

{{< nbas-callout title="Meanwhile, the stars" >}}
In 1838 – while Encke's too-large AU was still the official one – Friedrich Bessel measured the first
distance to a star, 61 Cygni. Its parallax was 0.314″, give or take 0.020″.

A star's parallax is measured with Earth's orbit as the baseline, so it gives the distance **in AU**,
with no need to know how long an AU is: about 657,000 AU for 61 Cygni. The AU only mattered when
you wanted the answer in miles.

And Encke's 2.5% error was the smaller problem. Bessel's own stated uncertainty was about 6%, and
the modern parallax, 0.286″, puts 61 Cygni about 10% farther away than he found. 
{{< /nbas-callout >}}

{{< clear >}}
---

## Borrowing the Speed of Light

Encke's value started to come apart in the 1860s, from directions that had nothing to do with Venus. 
Peter Andreas Hansen found that a small wobble in the Moon's motion, which depends on the Sun's 
distance, wanted a parallax near 8.97″.[^eb1911] Urbain Le Verrier, working from the motions 
of the planets, concluded the AU was about 3% smaller than Encke's – and if so, then the speed of light, 
which astronomers were still getting from Bradley's minutes-per-AU, had to be about 3% smaller too.[^bea]

{{< nbas-image src="fig-foucault-mirror.webp" fullwidth="true"
caption="Foucault's rotating mirror, from the last article: the measurement that settled the AU in 1862 was a measurement of the speed of light."
alt="Diagram of Foucault's rotating-mirror apparatus: light from a source bounces off a spinning mirror to a fixed mirror and back, and returns beside the source because the spinning mirror has turned slightly." >}}

This is where the last article left Léon Foucault: Le Verrier wanted a better speed of light. 
In 1862 Foucault measured it in the lab, 298,000 km/s, and with Bradley's aberration that gave 
the solar parallax as 8.86″.[^foucault] He overshot slightly – but Encke was finished.

Notice which way the dependency now runs. Rømer and Bradley needed the AU to get the speed of light. 
Foucault used the speed of light to get the AU.

But a value borrowed from the speed of light was only as good as the two measurements behind it,
Foucault's and Bradley's. And two more transits of Venus were coming, in 1874 and 1882.

{{< clear >}}
---

## Back to Venus: 1874 and 1882

{{< nbas-image src="1874-venus-luxor.webp" width="400" align="right"
caption="The 1874 transit, photographed from Luxor, Egypt, by William de Wiveleslie Abney. Public domain, via Wikimedia Commons."
alt="Nineteenth-century photograph of the Sun during the 1874 transit of Venus, taken from Luxor, Egypt." >}}

This time there was money, photography, and much better telescopes. But the results were 
barely better than the old ones![^eb1911] American photographs gave 8.77″ to 8.89″, depending on how 
they were measured; German heliometer measurements gave about 8.88″.

Here is the twist: all the contact timings from all the parties, combined, gave 8.794″[^eb1911] – today's value, 
to the last digit. But the photographs and the heliometers said something else, and nobody could decide which 
to believe. A right answer you can't recognize isn't much use. 
More effort doesn't fix a measurement when the source of the error hasn't been understood.

That failure turned astronomers back to where Cassini had started: Mars, and things like it.[^eb1911]
(The next transits of Venus weren't due until 2004 and 2012.)

{{< clear >}}
---

## Better Targets

But why go back to Mars?  That sounds like a step backward. 
At a transit, Venus is about 0.28 AU from Earth – closer than Mars ever gets.

{{< nbas-image src="David_Gill.webp" width="200" align="right"
caption="Sir David Gill (1843–1914). Photograph by J. E. (John Jabez Edwin) Mayall (1813–1901). Public domain, via Wikimedia Commons." 
alt="Photographic portrait of the astronomer Sir David Gill." >}}

The reason is that at a transit you aren't measuring just Venus:
you're measuring Venus **against the Sun** – and when an observer
moves, the Sun shifts too, by its own (smaller) parallax. What's left is the difference: about 23″ per Earth 
radius of baseline. Mars at a good opposition, at 0.377 AU, gives… about 23″. Practically a tie. The 
real differences are everything else that makes Mars a better target: Mars can be measured at night, 
against stars, over and over again, at every good opposition; Venus offers two pairs of transits in 
250 years and the problem of the black drop.

In fact, David Gill had gone back to Mars even before the last transit. In 1877, between the two, he took a
heliometer – a telescope with a split lens, built for measuring small angles precisely – to Ascension Island in the South Atlantic for Mars's opposition. He used Flamsteed's method: one site, 
evening and morning, Earth's rotation supplying the baseline. His result: 8.78″.[^eb1911]

Gill then moved on to minor planets. A planet like Mars shows a disk, and measuring the center 
of a disk is harder than measuring a point – but an asteroid does look like a point. Campaigns he organized on 
7 Iris and 80 Sappho in 1888 and 12 Victoria in 1889 gave 8.812″, 8.798″ and 8.801″, with a mean of 8.802″.[^eb1911]

Then, in 1898, Gustav Witt discovered asteroid 433 Eros,[^imcce105] and here "closer is better" finally 
applies. Eros can come much nearer than Mars – 0.32 AU in 1901, 0.17 AU in 1931[^nssdc] – and at 0.17 AU 
its parallax is about 52″ per Earth radius, more than twice what Mars or Venus can offer.

{{< nbas-image src="fig-eros-orbit.svg" fullwidth="true"
caption="Why Eros was worth waiting for. Its stretched orbit brings it much closer to Earth than Mars ever comes: in January 1931 it passed within about 0.17 AU. Seen from above, to scale."
alt="Top-down diagram of the orbits of Earth, Mars and the asteroid Eros around the Sun, to scale. Eros’s elongated orbit comes close to Earth’s on one side, where the two planets are marked at their January 1931 closest approach, about 0.17 AU apart." >}}
The 1931 approach drew an international campaign. Reducing all of it took ten years; in 1941 
Harold Spencer Jones, the Astronomer Royal, announced a solar parallax of 8.790″ ± 0.001″.[^imcce105]

{{< clear >}}
---

## Beating Down the Error

### Precise, But Not Accurate

That ± 0.001″ is worth a closer look, because the right answer is 8.794″ – four times the stated uncertainty away.

That doesn't mean Spencer Jones got his arithmetic wrong. An error bar like that describes how well 
the measurements agree with one another: it's a statement of **precision**. It can't account for an 
effect nobody has thought of, which shifts every measurement the same way – a question of **accuracy**. 
His own obituary called the result disappointing and suspected some systematic error in this kind of 
parallax work.[^baa] Nobody has pinned down exactly what it was; looking back, one modern review simply
calls the historical error bars "all too optimistic about their external accuracy."[^mignard]

A rival value tells the same story from the other side. Eugene Rabe, using the way Eros's 
orbit is pulled by the Earth and Moon, got 8.7984″ ± 0.0004″ in 1950[^baa] – an even smaller 
error bar, off in the other direction. In 1967, a reanalysis found a mistake in one step of his orbit calculation.[^imcce106]

{{< nbas-image src="fig-au-error.svg" fullwidth="true"
caption="Three centuries of measuring the AU: how far each result was from today’s value. Up-pointing triangles made the Sun too far away, down-pointing ones too close. Progress was not steady: Hornsby’s 1771 answer was better than Encke’s fifty years later."
alt="Chart of the error in the astronomical unit against year, on a logarithmic scale from 10% to 0.0001%. Errors fall from about 7–14% in the 1600s and 1700s to about 0.05% by the 1940s, with Encke’s 1820s result (2.5%) worse than Hornsby’s 1771 result (0.16%); the 1961 radar result is off by 0.0004%." >}}

### Radar

Radar – finally – ended the angle-measuring business altogether. Send a radio pulse to Venus, 
time the echo, multiply by the speed of light, divide by two: that's the distance, with no triangle at all.

The first attempts didn't hold up. Lincoln Laboratory reported an echo from Venus in 1958, and 
Jodrell Bank seemed to confirm it in 1959, but neither could repeat the result.[^airspace] 
On March 10, 1961, the Jet Propulsion Laboratory's antenna at Goldstone, California, detected 
Venus unambiguously. Over the following two months, its echoes gave the AU as 149,598,500 ± 500 km[^radar] – within 
about 600 km of today's value. Several other groups soon made the same measurement.[^nbs]

These echoes came around the inferior conjunction of April 1961, when Venus passes between the Earth and
the Sun and is closest to us, about 0.28 AU away. It doesn't cross the Sun's face: Venus's orbit
is tilted slightly, so at most conjunctions it passes a little above or below the Sun. That's why transits
are so rare.

The answer was needed for more than tidiness. JPL's Richard Goldstein later recalled that if 
Mariner 2 had been aimed using the older value, it might have missed Venus by more than 100,000 miles.[^airspace] 
(The Sun's gravity delays radar echoes too – the effect we met at the end of the last article – but it
matters most when Venus is on the far side of the Sun and the signal grazes it. Near inferior conjunction
the echoes don't pass close to the Sun, so the correction is small.)

The International Astronomical Union adopted the radar value in 1964.[^imcce106] Now the only thing 
in the "what else they needed" column was the speed of light – and that had just been measured to 
better than a part in a million.

### From Measurement to Definition

In 1976 the IAU defined the AU through a constant of gravity: the length for which the 
"Gaussian gravitational constant" takes a fixed value.[^iau2012] That definition, which tied the AU 
to the mass of the Sun, didn't last. Relativity made it awkward – the value depended on the 
frame of reference you measured in – _and_ the Sun is slowly losing mass. In 2012 the IAU cut the knot: 
1 AU is 149,597,870,700 meters, exactly.[^capitaine]

For most of this story the two numbers lived in a tangle. Rømer and Bradley could give the speed of light
only in minutes per AU, while parallax measurements gave the AU in kilometers with no help from light at
all. From 1849, Fizeau's toothed wheel gave the speed of light a kilometer value of its own – and in 1862
the two independent routes met for the first time. The route through the speed of light won. A century
later, radar made the AU depend on the speed of light alone.

Today both are fixed the same way – the speed of light in 1983, the AU in 2012 – each measured so well
that it was made exact.

---

## Wrapup

The Solar System's proportions were known for centuries before its size. Aristarchus had the right geometry 
and an angle impossible to measure; Copernicus and Kepler drew the map; Cassini put the first real number 
on it by looking at Mars from two continents. Halley traded an angle for a clock, and the black drop – which 
turned out to have nothing to do with Venus – smeared the clock. Hornsby got the right answer and Encke, 
more thoroughly, a worse one, thanks partly to a color-blind accuser. Gill and Eros gave the angle 
a better target, and radar replaced the angle with an echo.

And the two constants leaned on each other the whole way: Rømer needed the AU to get the 
speed of light; radar needed the speed of light to get the AU.

One distance, measured in real units, unlocks every other one in the Solar System. The next 
step is to use the AU itself as the baseline – Earth on one side of its orbit, then the other – and reach for the stars.

---

#### Footnotes

[^iau2012]: IAU 2012 Resolution B2, "on the re-definition of the astronomical unit of length." The resolution also quotes the 1976 definition.
[^aristarchus]: Aristarchus, *On the Sizes and Distances of the Sun and Moon*, hypothesis 4 and proposition 7; see also S. van der Werf & T. van Albada, "An explanation for Aristarchus' measurement of the sun's distance," *Comptes Rendus. Physique* 26 (2025), 381–391.
[^kutrovatz]: G. Kutrovátz, "Aristarchus' lunar dichotomy as an actual measurement," *Polanyiana* (2021), citing A. Van Helden, *Measuring the Universe* (Chicago, 1985).
[^ptolemy]: C. C. Carman, "Rounding numbers: Ptolemy's calculation of the Earth-Sun distance," *Archive for History of Exact Sciences* 63 (2009), 205–242.
[^hornsby1763]: T. Hornsby, "A Discourse on the Parallax of the Sun," *Philosophical Transactions* 53 (1763).
[^eratosthenes]: One late source, Eusebius, reports a solar distance attributed to Eratosthenes. Read one way, the Greek gives a figure startlingly close to the modern value; read another, it's far too small – and the *Dictionary of Scientific Biography* dismisses the report entirely. It makes a good story, and we can't stand behind it. (Eusebius, *Praeparatio Evangelica* XV.53; translations give 4,080,000 or 804,000,000 stadia.)
[^copernicus]: N. Copernicus, *De revolutionibus orbium coelestium* (1543). Saturn (9.175) and Jupiter (5.219) as given in B. R. Goldstein, "Copernicus and the Origin of His Heliocentric System," *Journal for the History of Astronomy* 33 (2002), 219–235; inner planets as commonly tabulated.
[^spitz]: The method as reconstructed in "Copernicus' Method," Spitz Inc. blog (2018).
[^kepler]: J. Kepler, *Harmonices Mundi* (Linz, 1619), Book V.
[^britannica]: *Encyclopaedia Britannica*, "Parallax: Solar parallax."
[^lacaille]: "Nicolas-Louis de Lacaille," *Sky & Telescope*, October 2017, p. 38.
[^horrocks]: *Dictionary of Scientific Biography*, "Horrocks, Jeremiah"; *Encyclopaedia Britannica* (1911), "Horrocks, Jeremiah."
[^imcce99]: IMCCE, "À la recherche de la parallaxe solaire (3/11)," *Lettre d'information* 99 (March 2014).
[^halley]: E. Halley, "A New Method of Determining the Parallax of the Sun, or His Distance from the Earth," *Philosophical Transactions* 29 (1716); English translation in the *Abridged Transactions*, vol. VI (1809).
[^vangent]: R. H. van Gent, "The Transits of Venus of 1761 and 1769," Transit of Venus Bibliography, Utrecht University (online).
[^vt2004]: ESO/IMCCE, Venus Transit 2004 project, information sheet 5b.
[^vt2004b]: ESO/IMCCE, Venus Transit 2004 project, information sheet 20b.
[^orchiston]: W. Orchiston, "James Cook's 1769 transit of Venus expedition to Tahiti," *Proceedings of the IAU* (2005).
[^cook]: J. Cook, journal entry for 3 June 1769 (ship's date 4 June), South Seas project transcription.
[^schneider]: G. Schneider, J. M. Pasachoff & L. Golub, "TRACE observations of the 15 November 1999 transit of Mercury and the Black Drop effect," *Icarus* 168 (2004).
[^pasachoff]: J. M. Pasachoff, G. Schneider & L. Golub, "The black-drop effect explained," *Proceedings of the IAU*, IAU Colloquium 196 (2004), 242–253.
[^hornsby1771]: T. Hornsby, "The Quantity of the Sun's Parallax, as Deduced from the Observations of the Transit of Venus, on June 3, 1769," *Philosophical Transactions* 61 (1771).
[^eb1911]: *Encyclopaedia Britannica* (1911), "Parallax," section on solar parallax.
[^aspaas]: P. Aspaas & L. Kontler, *Maximilian Hell (1720–92) and the Ends of Jesuit Science in Enlightenment Europe* (Brill, 2020), pp. 299–303. Newcomb's vindication appeared in *Monthly Notices of the RAS* (1883).
[^hudon]: D. Hudon, "A (Not So) Brief History of the Transits of Venus," *Journal of the RASC*, Table 3 (Newcomb, 1891: 8.79″ ± 0.051″).
[^bea]: *Biographical Encyclopedia of Astronomers*, "Foucault, Jean-Bernard-Léon."
[^foucault]: Obituary of Léon Foucault, *Proceedings of the Royal Society*. Foucault's own papers: *Comptes rendus* 55 (1862).
[^imcce105]: IMCCE, "À la recherche de la parallaxe solaire (9/11)," *Lettre d'information* 105 (October 2014).
[^nssdc]: NASA NSSDC, "Near-Earth Asteroid 433 Eros."
[^baa]: Obituary of Sir Harold Spencer Jones, British Astronomical Association.
[^imcce106]: IMCCE, "À la recherche de la parallaxe solaire (10/11)," *Lettre d'information* 106 (November 2014).
[^mignard]: F. Mignard, "The Solar parallax with Gaia," technical note, ESA/OCA.
[^airspace]: "Before Launching Probes to Venus, NASA Had to Figure Out Exactly Where It Was," *Air & Space* / Smithsonian.
[^radar]: Wikipedia, "Radar astronomy"; the same value, in miles, appears in NASA's Mariner II telecommunications report (1963).
[^nbs]: G. H. Pettengill, "A Review of Radar Studies of Planetary Surfaces," *Journal of Research of the NBS* 69D (1965), 1617–1623.
[^capitaine]: N. Capitaine, B. Guinot & S. Klioner, "Proposal for the re-definition of the astronomical unit of length" (2011).

---
