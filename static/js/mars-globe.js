(() => {
  // assets/js/mars-globe.js
  var THREE = window.THREE;
  var MAP_LONGITUDE_OFFSET = 0;
  var CAMERA_DIST = 8;
  var TEXTURE_PATH = "/images/planets/mars/mars.png";
  var CANVAS_ID = "mars-globe-canvas";
  var META_ID = "mars-globe-meta";
  var _sphere = null;
  var _renderer = null;
  var _scene = null;
  var _camera = null;
  function degToRad(d) {
    return d * Math.PI / 180;
  }
  function applyRotations(cml, subEarthLat) {
    _sphere.rotation.set(0, degToRad(cml + MAP_LONGITUDE_OFFSET) - Math.PI / 2, 0);
    const latRad = degToRad(subEarthLat);
    _camera.position.set(
      0,
      CAMERA_DIST * Math.sin(latRad),
      CAMERA_DIST * Math.cos(latRad)
    );
    _camera.lookAt(0, 0, 0);
  }
  function updateMeta(mars, cml, subEarthLat, date) {
    const meta = document.getElementById(META_ID);
    if (!meta) return;
    meta.innerHTML = `
    <table class="sso-table"><tbody>
      <tr><td>Central Meridian</td><td>${cml.toFixed(1)}\xB0</td></tr>
      <tr><td>Sub-Earth Lat</td><td>${subEarthLat.toFixed(1)}\xB0</td></tr>
      <tr><td>Diameter</td><td>${mars.sdFmt}</td></tr>
      <tr><td>Illumination</td><td>${mars.illuminationPct}%</td></tr>
    </tbody></table>`;
  }
  function renderFrame() {
    _renderer.render(_scene, _camera);
  }
  function initMarsGlobe() {
    const canvas = document.getElementById(CANVAS_ID);
    if (!canvas) return;
    if (!window.SolarSystem) {
      console.error("[Mars] window.SolarSystem not available");
      return;
    }
    const date = /* @__PURE__ */ new Date();
    const jde = window.SolarSystem.dateToJDE(date);
    const planets = window.SolarSystem.getPlanets(jde);
    const mars = planets.find((p) => p.name === "Mars");
    if (!mars || mars.error) {
      console.error("[Mars] No data");
      return;
    }
    const { cml, subEarthLat } = window.SolarSystem.marsCML(jde);
    const width = canvas.clientWidth || 400;
    const height = canvas.clientHeight || 400;
    _renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
    _renderer.setSize(width, height);
    _renderer.setPixelRatio(window.devicePixelRatio);
    _renderer.outputColorSpace = THREE.LinearSRGBColorSpace;
    _scene = new THREE.Scene();
    _camera = new THREE.PerspectiveCamera(15, width / height, 0.1, 100);
    const texture = new THREE.TextureLoader().load(TEXTURE_PATH, renderFrame);
    texture.colorSpace = THREE.LinearSRGBColorSpace;
    const geometry = new THREE.SphereGeometry(1, 64, 64);
    const material = new THREE.MeshBasicMaterial({ map: texture });
    _sphere = new THREE.Mesh(geometry, material);
    _scene.add(_sphere);
    applyRotations(cml, subEarthLat);
    window.addEventListener("resize", () => {
      _renderer.setSize(canvas.clientWidth, canvas.clientHeight);
      _camera.aspect = canvas.clientWidth / canvas.clientHeight;
      _camera.updateProjectionMatrix();
      renderFrame();
    });
    updateMeta(mars, cml, subEarthLat, date);
    renderFrame();
  }
  window.renderMarsGlobe = function(date) {
    if (!_sphere || !_camera) return;
    const jde = window.SolarSystem.dateToJDE(date);
    const planets = window.SolarSystem.getPlanets(jde);
    const mars = planets.find((p) => p.name === "Mars");
    if (!mars || mars.error) return;
    const { cml, subEarthLat } = window.SolarSystem.marsCML(jde);
    applyRotations(cml, subEarthLat);
    updateMeta(mars, cml, subEarthLat, date);
    renderFrame();
  };
  document.addEventListener("DOMContentLoaded", initMarsGlobe);
})();
