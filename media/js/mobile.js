/* global _, $, Backbone */

// FIXME - organize the code in this script

// Instantiate iScroll objects
var scroller_id = "iscroll_wrapper";
var iScroll;
$(document).ready(function loaded() {
        iScroll = new iScroll(scroller_id);
        document.addEventListener('touchmove', function (e) { e.preventDefault(); }, false);
        document.addEventListener('DOMContentLoaded', function () { setTimeout(loaded, 200); }, false);
});

// Update content component and iscroll after an ajax update 
function update_content_with_iscroll(html) {
    $('#content').html(html);
    // scroll to x, y, time in mss
    iScroll.scrollTo(0, 0, 0);
    $('#content').fadeIn('fast');
    iScroll.refresh();
}

// Hides the Content Tag
function hide_content() {
    $('#content').fadeOut(0);
}


// Setup Ajax
$.ajaxSetup({
    cache: false
});




function initialize_router(pushState) {
    
    if (pushState) {
        
        // Setup Backbone Router
        var app = new AppRouter;
        Backbone.history.start({
            pushState: true,
            silent: true
        });
    

        // https://github.com/tbranyen/backbone-boilerplate
        // All navigation that is relative should be passed through the navigate
        // method, to be processed by the router.  If the link has a data-bypass
        // attribute, bypass the delegation completely.
        $(document).on("click", "a:not([data-bypass])", function(evt) {
            // Get the anchor href and protcol
            var href = $(this).attr("href");
            var protocol = this.protocol + "//";

            // Ensure the protocol is not part of URL, meaning its relative.
            if (href && href.slice(0, protocol.length) !== protocol) {
        
                // Stop the default event to ensure the link will not cause a page
                // refresh.
                evt.preventDefault();

                // `Backbone.history.navigate` is sufficient for all Routers and will
                // trigger the correct events.  The Router's internal `navigate` method
                // calls this anyways.
                Backbone.history.navigate(href, true);
            }
        });
    
    // else pushState is False
    } else {

        // Setup Backbone Router
        var app = new AppRouter;
        Backbone.history.start({
            silent: true
        });
   } 

}
initialize_router(true);



/* var myScrolls = [];

var myScroll = function () {
    var scroller_id = 'wrapper';

    if (scroller_id in myScroll) {
        myScrolls[scroller_id].refresh();
    } else {
        myScrolls[scroller_id] = new iScroll(
                scroller_id,
                {
                    hScroll         : false,
                    vScroll         : true,
                    hScrollbar      : false,
                    vScrollbar      : true,
                    fixedScrollbar  : true,
                    fadeScrollbar   : false,
                    hideScrollbar   : false,
                    bounce          : true,
                    momentum        : true,
                    lockDirection   : false
                });
    }
};

$(document).delegate('[data-role="page"]', 'pageshow', myScroll);
$(document).delegate('[data-role="page"]', 'pagecreate', myScroll);
$(window).bind('orientationchange', myScroll);

*/
//document.body.addEventListener(
//    'touchmove',
//    function(e) {
//        e.preventDefault();
//    },
//    false);
