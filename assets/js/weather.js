(function() {
    const container = document.getElementById('weather-container');
    
    // ASSEMBLE THESE THREE PARTS INTO ONE SINGLE URL
    const part1 = 'https://api.open-meteo.com';
    const part2 = '/v1/forecast';
    const part3 = '?latitude=42.698&longitude=-73.109&current=temperature_2m,relative_humidity_2m,dew_point_2m,wind_speed_10m,wind_direction_10m&temperature_unit=fahrenheit&wind_speed_unit=mph';
    
    const weatherUrl = part1 + part2 + part3;

    const getDir = (deg) => ['N','NE','E','SE','S','SW','W','NW'][Math.round(deg/45)%8];

    if (container) {
        fetch(weatherUrl)
            .then(r => {
                if (!r.ok) throw new Error('API_FETCH_FAIL');
                return r.json();
            })
            .then(data => {
                const c = data.current;
                container.innerHTML = '<div style="font-size:0.9em; padding:5px; color:#fff;">' +
                    '<p style="text-align:center; font-weight:bold; margin:0 0 8px 0;">North Adams, MA</p>' +
                    '<div style="display:flex; justify-content:space-between; margin:2px 0;"><span style="color:#aaa;">Temp:</span><b>' + c.temperature_2m + '°F</b></div>' +
                    '<div style="display:flex; justify-content:space-between; margin:2px 0;"><span style="color:#aaa;">Dew Pt:</span><b>' + c.dew_point_2m + '°F</b></div>' +
                    '<div style="display:flex; justify-content:space-between; margin:2px 0;"><span style="color:#aaa;">Humidity:</span><b>' + c.relative_humidity_2m + '%</b></div>' +
                    '<div style="display:flex; justify-content:space-between; margin:2px 0;"><span style="color:#aaa;">Wind:</span><b>' + c.wind_speed_10m + ' mph ' + getDir(c.wind_direction_10m) + '</b></div>' +
                    '</div>';
            })
            .catch(() => {
                container.innerHTML = 'WEATHER OFFLINE';
            });
    }
})();
