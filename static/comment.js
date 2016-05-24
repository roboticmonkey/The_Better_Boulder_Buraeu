"use strict";

function saveBComment(evt){
    evt.preventDefault();

    var comment = $('#b-comment-field').val();

    var formInputs = {'comment' : comment};

    $.post('/add-b-comment.json',
            formInputs,
            showComment);
}



function showComment(results){
    $('#b-comments').prepend('<li>'+results['username']+'</li>'+
                              '<li>'+results['comment']+'</li>'+
                                '<li>'+results['date']+ '</li>' );
}



//this needs to be below the function it is calling
$('#boulder-comment').on('submit', saveBComment);


