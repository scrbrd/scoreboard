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
            Function: remapRival
            Remap rival object ("id" --> "value", "name" --> "label").

            Parameters:
                r - (object) Each object is handed over by map function.
        */
        function remapRival(r) {
            return {
                label: r[Const.DATA.NAME], 
                value: r[Const.DATA.ID],
            };
        }


        /*
            Function: sortByLabel
            Used by sort function to sort the objects by their label
            attributes.

            Parameters:
                a
                b
        */
        function sortByLabel(a, b) {
            aVal = a.label;
            bVal = b.label;
            if (aVal > bVal) { 
                return 1; 
            } else if (aVal < bVal) { 
                return -1; 
            } else { 
                return 0; 
            }
        }

        return {
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
    }
);

