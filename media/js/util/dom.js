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
            Reusable Functions for manipulating the DOM.

            @exports Dom

            @requires $
            @requires Const
        */
        function($, Const) {
       
    /**
        Remap rival object ("id" --> "value", "name" --> "label").
        @private
        @param {Object} r An object keyed "id" and "name"
        @return {Object} An object keyed "label" and "value".
    */
    function remapRival(r) {
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
        /*
            Function: autocompletePlayer
            Set the player input boxes to autocomplete.

            Parameters:
                rivals - (list) List of objects representing rivals
                        with the keys "id", "name".
                form - (string) Identifier of which form to act on.
                inputClass - (string) Class of input fields to act on.
        */
        autocompletePlayer: function(rivals, form, inputClass) {
            // remap rivals and sort by name/label
            selectData = $.map(rivals, remapRival);
            selectData.sort(sortByLabel);
            
            playerSelection = form + ' ' + inputClass;
            $(playerSelection).autocomplete({
                autoFocus: true, // autofocus on first value
                delay: 0, // immediately
                source: selectData, // autocomplete on this data
            });
            // TODO: add other fields, css, grab select and focus
        },
    };
});

