/* 
    Filanem: app
    Run all application logic.

    Dependencies:
        $
        view/document
        router
*/
require(
    [
        "jQuery",
        "view/document",
        "js/router",
        "controller/loadTab",
    ],
    function ($, Doc, Router, LoadTabController) {

        // Setup application before DOM loads
        $.ajaxSetup({
            cache: false,
        });
        
        var pushStateRouting = true;
        var appRouter = Router.initializeAppRouter(pushStateRouting);
        // TODO remove facebook's #_=_ insertion that happens at login
        

        // Run DOM dependent logic
        $(document).ready(function () {
            // Do all DOM initializations with Views
            var docView = Doc.construct(pushStateRouting, appRouter);

            // track initial page load
            LoadTabController.trackViewPage(docView);

            // only load dialog after the rest of it
            docView.lazyInitialize();
        });
    }
);
