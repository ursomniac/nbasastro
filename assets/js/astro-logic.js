(function() {
    window.getAstroData = function() {
        const planetTarget = document.getElementById('planetary-dashboard-target');
        const moonTarget = document.getElementById('jupiter-moons-target');
        const timePicker = document.getElementById('astro-time-picker');
        const timeDisplay = document.getElementById('current-obs-time');
        const Astro = window.Astronomy;
        
        if (!planetTarget || !moonTarget || !Astro || !Astro.MakeTime) return;

        try {
            let date = timePicker && timePicker.value ? new Date(timePicker.value) : new Date();
            if (timeDisplay) timeDisplay.innerText = date.toLocaleString();

            const time = Astro.MakeTime(date);
            const obs = new Astro.Observer(42.7, -73.1, 0);
            const planets = [
                { name: 'Sun', id: Astro.Body.Sun }, { name: 'Moon', id: Astro.Body.Moon },
                { name: 'Mercury', id: Astro.Body.Mercury }, { name: 'Venus', id: Astro.Body.Venus },
                { name: 'Mars', id: Astro.Body.Mars }, { name: 'Jupiter', id: Astro.Body.Jupiter },
                { name: 'Saturn', id: Astro.Body.Saturn }, { name: 'Uranus', id: Astro.Body.Uranus },
                { name: 'Neptune', id: Astro.Body.Neptune }, { name: 'Pluto', id: Astro.Body.Pluto }
            ];

            let pHTML = `<table class="astro-table"><thead><tr><th>Body</th><th>RA</th><th>DEC</th><th>AZ</th><th>ALT</th><th>MAG</th><th>PHASE</th><th>RISE/SET</th><th>TRANSIT</th></tr></thead><tbody>`;
            for (const p of planets) {
                const equ = Astro.Equator(p.id, time, obs, true, true);
                const hor = Astro.Horizon(time, obs, equ.ra, equ.dec, "normal");
                const ill = Astro.Illumination(p.id, time);
                let ev = "-";
                try {
                    const nr = Astro.SearchRiseSet(p.id, obs, 1, time, 1);
                    const ns = Astro.SearchRiseSet(p.id, obs, -1, time, 1);
                    if (nr && ns) {
                        const isR = nr.date < ns.date;
                        ev = (isR ? "↑ " : "↓ ") + (isR ? nr.date : ns.date).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
                    }
                } catch(e) {}
                let tr = "-";
                try {
                    const lst0 = Astro.SiderealTime(Astro.MakeTime(new Date(date.getFullYear(), date.getMonth(), date.getDate()))) + (obs.longitude / 15.0);
                    let tH = (equ.ra - lst0);
                    while (tH < 0) tH += 24; while (tH >= 24) tH -= 24;
                    tr = new Date(new Date(date.getFullYear(), date.getMonth(), date.getDate()).getTime() + (tH * 0.99726957 * 3600000)).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
                } catch(e) {}

                pHTML += `<tr><td><strong>${p.name}</strong></td><td>${equ.ra.toFixed(2)}</td><td>${equ.dec.toFixed(2)}</td><td>${hor.azimuth.toFixed(1)}°</td><td>${hor.altitude.toFixed(1)}°</td><td>${(p.name==='Sun'?-26.7:ill.mag).toFixed(1)}</td><td>${(ill.phase_fraction * 100).toFixed(0)}%</td><td>${ev}</td><td>${tr}</td></tr>`;
            }
            planetTarget.innerHTML = pHTML + `</tbody></table>`;

            const jmFn = Astro.JupiterMoons || Astro.jupitermoons;
            if (jmFn) {
                let mHTML = `<table class="astro-table"><thead><tr><th>Moon</th><th>X (E/W)</th><th>Y (N/S)</th><th>Z (Depth)</th></tr></thead><tbody>`;
                const jm = jmFn(time);
                const mList = [{l:'Io',k:'io'},{l:'Europa',k:'europa'},{l:'Ganymede',k:'ganymede'},{l:'Callisto',k:'callisto'}];
                mList.forEach(m => {
                    const pos = jm[m.k].rect || jm[m.k];
                    mHTML += `<tr><td>${m.l}</td><td>${(pos.x * 2092.5).toFixed(2)}</td><td>${(pos.y * 2092.5).toFixed(2)}</td><td>${(pos.z * 2092.5).toFixed(2)}</td></tr>`;
                });
                moonTarget.innerHTML = mHTML + `</tbody></table>`;
            }
        } catch (e) { console.error("Astro Error:", e); }
    };
    const checker = setInterval(() => {
        if (window.Astronomy && window.Astronomy.Body) { clearInterval(checker); window.getAstroData(); }
    }, 100);
})();
