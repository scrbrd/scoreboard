/**
    Handle requesting a new page, its effect on the page state, and tracking
    with MixPanel.

    LoadPageController.controller inherits from BaseController.controller.

    @exports LoadPageController

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
        Controller instance for page and and dialog loading.
        @constructor
    */
    var loadPageController = (function () {
        var that = Object.create(BaseController.controller);

        /** 
            Bind VIEW_PAGE, RELOAD_PAGE, and VIEWED_PAGE events.
        */
        that.initialize = function () {
            var events = {};

            events[Event.CLIENT.DISPLAY_DIALOG] = that.handleViewedDialog;
            events[Event.CLIENT.RELOAD_PAGE] = that.handleReloadPage;
            events[Event.CLIENT.VIEW_PAGE] = that.handleViewPage;
            
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
            } else if (pageType === Const.PAGE_TYPE.DIALOG) {
                MP.trackViewDialog(pageName, path);
            } else {
                console.log("never called");
            }
        };

        /**
            Update MixPanel for a display dialog event.

            TODO does routing from a CLIENT event to a handleSubmit break 
            some encapsualtion?
            @param {string} pageName
            @param {string} path
        */
        that.handleViewedDialog = function (pageName, path) {
            that.handleSuccess(Const.PAGE_TYPE.DIALOG, pageName, path);
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
        controller: loadPageController,
    };
});
