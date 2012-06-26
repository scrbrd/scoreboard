/**
    A set of widgets for adding autocomplete functionality.

    AutocompleteUtil is a wrapper around the autocomplete widget for jquery-ui.

    @exports AutocompleteUtil

    @requires $
    @requires Const
*/
define(
        [
            "jQuery",
            "js/constants",
        ],
        function($, Const) {

    /**
        Provide generic autocomplete functionality.

        @param {Object} elem A $ AutocompleteInput element. 
        @param {Object} selectData A list of objects with keys label, value.
    */
    function autocomplete(elem, selectData) {
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
        
        selectData.sort(sortByLabel);

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

    return {
        autocomplete: autocomplete,
        autocompletePlayers: autocompletePlayers,
    };
});

