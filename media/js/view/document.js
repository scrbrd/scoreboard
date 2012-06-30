/* 
    Module: Document
    Manage all DOM manipulations by extending Backbone's View.

    Package:
        view

    Dependencies:
        $
        Backbone
        Const

    Lazy Dependencies:
        DialogView - view.DialogView
        dialogHTML - (string) text.dialog.creategame

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
            
        ],
        function($, Backbone, Const, Event, EventDispatcher, DOMUtil, Tab) {

    /*
        Class: DocView
        Manage all DOM manipulations under <body>. Accessed as a Singleton.

        Subclasses:
            <Backbone.View at http://documentcloud.github.com/backbone/#View>

    */
    var DocView = Backbone.View.extend({
    
        // Variable: el
        // Element of this View.

        // Variable: dialog
        // DialogView under DocView.
        dialog: null,

        tab: null,

        // Function: initialize
        // Setup DialogView with dialog html file.
        initialize: function (
                viewerContextModel,
                pageStateModel) {

            this.setElement(Const.DOM.BODY);
            this.viewerContextModel = viewerContextModel;
            this.pageStateModel = pageStateModel;

            this.updateViewerContextModel(viewerContextModel);
            this.updatePageStateModel(pageStateModel);

            if (pageStateModel.pageType() === Const.PAGE_TYPE.TAB) {
                this.setTabView(pageStateModel);
            } else {
                // TODO have this happen automatically.
                this.pageStateModel.setPageType(Const.PAGE_TYPE.LANDING);
            }

            // get initial context and content for model
            // jQuery doesn't have an outerHTML function so i'm using [0]
            console.log("initial load page type: ", pageStateModel.pageType());
            EventDispatcher.trigger(
                    Event.SERVER.VIEWED_PAGE,
                    pageStateModel.pageType(),
                    pageStateModel.pageName(),
                    this.path());
        },

        updateViewerContextModel: function (model) {
            var viewerElem = $(Const.MODEL_ID.VIEWER_CONTEXT);
            model.setRivals(viewerElem.data(Const.DATA.RIVALS));
        },

        updatePageStateModel: function (model) {
            // on initial load i'm leaving content and context fields empty.
            var pageStateElem = $(Const.MODEL_ID.PAGE_STATE);
            var contextElem = $(Const.MODEL_ID.CONTEXT);
            
            model.setPageType(pageStateElem.data(Const.DATA.PAGE_TYPE));
            model.setPageName(pageStateElem.data(Const.DATA.PAGE_NAME));
            model.setContextID(contextElem.data(Const.DATA.ID));
        },

        path: function () {
            return $(location).attr('href');
        },

        // Function: lazyIntialize():
        // Initialize post DOM load functionality.
        //
        // Dependencies:
        // DialogView - view.DialogView
        // dialogHTML - (string) text.dialog.creategame
        lazyInitialize: function (viewerContext, pageState) {
            var thisDocView = this;
            require(
                    [
                        "view/dialog", 
                        "controller/dialog",
                        "text!/dialog/creategame"], 
                    function (Dialog, DialogController, dialogHTML) {
                thisDocView.dialog = thisDocView.setDialog(
                        Dialog, 
                        DialogController,
                        dialogHTML,
                        viewerContext, 
                        pageState);
            });
        },
        
        setTabView: function (model) {
            this.tab = Tab.construct(model);
        },


        /* 
            Function: events
            Add all event handlers.

            Events:
                click JS_LINK --> showDialog
            
            Note: Keep _events notation to allow event keys to be 
            variables.
        */
        events: function () {
            var _events = {};

            _events["touchstart " + Const.CLASS.JS_LINK] = "showDialog";
            _events["click " + Const.CLASS.JS_LINK] = "showDialog";
            return _events;
        },

        /*
            Function: setDialog
            Add dialog html to the DOM and initialize DialogView.

            Parameters:
                dialogHTML - (string) HTML with dialog markup.

            Set element to '#dialog-containe', and grab the
            height from the current page.
        */
        setDialog: function (
                Dialog, 
                DialogController, 
                dialogHTML, 
                viewerContext, 
                pageState) {
            var pageHeight = $(Const.ID.TAB).height(); // page height
            var createGameView = Dialog.construct(
                    dialogHTML,
                    viewerContext,
                    pageState,
                    pageHeight);
            return createGameView;
        }, 


        /* 
            Function: showDialog
            Show the dialog portion of the DOM.
        */
        showDialog: function () {
            EventDispatcher.trigger(
                    Event.CLIENT.DISPLAY_DIALOG,
                    Const.PAGE_NAME.CREATE_GAME,
                    this.path());
            return true;
        },


        /* 
            Function: hideDialog
            Hide the dialog portion of the DOM.
        */
        hideDialog: function () {
            this.dialog.hide();
        },

        

        /*
        

        */
        initializePushStateDOM: function () {
            // SRC = https://github.com/tbranyen/backbone-boilerplate
            // All navigation that is relative should be passed through 
            // the navigate method, to be processed by the router.  If 
            // the link has a data-bypass attribute, bypass the 
            // delegation completely.
            var model = this.pageStateModel;

            $(document).on(
                    "touchstart click", 
                    "a:not(" + Const.CLASS.EXTERNAL_LINK + ")", 
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
                                model);
                    }
                }
            });

            this.reloadPage = function () {
                href = "/" + model.pageName();
                EventDispatcher.trigger(
                        Event.CLIENT.RELOAD_PAGE,
                        href,
                        model);
            };

            $(document).on(
                    "touchstart click", 
                    Const.CLASS.FACEBOOK_LOGIN_BUTTON, 
                    function (event) {
                EventDispatcher.trigger(Event.CLIENT.REQUEST_FACEBOOK_LOGIN);
                return true;
            });

        },

        /**
        

        */
        refresh: function () {
           this.reloadPage();
        },

    });

    // Variable: docView
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
        },
    };
});
