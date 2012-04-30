/* Filename: main.js
 *
 * Main js that configures require and loads other js files
 *
 * global require
 *
 */


// these shortcuts will be used in application files
require.config({
    paths: {
        // TODO - apparently there is an AMD version of jquery
        jQuery: "libs/jquery/jquery",
        Underscore: "libs/underscore/underscore",
        Backbone: "libs/backbone/backbone",
        iScroll: "libs/iscroll/iscroll"
    }
});


require(
    [
        // all app logic
        "app",

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
