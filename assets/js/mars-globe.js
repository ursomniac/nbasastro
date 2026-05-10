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

const THREE = window.THREE

// ---------------------------------------------------------------------------
// MAP CALIBRATION — adjust until known features match Stellarium
// ---------------------------------------------------------------------------
const MAP_LONGITUDE_OFFSET = 0.0

//const CAMERA_DIST = 3.0
const CAMERA_DIST = 8.0

const TEXTURE_PATH = '/images/planets/mars/mars.png'
const CANVAS_ID    = 'mars-globe-canvas'
const MARKER_ID    = 'mars-marker-canvas'
const META_ID      = 'mars-globe-meta'

let _sphere   = null
let _renderer = null
let _scene    = null
let _camera   = null
let _currentCML = 0
let _currentLat = 0

function degToRad(d) { return d * Math.PI / 180 }

function applyRotations(cml, subEarthLat) {
  _currentCML = cml
  _currentLat = subEarthLat
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

// ---------------------------------------------------------------------------
// Marker overlay
// ---------------------------------------------------------------------------

// Project a Mars surface point (lon, lat in degrees) to canvas pixel coords.
// Returns { x, y, visible } where visible = point is on the facing hemisphere.
function projectFeature(lonDeg, latDeg, canvasW, canvasH) {
  // 3D point on unit sphere in Mars body frame (lon=0 faces +Z, north=+Y)
  const lonRad = degToRad(lonDeg)
  const latRad = degToRad(latDeg)
  const x0 =  Math.cos(latRad) * Math.cos(lonRad)
  const y0 =  Math.sin(latRad)
  const z0 =  Math.cos(latRad) * Math.sin(lonRad)

  // Apply sphere Y rotation (same as applyRotations)
  const sphereY = degToRad(_currentCML + MAP_LONGITUDE_OFFSET) - Math.PI / 2
  const cosY = Math.cos(sphereY), sinY = Math.sin(sphereY)
  const xr =  x0 * cosY + z0 * sinY
  const yr =  y0
  const zr = -x0 * sinY + z0 * cosY

  // Camera is at (0, CAMERA_DIST*sin(lat), CAMERA_DIST*cos(lat)) looking at origin
  // Transform point into camera space
  const camLatRad = degToRad(_currentLat)
  const cosL = Math.cos(camLatRad), sinL = Math.sin(camLatRad)

  // Camera basis vectors (right, up, forward=-lookDir)
  // forward = normalize(origin - camPos) = (0, -sinL, -cosL)
  // right   = cross(forward, worldUp≈(0,1,0)) ... simplified for Y-only camera tilt
  // We only need to check visibility and project — use dot products.

  // Point in camera space:
  // cam_z = dot(point - camPos, -forward) = dot(point, (0, sinL, cosL)) - CAMERA_DIST
  // (since camPos = CAMERA_DIST*(0,sinL,cosL) and forward=(0,-sinL,-cosL))
  const camZ = xr * 0 + yr * sinL + zr * cosL  // dot with (0,sinL,cosL)
  // Visible if point is in front of camera (camZ component relative to cam)
  // The sphere center is at origin, cam looks at it from distance CAMERA_DIST.
  // A surface point is visible if its projection toward cam is positive, i.e.
  // the dot of the rotated point with the camera direction > 0.
  const camDir = { x: 0, y: sinL, z: cosL }  // unit vector from origin toward camera
  const dotCam = xr * camDir.x + yr * camDir.y + zr * camDir.z
  const visible = dotCam > 0.05  // small threshold avoids limb flicker

  // Project using Three.js camera (perspective)
  // Use the actual Three.js project() utility via a Vector3
  const vec = new THREE.Vector3(xr, yr, zr)
  vec.project(_camera)
  // vec is now in NDC [-1,1]; convert to canvas pixels
  const px = (vec.x  + 1) / 2 * canvasW
  const py = (-vec.y + 1) / 2 * canvasH

  return { x: px, y: py, visible }
}

let _hoveredFeature = null

function renderMarkers() {
  const overlay = document.getElementById(MARKER_ID)
  if (!overlay || !_camera) return

  const webgl = document.getElementById(CANVAS_ID)
  //const W = webgl.clientWidth  || webgl.width
  //const H = webgl.clientHeight || webgl.height
  const W = webgl.offsetWidth  || webgl.width
  const H = webgl.offsetHeight || webgl.height

  if (overlay.width !== W || overlay.height !== H) {
    overlay.width  = W
    overlay.height = H
  }

  const ctx = overlay.getContext('2d')
  ctx.clearRect(0, 0, W, H)

  const features = window.SolarSystem && window.SolarSystem.MARS_FEATURES
  if (!features) return

  const projected = features.map(f => ({
    ...f,
    ...projectFeature(f.lon, f.lat, W, H)
  }))

  projected.forEach(f => {
    if (!f.visible) return

    // Draw + marker
    const r = 5
    ctx.save()
    ctx.strokeStyle = '#ffcc44'
    ctx.lineWidth = 1.5
    ctx.beginPath()
    ctx.moveTo(f.x - r, f.y)
    ctx.lineTo(f.x + r, f.y)
    ctx.moveTo(f.x, f.y - r)
    ctx.lineTo(f.x, f.y + r)
    ctx.stroke()

    // Draw id letter
    ctx.font = 'bold 11px monospace'
    ctx.fillStyle = '#ffcc44'
    ctx.textAlign = 'left'
    ctx.textBaseline = 'bottom'
    ctx.fillText(f.id, f.x + r + 2, f.y)
    ctx.restore()
  })

  // Hover label
  if (_hoveredFeature && _hoveredFeature.visible) {
    const f = _hoveredFeature
    const pad = 5
    ctx.font = '12px sans-serif'
    const tw = ctx.measureText(f.name).width
    const bx = f.x + 10
    const by = f.y - 20
    const bw = tw + pad * 2
    const bh = 20

    ctx.save()
    ctx.fillStyle = 'rgba(0,0,0,0.75)'
    ctx.beginPath()
    ctx.roundRect(bx, by, bw, bh, 3)
    ctx.fill()
    ctx.fillStyle = '#ffffff'
    ctx.textAlign = 'left'
    ctx.textBaseline = 'middle'
    ctx.fillText(f.name, bx + pad, by + bh / 2)
    ctx.restore()
  }
}

function setupMarkerHover() {
  const overlay = document.getElementById(MARKER_ID)
  if (!overlay) return

  overlay.addEventListener('mousemove', e => {
    const rect = overlay.getBoundingClientRect()
    const mx = (e.clientX - rect.left) * (overlay.width  / rect.width)
    const my = (e.clientY - rect.top)  * (overlay.height / rect.height)

    const features = window.SolarSystem && window.SolarSystem.MARS_FEATURES
    if (!features) return

    const W = overlay.width, H = overlay.height
    const HIT = 14  // px hit radius

    let found = null
    let best = HIT * HIT
    features.forEach(f => {
      const p = projectFeature(f.lon, f.lat, W, H)
      if (!p.visible) return
      const dx = p.x - mx, dy = p.y - my
      const d2 = dx*dx + dy*dy
      if (d2 < best) { best = d2; found = { ...f, ...p } }
    })

    _hoveredFeature = found
    renderMarkers()
  })

  overlay.addEventListener('mouseleave', () => {
    _hoveredFeature = null
    renderMarkers()
  })
}

// ---------------------------------------------------------------------------

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
  renderMarkers()
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

  const width  = canvas.offsetWidth  || canvas.width  || 400
  const height = canvas.offsetHeight || canvas.height || 400

console.log('[Mars] canvas size at init:', width, height)

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
  setupMarkerHover()

  window.addEventListener('resize', () => {
    const w = canvas.offsetWidth || canvas.width
    const h = canvas.offsetHeight || canvas.height
    _renderer.setSize(w, h)
    _camera.aspect = w / h
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

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initMarsGlobe)
} else {
  initMarsGlobe()
}
