/* Filename: app.js
 *
 * Application logic
 *
 * global require
 *
 *
 */

define(
    [
        // Aliases from main.js to module versions of packages
        "jQuery",
        "constants",
        "view/document",
        "router",
    ],
    function($, Constants, DocView, Router) {

        // setup ajax and initialize Route and Views
        function initialize() {

            // Pre DOM Loaded Initialization
            // FIXME cache: true for production?
            $.ajaxSetup({
                cache: false // always hits server
            });
            

            // Post DOM Loaded Initialization 
            $(function() {
                DocView.initialize();
                Router.initialize(true); // pushstate = true
                // TODO remove facebook's #_=_ insertion
            });
        }

        return {
            initialize: initialize,
        }


    }
);
