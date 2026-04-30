---
title: "Solar System Dashboard"
date: 2026-04-29
url: "/solar-system-dashboard/"
---

### Observation Time
Select a date and time to calculate positions:
<input type="datetime-local" id="astro-time-picker" class="astro-input">
<button onclick="window.getAstroData()" class="btn">Update Positions</button>

#### Active Observation Time: <span id="current-obs-time">Now</span>


### Planet Positions 

<div id="planetary-dashboard-target"></div>

### About Jupiter's Moons
The Galilean moons are visible in even small telescopes. Their positions below are measured in Jupiter Radii.

<div id="jupiter-moons-target"></div>

You can use these coordinates to identify which moon is which tonight!

{{< planet-data >}}

