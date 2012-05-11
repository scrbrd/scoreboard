/* 
    Module: Document
    Manage all DOM manipulations by extending Backbone's View.

    Package:
        view

    Dependencies:
        MP
        $
        Backbone
        Const
        Scroller - iScroll
        DialogView - view.DialogView
        dialogHTML - (string) text.dialog.creategame

*/
define(
    [
        "MP",
        "jQuery",
        "Backbone",
        "js/constants",
        "iScroll",
        "view/dialog",
        "text!/dialog/creategame",
    ],
    function(MP, $, Backbone, Const, Scroller, DialogView, dialogHTML) {

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

            // Variable: content
            // jQuery element for content.
            content: null,

            // Variable: content
            // jQuery element for context.
            content: null,

            // Variable: path
            // Current path of url.
            path: null,
            
            // Variable: pageName
            // Current page name (from content).
            pageName: null,
            
            // Function: initialize
            // Setup DialogView with dialog html file.
            initialize: function () {
                this.refreshDoc();
                
                this.dialog = this.setDialog(dialogHTML);
                this.trackViewPageByName(this.pageName, this.path);
            },

           
            // Function: refreshDoc
            // Resets doc variables to point to current set
            refreshDoc: function () {
                this.content = this.$(Const.ID.CONTENT);
                this.context = this.$(Const.ID.CONTEXT);
                this.path = $(location).attr('href');
                this.pageName = this.content.data(Const.DATA.PAGE_NAME);
            },


            /* 
                Function: events
                Add all event handlers.

                Events:
                    click .dialog-link --> showDialog
                
                Note: Keep _events notation to allow event keys to be 
                variables.
            */
            events: function () {
                var _events = {};

                _events["click " + Const.CLASS.DIALOG_LINK] = "showDialog";
                return _events;
            },

            /*
                Function: setDialog
                Add dialog html to the DOM and initialize DialogView.

                Parameters:
                    dialogHTML - (string) HTML with dialog markup.

                Set element to '#dialog-containe', and grab the
                height, context id, and rivals list from the current page.
            */
            setDialog: function (dialogHTML) {
                var pageHeight = $(Const.ID.PAGE).height(); // page height
                var createGameDialog = DialogView.initializeCreateGame({
                    el: Const.ID.DIALOG_CONTAINER,
                    html: dialogHTML,
                    height: pageHeight,
                    contextID: this.context.data(Const.DATA.ID),
                    rivals: this.context.data(Const.DATA.RIVALS)
                });
                return createGameDialog;
            }, 


            /* 
                Function: showDialog
                Show the dialog portion of the DOM.
            */
            showDialog: function () {
                this.dialog.show();
            },


            /* 
                Function: hideDialog
                Hide the dialog portion of the DOM.
            */
            hideDialog: function () {
                this.dialog.hide();
            },

            /*
                Function: trackViewPageByName
                Track the right type of page view by checking the page's name.

                Parameters:
                    name - specific name of tab page
                    path - path to page
            */
            trackViewPageByName: function (name, path) {
                if (name === Const.PAGE_NAME.RANKINGS ||
                        name === Const.PAGE_NAME.GAMES) {
                    MP.trackViewTab(name, path);
                } else if (name === Const.PAGE_NAME.CREATE_GAME) {
                    MP.trackViewDialog(name, path);
                } else {
                    MP.trackViewLanding(name, path);
                }

            },

        });

        // Variable: docView
        // Store Singleton DocView.
        var docView = new DocView();
        

        return {
            /* 
                Function: updatePage
                Update both the context and the content with new html. 
                Then update mixpanel with a Tab View Page.

                Parameters:
                    contextHTML - (string) new html for updating context
                    contentHTML - (string) new html for udpating content
            */
            updatePage: function (contextHTML, contentHTML) {
                this.updateContext(contextHTML);
                this.updateContent(contentHTML);

                docView.trackViewPageByName(docView.pageName, docView.path);
            },
            

            /*
                Function: updateContent
                Update the content with the new html.

                Parameters:
                    newHTML - (string) HTML with new content.

                Hide the old content, rescroll to screen top, update new 
                content, show new content, and reset the Scroller. Must 
                reset the Scroller because the newHTML will need to be
                incorporated into its functionality.
            */
            updateContent: function (newHTML) {
                docView.content.toggle(false); 
                Scroller.scrollTo(0, 0, 0);  // scroll to x, y, time (ms)

                docView.content.replaceWith(newHTML);
                docView.refreshDoc();
                
                docView.content.fadeIn('fast');
                Scroller.reset();
            },
           

            /*
                Function: hideContent
                Hide the content and show a loading screen.
            */
            hideContent: function () {
                var loading = "I know I put the results here somewhere...";
                
                docView.content.toggle(false);
                docView.content.html(loading).toggle(true);
            },


            /*
                Function: updateContext
                Update the context header with new html.

                Parameters:
                    newHTML - (string) HTML with new content.
            */
            updateContext: function (newHTML) {
                docView.context.replaceWith(newHTML);
                docView.refreshDoc();
            },
        };
    }
);

