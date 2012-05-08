/* 
    Module: Dom
    Reusable Functions for manipulating the DOM.
    
    Package:
        util

    Dependencies:
        $ 
        Const

*/
define(
    [
        "jQuery",
        "js/constants",
    ],
    function($, Const) {
       
        /*
            Class: Autocomplete
            A collection of static autocomplete functions.
        */
        var Autocomplete = {

            /*
                Function: autocompletePlayer
                Set the player input boxes to autocomplete.

                Parameters:
                    rivals - (list) List of objects representing rivals
                            with the keys "id", "name".
                    form - (string) Identifier of which form to act on.
                    input_class - (string) Class of input fields to act on.
            */
            autocompletePlayer: function(rivals, form, input_class) {
                // remap rivals and sort by name/label
                select_data = $.map(rivals, this._remapRival);
                select_data.sort(this._sortByLabel);
                
                player_selection = form + ' ' + input_class;
                $(player_selection).autocomplete({
                    autoFocus: true, // autofocus on first value
                    delay: 0, // immediately
                    source: select_data, // autocomplete on this data
                });
                // TODO: add other fields, css, grab select and focus
            },


            /*
                Function: _remapRival
                Remap rival object ("id" --> "value", "name" --> "label").

                PRIVATE

                Parameters:
                    r - (object) Each object is handed over by map function.
            */
            _remapRival: function(r) {
                return {
                    label: r[Const.DATA.NAME], 
                    value: r[Const.DATA.ID],
                }
            },


            /*
                Function: _sortByLabel
                Used by sort function to sort the objects by their label
                attributes.

                PRIVATE

                Parameters:
                    a
                    b
            */
            _sortByLabel: function(a, b) {
                a_val = a.label;
                b_val = b.label;
                if (a_val > b_val) { return 1; }
                else if (a_val < b_val) { return -1; }
                else { return 0; }
            },
        }

        return {
            Autocomplete: Autocomplete,
        }
    }
);

