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
        var num = each.route_num
        if (num) {
            var content = '<a href="'+link+'">'+title+'</a><br><p>Number of Routes: '+ num + '</p>';
        } else {
            var content = '<a href="'+link+'">'+title+'</a>';
        }
        
        console.log(content)

        if (each.route === "/locations/"){
            var mColor = "#59b300";
            var mSize = "large";
        } else if (each.route === "/sub_locations/"){
            var mColor = '#ff66b3';
            var mSize = "medium";
        } else if (each.route === "/boulders/"){
            var mColor = '#ffb84d';
            var mSize = 'small';
        }
        
        if (each.lat !== ""){
            var latlong = [Number(each.lat), Number(each.lon)];
            var marker = L.marker(new L.LatLng(latlong[0], latlong[1]), {
            icon: L.mapbox.marker.icon({'marker-symbol': 'rocket', 'marker-color': mColor, 'marker-size': mSize}),
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
