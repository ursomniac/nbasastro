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
 * window.SolarSystem.jupiterCML(jde) must be available (added to sso.js)
 */

import * as THREE from 'three'

// ---------------------------------------------------------------------------
// GRS CONFIGURATION — update these when new drift data is available
// Source: ~85° on 2026-02-01, drift ~1.75°/month westward (JUPOS)
// ---------------------------------------------------------------------------
const GRS_LONGITUDE_EPOCH   = 85.0
const GRS_EPOCH_JD          = 2461042.5
const GRS_DRIFT_DEG_PER_DAY = -0.0575

// ---------------------------------------------------------------------------
// MAP CALIBRATION — align texture longitude 0° with System II 0°
// Calibration reference: S&T GRS transit 2026-05-03 00:46 UTC
// At that time CML=84.0°, GRS=78.0°, GRS should appear near center of disk.
// Adjust this value until GRS appears at center at transit time.
// ---------------------------------------------------------------------------
//const MAP_LONGITUDE_OFFSET = 148.6
// const MAP_LONGITUDE_OFFSET = -20.2
const MAP_LONGITUDE_OFFSET = 317.4

const TEXTURE_PATH = '/images/planets/cassini_jupiter_20001211.jpg'
const CANVAS_ID    = 'jupiter-globe-canvas'
const META_ID      = 'jupiter-globe-meta'

let _sphere   = null
let _renderer = null
let _scene    = null
let _camera   = null
let _sunLight = null

function degToRad(d) { return d * Math.PI / 180 }

function grsLongitude(jde) {
  const lon = GRS_LONGITUDE_EPOCH + GRS_DRIFT_DEG_PER_DAY * (jde - GRS_EPOCH_JD)
  return ((lon % 360) + 360) % 360
}

// ---------------------------------------------------------------------------
// Three.js SphereGeometry UV mapping:
// - At rotation.y = 0, texture center (U=0.5) faces the camera (+Z axis)
// - Increasing rotation.y rotates the sphere counter-clockwise (viewed from above)
//   which moves texture features to the RIGHT on screen
// - Jupiter longitude increases WESTWARD = features move right-to-left on screen
//   so to advance CML (westward rotation), we DECREASE rotation.y
//
// To place grsLon at screen center:
//   We need to rotate from wherever grsLon currently is to the front.
//   grsOffset = angular distance from CML to GRS = (grsLon - cml)
//   Positive grsOffset means GRS is east of center (left of center on screen)
//   To bring it to center we rotate the sphere left = decrease rotation.y
//   rotation.y = degToRad(-(grsOffset)) + MAP_LONGITUDE_OFFSET_RAD
// ---------------------------------------------------------------------------
function computeSphereRotation(cml, grsLon) {
  const grsOffset = ((grsLon - cml) + 360) % 360
  return degToRad(-(grsOffset) + MAP_LONGITUDE_OFFSET)
}

function sunDirection(jup) {
  const { helioLon, helioLat } = jup
  return new THREE.Vector3(
    -Math.cos(helioLat) * Math.cos(helioLon),
    -Math.sin(helioLat),
    -Math.cos(helioLat) * Math.sin(helioLon)
  ).normalize()
}

function updateMeta(jup, cml, grsLon, date) {
  const meta = document.getElementById(META_ID)
  if (!meta) return
  const grsFromCenter = ((grsLon - cml + 180 + 360) % 360) - 180
  const grsSign = grsFromCenter >= 0 ? '+' : ''
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
  console.log(`[Jupiter] CML: ${cml.toFixed(1)}°  GRS: ${grsLon.toFixed(1)}°  GRS from center: ${grsFromCenter.toFixed(1)}°  rotation.y: ${computeSphereRotation(cml, grsLon).toFixed(4)} rad`)
}

function renderFrame() {
  _renderer.render(_scene, _camera)
}

function initJupiterGlobe() {
  const canvas = document.getElementById(CANVAS_ID)
  if (!canvas) return

  if (!window.SolarSystem) {
    console.error('[Jupiter] window.SolarSystem not available')
    return
  }

  const date    = new Date()
  const jde     = window.SolarSystem.dateToJDE(date)
  const planets = window.SolarSystem.getPlanets(jde)
  const jup     = planets.find(p => p.name === 'Jupiter')

  if (!jup || jup.error) {
    console.error('[Jupiter] Could not get Jupiter data:', jup?.error)
    return
  }

  const cml    = window.SolarSystem.jupiterCML(jde).sysii
  const grsLon = grsLongitude(jde)

  const width  = canvas.clientWidth  || 400
  const height = canvas.clientHeight || 400

  _renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true })
  _renderer.setSize(width, height)
  _renderer.setPixelRatio(window.devicePixelRatio)

  _scene  = new THREE.Scene()
  _camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 100)
  _camera.position.z = 2.5

  const texture  = new THREE.TextureLoader().load(TEXTURE_PATH, renderFrame)
  const geometry = new THREE.SphereGeometry(1, 64, 64)
  const material = new THREE.MeshStandardMaterial({ map: texture })
  _sphere = new THREE.Mesh(geometry, material)

  // Tilt and longitude on separate objects so they don't interact
  _sphere.rotation.y = computeSphereRotation(cml, grsLon)
  const pivot = new THREE.Object3D()
  pivot.rotation.z = degToRad(3.13)
  pivot.add(_sphere)
  _scene.add(pivot)

  _scene.add(new THREE.AmbientLight(0xffffff, 0.7))

  _sunLight = new THREE.DirectionalLight(0xffffff, 2.5)
  _sunLight.position.copy(sunDirection(jup))
  _scene.add(_sunLight)

  window.addEventListener('resize', () => {
    _renderer.setSize(canvas.clientWidth, canvas.clientHeight)
    _camera.aspect = canvas.clientWidth / canvas.clientHeight
    _camera.updateProjectionMatrix()
    renderFrame()
  })

  updateMeta(jup, cml, grsLon, date)
  renderFrame()
}

window.renderJupiterGlobe = function(date) {
  if (!_sphere || !_sunLight) return
  const jde     = window.SolarSystem.dateToJDE(date)
  const planets = window.SolarSystem.getPlanets(jde)
  const jup     = planets.find(p => p.name === 'Jupiter')
  if (!jup || jup.error) return
  const cml    = window.SolarSystem.jupiterCML(jde).sysii
  const grsLon = grsLongitude(jde)
  _sphere.rotation.y = computeSphereRotation(cml, grsLon)
  _sunLight.position.copy(sunDirection(jup))
  updateMeta(jup, cml, grsLon, date)
  renderFrame()
}

document.addEventListener('DOMContentLoaded', initJupiterGlobe)
