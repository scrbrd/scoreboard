/* 
    Module: Main
    Setup Require.js and load application.

    Main is run first as part of the require.js framework. Require
    the App, require the non-AMD javascript modules in the correct
    order, load the plugins (text, domReady, order), and initialize
    App.
    
    Settings:
        baseUrl - everything is relative to the root directory
        paths - all shortcut paths to use throughout javascript

*/
require.config({
    baseUrl: "/",

    paths: {
        // TODO - apparently there is an AMD version of jquery
        jQuery: "static/js/lib/jquery/jquery",
        Underscore: "static/js/lib/underscore/underscore",
        Backbone: "static/js/lib/backbone/backbone",
        iScroll: "static/js/lib/iscroll/iscroll",
        MP: "static/js/lib/mixpanel/mixpanel",
        js: "static/js",
        lib: "static/js/lib",
        util: "static/js/util",
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
        "order!lib/jquery/jquery-ui/jquery-ui-min",
        "order!lib/jquery/form2js/form2js",
        "order!lib/jquery/form2js/jquery.toObject",
        "order!lib/underscore/underscore-min",
        "order!lib/backbone/backbone-min",
        "lib/iscroll/iscroll-min",
        "lib/mixpanel/mixpanel-min",
    ],
    function (App) {
        App.initialize();
    }

);
