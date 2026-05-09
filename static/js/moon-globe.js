(() => {
  // assets/js/moon-globe.js
  var THREE = window.THREE;
  var TEXTURE_PATH = "/images/planets/2k_moon.jpg";
  var CANVAS_ID = "sso-moon-canvas";
  var META_ID = "sso-moon-rows";
  var CAMERA_DIST = 6;
  var vertexShader = `
  varying vec2 vUv;
  varying vec3 vNormal;
  void main() {
    vUv = uv;
    vNormal = normalize(normalMatrix * normal);
    gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
  }
`;
  var fragmentShader = `
  uniform sampler2D moonTexture;
  uniform vec3 sunDirection;   // direction FROM moon TOWARD sun, in view space
  uniform float earthshine;    // ambient fill for dark side

  varying vec2 vUv;
  varying vec3 vNormal;

  void main() {
    vec4 texColor = texture2D(moonTexture, vUv);

    // Dot product of surface normal with sun direction
    // Positive = lit side, negative = dark side
    float intensity = dot(normalize(vNormal), normalize(sunDirection));

    // Sharp terminator: no smoothstep, just clamp
    //float lit = max(0.0, intensity);
    //float lit = step(0.0, dot(normalize(vNormal), normalize(sunDirection)));
    float lit = smoothstep(-0.05, 0.05, dot(normalize(vNormal), normalize(sunDirection)));
    // Earthshine: very dim blue-grey fill on dark side
    //float dark = earthshine * (1.0 - lit);
    float dark = earthshine;

    //vec3 color = texColor.rgb * (lit + dark);
    vec3 color = texColor.rgb * mix(dark, 1.0, lit);
    gl_FragColor = vec4(color, 1.0);
  }
`;
  var _renderer = null;
  var _scene = null;
  var _camera = null;
  var _sphere = null;
  var _material = null;
  var _initiated = false;
  function degToRad(d) {
    return d * Math.PI / 180;
  }
  function renderFrame() {
    if (_renderer && _scene && _camera) {
      _renderer.render(_scene, _camera);
    }
  }
  function updateMeta(moon, lib) {
    const tbody = document.getElementById(META_ID);
    if (!tbody) return;
    let con = "\u2014";
    if (window.Astronomy && moon.ra !== void 0) {
      try {
        const result = window.Astronomy.Constellation(
          moon.ra * (180 / Math.PI) / 15,
          moon.dec * (180 / Math.PI)
        );
        if (result) con = result.name;
      } catch (e) {
      }
    }
    const diamArcmin = lib.diam_deg ? (lib.diam_deg * 60).toFixed(1) + "'" : "\u2014";
    tbody.innerHTML = `
    <tr><td>Constellation</td><td>${con}</td></tr>
    <tr><td>RA</td><td>${moon.raFmt}</td></tr>
    <tr><td>Dec</td><td>${moon.decFmt}</td></tr>
    <tr><td>Distance</td><td>${moon.rangeFmt}</td></tr>
    <tr><td>Phase</td><td>${moon.phaseName}</td></tr>
    <tr><td>Age</td><td>${moon.ageFmt}</td></tr>
    <tr><td>Illumination</td><td>${moon.illumination}%</td></tr>
    <tr><td>Lib. Longitude</td><td>${lib.elon.toFixed(2)}\xB0</td></tr>
    <tr><td>Lib. Latitude</td><td>${lib.elat.toFixed(2)}\xB0</td></tr>
    <tr><td>Diameter</td><td>${diamArcmin}</td></tr>
  `;
  }
  function applyState(phase, lib, agedays) {
    if (!_sphere || !_camera || !_material) return;
    _sphere.rotation.set(0, -Math.PI / 2 + degToRad(lib.elon), 0);
    const latRad = degToRad(lib.elat);
    _camera.position.set(
      0,
      CAMERA_DIST * Math.sin(latRad),
      CAMERA_DIST * Math.cos(latRad)
    );
    _camera.lookAt(0, 0, 0);
    const phi = degToRad(phase);
    const isWaning = agedays > 14.765;
    const xSign = isWaning ? -1 : 1;
    const sunWorld = new THREE.Vector3(xSign * Math.sin(phi), 0, -Math.cos(phi));
    const sunView = sunWorld.clone().transformDirection(_camera.matrixWorldInverse);
    _material.uniforms.sunDirection.value = sunView;
  }
  function initMoonGlobe() {
    const container = document.getElementById(CANVAS_ID);
    if (!container) return;
    if (!window.SolarSystem) {
      console.error("[Moon] window.SolarSystem not available");
      return;
    }
    if (!window.Astronomy) {
      console.error("[Moon] window.Astronomy not available");
      return;
    }
    const date = /* @__PURE__ */ new Date();
    const jde = window.SolarSystem.dateToJDE(date);
    const moon = window.SolarSystem.getMoon(jde);
    if (!moon || moon.error) {
      console.error("[Moon] No moon data");
      return;
    }
    const astroTime = window.Astronomy.MakeTime(date);
    const lib = window.Astronomy.Libration(astroTime);
    const phase = parseFloat(moon.phaseAngle) || 0;
    container.innerHTML = "";
    const canvas = document.createElement("canvas");
    const size = container.clientWidth || 300;
    canvas.width = size;
    canvas.height = size;
    canvas.style.width = "100%";
    canvas.style.height = "auto";
    canvas.style.borderRadius = "50%";
    container.appendChild(canvas);
    _renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
    _renderer.setSize(size, size);
    _renderer.setPixelRatio(window.devicePixelRatio);
    _renderer.outputColorSpace = THREE.LinearSRGBColorSpace;
    _scene = new THREE.Scene();
    const h = 1.05;
    _camera = new THREE.OrthographicCamera(-h, h, h, -h, 0.1, 100);
    const texture = new THREE.TextureLoader().load(TEXTURE_PATH, () => {
      applyState(phase, lib, moon.agedays);
      renderFrame();
    });
    texture.colorSpace = THREE.LinearSRGBColorSpace;
    _material = new THREE.ShaderMaterial({
      uniforms: {
        moonTexture: { value: texture },
        sunDirection: { value: new THREE.Vector3(0, 0, 1) },
        earthshine: { value: 0.06 }
      },
      vertexShader,
      fragmentShader
    });
    const geometry = new THREE.SphereGeometry(1, 64, 64);
    _sphere = new THREE.Mesh(geometry, _material);
    _scene.add(_sphere);
    applyState(phase, lib, moon.agedays);
    window.addEventListener("resize", () => {
      const w = container.clientWidth || 300;
      _renderer.setSize(w, w);
      _camera.updateProjectionMatrix();
      renderFrame();
    });
    updateMeta(moon, lib);
    _initiated = true;
    renderFrame();
    console.log(`[Moon] shader \u2014 phase: ${phase.toFixed(1)}\xB0  elon: ${lib.elon.toFixed(2)}\xB0  elat: ${lib.elat.toFixed(2)}\xB0`);
  }
  window.renderMoonGlobe = function(date, moon) {
    if (!_initiated || !window.Astronomy) return;
    const astroTime = window.Astronomy.MakeTime(date);
    const lib = window.Astronomy.Libration(astroTime);
    const phase = parseFloat(moon.phaseAngle) || 0;
    applyState(phase, lib, moon.agedays);
    updateMeta(moon, lib);
    renderFrame();
  };
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initMoonGlobe);
  } else {
    initMoonGlobe();
  }
})();
