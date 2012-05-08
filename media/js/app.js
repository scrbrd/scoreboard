/* 
    Module: App
    Run all application logic.

    Dependencies:
        $
        DocView
        Router
*/
define(
    [
        "jQuery",
        "view/document",
        "js/router",
    ],
    function($, DocView, Router) {
        return {
            
            /*
                Function: initialize
                Run all application logic
            */
            initialize: function() {

                // Setup application before DOM loads
                $.ajaxSetup({
                    cache: false,
                });
                

                // Run DOM dependent logic
                $(function() {
                    doc_view = DocView.getDocView();
                    Router.setupNavRouter(true); // pushstate = true
                    // TODO remove facebook's #_=_ insertion
                });
            }
        }
    }
);
