/* Filename: dialog.js
 *
 * Extend Backbone's View to manage dialog functionality.
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
        "js/crud",
    ],
    function($, Backbone, Constants, Crud) {

        var DialogView = Backbone.View.extend({
           
            // Required:
            // string   html            html to add to the dialog id
            // int      page_height     height that dialog should be
            initialize: function() {
                this.$el.hide(); //hide dialog section
                this.$el.append(this.options.html); // insert html
                this.$el.height(this.options.page_height); // set the correct height
            },

            // events for this View
            events: {
                "submit form[name='create-game']":      "submit_dialog",
                "click button.close":               "close_dialog",
            },

            // Handle form submission
            submit_dialog: function(event) {
                // using toObject from form2js jquery plugin
                Crud.create("game", $(event.target).toObject());
                this.hide();
                // TODO reset form (after game is created successfully...)
                return false;
            },

            // Handle closing dialog
            close_dialog: function() {
                this.hide();
                // TODO reset form
                return false;
            },
            
            // Show dialog screen
            show: function() {
                this.$el.slideDown('fast');
            },

            // Hide dialog screen
            hide: function() {
                this.$el.slideUp('fast');
            },

        });

        
        return DialogView;
    }
);

