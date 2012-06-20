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
            "view/tab",
            
        ],
        function($, Backbone, Const, Event, EventDispatcher, Tab) {

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

        tabView: null,

        // Function: initialize
        // Setup DialogView with dialog html file.
        initialize: function (initDOMForRouting, model) {
            this.setElement(Const.DOM.BODY);
            this.model = model;
            this.setTabView(model);

            if (initDOMForRouting) {
                this.initializeDOMForRouting(model);
            }

            // get initial context and content for model
            // jQuery doesn't have an outerHTML function so i'm using [0]
            EventDispatcher.trigger(
                    Event.SERVER.VIEWED_PAGE,
                    this.model,
                    this.tabView.contextView.$el.clone()[0],
                    this.tabView.contentView.$el.clone()[0],
                    this);
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
        lazyInitialize: function () {
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
                        dialogHTML);
            });
        },
        
        setTabView: function (model) {
            this.tabView = Tab.construct(model);
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
        setDialog: function (Dialog, DialogController, dialogHTML) {
            var pageHeight = $(Const.ID.TAB).height(); // page height
            var createGameView = Dialog.construct(
                    this, 
                    dialogHTML, 
                    pageHeight);
            DialogController.initialize(this);
            return createGameView;
        }, 


        /* 
            Function: showDialog
            Show the dialog portion of the DOM.
        */
        showDialog: function () {
            var contextID = this.model.contextID();
            var rivals = this.model.rivals();
            EventDispatcher.trigger(
                    Event.CLIENT.DISPLAY_DIALOG,
                    Const.PAGE_NAME.CREATE_GAME,
                    contextID, 
                    rivals, 
                    this.path());
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
        initializeDOMForRouting: function (model) {
            // SRC = https://github.com/tbranyen/backbone-boilerplate
            // All navigation that is relative should be passed through 
            // the navigate method, to be processed by the router.  If 
            // the link has a data-bypass attribute, bypass the 
            // delegation completely.
            $(document).on(
                    "touchstart click", 
                    "a:not(.data-bypass)", 
                    function (event) {
                // Get the anchor href and protcol
                var href = $(this).attr("href");
                var protocol = this.protocol + "//";

                // Ensure the protocol is not part of URL, meaning its relative.
                if (href && href.slice(0, protocol.length) !== protocol) {
            
                    // Stop the default event to ensure the link will not cause a page
                    // refresh.
                    event.preventDefault();

                    // `Backbone.history.navigate` is sufficient for all Routers and will
                    // trigger the correct events.  The Router's internal 
                    // `navigate` method calls this anyways.
                    // can use something separate from routing by labeling
                    // route-bypass
                    if ($(this).hasClass(Const.CLASS.INACTIVE_NAV.substr(1))) {
                        EventDispatcher.trigger(
                                Event.CLIENT.VIEW_PAGE,
                                this,
                                href,
                                model);
                    }
                }
            });

            this.reloadPage = function (model) {
                href = "/" + model.pageName();
                        EventDispatcher.trigger(
                                Event.CLIENT.RELOAD_PAGE,
                                href,
                                model);
            };
        },

        /**
        

        */
        refresh: function () {
           this.reloadPage(this.model);
        },

    });

    // Variable: docView
    // Keep track of Singleton DocView instantiation.
    var docView = null;

    return {
        construct: function (initDOMForRouting, loadTabController, model) {
            if (docView === null) {
                docView = new DocView(initDOMForRouting, loadTabController, model);

            }
            return docView;
        },
        retrieve: function () {
            return docView;
        },
        refresh: function () {
            docView.refresh();
        },
    };
});
