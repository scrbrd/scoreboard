/**
    Handle requesting a new tab and its effect on the page state.

    LoadTabController.controller inherits from BaseController.controller.

    @exports LoadTabController

    @requires $
    @requires Backbone
    @requires MP
    @requires Const
    @requires Event
    @requires BaseController
    @requires Crud
*/
define(
        [
            "jQuery",
            "Backbone",
            "MP",
            "js/constants",
            "js/event",
            "controller/base",
            "js/crud",
        ],
        function ($, Backbone, MP, Const, Event, BaseController, Crud) {
    
    /**
        Controller instance for tab and page loading.
        @constructor
    */
    var loadTabController = (function () {
        var that = Object.create(BaseController.controller);

        /** 
            Bind VIEW_PAGE, RELOAD_PAGE, and VIEWED_PAGE events.
        */
        that.initialize = function () {
            var events = {};

            events[Event.CLIENT.VIEW_PAGE] = that.handleViewPage;
            events[Event.CLIENT.RELOAD_PAGE] = that.handleReloadPage;
            events[Event.SERVER.VIEWED_PAGE] = that.handleSuccess;
            that.initializeEvents(events);
        };
   
        /**
            Handle loading a new tab by generating a loading screen and 
            sending a request to the server.
            @param {string} href The requested url.
            @param {Object} pageStateModel The Page State to keep updated.
        */
        that.handleSubmit = function (href, pageStateModel) {
            // set loading screen
            var loading = "<div class=\"loading\">Loading...</div>";
            pageStateModel.setContent(loading);
            
            Crud.readTab(href, pageStateModel);
        };
        
        /** 
            Handle successful VIEWED_PAGE by tracking the event with MixPanel.
            @param {string} pageType
            @param {string} pageName
            @param {string} path
        */
        that.handleSuccess = function (pageType, pageName, path) {
            if (pageType === Const.PAGE_TYPE.TAB) {
                MP.trackViewTab(pageName, path);
            } else if (pageType === Const.PAGE_TYPE.LANDING) {
                MP.trackViewLanding(pageName, path);
            } else  {
                console.log("never called");
                MP.trackViewDialog(pageName, path);
            } 
        };

        /**
            Update the URL with the new page name and submit the request.
            @param {string} anchor The anchor tag that launched this event.
            @param {string} href The requested url.
            @param {Object} pageStateModel The Page State to keep updated.
        */
        that.handleViewPage = function (anchor, href, pageStateModel) {
            // switch active tab
            var pageName = "";
            if ($(anchor).hasClass(Const.PAGE_NAME.RANKINGS)) {
                pageName = Const.PAGE_NAME.RANKINGS;
            } else if ($(anchor).hasClass(Const.PAGE_NAME.GAMES)) {
                pageName = Const.PAGE_NAME.GAMES;
            }
            pageStateModel.setPageName(pageName);

            // Update URL
            Backbone.history.navigate(href, {trigger: false});

            that.handleSubmit(href, pageStateModel);
        };

        /** 
            Wrapper around handleSubmit for requesting a reloaded page.
            @param {string} href The requested url.
            @param {Object} pageStateModel The Page State to keep updated.
        */
        that.handleReloadPage = function(href, pageStateModel) {
            that.handleSubmit(href, pageStateModel);
        };
        
        return that;
    }());

    return {
        controller: loadTabController,
    };
});
