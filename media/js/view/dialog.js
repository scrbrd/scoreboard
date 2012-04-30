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
        "constants",
        "crud",
    ],
    function($, Backbone, Constants, Crud) {

        var DialogView = Backbone.View.extend({
           
            
            initialize: function(dialog_html, page_height) {
                this.$el.hide(); //hide dialog section
                this.$el.html(dialog_html); // insert html
                this.$el.height(page_height); // set the correct height
            },

            parameters: function() {
                // TODO get game info from dialog
                parameters = {};
                parameters["league"] = 643;
                parameters["creator"] = 655;
                parameters["game_score"] = [{"id": 651, "score": 1}, {"id": 658, "score": 3}];

                return parameters;
            },

            events: {
                "click button.close":       "hide",      // hide dialog
                "click button.submit":      function() {
                    Crud.create("game", this.parameters);
                    this.hide();
                },

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

