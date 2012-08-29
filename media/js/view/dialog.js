/**
    A specific (TODO: generic) implementation of a Dialog View.

    dialog.js subclasses Backbone.View to provide DOM manipulation of
    a dialog. Views should be passed Models and only interact with Controllers
    through Events. DialogView doesn't need to know about any other Views.

    @exports DialogView

    @requires $
    @requires Backbone
    @requires Const
    @requires iScroll
    @requires Event
    @requires EventDispatcher
    @requires DOMUtil
    @requires Components
*/
define(
        [
            "jQuery",
            "Backbone",
            "iScroll",
            "js/constants",
            "js/event",
            "js/eventDispatcher",
            "util/dom",
            "view/components"
        ],
        function (
                $,
                Backbone,
                Scroller,
                Const,
                Event,
                EventDispatcher,
                DOMUtil,
                Components) {


var MODEL_EVENT = {
    CHANGE_RIVALS: "change:" + Const.DATA.RIVALS,
    CHANGE_SPORTS: "change:" + Const.DATA.SPORTS,
    CHANGE_CONTEXT_ID: "change:" + Const.DATA.ID
};

/**
    Manage all DOM manipulations under "#dialog".
    @constructor
*/
var DialogView = Backbone.View.extend({

    form: null,
    pageName: Const.PAGE_NAME.CREATE_GAME, // TODO: put this in DialogStateModel
    scroller: null, // only create it on show, delete it on hide
    switchControl: null,
    rivalryTagsGroup: null,
    camaraderieTagsGroup: null,
    opponentAutocompletes: null,
    sportAutocomplete: null,

    /**
        Hide and stretch dialog, initialize its form, and bind change
        events from Models.
        @param {Object} viewerContextModel
        @param {Object} pageStateModel
        @param {string} height height of the dialog
    */
    initialize: function (
            sessionModel,
            pageStateModel,
            height) {

        this.setElement(Const.ID.CREATE_GAME);

        this.sessionModel = sessionModel;
        this.pageStateModel = pageStateModel;

        this.$el.hide();
        this.$el.height(height);
        this.form = this.$(Const.NAME.CREATE_GAME);

        this.sessionModel.on(
                MODEL_EVENT.CHANGE_RIVALS,
                this.render,
                this);
        this.sessionModel.on(
                MODEL_EVENT.CHANGE_SPORTS,
                this.render,
                this);
        this.pageStateModel.on(
                MODEL_EVENT.CHANGE_CONTEXT_ID,
                this.render,
                this);

        this.render();
    },

    /**
        Set up DialogView event triggers.
        Keep _events notation to allow event keys to be variables.
    */
    events: function () {
        var _events = {};
        var submitForm = Const.NAME.CREATE_GAME;
        var closeButton = Const.CLASS.CLOSE_BUTTON;
        var switchControl = Const.CLASS.SWITCH_CONTROL;

        // TODO: make the event types constants
        // note that the space after each action string is critical
        _events["submit " + submitForm] = "submit";
        _events["touchstart " + closeButton] = "hide";
        _events["click " + closeButton] = "hide";
        // TODO: make click/touchstart conditional upon the web/mobile
        // environment. can't use both because toggle isn't idempotent.
        //_events["touchstart " + switchControl] = "flipSwitch";
        _events["click " + switchControl] = "flipSwitch";

        return _events;
    },

    /**
        Render this dialog.
    */
    render: function () {
        var leagueID = this.pageStateModel.contextID();
        var rivals = this.sessionModel.rivals();
        var sports = this.sessionModel.sports();

        this.initForm(leagueID, rivals, sports);

        return this;
    },

    /**
        Set up dialog's form with event bindings and autocomplete
        functionality.
        @param {string} leagueID the league that the Game will be part of
        @param {Array} rivals An array of rivals for Autocomplete
        @param {Array} sports An array of Sports for Autocomplete
    */
    initForm: function (leagueID, rivals, sports) {
        var formPageName = this.pageName;
        this.form.find(Const.NAME.LEAGUE_ID).val(leagueID);
        // TODO: add additional row functionality
        // disabled row, gets enabled, add new row

        // set up Autocompletes
        this.opponentAutocompletes = [];
        var that = this;
        this.form.find(Const.CLASS.AUTOCOMPLETE_PLAYER)
            .each(function (index, elem) {
                that.opponentAutocompletes.push(
                        Components.OpponentAutocomplete($(elem), rivals));
            });

        this.sportAutocomplete = Components.SportAutocomplete(
            this.form.find(Const.CLASS.AUTOCOMPLETE_SPORT),
            sports);

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

        // set up opponent tag groups
        this.rivalryTagsGroup = this.form.find(
            Const.CLASS.OPPONENT_TAGS_GROUP + '.' + Const.VALUE.RIVALRY);
        this.camaraderieTagsGroup = this.form.find(
            Const.CLASS.OPPONENT_TAGS_GROUP + '.' + Const.VALUE.CAMARADERIE);

        this.switchControl = this.form.find(Const.CLASS.SWITCH_CONTROL);
        // TODO: get isOn from model, which means its not appropriate for this
        // to be in the view. build a component.
        this.initSwitch(true);
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
            that.resetForm(true);
            // iScroll is destroyed automatically on close.
        });
        return false;
    },

    /**
        Display dialog.
    */
    show: function () {
        // TODO: How can we make this 'fast' and not have the close button
        // automatically triggered...?
        var that = this;
        this.$el.slideDown('slow', function () {
            // enabled close button once the dialog opens.
            that.$el.find(Const.CLASS.CLOSE_BUTTON).get(0).disabled = false;

            // the dialog has to be showing to add the scroller
            that.scroller = Scroller.Scroller(DOMUtil.getIDFromSelector(
                    Const.ID.DIALOG_OUTER_CONTENT_CONTAINER));

            // TODO: auto-focus and make the keyboard come up.
            //var a = this.$('.ui-autocomplete-input').first();
            //a.focus();
        });

        return false;
    },

    /**
        Reset dialog's form.
        @param {boolean} switchState turn the swtich on or off (true or false)
    */
    resetForm: function (switchState) {
        this.form[0].reset();
        for (var i = 0; i < this.opponentAutocompletes.length; i += 1) {
            this.opponentAutocompletes[i].resetAndClear();
        }

        this.sportAutocomplete.resetAndClear();

        // TODO: this should either be a constant or delivered from the model
        // also clear the thumbnails
        var thumbnail = this.$el.find(Const.CLASS.AUTOCOMPLETE_THUMBNAIL)
            .attr("src", "/static/images/thumbnail.jpg");

        // TODO: get isOn from model, which means its not appropriate for this
        // to be in the view. build a component.
        this.resetSwitch(switchState);
    },

    /**
        Reset the state of the Switch and what it controls.
        @param {boolean} switchState turn the switch on or off (true or false)
    */
    resetSwitch: function (switchState) {
        if (this.isSwitchOn() !== switchState) {
            this.flipSwitch();
        }
    },

    /**
        Initialize the state of the Switch and what it controls.
        @param {boolean} flipOn intialize the Switch to flipOn
    */
    initSwitch: function (flipOn) {
        // sync components controlled by the switch with its default state
        this.initSwitchComponents(this.isSwitchOn());

        // if the default doesn't match the specified initial state, flip it
        if (this.isSwitchOn() !== flipOn) {
            this.flipSwitch();
        }
    },

    /**
        Toggle the visual and internal Switch state and what it controls.
    */
    flipSwitch: function () {
        // visually flip the switch
        this.toggleSwitchControl();

        // flip the internal state of the switch
        this.toggleSwitchCheckbox();

        // flip the components controlled by the switch
        this.toggleSwitchComponents();

        // adjust the scroller to the new dialog height
        this.refreshScroller();
    },

    /**
        Determine whether the Switch is currently on.
        @return {boolean}
    */
    isSwitchOn: function () {
        var onClass = DOMUtil.getClassFromSelector(Const.CLASS.SWITCH_ON);
        return this.switchControl.hasClass(onClass);
    },

    /**
        Toggle the visual display of the Switch.
    */
    toggleSwitchControl: function () {
        var onClass = DOMUtil.getClassFromSelector(Const.CLASS.SWITCH_ON);
        this.switchControl.toggleClass(onClass);
    },

    /**
        Toggle the internal state of the Switch.
    */
    toggleSwitchCheckbox: function () {
        var checkbox = this.switchControl.find(Const.CLASS.SWITCH_CHECKBOX);
        // TODO: add html property constants.
        checkbox.prop("checked", this.isSwitchOn());
    },

    /**
        Initialize the components controlled by the Switch.
        @param {boolean} flipOn initialize the Switch components to flipOn
    */
    initSwitchComponents: function (flipOn) {
        this.toggleSwitchCheckbox(flipOn);
    },

    /**
        Toggle the components controlled by the Switch.
        @param {boolean} overrideAndFlipOn optionally specify on/off state
    */
    toggleSwitchComponents: function (overrideAndFlipOn) {
        var flipOn = this.isSwitchOn();
        if (typeof(overrideAndFlipOn) !== "undefined") {
            flipOn = overrideAndFlipOn;
        }

        // reset the form but not the checkbox
        var checkbox = this.switchControl.find(Const.CLASS.SWITCH_CHECKBOX);
        var checkboxState = checkbox.prop("checked");
        this.resetForm(checkboxState);
        checkbox.prop("checked", checkboxState);

        // for reasons passing understanding, toggle does NOT work for hiding
        // and showing these elements. fuck it we're doing it live!
        if (flipOn) {
            this.rivalryTagsGroup.show();
            this.camaraderieTagsGroup.hide();
        } else {
            this.rivalryTagsGroup.hide();
            this.camaraderieTagsGroup.show();
        }
    },

    /**
        Refresh the Scroller for this dialog.
    */
    refreshScroller: function () {
        if (this.scroller !== null) {
            this.scroller.refresh();
        }
    }

});

return {
    construct: function (
            sessionModel,
            pageStateModel,
            pageHeight) {
        return new DialogView(
                sessionModel,
                pageStateModel,
                pageHeight);
    }
};


});
