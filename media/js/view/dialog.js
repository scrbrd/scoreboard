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
            "util/dom",
            "controller/createGame",
        ],
        function($, Backbone, Const, DomUtil, CreateGameController) {

    /*
        Class: DialogView
        Manage all DOM manipulations under "#dialog".

        Subclasses:
            <Backbone.View at http://documentcloud.github.com/backbone/#View>
    */
    var DialogView = Backbone.View.extend({
        
        // Variable: form
        // The jQuery object of the included form
        form: null,
        
        
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
        initialize: function () {
            this.$el.hide();
            this.$el.append(this.options.html); 
            this.$el.height(this.options.height); 
            this.form = this.$(Const.NAME.CREATE_GAME);
        },


        /* 
            Function: events
            Add all event handlers.

            Events:
                submit form[name='.create-game'] --> submit
                click button.close --> hide

            Note: Keep _events notation to allow event keys to be 
            variables.
        */
        events: function () {
            var _events = {};
            var submitForm = Const.NAME.CREATE_GAME;
            var closeButton = Const.CLASS.CLOSE_BUTTON;
            
            _events["submit " + submitForm] = "submit";
            _events["touchstart " + closeButton] = "hide"; 
            _events["click " + closeButton] = "hide";
            return _events;
        },


        /* 
            Function: setupForm
            Sets up the dialog's form with contextual 
            values and autocomplete functionality.

            Parameters:
                league_id - (int) Api id for page's League object.
                rivals - (list) List of objects representing rivals,
                        with the keys "id", "name"

        */
        setupForm: function(league_id, rivals) {
            // Pull page's league id value from context object
            this.form.find(Const.NAME.LEAGUE).val(league_id);
        
            // TODO: add additional row functionality
            // diabled row, gets enabled, add new row

            // set up autocomplete for each player selection
            $(Const.NAME.CREATE_GAME + ' ' + Const.CLASS.AUTOCOMPLETE)
                .each(function (index, elem) {
                    DomUtil.autocomplete(elem, rivals);
                });
    
        },
        
                    
        /* 
            Function: submit
            Submit dialog's form and hangle all data manipulation.

            Parameters:
                event - the event that caused this handler to trigger

            See:
                form2js.toObject
        */
        submit: function (event) {
            var createGameParams = $(event.target).toObject();
            CreateGameController.handleSubmit(createGameParams);
            return false;
        },


        /* 
            Function: hideDialog
            Hides dialog.
        */
        hide: function () {
            var form = this.form;
            // FIXME make this blurring work and clear the autocomplete.
            $('input:focus').blur(); // blurring the focus should hide keyboard
            this.$el.slideUp('fast', function() {
                // TODO: make this nicer...
                form[0].reset();
            });
            return false;
        },
    

        /* 
            Function: render
            Show this View with proper bells and whistles.
        */
        render: function (leagueID, rivals, path) {
            this.setupForm(leagueID, rivals);
            this.$el.slideDown('fast', function () {
                //var a = this.$('.ui-autocomplete-input').first();
                //a.focus();
            });

            this.trigger(
                    Const.EVENT.DISPLAYED_DIALOG, 
                    Const.PAGE_NAME.CREATE_GAME, 
                    path);
            return false;
        },



    });

    return {
        construct: function (options) {
            return new DialogView(options);
        },

    };
});

