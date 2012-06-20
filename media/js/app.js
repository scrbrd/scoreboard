/**
    Run all application logic.
    
    @module app 
    
    @requires jQuery
    @requires Doc
    @requires Router
    @requires LoadTabController
    @requires CreateGameController
    @requires DialogController
    @requires HTMLReader
*/
require(
        [
            "jQuery",
            "view/document",
            "js/router",
            "controller/loadTab",
            "controller/createGame",
            "controller/dialog",
            "model/htmlReader",
        ],
        function (
                $, 
                Doc, 
                Router, 
                LoadTabController, 
                CreateGameController,
                DialogController,
                HTMLReader) {

    // Setup application before DOM loads
    $.ajaxSetup({
        cache: false,
    });
    
    var pushStateRouting = true;
    var appRouter = Router.initialize(pushStateRouting);
    // TODO remove facebook's #_=_ insertion that happens at login
    
    // intialize Controllers
    LoadTabController.initialize(appRouter);
    CreateGameController.initialize();
    DialogController.initialize();

    // Run DOM dependent logic
    $(document).ready(function () {
        // Do all DOM initializations with Model and Views
        var tabModel = new HTMLReader();
        var docView = Doc.construct(
                pushStateRouting, 
                tabModel);

        // only load dialog after the rest of it
        docView.lazyInitialize();
    });
});
