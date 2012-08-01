/**
    A specific (TODO: generic) implementation of a Dialog View.

    dialog.js subclasses Backbone.View to provide DOM manipulation of
    a dialog. Views should be passed Models and only interact with Controllers
    through Events. DialogView doesn't need to know about any other Views.

    @exports DialogView

    @requires $
    @requires Backbone
    @requires Const
    @requires Event
    @requires EventDispatcher
    @requires AutocompleteUtil
*/
define(
        [
            "jQuery",
            "Backbone",
            "js/constants",
            "js/event",
            "js/eventDispatcher",
            "util/autocomplete"
        ],
        function (
                $,
                Backbone,
                Const,
                Event,
                EventDispatcher,
                AutocompleteUtil) {


var MODEL_EVENT = {
    CHANGE_RIVALS: "change:" + Const.DATA.RIVALS,
    CHANGE_CONTEXT_ID: "change:" + Const.DATA.ID
};

/**
    Manage all DOM manipulations under "#dialog".
    @constructor
*/
var DialogView = Backbone.View.extend({

    // the dialog's form
    form: null,

    // page name of the dialog
    // TODO: put this in DialogStateModel
    pageName: Const.PAGE_NAME.CREATE_GAME,

    /**
        Hide and stretch dialog, initialize its form, and bind change
        events from Models.
        @param {string} html html that this View contains
        @param {Object} viewerContextModel
        @param {Object} pageStateModel
        @param {string} height height of the dialog
    */
    initialize: function (
            html,
            sessionModel,
            pageStateModel,
            height) {
        this.setElement(Const.ID.DIALOG_CONTAINER);
        this.sessionModel = sessionModel;
        this.pageStateModel = pageStateModel;

        this.$el.hide();
        this.$el.append(html);
        this.$el.height(height);
        this.form = this.$(Const.NAME.CREATE_GAME);

        this.sessionModel.on(
                MODEL_EVENT.CHANGE_RIVALS,
                this.render,
                this);
        this.pageStateModel.on(
                MODEL_EVENT.CHANGE_CONTEXT_ID,
                this.render,
                this);

        this.render();
    },

    /**
        Setup DialogView event triggers.
        Keep _events notation to allow event keys to be variables.
    */
    events: function () {
        var _events = {};
        var submitForm = Const.NAME.CREATE_GAME;
        var closeButton = Const.CLASS.CLOSE_BUTTON;

        // TODO: make the event types constants
        _events["submit " + submitForm] = "submit";
        _events["touchstart " + closeButton] = "hide";
        _events["click " + closeButton] = "hide";

        return _events;
    },

    /**
        Render this dialog.
    */
    render: function () {
        var leagueID = this.pageStateModel.contextID();
        var rivals = this.sessionModel.rivals();

        this.setupForm(leagueID, rivals);

        return this;
    },

    /**
        Setup dialog's form with event bindings and autocomplete
        functionality.
        @param {string} leagueID the league that the Game will be part of
        @param {Array} rivals An array of rivals for autocomplete
    */
    setupForm: function (leagueID, rivals) {
        var formPageName = this.pageName;
        this.form.find(Const.NAME.LEAGUE_ID).val(leagueID);

        // TODO: add additional row functionality
        // diabled row, gets enabled, add new row

        // set up autocomplete for each player selection
        var selectedPlayers = {};
        $(Const.NAME.CREATE_GAME + ' ' + Const.CLASS.AUTOCOMPLETE_PLAYERS)
            .each(function (index, elem) {
                AutocompleteUtil.autocompletePlayers(
                        elem,
                        rivals,
                        selectedPlayers);
            });

        // FIXME: this probably doesn't work anymore.
        // add event handler for player data entry.
        $(Const.NAME.CREATE_GAME + ' ' + Const.NAME.OPPONENT_ID)
            .change(function (evt) {
                EventDispatcher.trigger(
                        Event.CLIENT.ENTER_GAME_DATA,
                        Const.DATA.PLAYER,
                        evt.target.value,
                        formPageName);
            });

        // FIXME: this probably doesn't work anymore.
        // add event handler for result (W/L) data entry.
        $(Const.NAME.CREATE_GAME + ' ' + Const.NAME.OPPONENT_RESULT)
            .change(function (evt) {
                EventDispatcher.trigger(
                        Event.CLIENT.ENTER_GAME_DATA,
                        Const.DATA.RESULT,
                        evt.target.value,
                        formPageName);
            });

        // bind opponent group display to checkbox value
        var checkbox = $(".switch input[name='game-type']");
        var that = this;
        checkbox.change(function (evt) {
            // reset form
            var checkedVal = checkbox.prop("checked");
            that.resetForm();
            checkbox.prop("checked", checkedVal);

            // switch form type
            if (checkbox.prop("checked")) {
                $(Const.CLASS.OPPONENT_TAGS_GROUP +
                    '.' + Const.VALUE.RIVALRY).show();
                $(Const.CLASS.OPPONENT_TAGS_GROUP +
                    '.' + Const.VALUE.CAMARADERIE).hide();
            } else {
                $(Const.CLASS.OPPONENT_TAGS_GROUP +
                    '.' + Const.VALUE.RIVALRY).hide();
                $(Const.CLASS.OPPONENT_TAGS_GROUP +
                    '.' + Const.VALUE.CAMARADERIE).show();
            }
        });
        checkbox.change();

    },

    /**
        Submit dialog's form and handle all data manipulation.
        @param {Object} evt the event that triggered submit
    */
    submit: function (evt) {
        // See: form2js.toObject
        var createGameParams = $(evt.target).toObject();
        EventDispatcher.trigger(
            Event.CLIENT.CREATE_GAME,
            this.sessionModel,
            createGameParams);
        return false;
    },

    /*
        Hide dialog.
    */
    hide: function () {
        // disable close button to prevent false positives.
        this.$el.find(Const.CLASS.CLOSE_BUTTON).get(0).disabled = true;

        var that = this;
        // FIXME: make this blurring work and clear the autocomplete.
        $('input:focus').blur(); // blurring the focus should hide keyboard
        this.$el.slideUp('fast', function () {
            that.resetForm();
        });
        return false;
    },

    /**
        Display dialog.
    */
    show: function () {
        // TODO: How can we make this 'fast' and not have the close button
        // automatically triggered...?
        this.$el.slideDown('slow', function () {
            // enabled close button once the dialog opens.
            $(this).find(Const.CLASS.CLOSE_BUTTON).get(0).disabled = false;

            // TODO: auto-focus and make the keyboard come up.
            //var a = this.$('.ui-autocomplete-input').first();
            //a.focus();
        });

        return false;
    },

    /**
        Reset dialog's form.
    */
    resetForm: function () {
        this.form[0].reset();
        // also clear the thumbnails
        var thumbnail = this.$el.find(Const.CLASS.AUTOCOMPLETE_THUMBNAIL)
            .attr("src", "/static/images/thumbnail.jpg");
    }
});

return {
    construct: function (
            dialogHTML,
            sessionModel,
            pageStateModel,
            pageHeight) {
        return new DialogView(
                dialogHTML,
                sessionModel,
                pageStateModel,
                pageHeight);
    }
};


});
