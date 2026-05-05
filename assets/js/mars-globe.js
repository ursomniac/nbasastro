/**
 * mars-globe.js — Mars 3D Globe Renderer
 * Northern Berkshire Astronomical Society
 *
 * To rebuild: npm run build:mars
 * Output:     static/js/mars-globe.js
 *
 * Algorithm:
 * 1. Sphere with texture, north up, longitude 0° facing camera at (0,0,3)
 * 2. Rotate sphere around Y axis only for longitude (no tilt distortion)
 * 3. Move camera to sub-Earth latitude elevation — correct perspective
 *
 * Depends on: window.SolarSystem.marsCML(jde) returning { cml, subEarthLat }
 */

import * as THREE from 'three'

// ---------------------------------------------------------------------------
// MAP CALIBRATION — adjust until known features match Stellarium
// ---------------------------------------------------------------------------
const MAP_LONGITUDE_OFFSET = 0.0

//const CAMERA_DIST = 3.0
const CAMERA_DIST = 8.0

const TEXTURE_PATH = '/images/planets/mars/mars.png'
const CANVAS_ID    = 'mars-globe-canvas'
const META_ID      = 'mars-globe-meta'

let _sphere   = null
let _renderer = null
let _scene    = null
let _camera   = null

function degToRad(d) { return d * Math.PI / 180 }

function applyRotations(cml, subEarthLat) {
  // Rotate sphere longitude only — no X tilt (avoids perspective distortion)
  //_sphere.rotation.set(0, degToRad(-cml + MAP_LONGITUDE_OFFSET) + Math.PI / 2, 0)
  //_sphere.rotation.set(0, degToRad(-cml + MAP_LONGITUDE_OFFSET), 0)
  //_sphere.rotation.set(0, degToRad(-cml + MAP_LONGITUDE_OFFSET) - Math.PI / 2, 0)
  //_sphere.rotation.set(0, degToRad(cml + MAP_LONGITUDE_OFFSET) + Math.PI / 2, 0)
  _sphere.rotation.set(0, degToRad(cml + MAP_LONGITUDE_OFFSET) - Math.PI / 2, 0)

  // Move camera to sub-Earth latitude — correct observer position
  const latRad = degToRad(subEarthLat)
  _camera.position.set(
    0,
    CAMERA_DIST * Math.sin(latRad),
    CAMERA_DIST * Math.cos(latRad)
  )
  _camera.lookAt(0, 0, 0)
}

function updateMeta(mars, cml, subEarthLat, date) {
  const meta = document.getElementById(META_ID)
  if (!meta) return
  meta.innerHTML = `
    <table class="sso-table"><tbody>
      <tr><td>Central Meridian</td><td>${cml.toFixed(1)}°</td></tr>
      <tr><td>Sub-Earth Lat</td><td>${subEarthLat.toFixed(1)}°</td></tr>
      <tr><td>Diameter</td><td>${mars.sdFmt}</td></tr>
      <tr><td>Illumination</td><td>${mars.illuminationPct}%</td></tr>
    </tbody></table>`
  //console.log(`[Mars] CML: ${cml.toFixed(1)}°  subEarthLat: ${subEarthLat.toFixed(1)}°`)
}

function renderFrame() {
  _renderer.render(_scene, _camera)
}

function initMarsGlobe() {
  const canvas = document.getElementById(CANVAS_ID)
  if (!canvas) return

  if (!window.SolarSystem) {
    console.error('[Mars] window.SolarSystem not available')
    return
  }

  const date    = new Date()
  const jde     = window.SolarSystem.dateToJDE(date)
  const planets = window.SolarSystem.getPlanets(jde)
  const mars    = planets.find(p => p.name === 'Mars')
  if (!mars || mars.error) { console.error('[Mars] No data'); return }

  const { cml, subEarthLat } = window.SolarSystem.marsCML(jde)

  const width  = canvas.clientWidth  || 400
  const height = canvas.clientHeight || 400

  _renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true })
  _renderer.setSize(width, height)
  _renderer.setPixelRatio(window.devicePixelRatio)
  _renderer.outputColorSpace = THREE.LinearSRGBColorSpace

  _scene  = new THREE.Scene()
  //_camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 100)
  _camera = new THREE.PerspectiveCamera(15, width / height, 0.1, 100)

  const texture = new THREE.TextureLoader().load(TEXTURE_PATH, renderFrame)
  texture.colorSpace = THREE.LinearSRGBColorSpace

  const geometry = new THREE.SphereGeometry(1, 64, 64)
  const material = new THREE.MeshBasicMaterial({ map: texture })
  _sphere = new THREE.Mesh(geometry, material)
  _scene.add(_sphere)

  applyRotations(cml, subEarthLat)

  window.addEventListener('resize', () => {
    _renderer.setSize(canvas.clientWidth, canvas.clientHeight)
    _camera.aspect = canvas.clientWidth / canvas.clientHeight
    _camera.updateProjectionMatrix()
    renderFrame()
  })

  updateMeta(mars, cml, subEarthLat, date)
  renderFrame()
}

window.renderMarsGlobe = function(date) {
  if (!_sphere || !_camera) return
  const jde     = window.SolarSystem.dateToJDE(date)
  const planets = window.SolarSystem.getPlanets(jde)
  const mars    = planets.find(p => p.name === 'Mars')
  if (!mars || mars.error) return
  const { cml, subEarthLat } = window.SolarSystem.marsCML(jde)
  applyRotations(cml, subEarthLat)
  updateMeta(mars, cml, subEarthLat, date)
  renderFrame()
}

document.addEventListener('DOMContentLoaded', initMarsGlobe)
