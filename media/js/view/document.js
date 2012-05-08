/* 
    Module: Document
    Manage all DOM manipulations by extending Backbone's View.

    Package:
        view

    Dependencies:
        $
        Backbone
        Const
        Scroller - iScroll
        DialogView - view.DialogView
        dialog_html - (string) text.dialog.creategame

*/
define(
    [
        "jQuery",
        "Backbone",
        "js/constants",
        "iScroll",
        "view/dialog",
        "text!/dialog/creategame",
    ],
    function($, Backbone, Const, Scroller, DialogView, dialog_html) {

        
        // Variable: doc_view
        // Store Singleton DocView.
        var doc_view = null;
        
        
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


            // Function: initialize
            // Setup DialogView with dialog html file.
            initialize: function() {
                this.dialog = this.setDialog(dialog_html);
            },

            
            /* 
                Function: events
                Add all event handlers.

                Events:
                    click .dialog-link --> showDialog
                
                Note: Keep _events notation to allow event keys to be 
                variables.
            */
            events: function() {
                var _events = {};

                _events["click " + Const.CLASS.DIALOG_LINK] = "showDialog";
                return _events;
            },


            /*
                Function: updateContent
                Update the content with the new html.

                Parameters:
                    new_html - (string) HTML with new content.

                Hide the old content, update to the new content, rescroll
                to screen top, show new content, and resize the scroller.
            */
            updateContent: function(new_html) {
                $(Const.ID.CONTENT).toggle(false); 
                $(Const.ID.CONTENT).html(new_html);                
                Scroller.scrollTo(0, 0, 0);  // scroll to x, y, time (ms)
                $(Const.ID.CONTENT).fadeIn('fast');
                Scroller.refresh();
            },
           

            /*
                Function: hideContent
                Hide the content and show a loading screen.
            */
            hideContent: function() {
                $(Const.ID.CONTENT).toggle(false);
                var loading_str = "I know I put the results here somewhere..."
                $(Const.ID.CONTENT).html(loading_str).toggle(true);
            },


            /*
                Function: updateContext
                Update the context header with new html.

                Parameters:
                    new_html - (string) HTML with new content.
            */
            updateContext: function(new_html) {
                $(Const.ID.CONTEXT).replaceWith(new_html);
            },


            /*
                Function: setDialog
                Add dialog html to the DOM and initialize DialogView.

                Parameters:
                    dialog_html - (string) HTML with dialog markup.

                Set element to '#dialog-containe', and grab the
                height, context id, and rivals list from the current page.
            */
            setDialog: function(dialog_html) {
                var page_height = $(Const.ID.PAGE).height(); // page height
                var create_game_dialog = new DialogView({
                    el: Const.ID.DIALOG_CONTAINER,
                    html: dialog_html,
                    height: page_height,
                    context_id: $(Const.ID.CONTEXT).data(Const.DATA.ID),
                    rivals: $(Const.ID.CONTEXT).data(Const.DATA.RIVALS)
                });
                return create_game_dialog;
            }, 


            /* 
                Function: showDialog
                Show the dialog portion of the DOM.
            */
            showDialog: function() {
                this.dialog.show();
            },


            /* 
                Function: hideDialog
                Hidethe dialog portion of the DOM.
            */
            hideDialog: function() {
                this.dialog.hide();
            },

        });


        /* 
            Function: getDocView
            Provide access to singleton DocView.
        */
        function getDocView() {
            if (doc_view == null) {
                doc_view = new DocView();
            }
            return doc_view;
        }

        return {
            getDocView: getDocView
        };
    }
);

