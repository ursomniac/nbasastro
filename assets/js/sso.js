/**
 * sso.js — Solar System Observatory
 * Northern Berkshire Astronomical Society
 *
 * THIS IS YOUR FILE. You own and maintain this.
 *
 * To rebuild: npm run build:sso
 * Output:     static/js/astronomia.js  (never edit this directly)
 */

import { Planet } from 'astronomia/planetposition'
import solar from 'astronomia/solar'
import moonposition from 'astronomia/moonposition'
import moonillum from 'astronomia/moonillum'
import moonphase from 'astronomia/moonphase'
import base from 'astronomia/base'
import nutation from 'astronomia/nutation'
import { Ecliptic } from 'astronomia/coord'
import mars from 'astronomia/mars'
import jupiter from 'astronomia/jupiter'
import jupitermoons from 'astronomia/jupitermoons'
import saturnmoons from 'astronomia/saturnmoons'
import saturnring from 'astronomia/saturnring'
import elliptic from 'astronomia/elliptic'
import sidereal from 'astronomia/sidereal'
import { semidiameter as calcSD, Sun as SunSD, JupiterEquatorial, SaturnEquatorial, Mars as MarsSD, Mercury as MercurySD, VenusSurface, Uranus as UranusSD, Neptune as NeptuneSD } from 'astronomia/semidiameter'
import illum from 'astronomia/illum'

import vsop87Dearth   from 'astronomia/data/vsop87Dearth'
import vsop87Dmercury from 'astronomia/data/vsop87Dmercury'
import vsop87Dvenus   from 'astronomia/data/vsop87Dvenus'
import vsop87Dmars    from 'astronomia/data/vsop87Dmars'
import vsop87Djupiter from 'astronomia/data/vsop87Djupiter'
import vsop87Dsaturn  from 'astronomia/data/vsop87Dsaturn'
import vsop87Duranus  from 'astronomia/data/vsop87Duranus'
import vsop87Dneptune from 'astronomia/data/vsop87Dneptune'

import vsop87Bearth   from 'astronomia/data/vsop87Bearth'
import vsop87Bmercury from 'astronomia/data/vsop87Bmercury'
import vsop87Bvenus   from 'astronomia/data/vsop87Bvenus'
import vsop87Bmars    from 'astronomia/data/vsop87Bmars'
import vsop87Bjupiter from 'astronomia/data/vsop87Bjupiter'
import vsop87Bsaturn  from 'astronomia/data/vsop87Bsaturn'
import vsop87Buranus  from 'astronomia/data/vsop87Buranus'
import vsop87Bneptune from 'astronomia/data/vsop87Bneptune'

const DEG = 180 / Math.PI

function dateToJDE(date) {
  return date.getTime() / 86400000 + 2440587.5
}

function formatDeg(rad) {
  const deg = rad * DEG
  const sign = deg < 0 ? '-' : '+'
  const abs = Math.abs(deg)
  const d = Math.floor(abs)
  const mTotal = (abs - d) * 60
  const m = Math.floor(mTotal)
  const s = ((mTotal - m) * 60).toFixed(2)
  return `${sign}${d}° ${String(m).padStart(2,'0')}' ${String(s).padStart(5,'0')}"`
  //return `${sign}${String(d).padStart(3,'0')}° ${String(m).padStart(2,'0')}' ${String(s).padStart(4,'0')}"`
}

function formatRA(rad) {
  const hours = (rad * DEG) / 15
  const h = Math.floor(hours)
  const mTotal = (hours - h) * 60
  const m = Math.floor(mTotal)
  const s = ((mTotal - m) * 60).toFixed(1)
  return `${String(h).padStart(2,'0')}h ${String(m).padStart(2,'0')}m ${String(s).padStart(4,'0')}s`
}

function eclToEqu(lon, lat, jde) {
  const e = nutation.meanObliquity(jde)
  const ecl = new Ecliptic(lon, lat)
  return ecl.toEquatorial(e)
}

