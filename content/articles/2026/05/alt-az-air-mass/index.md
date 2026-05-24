---
title: "Altitude, Azimuth, and Air Mass"
date: 2026-05-15
byline: "Three angles that affect observing"
authors: ["bob-donahue"]
series: ["how-the-sky-works"]
knowledgetopics: ["observing"]
math: true
---

## Introduction

Where you observe sometning in the sky, it's sometimes important to consider it's 
position in the sky relative to the horizon.


## Altitude and Azimuth

{{< nbas-image src="horizontal-coordinate-system.png" width=500 align="right" >}}
Just like the other coordinate systems we've discussed in the article 
[Coordinate Systems in the Sky]({{< relref "articles/2026/05/coordinate-systems/index.md" >}}),
there's also the 
_Horizontal_ coordinate system, defined by _altitude_ and _azimuth_.

Unlike the others, this system is completely dependent on the observer's location, and
the date and time.    Why it's useful is that - it relates to the observer's location 
and the date and time.

### Altitude

Altitude is simple - it's how many degrees above the horizon and object lies at that instant.
Overhead is 90°.  (Also, the declination at the zenith is equal to your latitude.)

### Azimuth 

Azimuth is basically the compass heading:  North is 0°, East is 90°, South is 180°, and
West is 270°.  

{{< nbas-image src="CS-z-m-riseset.jpg" width=500 align="left" >}}
As objects cross the sky, they'll rise at a particular azimuth (related to their declination)
on the horizon, traverse to the _meridian_ (the line going from N to S crossing overhead), 
and then set at another azimuth.

Objects with low declination never rise very high above the horizon:
(if you love the math, $ Alt_{max} = 90° - | L - \delta | $
where $L$ is the observer's latitude and $\delta$ is the declination of the object).
That's why when the Moon and planets are in the ecliptic 
constellations like Scorpius and Sagittarius, they're not close to overhead like they are
with Taurus and Gemini (from the Berkshies).

That also means that objects with very high declinations (more math: those with $| \delta | \ge 90^\circ - |L|$ - or anything north of +47.3° here in the Berkshires) never rise or set: 
they're _circumpolar_.   At the equator, nothing is circumpolar;  at the North or South 
poles, _everything_ is circumpolar.

And - you may have guessed - objects that are far south (below -47.3° declination) never 
come up over the horizon.  So we'll never get to see the Magellanic Clouds, or the Southern
Cross, or Alpha Centauri. 😕   (But our Southern Hemisphere counterparts never get to see
the Big Dipper, either.)

## Airmass

{{< nbas-image src="Air-Mass-Angles-01-1.jpg" width=500 align="right" >}}
You may have noticed that objects closer to the horizon are dimmer than overhead, or that
it's harder to see fainter stars until that area of sky is higher in altitude.  Aside from
light pollution (another topic for another time), this is an effect _airmass_.

Think of it this way.  When you're standing on a globe and looking "up" you are looking 
through **one** air mass, the atmosphere and into space.   But if you're not looking
straight up, that means you're looking "out" but at an angle so the light you're seeing
has to travel through more atmosphere &mdash; more _airmass_ to reach you.

As you get closer to the horizon, that's a **lot** of atmosphere, and the fainter stars
get pretty much attenuated along the way.

(Here comes the math:  this can be modeled with sec(z) where $z$ is the distance from 
overhead or sec (90°-Alt.)".  The "sec" is for secant and you might remember that's the
inverse of the cosine, so it's also $1. / \cos(z)$.)     When $z$ = 0° that's sec($z$) = 1.
As $z$ approaches 90° (the horizon) sec($z$) blows up going to infinity (which I suppose
"the ground" pretty much does the job).

But at what point are you looking through 2 airmasses?   30° altitude, or 60° down from
zenith.   4 airmasses?  14.5° altitude (or 75.5° down from zenith).

## Atmospheric extinction

Another important consideration &mdash; especially for astronomical imaging is _extinction_.
The closer an object is to the horizon, the thicker the atmosphere, which causes low
objects to appear fainter.   How much fainter?  On average for visual observing it's about
0.15 &ndash; 0.20 magnitudes per airmass.  That doesn't like much but for faint extended
objects like nebulae and galaxies, it can have a profound effect.   

So your 3rd magnitude star only 15° above the horizon will be almost a magnitude fainter
then if it's overhead.  And that's assuming completely dark skies:  light domes from cities,
and light pollution overall will decrease that more.

It's also wavelength
dependent:  blue light suffers great extinction than red;  you already see this with 
every sunrise and sunset with the red solar disk as it huge the horizon.  Blue and violet
light scatter more in the atmosphere (Rayleigh scattering) - it's why the sky is blue - and
it's also way distant objects like mountains or city skyscapers look bluish.

## Airglow

Astronomical airglow is a faint, natural luminescence of the Earth’s upper 
atmosphere caused by chemoluminescence, where atmospheric gases (oxygen, nitrogen) 
emit light—primarily green and red—after being excited by solar ultraviolet 
radiation during the day, ripping apart molecues that recombine at night, releasing
energy.   It occurs globally at all times, peaking at 
90 &ndash; 100 km altitude, and is roughly 40% brighter during solar maximum.

This shouldn't be confused with the aurora, though both happen in the upper atmosphere.
The difference is that aurorae are powered by solar wind particles hitting Earth's
magnetic field.


