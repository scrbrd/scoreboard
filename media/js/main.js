/**
    Setup Require.js and load application.
    
    Main is run first as part of the require.js framework. Require
    the App, require the non-AMD javascript modules in the correct
    order, and load the plugins (text, domReady, order).

    @module main
    @requires app
*/
require.config({
    /**
        The base URL for require is "/".
        @property {string} baseUrl
    */
    baseUrl: "/",

    /**
        All the path shortcuts to use in the application.
        @property {Object} paths
    */
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
        controller: "static/js/controller",
        order: "static/js/lib/require/order",
        text: "static/js/lib/require/text",
        domReady: "static/js/lib/require/domReady",
    },
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
    ]
);