function getSun(jde) {
  try {
    const earth = new Planet(vsop87Dearth)
    const pos = solar.trueVSOP87(earth, jde)
    const equ = eclToEqu(pos.lon, pos.lat, jde)
    const sdRad = calcSD(SunSD, pos.range)
    const sdArcsec = sdRad * DEG * 3600 * 2
    const distKm = pos.range * 149597870.7
    const lightSeconds = distKm / 299792.458
    const ltMin = Math.floor(lightSeconds / 60)
    const ltSec = (lightSeconds % 60).toFixed(1)
    const lightTimeFmt = `${ltMin}m ${String(ltSec).padStart(4,'0')}s`
    return {
      name: 'Sun',
      ra: equ.ra,
      dec: equ.dec,
      range: pos.range,
      raFmt: formatRA(equ.ra),
      decFmt: formatDeg(equ.dec),
      rangeFmt: pos.range.toFixed(6) + ' AU',
      sdArcsec,
      sdFmt: sdArcsec.toFixed(1) + '"',
      lightTimeFmt,
      error: null
    }
  } catch (e) {
    return { name: 'Sun', error: e.message }
  }
}

function getPhaseName(angleDeg) {
  const a = angleDeg
  if (a >= 350 || a < 10)  return 'New Moon'
  if (a < 80)              return 'Waxing Crescent'
  if (a < 100)             return 'First Quarter'
  if (a < 170)             return 'Waxing Gibbous'
  if (a < 190)             return 'Full Moon'
  if (a < 260)             return 'Waning Gibbous'
  if (a < 280)             return 'Last Quarter'
  return                          'Waning Crescent'
}

function getMoon(jde) {
  try {
    const pos = moonposition.position(jde)
    const equ = eclToEqu(pos.lon, pos.lat, jde)
    const sun = getSun(jde)
    const elongation = base.pmod(equ.ra - sun.ra + Math.PI, 2 * Math.PI) - Math.PI
    const illumAngle = base.pmod(Math.abs(elongation), 2 * Math.PI)
    const illumination = base.illuminated(Math.PI - illumAngle)
    const phaseAngleDeg = illumAngle * DEG
    const fractionalYear = 2000 + (jde - 2451545.0) / 365.25
    const lastNewJDE = moonphase.newMoon(fractionalYear)
    let agedays = jde - lastNewJDE
    if (agedays < 0) agedays += moonphase.meanLunarMonth
    if (agedays > moonphase.meanLunarMonth) agedays -= moonphase.meanLunarMonth
    return {
      name: 'Moon',
      ra: equ.ra,
      dec: equ.dec,
      range: pos.range,
      raFmt: formatRA(equ.ra),
      decFmt: formatDeg(equ.dec),
      rangeFmt: pos.range.toFixed(0) + ' km',
      illumination: (illumination * 100).toFixed(1),
      phaseAngle: phaseAngleDeg.toFixed(1),
      phaseName: getPhaseName(phaseAngleDeg),
      ageFmt: agedays.toFixed(1) + ' days',
      agedays: agedays, 
      error: null
    }
  } catch (e) {
    return { name: 'Moon', error: e.message }
  }
}

const PLANET_DATA = [
  { name: 'Mercury', vsop: vsop87Bmercury, vsopD: vsop87Dmercury, sd0: MercurySD },
  { name: 'Venus',   vsop: vsop87Bvenus,   vsopD: vsop87Dvenus,   sd0: VenusSurface },
  { name: 'Mars',    vsop: vsop87Bmars,    vsopD: vsop87Dmars,    sd0: MarsSD },
  { name: 'Jupiter', vsop: vsop87Bjupiter, vsopD: vsop87Djupiter, sd0: JupiterEquatorial },
  { name: 'Saturn',  vsop: vsop87Bsaturn,  vsopD: vsop87Dsaturn,  sd0: SaturnEquatorial },
  { name: 'Uranus',  vsop: vsop87Buranus,  vsopD: vsop87Duranus,  sd0: UranusSD },
  { name: 'Neptune', vsop: vsop87Bneptune, vsopD: vsop87Dneptune, sd0: NeptuneSD },
]

