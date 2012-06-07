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
            "view/tab",
            
        ],
        function($, Backbone, Const, Tab) {

    /*
        Class: DocView
        Manage all DOM manipulations under <body>. Accessed as a Singleton.

        Subclasses:
            <Backbone.View at http://documentcloud.github.com/backbone/#View>

    */
    var DocView = Backbone.View.extend({
    
        // Variable: el
        // Element of this View.
        el: $(Const.DOM.BODY),

        // Variable: dialog
        // DialogView under DocView.
        dialog: null,

        tabView: null,

        // Function: initialize
        // Setup DialogView with dialog html file.
        initialize: function (initDOMForRouting, loadTabController) {
            this.setTabView();

            if (initDOMForRouting) {
                this.initializeDOMForRouting(loadTabController);
            }

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

            // FIXME XXX remove this - it's only for debugging.
            setTimeout(function () {
                thisDocView.showDialog(); 
            }, 300);
        },
        
        setTabView: function () {
            var tabViewParams = {
                context: Const.ID.CONTEXT,
                nav: Const.DOM.NAV,
                content: Const.ID.CONTENT,
            };
            this.tabView = Tab.construct(tabViewParams);

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
            var createGameView = Dialog.construct({
                el: Const.ID.DIALOG_CONTAINER,
                html: dialogHTML,
                height: pageHeight,
            });
            DialogController.initialize(createGameView);
            return createGameView;
        }, 


        /* 
            Function: showDialog
            Show the dialog portion of the DOM.
        */
        showDialog: function () {
            console.log(this);
            var id = this.tabView.contextView.contextID();
            var rivals = this.tabView.contextView.rivals();
            this.dialog.render(id, rivals, this.path());
        },


        /* 
            Function: hideDialog
            Hide the dialog portion of the DOM.
        */
        hideDialog: function () {
            this.dialog.hide();
        },

        

        /* 
            Function: updateTab
            Update both the context and the content with new html. 
            Then update mixpanel with a Tab View Page.

            Parameters:
                contextHTML - (string) new html for updating context
                contentHTML - (string) new html for udpating content
        */
        updateTab: function (contextHTML, contentHTML) {
            this.tabView.render(contextHTML, contentHTML);
        },
        
        /*
        

        */
        initializeDOMForRouting: function (loadTabController) {
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
                        loadTabController.handleSubmit(this, href);
                    }
                }
            });
        },

    });

    // Variable: docView
    // Keep track of Singleton DocView instantiation.
    var docView = null;

    return {
        construct: function (initDOMForRouting, loadTabController) {
            if (docView === null) {
                docView = new DocView(initDOMForRouting, loadTabController);

            }
            return docView;
        },
        retrieve: function() {
            return docView;
        },
    };
});
