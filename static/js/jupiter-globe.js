(() => {
  // assets/js/jupiter-globe.js
  var THREE = window.THREE;
  var MAP_LONGITUDE_OFFSET = 317.4;
  var TEXTURE_PATH = "/images/planets/cassini_jupiter_20001211.jpg";
  var CANVAS_ID = "jupiter-globe-canvas";
  var META_ID = "jupiter-globe-meta";
  var _sphere = null;
  var _renderer = null;
  var _scene = null;
  var _camera = null;
  var _sunLight = null;
  function degToRad(d) {
    return d * Math.PI / 180;
  }
  function grsLongitude(jde) {
    const cfg = window.SolarSystem.GRS_CONFIG;
    const lon = cfg.lon + cfg.driftPerDay * (jde - cfg.epochJD);
    return (lon % 360 + 360) % 360;
  }
  function computeSphereRotation(cml, grsLon) {
    const grsOffset = (grsLon - cml + 360) % 360;
    return degToRad(-grsOffset + MAP_LONGITUDE_OFFSET);
  }
  function sunDirection(jup) {
    const { helioLon, helioLat } = jup;
    return new THREE.Vector3(
      -Math.cos(helioLat) * Math.cos(helioLon),
      -Math.sin(helioLat),
      -Math.cos(helioLat) * Math.sin(helioLon)
    ).normalize();
  }
  function updateMeta(jup, cml, grsLon, date) {
    const meta = document.getElementById(META_ID);
    if (!meta) return;
    const grsFromCenter = (grsLon - cml + 180 + 360) % 360 - 180;
    const grsSign = grsFromCenter >= 0 ? "+" : "";
    meta.innerHTML = `
    <table class="sso-table"><tbody>
      <tr><td>Central Meridian (Sys II)</td><td>${cml.toFixed(1)}\xB0</td></tr>
      <tr><td>GRS Longitude (Sys II)</td><td>${grsLon.toFixed(1)}\xB0</td></tr>
      <tr><td>GRS from Center</td><td>${grsSign}${grsFromCenter.toFixed(1)}\xB0</td></tr>
      <tr><td>Diameter</td><td>${jup.sdFmt}</td></tr>
      <tr><td>Illumination</td><td>${jup.illuminationPct}%</td></tr>
    </tbody></table>`;
  }
  function renderFrame() {
    _renderer.render(_scene, _camera);
  }
  function initJupiterGlobe() {
    const canvas = document.getElementById(CANVAS_ID);
    if (!canvas) return;
    if (!window.SolarSystem) {
      console.error("[Jupiter] window.SolarSystem not available");
      return;
    }
    const date = /* @__PURE__ */ new Date();
    const jde = window.SolarSystem.dateToJDE(date);
    const planets = window.SolarSystem.getPlanets(jde);
    const jup = planets.find((p) => p.name === "Jupiter");
    if (!jup || jup.error) {
      console.error("[Jupiter] Could not get Jupiter data:", jup?.error);
      return;
    }
    const cml = window.SolarSystem.jupiterCML(jde).sysii;
    const grsLon = grsLongitude(jde);
    const width = canvas.clientWidth || 400;
    const height = canvas.clientHeight || 400;
    _renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
    _renderer.setSize(width, height);
    _renderer.setPixelRatio(window.devicePixelRatio);
    _renderer.toneMapping = THREE.ReinhardToneMapping;
    _renderer.toneMappingExposure = 0.6;
    _scene = new THREE.Scene();
    _camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 100);
    _camera.position.z = 3;
    const texture = new THREE.TextureLoader().load(TEXTURE_PATH, renderFrame);
    const geometry = new THREE.SphereGeometry(1, 64, 64);
    const material = new THREE.ShaderMaterial({
      uniforms: { map: { value: texture } },
      vertexShader: `
    varying vec2 vUv;
    void main() { vUv = uv; gl_Position = projectionMatrix * modelViewMatrix * vec4(position,1.0); }
  `,
      fragmentShader: `
    uniform sampler2D map;
    varying vec2 vUv;
    void main() {
      vec4 c = texture2D(map, vUv);
      vec3 col = (c.rgb - 0.5) * 1.4 + 0.5;
      float gray = dot(col, vec3(0.299, 0.587, 0.114));
      col = mix(vec3(gray), col, 1.3);
      gl_FragColor = vec4(clamp(col, 0.0, 1.0), 1.0);
    }
  `
    });
    _sphere = new THREE.Mesh(geometry, material);
    _sphere.rotation.y = computeSphereRotation(cml, grsLon);
    const pivot = new THREE.Object3D();
    pivot.rotation.z = degToRad(3.13);
    pivot.add(_sphere);
    _scene.add(pivot);
    _scene.add(new THREE.AmbientLight(16777215, 0.7));
    _sunLight = new THREE.DirectionalLight(16777215, 2.5);
    _sunLight.position.copy(sunDirection(jup));
    _scene.add(_sunLight);
    window.addEventListener("resize", () => {
      _renderer.setSize(canvas.clientWidth, canvas.clientHeight);
      _camera.aspect = canvas.clientWidth / canvas.clientHeight;
      _camera.updateProjectionMatrix();
      renderFrame();
    });
    updateMeta(jup, cml, grsLon, date);
    renderFrame();
  }
  window.renderJupiterGlobe = function(date) {
    if (!_sphere || !_sunLight) return;
    const jde = window.SolarSystem.dateToJDE(date);
    const planets = window.SolarSystem.getPlanets(jde);
    const jup = planets.find((p) => p.name === "Jupiter");
    if (!jup || jup.error) return;
    const cml = window.SolarSystem.jupiterCML(jde).sysii;
    const grsLon = grsLongitude(jde);
    _sphere.rotation.y = computeSphereRotation(cml, grsLon);
    _sunLight.position.copy(sunDirection(jup));
    updateMeta(jup, cml, grsLon, date);
    renderFrame();
  };
  document.addEventListener("DOMContentLoaded", initJupiterGlobe);
})();