function getPlanets(jde) {
  const earth = new Planet(vsop87Bearth)
  const earthD = new Planet(vsop87Dearth)
  const earthPos = earthD.position(jde)
  const earthR = earthPos.range

  return PLANET_DATA.map(p => {
    try {
      const planet = new Planet(p.vsop)
      const planetD = new Planet(p.vsopD)
      const planetPos = planetD.position(jde)
      const planetSph = new Planet(p.vsop).position(jde)
      const r = planetPos.range

      const dx = planetPos.range * Math.cos(planetPos.lat) * Math.cos(planetPos.lon) -
                 earthPos.range  * Math.cos(earthPos.lat)  * Math.cos(earthPos.lon)
      const dy = planetPos.range * Math.cos(planetPos.lat) * Math.sin(planetPos.lon) -
                 earthPos.range  * Math.cos(earthPos.lat)  * Math.sin(earthPos.lon)
      const dz = planetPos.range * Math.sin(planetPos.lat) -
                 earthPos.range  * Math.sin(earthPos.lat)
      const geoRange = Math.sqrt(dx*dx + dy*dy + dz*dz)

      const phaseAngle = illum.phaseAngle(r, geoRange, earthR)
      const illuminatedFraction = illum.fraction(r, geoRange, earthR)

      let mag = null
      try {
        switch(p.name) {
          case 'Mercury': mag = illum.mercury(r, geoRange, phaseAngle); break
          case 'Venus':   mag = illum.venus(r, geoRange, phaseAngle);   break
          case 'Mars':    mag = illum.mars(r, geoRange, phaseAngle);    break
          case 'Jupiter': mag = illum.jupiter(r, geoRange);             break
          case 'Saturn':  mag = null; break
          case 'Uranus':  mag = illum.uranus(r, geoRange);              break
          case 'Neptune': mag = illum.neptune(r, geoRange);             break
        }
      } catch(e) { mag = null }

      const sdRad = calcSD(p.sd0, geoRange)
      const sdArcsec = sdRad * DEG * 3600 * 2
      const pos = elliptic.position(planet, earth, jde)
      const distKm = geoRange * 149597870.7
      const lightSeconds = distKm / 299792.458
      const ltMin = Math.floor(lightSeconds / 60)
      const ltSec = (lightSeconds % 60).toFixed(1)
      const lightTimeFmt = `${ltMin}m ${String(ltSec).padStart(4,'0')}s`

      return {
        name: p.name,
        ra: pos.ra,
        dec: pos.dec,
        range: geoRange,
        r,
        sdArcsec,
        raFmt: formatRA(pos.ra),
        decFmt: formatDeg(pos.dec),
        rangeFmt: geoRange.toFixed(4) + ' AU',
        sdFmt: sdArcsec.toFixed(1) + '"',
        mag,
        magFmt: mag !== null ? mag.toFixed(1) : '—',
        illuminatedFraction,
        illuminationPct: (illuminatedFraction * 100).toFixed(1),
        phaseAngleDeg: phaseAngle * DEG,
	lightTimeFmt,
	helioLon: planetSph.lon,   // radians, heliocentric ecliptic longitude
	helioLat: planetSph.lat,   // radians, heliocentric ecliptic latitude
	earthLon: earthPos.lon,    // same for Earth (same for all planets)
	earthLat: earthPos.lat,
	earthR:   earthR,
        error: null
      }
    } catch (e) {
      return { name: p.name, error: e.message }
    }
  })
}

// Jupiter moon magnitudes: V = H + 5*log10(r_jupiter * delta_jupiter)
// r_jupiter = Jupiter's heliocentric distance (AU)
// delta_jupiter = Jupiter's geocentric distance (AU)
function getJupiterMoons(jde, jupiterR, jupiterDelta) {
  const NAMES = ['Io', 'Europa', 'Ganymede', 'Callisto']
  const H = [-1.68, -1.41, -2.09, -1.05]
  try {
    const pos = jupitermoons.positions(jde)
    return pos.map((p, i) => {
      const mag = H[i] + 5 * Math.log10(jupiterR * jupiterDelta)
      return {
        name: NAMES[i],
        x: p.x,
        y: p.y,
        z: p.z,
        side: p.x < 0 ? 'West' : 'East',
	offsetFmt: Math.sqrt(p.x*p.x + p.y*p.y).toFixed(1) + ' Rj',
        mag: mag.toFixed(2),
        error: null
      }
    })
  } catch (e) {
    return NAMES.map(n => ({ name: n, error: e.message }))
  }
}

