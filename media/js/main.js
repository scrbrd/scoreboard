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
        jQuery: "static/js/libs/jquery/jquery",
        Underscore: "static/js/libs/underscore/underscore",
        Backbone: "static/js/libs/backbone/backbone",
        iScroll: "static/js/libs/iscroll/iscroll",
        js: "static/js",
        libs: "static/js/libs",
        view: "static/js/view",
        order: "static/js/libs/require/order",
        text: "static/js/libs/require/text",
        domReady: "static/js/libs/require/domReady"
    }
});


require(
    [
        // all app logic
        "js/app",

        // non-AMD 'modules'
        "order!libs/jquery/jquery-min", 
        "order!libs/underscore/underscore-min", 
        "order!libs/backbone/backbone-min",
        "libs/iscroll/iscroll-min"
    ], 
    function(App) {
        App.initialize();
    }

);
