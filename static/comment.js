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
    $('#b-comments').prepend('<div class=" well row comment"><div class="col-md-3">'+
                            '<h4>'+results['username']+'</h4></div>'+
                            '<div class="comment-user col-md-8">'+
                            '<h5>'+results['date']+'</h5>'+
                            '<p>'+results['comment']+'</p></div></div>' );

}

//this needs to be below the function it is calling
$('#boulder-comment').on('submit', saveBComment);


// code for route comment

function saveRComment(evt){
    evt.preventDefault();
    // debugger;
    var comment = $('#r-comment-field').val();
    $('#r-comment-field').val("");

    var formInputs = {'comment' : comment};

    $.post('/add-r-comment.json',
            formInputs,
            showRComment);
}


function showRComment(results){
    $('#r-comments').prepend('<div class="well row comment"><div class="col-md-3">'+
                            '<h4>'+results['username']+'</h4></div>'+
                            '<div class="comment-user col-md-8">'+
                            '<h5>'+results['date']+'</h5>'+
                            '<p>'+results['comment']+'</p></div></div>' );

}


//this needs to be below the function it is calling
$('#route-comment').on('submit', saveRComment);


