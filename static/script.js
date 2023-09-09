// Leaflet Map
if(document.getElementById('mapa')) {
    var map = L.map('mapa').setView([10.67166, -71.65339], 13);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    L.marker([10.67166, -71.65339]).addTo(map)
        .bindPopup('Bella exclusiva atelier.')
        .openPopup()
}