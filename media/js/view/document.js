/* Filename: document.js
 *
 * Extend Backbone's View to manage the document.
 *
 * global require
 *
 */

define(
    [
        // Aliases from main.js to module versions of packages
        "jQuery",
        "Backbone",
        "js/constants",
        "iScroll",
        "view/dialog",
        "text!/dialog/creategame",
    ],
    function($, Backbone, Constants, Scroller, DialogView, dialog_html) {

        // DocView does basic Document Manipulation
        var DocView = Backbone.View.extend({
           
            // This View will hold the body
            el: $(Constants.DOM.BODY),

            // Reference to DialogView that will be set upon initialize.
            dialog: null,

            initialize: function() {
                this.dialog = this.setDialog(dialog_html);
            },

            events: function() {
                var _events = {}; // to allow for variables in the keys...
                _events["click " + Constants.CLASS.DIALOG_LINK] = "showDialog";
                return _events;
            },

            // Update content component, scroll to top, show, and refresh iScroll
            updateContent: function(new_html) {
                $(Constants.ID.CONTENT).toggle(false); // hide content 
                $(Constants.ID.CONTENT).html(new_html); // replace content
                Scroller.scrollTo(0, 0, 0);  // scroll to x, y, time in ms
                $(Constants.ID.CONTENT).fadeIn('fast'); // fade in
                Scroller.refresh(); // refresh scroller for changes in size
            },
            
            // Hide the content
            hideContent: function() {
                $(Constants.ID.CONTENT).toggle(false); // hide content
                var loading_str = "I know I put the results here somewhere..."
                $(Constants.ID.CONTENT).html(loading_str).toggle(true); // show 'loading'
            },

            // Update context header
            updateContext: function(new_html) {
                $(Constants.ID.CONTEXT).html(new_html);
            },

            // Add dialog to DOM
            setDialog: function(dialog_html) {
                var page_height = $(Constants.ID.PAGE).height(); // page height
                var create_game_dialog = new DialogView({
                    el: Constants.ID.DIALOG_CONTAINER,
                    html: dialog_html,
                    height: page_height,
                    context_id: $(Constants.ID.CONTEXT).data(Constants.DATA.ID),
                });
                return create_game_dialog;
            }, 

            // Show dialog
            showDialog: function() {
                this.dialog.show();
            },

            // Hide dialog
            hideDialog: function() {
                this.dialog.hide();
            },

        });

        // Singleton DocView
        var doc_view = null;

        // Singleton accessor to DocView 
        // Will only initialize on first request
        function getDocumentView() {
            if (doc_view == null) {
                doc_view = new DocView();
            }
            return doc_view;
        }

        // return module for DocView access
        return {
            getDocumentView: getDocumentView
        };
    }
);

