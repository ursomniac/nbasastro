(function() {

  const DEG = 180 / Math.PI;

  const PLANET_COLORS = {
    Mercury: '#a0a0a0',
    Venus:   '#f5a800',
    Earth:   '#3a7bd5',
    Mars:    '#e03000',
    Jupiter: '#f0b0c0',
    Saturn:  '#8b3a3a',
    Uranus:  '#00e000',
    Neptune: '#00e0e0',
  };

  const ZODIAC = ['♓','♈','♉','♊','♋','♌','♍','♎','♏','♐','♑','♒'];

  const ABBREV = {
    Mercury: 'Me', Venus: 'V', Earth: 'E', Mars: 'Ma',
    Jupiter: 'J', Saturn: 'Sa', Uranus: 'U', Neptune: 'N'
  };

  window.renderOrrery = function(planets) {
    const canvas = document.getElementById('orrery-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const W = canvas.width, H = canvas.height;
    const cx = W / 2, cy = H / 2;
    const MARGIN = 44;
    const maxR = cx - MARGIN;

    ctx.clearRect(0, 0, W, H);
    ctx.fillStyle = '#0d1421';
    ctx.fillRect(0, 0, W, H);

    const logMin = Math.log10(0.25);
    const logMax = Math.log10(35);

    function toPixR(au) {
      return ((Math.log10(au) - logMin) / (logMax - logMin)) * maxR;
    }

    function toXY(lon, au) {
      const pr = toPixR(au);
      return { x: cx + pr * Math.cos(lon), y: cy - pr * Math.sin(lon) };
    }

    // Orbit rings
    [0.31, 0.72, 1.0, 1.52, 5.2, 9.5, 19.2, 30.1].forEach(d => {
      ctx.beginPath();
      ctx.arc(cx, cy, toPixR(d), 0, Math.PI * 2);
      ctx.strokeStyle = '#1e2e48';
      ctx.lineWidth = 0.8;
      ctx.stroke();
    });

    // Spokes
    for (let deg = 0; deg < 360; deg += 30) {
      const r = deg * Math.PI / 180;
      ctx.beginPath();
      ctx.moveTo(cx, cy);
      ctx.lineTo(cx + maxR * Math.cos(r), cy - maxR * Math.sin(r));
      ctx.strokeStyle = '#1e2e48';
      ctx.lineWidth = 0.8;
      ctx.stroke();
    }

    // Outer ring
    ctx.beginPath();
    ctx.arc(cx, cy, maxR, 0, Math.PI * 2);
    ctx.strokeStyle = '#3a4a64';
    ctx.lineWidth = 1;
    ctx.stroke();

    // Degree labels — inside ring
    ctx.fillStyle = '#78909c';
    ctx.font = '8px monospace';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    for (let deg = 0; deg < 360; deg += 30) {
      const r = deg * Math.PI / 180;
      ctx.fillText(deg + '°', cx + (maxR - 8) * Math.cos(r), cy - (maxR - 8) * Math.sin(r));
    }

    // Zodiac glyphs — just outside ring
    ctx.fillStyle = '#b0bec5';
    ctx.font = '11px serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    for (let i = 0; i < 12; i++) {
      const r = (i * 30 + 15) * Math.PI / 180;
      const gx = cx + (maxR + 20) * Math.cos(r);
      const gy = cy - (maxR + 20) * Math.sin(r);
      if (gx > 8 && gx < W - 8 && gy > 8 && gy < H - 8) {
        ctx.fillText(ZODIAC[i], gx, gy);
      }
    }

    // Sun
    ctx.beginPath();
    ctx.arc(cx, cy, 5, 0, Math.PI * 2);
    ctx.fillStyle = '#f8d44e';
    ctx.fill();

    // Earth
    const earthLon = planets[0].earthLon;
    const earthR   = planets[0].earthR;
    const ep = toXY(earthLon, earthR);
    ctx.beginPath();
    ctx.arc(ep.x, ep.y, 4, 0, Math.PI * 2);
    ctx.fillStyle = PLANET_COLORS['Earth'];
    ctx.fill();
    ctx.fillStyle = '#d1d1d1';
    ctx.font = '8px sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'bottom';
    ctx.fillText('E', ep.x, ep.y - 6);

    // Planets
    planets.forEach(p => {
      if (p.error) return;
      const pp = toXY(p.helioLon, p.r);
      const dotR = (p.name === 'Jupiter' || p.name === 'Saturn') ? 5 : 4;
      ctx.beginPath();
      ctx.arc(pp.x, pp.y, dotR, 0, Math.PI * 2);
      ctx.fillStyle = PLANET_COLORS[p.name] || '#ffffff';
      ctx.fill();
      ctx.fillStyle = '#d1d1d1';
      ctx.font = '8px sans-serif';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'bottom';
      ctx.fillText(ABBREV[p.name] || p.name[0], pp.x, pp.y - 6);
    });

    // Table — Earth + planets sorted by D_sun
    const earth = { name: 'Earth', helioLon: earthLon, r: earthR };
    const rows = [earth, ...planets.filter(p => !p.error)]
      .sort((a, b) => a.r - b.r);

    const tbody = document.getElementById('orrery-tbody');
    if (!tbody) return;
    tbody.innerHTML = rows.map(p => {
      const lonDeg = ((p.helioLon * DEG) % 360 + 360) % 360;
      const col = PLANET_COLORS[p.name] || '#fff';
      return `<tr>
        <td><span class="orrery-dot" style="background:${col}"></span>${p.name}</td>
        <td>${lonDeg.toFixed(2)}</td>
        <td>${p.r.toFixed(2)}</td>
      </tr>`;
    }).join('');
  };

})();
