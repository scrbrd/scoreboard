/**
    Manage all DOM manipulations by extending Backbone's View.

    TODO: most of this functionality should be split between
    page, dialog, and tab. There might need to be a subpage.
    page: landing, tab, dialog
    tab: games, rankings

    TODO: handle the lazy dependencies.
    Lazy Dependencies:
        DialogView - view.DialogView
        dialogHTML - (string) text.dialog.creategame

    @exports DocView
    
    @requires $
    @requires Backbone
    @requires Const
    @requires Event
    @requires EventDispatcher
    @requires DOMUtil
    @requires TabView
    @requires DialogView
*/
define(
        [
            "jQuery",
            "Backbone",
            "js/constants",
            "js/event",
            "js/eventDispatcher",
            "util/dom",
            "view/tab",
            "view/dialog"
        ],
        function ($, Backbone, Const, Event, EventDispatcher, DOMUtil, Tab, Dialog) {


/**
    Manage all DOM manipulations under <body>.
    Accessed as a Singleton.
    @constructor
*/
var DocView = Backbone.View.extend({

    tab: null, // the application's tabView
    dialog: null, // the application's dialogView
    sessionModel: null,
    pageStateModel: null,

    /**
        Initialize View, pull data for models, and setup page.
        @param {Object} sessionModel
        @param {Object} pageStateModel
    */
    initialize: function (sessionModel, pageStateModel) {

        this.setElement(Const.DOM.BODY);
        this.sessionModel = sessionModel;
        this.pageStateModel = pageStateModel;

        this.updateSessionModel(sessionModel);
        this.updatePageStateModel(pageStateModel);

        // if the page is a tab then create the tab and associated dialog js
        // components.
        if (pageStateModel.pageType() === Const.PAGE_TYPE.TAB) {
            this.tab = Tab.construct(sessionModel, pageStateModel);

            // setup dialog
            this.dialog = this.setDialog(Dialog);
        } else {
            // TODO have this happen automatically.
            this.pageStateModel.setPageType(Const.PAGE_TYPE.LANDING);
        }


        console.log("initial load page type: ", pageStateModel.pageType());
        EventDispatcher.trigger(
                Event.SERVER.VIEWED_PAGE,
                pageStateModel.pageType(),
                pageStateModel.pageName(),
                this.path());
    },

    /**
        Pull data from HTML and insert into SessionModel.
        @param {Object} model
    */
    updateSessionModel: function (model) {
        var sessionElem = $(Const.MODEL_ID.SESSION);
        if (sessionElem.length > 0) {
            model.setRivals(sessionElem.data(Const.DATA.RIVALS));
            model.setSports(sessionElem.data(Const.DATA.SPORTS));
            model.setPersonID(sessionElem.data(Const.DATA.PERSON_ID));
            EventDispatcher.trigger(Event.SERVER.UPDATED_SESSION, model);
        }
    },

    /**
        Pull data from HTML and insert into PageStateModel
        @param {Object} model
    */
    updatePageStateModel: function (model) {
        // on initial load i'm leaving content and context fields empty.
        var pageStateElem = $(Const.MODEL_ID.PAGE_STATE);
        var contextElem = $(Const.MODEL_ID.CONTEXT);
        
        model.setPageType(pageStateElem.data(Const.DATA.PAGE_TYPE));
        model.setPageName(pageStateElem.data(Const.DATA.PAGE_NAME));
        model.setContextID(contextElem.data(Const.DATA.ID));
    },

    /**
        Grab the path from the location bar.
        TODO: put this in page state or a framework.
    */
    path: function () {
        return $(location).attr('pathname');
    },

    /**
        Setup View event triggers.
        Keep _events notation to allow event keys to be variables.
    */
    events: function () {
        var _events = {};

        // TODO: make the event types constants
        var selector = Const.CLASS.CREATE_BUTTON;
        _events["touchstart " + selector] = "showDialog";
        _events["click " + selector] = "showDialog";
        return _events;
    },

    /**
        Add dialog html to the DOM and initialize DialogView.
        @param {Object} Dialog DialogView
    */
    setDialog: function (Dialog) {
        // make the dialog height = current page height
        var pageHeight = $(Const.ID.TAB).height();
        var createGameView = Dialog.construct(
                this.sessionModel,
                this.pageStateModel,
                pageHeight);
        return createGameView;
    },

    /**
        Send off a show dialog event.
    */
    showDialog: function () {
        EventDispatcher.trigger(
                Event.CLIENT.DISPLAY_DIALOG,
                Const.PAGE_NAME.CREATE_GAME,
                this.path());

        this.dialog.show();
    },

    /**
        Hide the dialog.
    */
    hideDialog: function () {
        this.dialog.hide();
    },

    /**
        Reload current page.
    */
    refresh: function () {
        this.reloadPage();
    },

    /**
        Setup DOM anchors for routing by disabling the ones that
        javascript will handle.
    
        TODO: make this better, introduce constants, clean up 'this'
    */
    initializePushStateDOM: function () {
        // SRC = https://github.com/tbranyen/backbone-boilerplate
        // All navigation that is relative should be passed through
        // the navigate method, to be processed by the router.  If
        // the link has a data-bypass attribute, bypass the
        // delegation completely.
        var pageStateModel = this.pageStateModel;

        // For Anchors that are being internally routed (internal page views),
        // disable default functionality, and set up view page trigger.
        $(document).on(
                "touchstart click",
                Const.CLASS.ANCHOR + ":not(" + Const.CLASS.NON_ROUTING_ANCHOR + ")",
                function (event) {
            // Get the anchor href and protcol
            var href = $(this).attr("href");
            var protocol = this.protocol + "//";

            // Ensure the protocol is not part of URL, meaning its relative.
            if (href && href.slice(0, protocol.length) !== protocol) {
        
                // Stop the default event to ensure the link will not cause
                // a page refresh.
                event.preventDefault();

                // `Backbone.history.navigate` is sufficient for all
                // Routers and will
                // trigger the correct events.  The Router's internal
                // `navigate` method calls this anyways.
                // can use something separate from routing by labeling
                // route-bypass
                var inactiveClass = DOMUtil.getClassFromSelector(
                    Const.CLASS.INACTIVE_NAV);
                if ($(this).hasClass(inactiveClass)) {
                    EventDispatcher.trigger(
                            Event.CLIENT.VIEW_PAGE,
                            this,
                            href,
                            pageStateModel);
                }
            }
        });

        // Trigger RELOAD_PAGE when page is asked to be reloaded.
        this.reloadPage = function () {
            var pageName = pageStateModel.pageName();
            var contextID = pageStateModel.contextID();
            var href = "/" + pageName + "/" + contextID;
            EventDispatcher.trigger(
                    Event.CLIENT.RELOAD_PAGE,
                    href,
                    pageStateModel);
        };

        // Trigger Login Event before following link.
        $(document).on(
                "touchstart click",
                Const.CLASS.FACEBOOK_LOGIN_ANCHOR,
                function (event) {
            EventDispatcher.trigger(Event.CLIENT.REQUEST_FACEBOOK_LOGIN);
            return true;
        });
    }
});


// Keep track of Singleton DocView instantiation.
var docView = null;

return {
    construct: function (loadPageController, model) {
        if (docView === null) {
            docView = new DocView(loadPageController, model);
        }
        return docView;
    },
    initializePushStateDOM: function () {
        docView.initializePushStateDOM();
    },
    retrieve: function () {
        return docView;
    },
    refresh: function () {
        docView.refresh();
    }
};


});
