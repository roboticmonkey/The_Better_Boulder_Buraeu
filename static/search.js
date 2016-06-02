"use strict";


$("#search_btn").on('click', function(evt){
    // alert("hello");
    // evt.preventDefault(); // do i need this?

    var searchTerm = $("#field-search").val();

    $.get("/search.json", {"term": searchTerm}, handleSearch);
});
// console.log('loaded');

function renderList(data){
    var dataDestination = $("#search-results");
    // debugger;
    //clear results
    dataDestination.empty();

    for (var i = 0; i < data.data.length; i++) {
        var each = data.data[i];
        var link = each.route+each.id;
        if ((each.route === "/route/") || (each.lat === "")){
            dataDestination.append('<li><a href="'+link+'">'+each.name+'</a></li>');

        }
    }
}

function putMarkersOnMap(data){
    map.featureLayer.clearLayers();
    
    var featureLayer = new L.mapbox.FeatureLayer().addTo(map);
    var markers = new L.MarkerClusterGroup();

    for (var i = 0; i < data.data.length; i++) {
        
        var each = data.data[i];
        var title = each.name;
        var link = each.route+each.id;
        var content = '<a href="'+link+'">'+title+'</a>';
        console.log(content)
        
        if (each.lat !== ""){
            var latlong = [Number(each.lat), Number(each.lon)];
            var marker = L.marker(new L.LatLng(latlong[0], latlong[1]), {
            icon: L.mapbox.marker.icon({'marker-symbol': 'rocket', 'marker-color': '#59b300'}),
            title: title
            });

        marker.bindPopup(content);
        markers.addLayer(marker);
        }
    }
    
    map.featureLayer.addLayer(markers);
    
    map.fitBounds(markers.getBounds(), {
        maxZoom: 13,
    });

}

function handleSearch(data){
    putMarkersOnMap(data);
    renderList(data);
}
