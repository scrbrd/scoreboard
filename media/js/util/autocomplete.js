/**
    @namespace
    @name util
*/
define(
        [
            "jQuery",
            "js/constants",
        ],
        /**
            A set of widgets foradding autocomplete functionality.

            @exports Autocomplete

            @requires $
            @requires Const
        */
        function($, Const) {

        
    /**
        Provide generic autocomplete functionality.

        @param {Object} elem A $ AutocompleteInput element. 
        @param {Object} selectData A list of objects with keys label, value.
    */
    function autocomplete(elem, selectData) {
        // sort select data by label
        selectData.sort(sortByLabel);
        
        var labelInput = $(elem).children(Const.CLASS.AUTOCOMPLETE_LABEL);
        var valueInput = $(elem).children(Const.CLASS.AUTOCOMPLETE_VALUE);
        
        // clear label and value on focus
        labelInput.focus(function (event) {
            labelInput.val("");
            valueInput.val("");
        });

        // clear label if blur but no selection through autocomplete
        labelInput.blur(function (event) {
            if (valueInput.val() === "") {
                labelInput.val("");
            }
        });

        labelInput.autocomplete({
            autoFocus: true, // autofocus on first value
            delay: 0, // immediately
            source: selectData, // autocomplete on this data
            minLength: 1, // start autocomplete on third character
            appendTo: elem, // append dropdown to input element
            // pushes selection to hidden helper element and shows label
            select: function (event, ui) {
                var selectedPlayer = ui.item;
                labelInput.val(selectedPlayer.label);
                valueInput.val(selectedPlayer.value);

                // unfocus after selection
                labelInput.blur();
                return false;
            },
            // makes changes to display box when opened
            open: function (event, ui) {
                var a = $(elem).children(".ui-autocomplete").css("width", "");
                return false;
            },
        });
    }

        
    /**
        Provide autcomplete functionality for a Player input.
        
        @param {Object} elem A $ AutocompleteInput element. 
        @param {Object} players A list of objects with keys id, name.
    */
    function autocompletePlayers(elem, players) {
        // remap players to generic label/value autocomplete objects
        var selectData = $.map(players, remapPlayer);
        autocomplete(elem, selectData);
    }
        
            
    /**
        Remap player object ("id" --> "value", "name" --> "label").
        @private
        @param {Object} r An object keyed "id" and "name"
        @return {Object} An object keyed "label" and "value".
    */
    function remapPlayer(r) {
        return {
            label: r[Const.DATA.NAME], 
            value: r[Const.DATA.ID],
        };
    }


    /**
        Used by sort function to sort the objects by their label
        attributes.
        @private
        @param {Object} a An object with a "label" field.
        @param {Object} b Another object with a "label" field.
        @return {number} 0 if even, 1 if a>b, and -1 if b>a. 
    */
    function sortByLabel(a, b) {
        var returnVal = 0;
        aVal = a.label;
        bVal = b.label;
        if (aVal > bVal) { 
            returnVal = 1; 
        } else if (aVal < bVal) { 
            returnVal = -1; 
        } 
        return returnVal;
    }

    return /** @lends module:util.Dom */ {
        autocomplete: autocomplete,
        autocompletePlayers: autocompletePlayers,
    };
});

