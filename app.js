var mymap = L.map('mapid').setView([51.505, -0.09], 13);
L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoidmlyYWpyYWk5NyIsImEiOiJjaXV1YjJrcnkwMnVwMnRuMDU1aTFzZnVjIn0.SyFua7_mG0OERLQYFKoX4g', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
    maxZoom: 18,
    id: 'sk.eyJ1IjoidmlyYWpyYWk5NyIsImEiOiJjaXV1YjVnZTMwMnR4MnlsZzJjMjJmMjduIn0.Rw5cYgkfxRAtUPvHdqVulQ',
    accessToken: 'pk.eyJ1IjoidmlyYWpyYWk5NyIsImEiOiJjaXV1YjJrcnkwMnVwMnRuMDU1aTFzZnVjIn0.SyFua7_mG0OERLQYFKoX4g'
}).addTo(mymap);