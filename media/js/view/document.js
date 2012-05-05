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
            el: $(Constants.BODY_SELECTOR),

            // Reference to DialogView that will be set upon initialize.
            dialog: null,

            initialize: function() {
                this.dialog = this.set_dialog(dialog_html);
            },

            events: {
                "click .dialog-link":       "show_dialog"       // show hidden dialog
            },

            // Update content component, scroll to top, show, and refresh iScroll
            update_content: function(new_html) {
                $(Constants.CONTENT_SELECTOR).toggle(false); // hide content 
                $(Constants.CONTENT_SELECTOR).html(new_html); // replace content
                Scroller.scrollTo(0, 0, 0);  // scroll to x, y, time in ms
                $(Constants.CONTENT_SELECTOR).fadeIn('fast'); // fade in
                Scroller.refresh(); // refresh scroller for changes in size
            },
            
            // Hide the content
            hide_content: function() {
                $(Constants.CONTENT_SELECTOR).toggle(false); // hide content
                var loading_str = "I know I put the results here somewhere..."
                $(Constants.CONTENT_SELECTOR).html(loading_str).toggle(true); // show 'loading'
            },

            // Update context header
            update_context: function(new_html) {
                $(Constants.CONTEXT_SELECTOR).html(new_html);
            },

            // Add dialog to DOM
            set_dialog: function(dialog_html) {
                var page_height = $(Constants.PAGE_SELECTOR).height(); // page height
                create_game_dialog = new DialogView({
                    el: Constants.DIALOG_CONTAINER_SELECTOR,
                    html: dialog_html,
                    height: page_height,
                    context_id: $(Constants.CONTEXT_SELECTOR).data(Constants.DATA_ID),
                });
                return create_game_dialog;
            }, 

            // Show dialog
            show_dialog: function() {
                this.dialog.show();
            },

            // Hide dialog
            hide_dialog: function() {
                this.dialog.hide();
            },

        });

        // Singleton DocView
        var doc_view = null;

        // Singleton accessor to DocView 
        // Will only initialize on first request
        function get_document_view() {
            if (doc_view == null) {
                doc_view = new DocView();
            }
            return doc_view;
        }

        // return module for DocView access
        return {
            get_document_view: get_document_view
        };
    }
);

