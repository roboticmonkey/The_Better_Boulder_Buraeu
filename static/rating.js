"use strict";


//**************************************************

// Sets up the star rating variables that are needed
// By grabbing information from the hidden html fields

//***************************************************

var user = $("#user").val();
var avg = parseInt($("#avg").val());
var userScore = parseInt($("#user_score").val());

if (userScore) {
    var defaultVal = userScore;
    var color = "#92d2c2";
} else if (user && !(userScore)){
    var defaultVal = avg;
    var color = "c5c163";
} else {
    var defaultVal = avg;
    var color = "#c5c163";
}

if (user != "None") {
    var noWrite = false;
} else {
    var noWrite = true;
}

// Creates the rateYo object

$(function(){
    $("#rateYo").rateYo({
        starWidth: "30px",
        normalFill: "#B8B8B8",
        ratedFill: color,
        maxValue: 5,
        numStars: 5,
        fullStar: true,
        spacing: "5px",
        rating: defaultVal,
        
        readOnly: noWrite,
    });

    function successFunc(results){  

    }

    function boulderAjax(rating){
        var boulder = $("#boulder").val();
        var user = $("#user").val();
     
        var formInputs = {'user': user,
                          'boulder': boulder,
                          'rate': rating};
 
        if (user != "None"){
           $.post('/rate-boulder', formInputs, successFunc); 
        } 

    }

    function routeAjax(rating){
        var route = $("#route").val();
        var user = $("#user").val();

        var formInputs = {'user': user,
                          'route': route,
                          'rate': rating};
        
        if (user != "None"){
           $.post('/rate-route', formInputs, successFunc); 
        } 
    }

    var $rateYo = $('#rateYo').rateYo();
    
    $('#rateYo').click(function(e){
        var rating = $rateYo.rateYo("rating");
        $("#star-rating").val(String(rating));
        var boulderRoute = $('#boulder-route').val();
        
        if (boulderRoute === 'boulder') {
            boulderAjax(rating);
        } 
        if (boulderRoute === 'route'){
            routeAjax(rating);
        }
    });
});





