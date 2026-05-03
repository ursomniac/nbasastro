(function() {
    const container = document.getElementById('weather-container');
    const url = 'https://api.open-meteo.com/v1/forecast'
              + '?latitude=42.698&longitude=-73.109'
              + '&current=temperature_2m,relative_humidity_2m,dew_point_2m,wind_speed_10m,wind_direction_10m,cloud_cover'
              + '&hourly=cloud_cover'
              + '&temperature_unit=fahrenheit&wind_speed_unit=mph&forecast_days=1';

    const getDir = (deg) => ['N','NE','E','SE','S','SW','W','NW'][Math.round(deg/45)%8];

    if (!container) return;

    fetch(url)
        .then(r => { if (!r.ok) throw new Error(); return r.json(); })
        .then(data => {
            const c = data.current;
            const hours = data.hourly;

            // Next 8 hours of cloud cover
            const now = new Date();
            const currentHour = now.getHours();
            const sliceStart = currentHour;
            const sliceEnd = currentHour + 8;
            const cloudSlice = hours.cloud_cover.slice(sliceStart, sliceEnd);
            const timeSlice = hours.time.slice(sliceStart, sliceEnd);

            const bars = cloudSlice.map((pct, i) => {
                const h = new Date(timeSlice[i]);
                const label = i === 0 ? 'Now'
                    : h.toLocaleTimeString('en-US', {hour:'numeric'});
                const height = Math.max(4, Math.round(pct * 0.4));
                const cls = pct > 50 ? 'cloudy' : '';
                return { height, label, cls };
            });

            const firstLabel = bars[0]?.label || 'Now';
            const lastLabel = bars[bars.length - 1]?.label || '';

            container.innerHTML =
                '<div class="weather-city">North Adams, MA</div>' +
                '<div class="weather-row"><span>Temp</span><b>' + c.temperature_2m + '°F</b></div>' +
                '<div class="weather-row"><span>Dew Pt</span><b>' + c.dew_point_2m + '°F</b></div>' +
                '<div class="weather-row"><span>Humidity</span><b>' + c.relative_humidity_2m + '%</b></div>' +
                '<div class="weather-row"><span>Wind</span><b>' + c.wind_speed_10m + ' mph ' + getDir(c.wind_direction_10m) + '</b></div>' +
                '<div class="weather-row"><span>Cloud Cover</span><b>' + c.cloud_cover + '%</b></div>' +
                '<div class="weather-trend">' +
                    '<div class="weather-trend-label">Cloud cover — next 8 hrs</div>' +
                    '<div class="weather-trend-bars">' +
                        bars.map(b => `<div class="weather-trend-bar ${b.cls}" style="height:${b.height}px"></div>`).join('') +
                    '</div>' +
                    '<div class="weather-trend-times"><span>' + firstLabel + '</span><span>' + lastLabel + '</span></div>' +
                '</div>';
        })
        .catch(() => { container.innerHTML = '<p style="color:var(--text-muted)">Weather unavailable.</p>'; });
})();
