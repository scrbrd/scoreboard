/* Filename: main.js
 *
 * Main js that configures require and loads other js files
 *
 * global require
 *
 */


// these shortcuts will be used in application files
require.config({
    baseUrl: "/",

    paths: {
        // TODO - apparently there is an AMD version of jquery
        jQuery: "static/js/lib/jquery/jquery",
        Underscore: "static/js/lib/underscore/underscore",
        Backbone: "static/js/lib/backbone/backbone",
        iScroll: "static/js/lib/iscroll/iscroll",
        js: "static/js",
        lib: "static/js/lib",
        view: "static/js/view",
        order: "static/js/lib/require/order",
        text: "static/js/lib/require/text",
        domReady: "static/js/lib/require/domReady"
    }
});


require(
    [
        // all app logic
        "js/app",

        // non-AMD 'modules'
        "order!lib/jquery/jquery-min",
        "order!lib/underscore/underscore-min",
        "order!lib/backbone/backbone-min",
        "lib/iscroll/iscroll-min"
    ],
    function (App) {
        App.initialize();
    }

);
