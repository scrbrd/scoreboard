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
        "view/document",
        "js/router",
    ],
    function($, DocView, Router) {

        // setup ajax and initialize Route and Views
        function initialize() {

            // Pre DOM Loaded Initialization
            // FIXME cache: true for production?
            $.ajaxSetup({
                cache: false // always hits server
            });
            

            // Post DOM Loaded Initialization 
            $(function() {
                doc_view = DocView.getDocumentView();
                Router.initialize(true); // pushstate = true
                // TODO remove facebook's #_=_ insertion
            });
        }

        return {
            initialize: initialize,
        }


    }
);
