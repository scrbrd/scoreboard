/* Filename: iscroll.js
 *
 * Wrapper around iscroll to modularize it.
 *
 * global require, iScroll
 *
 */

define(
    [
        "jQuery",
        "constants",                         // constants.js
        "domReady!",                        // only call when DOM is ready
        "order!libs/iscroll/iscroll-min",
    ], 
    function($, Constants, doc) {
    
        // Instantiate iScroll object
        // TODO remove if and put that conditional in the script load
        var scroller;
       
        document.addEventListener(
                'touchmove', 
                function (e) { 
                    e.preventDefault(); 
                }, 
                false);
        if ($('#' + Constants.SCROLLER_ID).length) {
            scroller = new iScroll(Constants.SCROLLER_ID);
           
            // Remove global version of iScroll
            delete iScroll;
        }

    
        // Hide the address bar so the appl looks for appy
        // Edit to re-hide address bar on touch
        function hide_address_bar() {
    
            // Third Party module that hide the Address Bar in iPhone and Droid
            // From: https://gist.github.com/1172490

            var page = document.getElementById('page'),
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
                    page.style.height = window.innerHeight + 'px'
                } 
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
                    if (iphone && !fullscreen) height += 60;
                    page.style.height = height + 'px';
                } else if (android) {
                    // The stock Android browser has a location bar height of 56 pixels, but
                    // this very likely could be broken in other Android browsers.
                    page.style.height = (window.innerHeight + 56) + 'px'
                }
                // Scroll after a timeout, since iOS will scroll to the top of the page
                // after it fires the onload event
                setTimeout(scrollTo, 0, 0, 1);

                // rehide address bar on touch
                document.addEventListener(
                        'touchstart',
                        function(e) {
                            scrollTo(0,1);
                        });

            };
            (window.onresize = function() {
            var pageWidth = page.offsetWidth;
            // Android doesn't support orientation change, so check for when the width
            // changes to figure out when the orientation changes
            if (lastWidth == pageWidth) return;
            lastWidth = pageWidth;
            setupScroll();
            })();

        }

        hide_address_bar();

        // adjust length of scroller after address bar is hidden
        scroller.refresh();

        return scroller;
    }
);

