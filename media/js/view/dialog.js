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
                this.$el.height(this.options.height); // set the correct height
                
                // initialize form

                this._setupForm(this.options.context_id);
            },

            // events for this View
            events: function() {
                    var _events = {}; // to allow for variables in the keys...
                    _events["submit " + Constants.NAME.CREATE_GAME] = "submitDialog";
                    var closeButton = Constants.DOM.BUTTON + Constants.CLASS.CLOSE;
                    _events["click " + closeButton] = "closeDialog";
                    return _events;
            },

            // Handle form submission
            submitDialog: function(event) {
                // using toObject from form2js jquery plugin
                Crud.create("game", $(event.target).toObject());
                this.hide();
                // TODO reset form (after game is created successfully...)
                return false;
            },

            // Handle closing dialog
            closeDialog: function() {
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

            // Set up form
            _setupForm: function(league_id) {
                // pull user's league value from context object
                this.$el.find(Constants.NAME.LEAGUE).val(league_id);
            
                // TODO: add additional row functionality
                // diabled row, gets enabled, add new row


            },

        });

        
        return DialogView;
    }
);

