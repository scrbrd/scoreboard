/* 
    Module: Dialog
    Manage DOM manipulations of Dialog by extending Backbone's View.

    Package:
        view

    Dependencies:
        $
        Backbone
        Const
        Crud - Create, Read, Update, Delete
        DomUtil - util.DomUtil
*/
define(
    [
        "jQuery",
        "Backbone",
        "js/constants",
        "js/crud",
        "util/dom",
    ],
    function($, Backbone, Const, Crud, DomUtil) {

        /*
            Class: DialogView
            Manage all DOM manipulations under "#dialog".

            Subclasses:
                <Backbone.View at http://documentcloud.github.com/backbone/#View>

        */
        var DialogView = Backbone.View.extend({
           
            /*
                Function: initialize
                Initialize all sub-elements of DialogView.

                Options:
                    html - (string) HTML to add to the dialog element.
                    height - (int) Dialog element's height.
                    context_id - (int) Api id of the context of the dialog.
                    rivals - (json) List of objects representing rivals. 
                             These objects have keys "id", "name".

                First hides the dialog element, then adds the new markup, then
                stretches it to the proper height, and finally initializes its
                form.
            */
            initialize: function() {
                this.$el.hide();
                this.$el.append(this.options.html); 
                this.$el.height(this.options.height); 

                this._setupForm(this.options.context_id, this.options.rivals);
            },


            /* 
                Function: events
                Add all event handlers.

                Events:
                    submit form[name='.create-game'] --> submitDialog
                    click button.close --> closeDialog

                Note: Keep _events notation to allow event keys to be 
                variables.
            */
            events: function() {
                var _events = {};
                var submitForm = Const.NAME.CREATE_GAME;
                var closeButton = Const.DOM.BUTTON + Const.CLASS.CLOSE;
                
                _events["submit " + submitForm] = "submitDialog";
                _events["click " + closeButton] = "closeDialog";
                return _events;
            },


            /* 
                Function: submitDialog
                Submit dialog's form and hangle all data manipulation.

                Parameters:
                    event - the event that caused this handler to trigger

                See:
                    form2js.toObject
            */
            submitDialog: function(event) {
                // TODO reset form (after game is created successfully...)

                Crud.createGame($(event.target).toObject());
                this.hide();
                return false;
            },


            /* 
                Function: closeDialog
                Close and hide dialog.
            */
            closeDialog: function() {
                // TODO reset form
                
                this.hide();
                return false;
            },
            

            /* 
                Function: show
                Show this View with proper bells and whistles.
            */
            show: function() {
                this.$el.slideDown('fast');
            },


            /* 
                Function: hide
                Hide this View with proper bells and whistles.
            */
            hide: function() {
                this.$el.slideUp('fast');
            },


            /* 
                Function: _setupForm
                Sets up the dialog's form with contextual 
                values and autocomplete functionality.

                PRIVATE
                
                Parameters:
                    league_id - (int) Api id for page's League object.
                    rivals - (list) List of objects representing rivals,
                            with the keys "id", "name"

            */
            _setupForm: function(league_id, rivals) {
                // Pull page's league id value from context object
                this.$el.find(Const.NAME.LEAGUE).val(league_id);
            
                // TODO: add additional row functionality
                // diabled row, gets enabled, add new row

                // set up autocomplete for player selection
                DomUtil.Autocomplete.autocompletePlayer(
                        rivals,
                        Const.NAME.CREATE_GAME,
                        Const.CLASS.PLAYER_SELECT);
            },
        });
        return DialogView;
    }
);

