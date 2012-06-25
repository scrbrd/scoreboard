/**
    Run all application logic.
    
    @module app 
    
    @requires jQuery
    @requires Doc
    @requires Router
    @requires LoadTabController
    @requires CreateGameController
    @requires DialogController
    @requires LoginController
    @requires ViewerContextModel
    @requires PageStateModel
*/
require(
        [
            "jQuery",
            "view/document",
            "js/router",
            "controller/loadTab",
            "controller/createGame",
            "controller/dialog",
            "controller/login",
            "model/viewerContextModel",
            "model/pageStateModel",
        ],
        function (
                $, 
                Doc, 
                Router, 
                LoadTabController, 
                CreateGameController,
                DialogController,
                LoginController,
                ViewerContextModel,
                PageStateModel) {

    function initialize() {
        // Setup application before DOM loads
        $.ajaxSetup({
            cache: false,
        });
       
        var pushStateRouting = true;
        Router.initialize(pushStateRouting);
        // TODO remove facebook's #_=_ insertion that happens at login

        initializeControllers();

        // Run DOM dependent logic
        $(document).ready(function () {
            // Do all DOM initializations with Model and Views
            var viewerContextModel = ViewerContextModel.retrieve();
            var tabModel = PageStateModel.retrieve();
            var docView = Doc.construct(
                    pushStateRouting, 
                    viewerContextModel,
                    tabModel);

            // only load dialog after the rest of it
            docView.lazyInitialize(viewerContextModel, tabModel);
        });
    }

    function initializeControllers() {
        LoadTabController.initialize();
        CreateGameController.initialize();
        DialogController.initialize();
        LoginController.initialize();
    }

    initialize();
});
