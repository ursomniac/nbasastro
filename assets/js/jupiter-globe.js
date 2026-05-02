/**
 * jupiter-globe.js — Jupiter 3D Globe Renderer
 * Northern Berkshire Astronomical Society
 *
 * THIS IS YOUR FILE. You own and maintain this.
 *
 * To rebuild: npm run build:jupiter
 * Output:     static/js/jupiter-globe.js  (never edit this directly)
 *
 * Depends on: static/js/astronomia.js loaded first (provides window.SolarSystem)
 */

import * as THREE from 'three'

// ---------------------------------------------------------------------------
// GRS CONFIGURATION — update these when new drift data is available
// Source: web reports, ~85° on 2026-02-01, drift ~1.75°/month westward
// ---------------------------------------------------------------------------
const GRS_LONGITUDE_EPOCH   = 85.0
const GRS_EPOCH_JD          = 2461042.5
const GRS_DRIFT_DEG_PER_DAY = -0.0575

// ---------------------------------------------------------------------------
// MAP CALIBRATION — align texture map longitude 0° with System II 0°
// ---------------------------------------------------------------------------
const MAP_LONGITUDE_OFFSET = 148.6

const TEXTURE_PATH = '/images/planets/cassini_jupiter_20001211.jpg'
const CANVAS_ID    = 'jupiter-globe-canvas'

let _sphere   = null
let _sunLight = null
function degToRad(d) { return d * Math.PI / 180 }

function currentGRSLongitude(jde) {
  const daysSinceEpoch = jde - GRS_EPOCH_JD
  const lon = GRS_LONGITUDE_EPOCH + (GRS_DRIFT_DEG_PER_DAY * daysSinceEpoch)
  return ((lon % 360) + 360) % 360
}

function jupiterCML(jup, jde) {
  const { helioLon, helioLat, earthLon, earthLat, earthR, r } = jup
  const jx = Math.cos(helioLat) * Math.cos(helioLon)
  const jy = Math.cos(helioLat) * Math.sin(helioLon)
  const jz = Math.sin(helioLat)
  const ex = Math.cos(earthLat) * Math.cos(earthLon)
  const ey = Math.cos(earthLat) * Math.sin(earthLon)
  const ez = Math.sin(earthLat)
  const dx = earthR * ex - r * jx
  const dy = earthR * ey - r * jy
  const dz = earthR * ez - r * jz
  const subEarthLon = Math.atan2(dy, dx) * 180 / Math.PI
  const SYSTEM_II_RATE = 870.27
  const J2000 = 2451545.0
  const daysSinceJ2000 = jde - J2000
  const systemIIPhase = (SYSTEM_II_RATE * daysSinceJ2000) % 360
  return ((subEarthLon - systemIIPhase) % 360 + 360) % 360
}

function computeSphereRotation(cml, grsLon) {
  const grsOffset = ((grsLon - cml) + 360) % 360
  return degToRad(-(grsOffset + MAP_LONGITUDE_OFFSET))
}

function sunDirection(jup) {
  const { helioLon, helioLat } = jup
  return new THREE.Vector3(
    -Math.cos(helioLat) * Math.cos(helioLon),
    -Math.sin(helioLat),
    -Math.cos(helioLat) * Math.sin(helioLon)
  ).normalize()
}

