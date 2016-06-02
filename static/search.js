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
        dataDestination.append('<li><a href="'+link+'">'+each.name+'</a></li>');

    }
}

function putMarkersOnMap(data){
    map.featureLayer.clearLayers();

    var markers = new L.MarkerClusterGroup();

    var bounds = map.getBounds();
    for (var i = 0; i < data.data.length; i++) {
        
        var each = data.data[i];
        var title = each.name;
        var link = each.route+each.id;
        var latlong = [Number(each.lat), Number(each.lon)];
        var content = '<a href="'+link+'">'+title+'</a>';
        
        bounds._southWest._lat = Math.min(latlong[0], bounds._southWest._lat);
        bounds._southWest._lng = Math.min(latlong[0], bounds._southWest._lng);
        bounds._northEast._lat = Math.min(latlong[0], bounds._northEast._lat);
        bounds._northEast._lng = Math.min(latlong[0], bounds._northEast._lng);

        var marker = L.marker(new L.LatLng(latlong[0], latlong[1]), {
            icon: L.mapbox.marker.icon({'marker-symbol': 'rocket', 'marker-color': '0044FF'}),
            title: title
        });
        
        marker.bindPopup(content);
        markers.addLayer(marker);
    }

    map.featureLayer.addLayer(markers);
    map.fitBounds(bounds);

}

function handleSearch(data){
    putMarkersOnMap(data);
    renderList(data);
}

// $(document).ready(function(){
//     // alert("hhh")
//   $.get("/search.json", {"term": ""}, putMarkersOnMap);
// });