// Saturn moon magnitudes: V = H + 5*log10(r_saturn * delta_saturn)
function getSaturnMoons(jde, saturnR, saturnDelta) {
  const NAMES = ['Mimas (M)','Enceladus (E)','Tethys (Te)','Dione (D)','Rhea (R)','Titan (Ti)','Hyperion (H)','Iapetus (I)']
  const H = [3.3, 2.1, 0.6, 0.8, 0.1, -1.3, 4.9, 1.5]
  try {
    const earth  = new Planet(vsop87Bearth)
    const saturn = new Planet(vsop87Bsaturn)
    const pos = saturnmoons.positions(jde, earth, saturn)
    return pos.map((p, i) => {
      let Hval = H[i]
      if (i === 7) {
         const phi = Math.atan2(p.y, p.x)
         Hval = 2.6 + 0.9 * Math.cos(phi)
      }
      const mag = Hval + 5 * Math.log10(saturnR * saturnDelta)
      return {
        name: NAMES[i],
        x: p.x,
        y: p.y,
        z: p.z,
        side: p.x < 0 ? 'West' : 'East',
	offsetFmt: Math.sqrt(p.x*p.x + p.y*p.y).toFixed(1),
        mag: mag.toFixed(2),
        error: null
      }
    })
  } catch (e) {
    return NAMES.map(n => ({ name: n, error: e.message }))
  }
}

function getSaturnRing(jde) {
  try {
    const earth  = new Planet(vsop87Bearth)
    const saturn = new Planet(vsop87Bsaturn)
    const [B, Bp, dU, P, aEdge, bEdge] = saturnring.ring(jde, earth, saturn)
    return {
      B: B * DEG,
      Brad: B,
      dU,
      P: P * DEG,
      aEdge,
      bEdge,
      bFmt: (B * DEG).toFixed(2) + '°',
      pFmt: (P * DEG).toFixed(2) + '°',
      aEdgeFmt: (aEdge * DEG * 3600).toFixed(2) + '"',
      bEdgeFmt: (bEdge * DEG * 3600).toFixed(2) + '"',
      error: null
    }
  } catch (e) {
    return { error: e.message }
  }
}

function formatSidereal(seconds) {
  const totalHours = seconds / 3600
  const h = Math.floor(totalHours) % 24
  const mTotal = (totalHours - Math.floor(totalHours)) * 60
  const m = Math.floor(mTotal)
  const s = ((mTotal - m) * 60).toFixed(1)
  return `${String(h).padStart(2,'0')}h ${String(m).padStart(2,'0')}m ${String(s).padStart(4,'0')}s`
}

function getAll(date, longitude = -73.11) {
  const jde = dateToJDE(date)
  const gst = sidereal.apparent(jde)
  const lstSeconds = gst + (longitude / 360) * 86400
  const lstNorm = ((lstSeconds % 86400) + 86400) % 86400

  const planets = getPlanets(jde)
  const saturnRing = getSaturnRing(jde)

  const jupiterPlanet = planets.find(p => p.name === 'Jupiter')
  const saturnPlanet  = planets.find(p => p.name === 'Saturn')

  // Saturn magnitude requires ring data
  if (saturnPlanet && !saturnRing.error) {
    const mag = illum.saturn(saturnPlanet.r, saturnPlanet.range, saturnRing.Brad, saturnRing.dU)
    saturnPlanet.mag = mag
    saturnPlanet.magFmt = mag.toFixed(1)
  }

  return {
    date: date.toISOString(),
    jde,
    gstFmt: formatSidereal(gst),
    lstFmt: formatSidereal(lstNorm),
    sun:          getSun(jde),
    moon:         getMoon(jde),
    planets,
    jupiterMoons: getJupiterMoons(jde, jupiterPlanet.r, jupiterPlanet.range),
    saturnMoons:  getSaturnMoons(jde, saturnPlanet.r, saturnPlanet.range),
    saturnRing,
  }
}

window.SolarSystem = {
  getAll, getSun, getMoon, getPlanets,
  getJupiterMoons, getSaturnMoons, getSaturnRing,
  dateToJDE, formatRA, formatDeg,
  marsCML: (jde) => {
    const earth = new Planet(vsop87Bearth)
    const marsP = new Planet(vsop87Bmars)
    const [DE, DS, ω, P] = mars.physical(jde, earth, marsP)
    return { 
	cml: ω * 180 / Math.PI, 
	subEarthLat: DE * 180 / Math.PI
    }
  },
  jupiterCML: (jde) => {
    const [DS, DE, ω1, ω2] = jupiter.physical2(jde)
    return { sysi: ω1 * 180 / Math.PI, sysii: ω2 * 180 / Math.PI }
  }
}

console.log('[SSO] SolarSystem library ready.')