function initJupiterGlobe() {
  const canvas = document.getElementById(CANVAS_ID)
  if (!canvas) return

  if (!window.SolarSystem) {
    console.error('[Jupiter] window.SolarSystem not available')
    return
  }

  const jde     = window.SolarSystem.dateToJDE(new Date())
  const planets = window.SolarSystem.getPlanets(jde)
  const jup     = planets.find(p => p.name === 'Jupiter')

  if (!jup || jup.error) {
    console.error('[Jupiter] Could not get Jupiter data:', jup?.error)
    return
  }

  const cml    = jupiterCML(jup, jde)
  const grsLon = currentGRSLongitude(jde)

  const width  = canvas.clientWidth  || 400
  const height = canvas.clientHeight || 400

  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true })
  renderer.setSize(width, height)
  renderer.setPixelRatio(window.devicePixelRatio)

  const scene  = new THREE.Scene()
  const camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 100)
  camera.position.z = 2.5

  const loader   = new THREE.TextureLoader()
  const texture  = loader.load(TEXTURE_PATH)
  const geometry = new THREE.SphereGeometry(1, 64, 64)
  const material = new THREE.MeshStandardMaterial({ map: texture })
  _sphere = new THREE.Mesh(geometry, material)

  _sphere.rotation.z = degToRad(3.13)
  _sphere.rotation.y = computeSphereRotation(cml, grsLon)
  scene.add(_sphere)

  const ambient = new THREE.AmbientLight(0xffffff, 0.7)
  scene.add(ambient)

  _sunLight = new THREE.DirectionalLight(0xffffff, 2.5)
  _sunLight.position.copy(sunDirection(jup))
  scene.add(_sunLight)

  const DEG_PER_MS = 870.27 / 86400000
  let lastTime = null

  const observer = new IntersectionObserver(entries => {
    if (entries[0].isIntersecting) renderer.setAnimationLoop(animate)
    else renderer.setAnimationLoop(null)
  }, { threshold: 0.1 })
  observer.observe(canvas)

  function animate(now) {
    if (lastTime !== null) {
      const delta = now - lastTime
      _sphere.rotation.y += degToRad(DEG_PER_MS * delta)
    }
    lastTime = now
    renderer.render(scene, camera)
  }

  renderer.setAnimationLoop(animate)

  window.addEventListener('resize', () => {
    const w = canvas.clientWidth
    const h = canvas.clientHeight
    renderer.setSize(w, h)
    camera.aspect = w / h
    camera.updateProjectionMatrix()
  })

const grsFromCenter = ((grsLon - cml + 180 + 360) % 360) - 180
  const grsSign = grsFromCenter >= 0 ? '+' : ''
  const meta = document.getElementById('jupiter-globe-meta')
  if (meta) {
    meta.innerHTML = `
      <table class="sso-table">
        <tbody>
          <tr><td>Date (UTC)</td><td>${new Date().toUTCString().replace(' GMT', ' UTC')}</td></tr>
          <tr><td>Central Meridian (Sys II)</td><td>${cml.toFixed(1)}°</td></tr>
          <tr><td>GRS Longitude (Sys II)</td><td>${grsLon.toFixed(1)}°</td></tr>
          <tr><td>GRS from Center</td><td>${grsSign}${grsFromCenter.toFixed(1)}°</td></tr>
          <tr><td>Distance</td><td>${jup.rangeFmt}</td></tr>
          <tr><td>Diameter</td><td>${jup.sdFmt}</td></tr>
          <tr><td>Illumination</td><td>${jup.illuminationPct}%</td></tr>
        </tbody>
      </table>
    `
  }
  console.log(`[Jupiter] CML: ${cml.toFixed(1)}°  GRS: ${grsLon.toFixed(1)}°  offset: ${grsFromCenter.toFixed(1)}°`)
}

window.renderJupiterGlobe = function(date) {
  if (!_sphere || !_sunLight) return
  const jde     = window.SolarSystem.dateToJDE(date)
  const planets = window.SolarSystem.getPlanets(jde)
  const jup     = planets.find(p => p.name === 'Jupiter')
  if (!jup || jup.error) return
  const cml    = jupiterCML(jup, jde)
  const grsLon = currentGRSLongitude(jde)
  const grsFromCenter = ((grsLon - cml + 180 + 360) % 360) - 180
  const grsSign = grsFromCenter >= 0 ? '+' : ''
  _sphere.rotation.y = computeSphereRotation(cml, grsLon)
  _sunLight.position.copy(sunDirection(jup))
  const meta = document.getElementById('jupiter-globe-meta')
  if (meta) {
    meta.innerHTML = `
      <table class="sso-table"><tbody>
        <tr><td>Date (UTC)</td><td>${date.toUTCString().replace(' GMT',' UTC')}</td></tr>
        <tr><td>Central Meridian (Sys II)</td><td>${cml.toFixed(1)}°</td></tr>
        <tr><td>GRS Longitude (Sys II)</td><td>${grsLon.toFixed(1)}°</td></tr>
        <tr><td>GRS from Center</td><td>${grsSign}${grsFromCenter.toFixed(1)}°</td></tr>
        <tr><td>Distance</td><td>${jup.rangeFmt}</td></tr>
        <tr><td>Diameter</td><td>${jup.sdFmt}</td></tr>
        <tr><td>Illumination</td><td>${jup.illuminationPct}%</td></tr>
      </tbody></table>`
  }
  console.log(`[Jupiter] CML: ${cml.toFixed(1)}°  GRS: ${grsLon.toFixed(1)}°`)
}
document.addEventListener('DOMContentLoaded', initJupiterGlobe)
