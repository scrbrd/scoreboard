/* global _, $, Backbone */

// Instantiate iScroll objects
var scroller_id = "iscroll_wrapper";
var iScroll;
$(document).ready(function loaded() {
        iScroll = new iScroll(scroller_id);
        document.addEventListener('touchmove', function (e) { e.preventDefault(); }, false);
        document.addEventListener('DOMContentLoaded', function () { setTimeout(loaded, 200); }, false);
});


// Setup Ajax
$.ajaxSetup({
    cache: false
});


// Setup Backbone Router
var app = new AppRouter;
Backbone.history.start({
        silent: true
});




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
