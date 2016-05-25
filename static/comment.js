"use strict";

function saveBComment(evt){
    evt.preventDefault();

    var comment = $('#b-comment-field').val();
    $('#b-comment-field').val("");

    var formInputs = {'comment' : comment};

    $.post('/add-b-comment.json',
            formInputs,
            showBComment);
}



function showBComment(results){
    $('#b-comments').prepend('<li>'+results['username']+'</li>'+
                              '<li>'+results['comment']+'</li>'+
                                '<li>'+results['date']+ '</li>' );

}

//this needs to be below the function it is calling
$('#boulder-comment').on('submit', saveBComment);


// code for route comment
function saveRComment(evt){
    evt.preventDefault();

    var comment = $('#r-comment-field').val();
    $('#r-comment-field').val("");

    var formInputs = {'comment' : comment};

    $.post('/add-r-comment.json',
            formInputs,
            showRComment);
}



function showRComment(results){
    $('#r-comments').prepend('<li>'+results['username']+'</li>'+
                              '<li>'+results['comment']+'</li>'+
                                '<li>'+results['date']+ '</li>' );

}



//this needs to be below the function it is calling
$('#route-comment').on('submit', saveRComment);


