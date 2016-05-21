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
    debugger;
    for (var i = 0; i < data.data.length; i++) {
        
        var each = data.data[i];
        var link = each.route+each.id;
        dataDestination.append('<li><a href="'+link+'">'+each.name+'</a></li>');
    }
    

}