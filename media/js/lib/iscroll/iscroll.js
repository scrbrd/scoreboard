/**
    Wrapper around iscroll to modularize it.
*/
define(
        [
            "jQuery",
            "js/constants",                         // constants.js
            "domReady!",                        // only call when DOM is ready
            "order!lib/iscroll/iscroll-min"
        ],
        function($, Const, doc) {
   

// Instantiate iScroll object
function Scroller() {

    var curr_scroll = null;
    var IScroller = iScroll;
    // delete variable to remove it from GLOBAL
    delete iScroll;
    var scroller_id = Const.ID.SCROLLER.substring(1);

    this.refresh = function() {
        curr_scroll.refresh();
    };

    this.scrollTo = function(x, y, time) {
        curr_scroll.scrollTo(x, y, time);
    };


    function initialize() {
        document.addEventListener(
                'touchmove',
                function (e) {
                    e.preventDefault();
                },
                false);
        curr_scroll = new IScroller(scroller_id);
    }

    initialize();
}



// Hide the address bar so the appl looks for appy
// Edit to re-hide address bar on touch
function hide_address_bar() {

    // Third Party module that hide the Address Bar in iPhone and Droid
    // From: https://gist.github.com/1172490

    var page = document.getElementById(Const.ID.TAB.substring(1)),
        ua = navigator.userAgent,
        iphone = ~ua.indexOf('iPhone') || ~ua.indexOf('iPod'),
        ipad = ~ua.indexOf('iPad'),
        ios = iphone || ipad,
        // Detect if this is running as a fullscreen app from the homescreen
        fullscreen = window.navigator.standalone,
        android = ~ua.indexOf('Android'),
        lastWidth = 0;

    if (android) {
        // Android's browser adds the scroll position to the innerHeight, just to
        // make this really fucking difficult. Thus, once we are scrolled, the
        // page height value needs to be corrected in case the page is loaded
        // when already scrolled down. The pageYOffset is of no use, since it always
        // returns 0 while the address bar is displayed.
        window.onscroll = function() {
            page.style.height = window.innerHeight + 'px';
        };
    }
    var setupScroll = window.onload = function() {
        // Start out by adding the height of the location bar to the width, so that
        // we can scroll past it
        if (ios) {
            // iOS reliably returns the innerWindow size for documentElement.clientHeight
            // but window.innerHeight is sometimes the wrong value after rotating
            // the orientation
            var height = document.documentElement.clientHeight;
            // Only add extra padding to the height on iphone / ipod, since the ipad
            // browser doesn't scroll off the location bar.
            if (iphone && !fullscreen) {
                height += 60;
            }
            page.style.height = height + 'px';
        } else if (android) {
            // The stock Android browser has a location bar height of 56 pixels, but
            // this very likely could be broken in other Android browsers.
            page.style.height = (window.innerHeight + 56) + 'px';
        }
        // Scroll after a timeout, since iOS will scroll to the top of the page
        // after it fires the onload event
        setTimeout(scrollTo, 0, 0, 1);

        // rehide address bar on touch (UNNECESSARY, plus it makes
        // certain selection quirky)
        //document.addEventListener(
        //        'touchstart',
        //        function(e) {
        //            scrollTo(0,1);
        //        });

    };
    (window.onresize = function() {
    var pageWidth = page.offsetWidth;
    // Android doesn't support orientation change, so check for when the width
    // changes to figure out when the orientation changes
    if (lastWidth === pageWidth) {
        return;
    }
    lastWidth = pageWidth;
    setupScroll();
    })();

}

hide_address_bar();

return {
    construct: function () {
        var scroller = new Scroller();

        // adjust length of scroller after address bar is hidden
        scroller.refresh();

        return scroller;
    }
};


});
