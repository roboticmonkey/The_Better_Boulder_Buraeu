L.mapbox.accessToken = 'pk.eyJ1Ijoicm9ib3RpY21vbmtleSIsImEiOiJjaW9nZXBtajAwMWd3djFtM3Nma3FqaXB2In0.21UysS7J-Y50PVNcD0mopg';
var map = L.mapbox.map('map', 'mapbox.pirates')
    .setView([37.7749, -122.4194], 9);

var myLayer = L.mapbox.featureLayer().addTo(map);
map.scrollWheelZoom.disable();