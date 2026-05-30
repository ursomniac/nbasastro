---
title: "Coordinates Systems in the Sky"
date: 2026-05-05
description: "Learn about three key coordinate systems used in astronomy, including Equatorial, Ecliptic, and Galactic."
byline: "The different coordinate systems and what they're used for"
authors: ["bob-donahue"]
series: ["how-the-sky-works"]
knowledgetopics: ["observing"]

---

## Introduction

Almost as soon as you start looking at the sky, or planning observations you're
confronted with a series of terms, and enough geometry that you're immediately 
re-living high-school math class.   Here's some explanation as to what some of these
terms mean and why they're useful/important.

## Coordinate Systems

In astronomy there are three coordinate systems that are used:

- **Equatorial**: based on the celestial poles and the equator. These are defined by 
the rotation of the Earth, where "up" or "down" corresponds to the point in the sky 
above/below the North and South Poles.   In the North that location is very close to the
position of Polaris, the "North Star" (Southern Hemisphere observers aren't quite as fortunate:
the "South Star" is &sigma; (Sigma) Octantis, which is barely visible to the naked eye.

  This the system you'll mostly deal with for amateur observations.

- **Ecliptic**: based on the Earth's orbit around the Sun.  All the planets and the Moon move along the Ecliptic (mostly) though because each planet/Moon has it's own orbital inclination, 
they might be slightly above or below the Ecliptic.  Like the Equatorial system, there are 
also North and South Ecliptic "poles" (the North in Draco, and the South in Dorado).

  For observing, this is mostly helpful in measuring things like elongations of the planets
  and other solar-system objects (comets and asteroids) from the Sun (how many degrees they are from the Sun's position).  

- **Galactic**: based on the plane of the Milky Way. 

  For observing we don't think about this too much: but it's a little helpful in understanding
  why certain types of objects tend to have low "galactic latitudes" or high ones.   
  Open clusters and most nebulae tend to be in the disk of the galaxy, so you'll find them 
  closer to the Milky Way;  galaxies are all over, but harder to see if they're at low
  galactic latitudes: the Milky Way is "in the way"!   

{{< nbas-image src="GalLongLat_ofStar.jpg"
align="left" width="400" >}}

  Globular clusters are slightly different:
  they tend to cluster close to the Milky Way, when you're looking "inward" during the Summer 
  because you're looking "toward" the center, but above or below the plane.  Since the Sun is
  out in the spiral arms of the galaxy, these clusters are mostly found surrounding 
  the Milky Way's bulge. (But there are always exceptions.)

  The North Galactic Pole is in Coma Berenices, the South in Scluptor, and it's not 
  surprising to find that around those constellations you find many more galaxies then in the
  constellations closer to the Milky Way (though they're there too - just harder to see).

## How they're All Arranged and Defined

{{< nbas-image src="Ecliptic_equator_galactic_anim.gif"
align="right" width="400" caption="Wikipedia commons" >}}

So each of them a have an equator and poles, and like latitude and longitude defining 
locations on the Earth, each has a latitude and a longitude:

{{< article-table title="Coordinate System Definitions" align="left" >}}

|   System   |  Latitude  | Longitude  | 0° at |
| :========= | :========= | :========= | :=================  |
| Galactic   | <i>l</i>   | <i>b</i>   | the Galactic Center |
| Ecliptic   | &lambda;   | &beta;     | Vernal Equinox      |
| Equatorial | Declination (&delta;)   | Right Ascension     | Vernal Equinox      |

{{< /article-table >}}

And like latitude and longitude they're measured in degrees:  0°to 360° for longitudes,
and -90° to +90° for latitudes.

With one exception.

Right Ascension is measured in **_hours_** (0h to 24h).   How does THAT work?

{{< clear >}}

### Why is Right Ascension measured in time and not degrees?

The reason for this is because the Earth is rotating.  Before telescopes with clock 
drives and tracking, astronomers mostly set up their telescopes pointing South (or North 
in the Southern Hemisphere) and moved then up or down in altitude.  Then they could take
measurements of an object's position based on how far it was from the horizon (the _altitude_,
measured in degrees from 0° to 90° overhead), and just wait for objects to cross 
the _meridian_ in front of the eyepiece's field of view.

So, one rotation = 24 hours.  Easy.
{{< nbas-image src="sidereal_solar_explanation.jpg"
align="left" width="400" >}}

But *that's* not right either!   In that 24 hours, the Earth has _also_ moved around the Sun
a bit, so that if you observed a star at precisely 10:15:27.3 PM on one night, it wouldn't 
cross at the same time the next night.  In fact, it'd happen 3m 56s earlier.

{{< clear >}}

### What is the Vernal Equinox?

Latitude is easy because there are specific points for the poles: once you know where 
they are, you can measure the angular distance from either pole and confidently know
you latitude.  Just like on the sky with latitudes or declinations.

{{< nbas-image src="Prime-meridian.jpg" width="500" 
align="right" caption="Wikimedia commons" >}}
Longitude is different:  there's no specific "zero point" - and basically you have to 
arbitrarily set one.   On Earth, "zero longitude" is set at a point at the Greenwich 
Observatory in England (the French also tried to set this at a point in Paris at one 
point).   And that's it.  Someone "decided" here's 0° and everyone went along with it.

For the Galactic coordinate system that 0° point is defined as the Galactic Center, though
no one knows _exactly_ where that **is**, but they have a good idea, and astronomers have
just agreed on one location that's "close enough".

For the other two 0° (and 0h) is in the same place.   It's where they intersect, defined by
the point where when the Sun is in that position, days and nights are equal:  in other words
the instant Spring begins.

You'll have noticed from the diagram that all three systems are at angles to each other:
23.44° between the Equatorial and Ecliptic systems, and 62.6° between the Equatorial and
Galactic planes.   The first is due to the tilt of the Earth axis.   The second is the "tilt"
between solar system and the Milky Way itself.   Because the planets (and in particular the
Earth) formed in a disk around the Sun, how that disk was tilted with respect to the Galaxy
at-large is random.

### What do you mean the coordinates are shifting?

As if things weren't complicated enough, all the coordinates you measure are _changing_.
Very slowly, but changing.

You might've read that Polaris hasn't always been the North Star, and the location of 
"North" with respect to the background stars changes over time.   This is the 26,000-year
_precession_ of the Earth's axis - the "wobble" that it has.

{{< nbas-image src="precession-earth-zodiac.png"
align="right" width="400" caption="Human Origin Project" >}}

What this does is it moves that Vernal Equinox point westward over time.  Right now it's in 
Pisces.  It _used_ to be in Aries (and sometimes you'll hear referred to as "the First Point
of Aries" because that's where it was about 2000 years ago), and eventually (a little over
500 years from now) it'll move into Aquarius.

**But** because of that shift, and because the equatorial 0h location is _also_ tied to that
point, _all the RA and Dec coordinates are changing all the time_!   To get around _that_
astornomers refer all the Equatorial and Ecliptic coordinates to an _epoch_.  These days
2000 is used, before that it was 1950, then 1900, and then 1875.  (No idea what the plans are
for 2050, if any).

**And** of course that's not the _only_ thing that affect's a star's coordinates!  They're 
also moving around the Galaxy in their own orbits, so there's drift there too over time
(most noticeable for the stars closest to the Sun).  But that's for another article.


