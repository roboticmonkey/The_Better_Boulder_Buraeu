"use strict";


$("#search_btn").on('click', function(evt){
    // alert("hello");
    // evt.preventDefault(); // do i need this?

    var searchTerm = $("#field-search").val();

    $.get("/search.json", {"term": searchTerm}, displayResults)
});
console.log('loaded');
function displayResults(data) {
    // adding the info to the page here?
    var dataDestination = $("#search-results");
    // var each = data.data[0];
    // debugger;
    var markers = new L.MarkerClusterGroup();

    for (var i = 0; i < data.data.length; i++) {
        
        var each = data.data[i];
        var title = each.name;
        var latlong = [Number(each.lat), Number(each.lon)];
        var link = each.route+each.id;
        dataDestination.append('<li><a href="'+link+'">'+each.name+'</a></li><br>'+each.lat);

        var marker = L.marker(new L.LatLng(latlong[0], latlong[1]), {
            icon: L.mapbox.marker.icon({'marker-symbol': 'rocket', 'marker-color': '0044FF'}),
            title: title
        });
        
        marker.bindPopup(title);
        markers.addLayer(marker);

    }

    map.addLayer(markers);
    

    

}

