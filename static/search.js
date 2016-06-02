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
    // var featureLayer = new L.FeatureGroup().addTo(map);
    var markers = new L.MarkerClusterGroup();

    var bounds = map.getBounds();

    for (var i = 0; i < data.data.length; i++) {
        
        var each = data.data[i];
        var title = each.name;
        var link = each.route+each.id;
        // var latlong = [Number(each.lat), Number(each.lon)];
        var content = '<a href="'+link+'">'+title+'</a>';
        console.log(content)
        
        
        if (each.lat !== ""){
            var latlong = [Number(each.lat), Number(each.lon)];
            var marker = L.marker(new L.LatLng(latlong[0], latlong[1]), {
            icon: L.mapbox.marker.icon({'marker-symbol': 'rocket', 'marker-color': '0044FF'}),
            title: title
            });
            // console.log(latlong);
            // console.log(marker);
            // bounds._southWest._lat = Math.min(latlong[0], bounds._southWest._lat);
            // bounds._southWest._lng = Math.min(latlong[1], bounds._southWest._lng);
            // bounds._northEast._lat = Math.max(latlong[0], bounds._northEast._lat);
            // bounds._northEast._lng = Math.max(latlong[1], bounds._northEast._lng);
        marker.bindPopup(content);
        markers.addLayer(marker);
        }
        
        
        // marker.bindPopup(content);
        
        
        // markers.addLayer(marker);
    }
    
    // console.log(markers);
    map.featureLayer.addLayer(markers);
    // console.log(markers.getBounds());
    // featureLayer.on('ready', function(){
    //     // map.fitBounds(featureLayer.getBounds());
    //     // map.fitBounds(bounds);
    // });
    
    map.fitBounds(markers.getBounds(), {
        maxZoom: 13,
    });

}

function handleSearch(data){
    putMarkersOnMap(data);
    renderList(data);
}

// $(document).ready(function(){
//     // alert("hhh")
//   $.get("/search.json", {"term": ""}, putMarkersOnMap);
// });