"use strict";

// create a jQuery plugin-- extends jQuery must use the $
(function($){

    //define the jQuery plugin
    // $.fn. extends jQuery
    $.fn.my_modal_box = function(prop){

        //default parameters

        var options = $.extend({
            height : "250",
            width : "500",
            title : "Title",
            description: "Example",
            top : "20%",
            left : "30%",

        }, prop);


        return this.click(function(e){
            // stuff happens here
            add_block_page();
            add_popup_box();
            add_styles();

            $('.my_modal_box').fadeIn();

        });

        function add_block_page(){
            // makes a div that covers the whole screen
            var block_page = $('<div class="block_page"></div>');

            // appends the div i just made to the body
            $(block_page).appendTo('body');
        }

        function add_styles(){
            //block page overlay
            
            //sets pageHeight to the current height of the html doc
            var pageHeight = $(document).height();
            //sets pageWidth to the current width of the window
            var pageWidth = $(window).width();

            // grabs the div with the class block_page and sets the css
            $('.block_page').css({
                'position':'absolute',
                'top': '0',
                'left':'0',
                //this rgb has opacity included. 0.0 transparent-1.0 opaque
                'background-color': 'rgba(0,0,0,0.6)',
                'height': pageHeight,
                'width': pageWidth,
                'z-index':'10'
            });

            //styles the modal box
            $('.my_modal_box').css({
                'position': 'absolute',
                'left': options.left,
                'top': options.top,
                'display': 'none',
                'height': options.height+'px',
                'width': options.width+'px',
                'border': '1px solid #fff',
                'box-shadow': '0px 2px 7px #292929',
                'border-radius': '10px',
                'background': "#f2f2f2",
                'z-index': '50',

            });

            //styles the modal close link
            $('.login_modal_close').css({
                'position':'relative',
                'top': '0px',
                'left': '10px',
                'float': 'right',
                'display': 'block',
                'height': '50px',
                'width': '50px',
                // 'background': 'url("/static/close.png") no-repeat',

            });
            // styles the inner modal box
            $('.my_inner_modal_box').css({
                'background-color': '#fff',
                'height':(options.height - 50) + 'px',
                'width':(options.width- 50) +'px',
                'padding': '10px',
                'margin': '15px',
                'border-radius': '10px',

            });

        }

        function add_popup_box(){

            //not sure if the line breaks in the code will work
            // 
            var pop_up = $('<div class="my_modal_box"><a href="#" '+ 
                            'class="login_modal_close">close</a>'+
                            '<div class="my_inner_modal_box">' +
                            '<h2>'+ options.title + '</h2>' +
                            '<div>' + options.description + 
                            '</div></div></div>');
            //adds the pop_up code to the div i created with the class
            // block_page
            $(pop_up).appendTo('.block_page');

            //set a click listener on the modal href to close it
            $('.login_modal_close').click(function(evt){
                //when modal is clicked the div with class block_page will
                // fade then be removed
                $('.block_page').fadeOut().remove();
                // finds the parent of the href that was clicked and removes
                // it as well. ie. the div with class my_modal_box
                $(this).parent().fadeOut().remove();

            });

        }

        

        //allows this plugin to be chainable with jQuery by returning
        // the jQuery object
        return this;
    };


//needs pass jQuery in this IIFE to be able to work with other plugins
// plus the IIFE lets us have some private variables
})(jQuery);