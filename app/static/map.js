const map = L.map('map').setView([39.5, -98.35], 4);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

const locations = window.MAP_LOCATIONS;

const icons = {
    David: new L.Icon({
        iconUrl: 'https://maps.google.com/mapfiles/ms/icons/red-dot.png',
        iconSize: [32, 32],
    }),
    Ebony: new L.Icon({
        iconUrl: 'https://maps.google.com/mapfiles/ms/icons/blue-dot.png',
        iconSize: [32, 32],
    }),
};

locations.forEach(loc => {
    L.marker([loc.lat, loc.lng], { icon: icons[loc.visited_by] })
        .addTo(map)
        .bindPopup(`<b>${loc.name}</b><br>(${loc.visited_by})`);
});
