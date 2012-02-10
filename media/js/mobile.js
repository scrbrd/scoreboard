/* global _, $, Backbone */

// Constants
var constants = {
    PAGE_SELECTOR:      "#page",            // page container
    DIALOG_SELECTOR:    "#dialog",          // dialog container
    CONTEXT_SELECTOR:   "header h2",        // context header
    CONTENT_SELECTOR:   "#content",         // content
    SCROLLER_ID:        "iscroll_wrapper",  // iscroll id
};


// Remove when this template comes from server
var header = "<div id=\"dialog\">Create Game";
var body = "<div>This is where you'll do all the cool stuff.</div>";
var submit = "<button class=\"submit\">Submit</button>";
var close = "<button class=\"close\">Close</button>";
var footer = "</div>";
var dialog_html = header + body + submit + close + footer;


// Instantiate iScroll object
// TODO remove if and put that conditional in the script load
var scroller;
$(document).ready(function loaded() {
    if ($('#' + constants.SCROLLER_ID).length) {
        scroller = new iScroll(constants.SCROLLER_ID);
        document.addEventListener(
                'touchmove', 
                function (e) { e.preventDefault(); }, 
                false);
        document.addEventListener(
                'DOMContentLoaded', 
                function () { setTimeout(loaded, 200); }, 
                false);
    }
});


// Handle DOM changes
var DomManager = {
    
    // Update content component, scroll to top, show, and refresh iScroll
    update_content: function(new_html) {
        $(constants.CONTENT_SELECTOR).toggle(false); // hide content 
        $(constants.CONTENT_SELECTOR).html(new_html); // replace content
        scroller.scrollTo(0, 0, 0);  // scroll to x, y, time in ms
        $(constants.CONTENT_SELECTOR).fadeIn('fast'); // fade in
        scroller.refresh(); // refresh scroller for changes in size
    },
    
    // Hide the content
    hide_content: function() {
        $(constants.CONTENT_SELECTOR).toggle(false); // hide content
        var loading_str = "I know I put the results here somewhere..."
        $(constants.CONTENT_SELECTOR).html(loading_str).toggle(true); // show 'loading'
    },

    // Update context header
    update_context: function(new_html) {
        $(constants.CONTEXT_SELECTOR).html(new_html);
    },

    // Populate and show dialog screen
    show_dialog: function(dialog_html) {
        $(constants.DIALOG_SELECTOR).slideDown('fast'); // show dialog screen
    },

    // Hide dialog screen
    hide_dialog: function() {
        $(constants.DIALOG_SELECTOR).slideUp('fast');
    },

    // Add dialog to DOM
    append_dialog: function(dialog_html) {
        var dialog = $(dialog_html).hide().insertAfter(constants.PAGE_SELECTOR);
        var page_height = $(constants.PAGE_SELECTOR).height();
        dialog.height(page_height); // makes sure the screen is entirely covered
    } 
};


// Add Handlers to Buttons
function initialize_buttons() {

    // Add "show dialog" functionality to create game button
    $('.dialog-link').on("click", function(event) {
        DomManager.show_dialog(dialog_html);
    });

    // Add "hide dialog" functionality to dialog's close button
    $('button.close').on("click", function(event) {
        DomManager.hide_dialog();
    });
    
    // Add "game creation" functionality to dialog's submit button
    $('button.submit').on("click", function(event) {
        // TODO get game info fom dialog
        parameters = {};
        parameters["league"] = 643;
        parameters["creator"] = 655;
        parameters["game_score"] = [{"id": 651, "score": 1}, {"id": 658, "score": 3}];

        CrudRouter.create("game", parameters)
        DomManager.hide_dialog();
    });

}

$(document).ready(function() {
    DomManager.append_dialog(dialog_html);
    initialize_buttons();

    // TODO remove facebook's #_=_ insertion
});


// Setup Ajax
$.ajaxSetup({
    cache: false
});


// Set up Backbone's Router
function initialize_router(pushState) {
   
    // Backbone using History API's PushState
    var app_router = new NavRouter;
    if (pushState) {
        Backbone.history.start({
            pushState: true,
            silent: true
        });
    
        // SRC = https://github.com/tbranyen/backbone-boilerplate
        // All navigation that is relative should be passed through the navigate
        // method, to be processed by the router.  If the link has a data-bypass
        // attribute, bypass the delegation completely.
        $(document).on("click", "a:not(.data-bypass)", function(event) {
            // Get the anchor href and protcol
            var href = $(this).attr("href");
            var protocol = this.protocol + "//";

            // Ensure the protocol is not part of URL, meaning its relative.
            if (href && href.slice(0, protocol.length) !== protocol) {
        
                // Stop the default event to ensure the link will not cause a page
                // refresh.
                event.preventDefault();

                // `Backbone.history.navigate` is sufficient for all Routers and will
                // trigger the correct events.  The Router's internal `navigate` method
                // calls this anyways.
                if (!$(this).hasClass('route-bypass')) {
                    app_router.navigate(href, {trigger: true});
                }
            }
        });
    
    // Backbone without using History's PushState
    } else {
        Backbone.history.start({
            silent: true
        });
   } 
}

initialize_router(true);

