/**
    Setup RequireJS and load application.
    
    main.js is the first script that RequireJS runs. We're using RequireJS
    to manage a module based framework that has no globals.
   
    Check out RequireJS: http://requirejs.org

    main's responsibilties are fairly limited:
    1. Load and run the main application module (App).
    2. Define 'paths' that can be used as shortcuts around the application.
    3. Load all third party libraries that are non-AMD.

    A note on non-AMD modules. Many libraries are not AMD modules so they
    end up becoming part of the global namespace. We wrap these libraries
    in custom AMD modules and then delete the global variables. That's all
    going down in 'lib'.

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
        model: "static/js/model",
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
