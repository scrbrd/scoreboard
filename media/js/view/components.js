/**
    All View components. (TODO: split this into a package tree that reflects the
    python layout.

    components.js is a collection of components that subclass Backbone.View.

    @exports Components

    @requires $
    @requires Underscore
    @requires Backbone
    @requires Const
    @requires DOMUtil
*/
define(
        [
            "jQuery",
            "Underscore",
            "Backbone",
            "js/constants",
            "util/dom"
        ],
        function (
                $,
                _,
                Backbone,
                Const,
                DOMUtil) {

/**
    A generic autocomplete component that uses jquery ui.
    @constructor
*/
var Autocomplete = Backbone.View.extend({
   
    labelInput: null,
    valueInput: null,

    /**
        Provide generic autocomplete functionality.
        @param {Object} elem A $ AutocompleteInput element.
    */
    initialize: function (elem) {
        this.setElement(elem);

        this.labelInput = this.$el.children(Const.CLASS.AUTOCOMPLETE_LABEL);
        this.valueInput = this.$el.children(Const.CLASS.AUTOCOMPLETE_VALUE);

        _.bindAll(this);
        this.labelInput.focus(this.buildAutocomplete);

        // if blurred without a selection then clear form.
        var that = this;
        this.labelInput.blur(function (evt) {
            if (that.valueInput.val() === "") {
                that.reset();
            }
        });
    },

    /**
        Supply a jQuery UI Autocomplete to the label input on focus.
    */
    buildAutocomplete: function () {
        // Get the freshest available data
        var selectData = this.generateSourceData();

        var that = this;
        this.labelInput.autocomplete({
            autoFocus: true, // autofocus on first value
            delay: 0, // immediately
            source: selectData, // autocomplete on this data
            minLength: 1, // start autocomplete on third character
            appendTo: that.el, // append dropdown to input element
            select: this.handleSelect, // coordinates label/value with inputs
            // makes changes to display box when opened
            open: function (event, ui) {
                var a = that.$el.children(".ui-autocomplete").css("width", "");
                return false;
            }
        });

        // allows subclasses to change out the ui's items render.
        this.renderItem();
    },

    /**
        Generate the data that the jquery ui autocomplete will pull.
        @return {Object} A dictionary with keys 'label' and 'value'.
    */
    generateSourceData: function () {
        // TODO: fill in this function
        return {};
    },

    /**
        Puts the label in the labelInput and the value in the valueInput, which
        overrides jQuery UI's default functionality.
        @param {Object} evt the event that triggered this function
        @param {Object} ui the jQuery Autocomplete object
        @return false so that jQuery UI Autocomplete can't overwrite the values.
    */
    handleSelect: function (evt, ui) {
        var selectedItem = ui.item;

        this.labelInput.val(selectedItem.label);
        this.valueInput.val(selectedItem.value);
        // TODO: what does this line do???
        this.valueInput.change();
        
        // blur input after selection
        this.labelInput.blur();

        // return false so LabelInput isn't overwritten with the value.
        return false;
    },

    /**
        Provide an alternative to the standard jQuery Autocomplete rendering. The
        commented code provides an example.
    */
    renderItem: function () {
        //this.labelInput.data("autocomplete")._renderItem = function () {};
    },

    /**
        Reset all the elements in the Autocomplete.
    */
    reset: function () {
        this.labelInput.val("");
        this.valueInput.val("");
    }

});

/**
    Stores selected players for all autocompletes to share so they don't allow
    the user to select the same people.

    TODO: make this a field in the SessionModel.
*/
var selectedPlayers = {};

/**
    A Tag autocomplete component that uses jquery ui.
    @constructor
*/
var TagAutocomplete = Autocomplete.extend({

    thumbnail: null,
    removeTagButton: null,
    players: null,

    // TODO: have this sent from server
    IMG_SRC: "/static/images/thumbnail.jpg",

    /**
        Provide tag autocomplete functionality.
        @param {Object} elem A $ TagAutocompleteInput element.
        @param {Array} players A list of players that can be selected from.
    */
    initialize: function(elem, players){
        Autocomplete.prototype.initialize.call(this, elem);

        this.thumbnail = this.$el.children(Const.CLASS.AUTOCOMPLETE_THUMBNAIL);
        this.removeTagButton = this.$el.find(Const.CLASS.REMOVE_TAG_BUTTON);

        this.players = players;

        // set the remove tag trigger. _bindAll set in prototype.initialize...
        this.removeTagButton.on("touchstart click", this.removeTag);
    },

    /**
        Generate a dictionary of players, but transform them to the standard.
        @return {Object} A dictionary with keys 'label' and 'value'.
    */
    generateSourceData: function () {
        // only autocomplete on unselected players
        var unselectedPlayers = [];
        for (var i = 0; i < this.players.length; i += 1) {
            var player = this.players[i];
            if (!selectedPlayers.hasOwnProperty(player.id)) {
                unselectedPlayers.push(player);
            }
        }

        // remap players to generic label/value autocomplete objects
        // and sort
        var sourceItems = $.map(unselectedPlayers, remapPlayer);
        sourceItems.sort(sortByLabel);
        return sourceItems;

    },

    /**
        In addition to the standrad label/value handling, also generate the proper
        thumbnail and activate the remove tag button, and remove the selected
        player from the autocomplete list.
        @param {Object} evt the event that triggered this function
        @param {Object} ui the jQuery Autocomplete object
        @return false so that jQuery UI Autocomplete can't overwrite the values.
    */
    handleSelect: function (evt, ui) {
        Autocomplete.prototype.handleSelect.call(this, evt, ui);

        var selectedItem = ui.item;
        
        // add selected player to list
        selectedPlayers[selectedItem.value] = selectedItem;

        this.labelInput.prop("disabled", true);
        this.thumbnail.attr("src", selectedItem.thumbnail);
        
        this.removeTagButton.css("visibility", "visible");
        
        // return false so LabelInput isn't overwritten with the value.
        return false;
    },

    /**
        Provide a jQuery Autocomplete menu-item with a thumbnail in it.
    */
    renderItem: function () {
        // FIXME put this item together on the server.
        this.labelInput.data("autocomplete")._renderItem = function (ul, item) {
            return $('<li class="ui-menu-item-with-thumbnail"></li>')
                .data("item.autocomplete", item)
                .append('<a><img src="' + item.thumbnail +
                    '" class="thumbnail" /><span>' + item.label + '</span></a>')
                .appendTo(ul);
        };
    },

    /**
        Reset the standard elements, the thumbnail, and the remove tag button.
        Re-enable the label input.
    */
    reset: function () {
        Autocomplete.prototype.reset.call(this);

        this.labelInput.prop("disabled", false);
        this.removeTagButton.css("visibility", "hidden");
        this.thumbnail.attr("src", this.IMG_SRC);
    },

    /**
        Reset the input and allow the selected player to be selected again.
    */
    removeTag: function () {
        var removedPlayerID = this.valueInput.val();
        this.reset();
        delete selectedPlayers[removedPlayerID];
    },

    /**
        Reset the input and clear the selected players list.
    */
    resetAndClear: function () {
        this.reset();
        selectedPlayers = {};
    }
});

/**
    Remap player object (id->value, name->label, picture->thumbnail).
    @param {Object} r An object keyed "id", "name", and "picture"
    @return {Object} An object keyed "label" and "value".
*/
function remapPlayer(r) {
    return {
        label: r[Const.DATA.NAME],
        value: r[Const.DATA.ID],
        thumbnail: r[Const.DATA.PICTURE]
    };
}

/**
    Used by sort function to sort the objects by their label
    attributes.
    @param {Object} a An object with a "label" field.
    @param {Object} b Another object with a "label" field.
    @return {number} 0 if even, 1 if a>b, and -1 if b>a.
*/
function sortByLabel(a, b) {
    var returnVal = 0;
    var aVal = a.label;
    var bVal = b.label;
    if (aVal > bVal) {
        returnVal = 1;
    } else if (aVal < bVal) {
        returnVal = -1;
    }
    return returnVal;
}


return {
    TagAutocomplete: function (autocomplete_element, players) {
        //check to make sure this element is the correct class
        if (autocomplete_element.hasClass(
                DOMUtil.getClassFromSelector(
                        Const.CLASS.AUTOCOMPLETE_PLAYERS))) {
            return new TagAutocomplete(autocomplete_element, players);
        } else {
            return null;
        }
    }
};


});
