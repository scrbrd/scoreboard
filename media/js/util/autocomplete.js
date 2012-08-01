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
            "js/constants"
        ],
        function ($, Const) {


/**
    Provide generic autocomplete functionality.
    @param {Object} elem A $ AutocompleteInput element.
    @param {Object} selectData A list of objects with keys label, value.
    @param {Function} renderFunction A function to render a special autocomplete
                                    list.
    @param {Function} selectFunction A callback function for select.
    @param {Function} removeFunction A callback function for removing a value.
*/
function autocomplete(
        elem,
        selectSource,
        renderFunction,
        selectFunction,
        removeFunction) {
    var labelInput = $(elem).children(Const.CLASS.AUTOCOMPLETE_LABEL);
    var valueInput = $(elem).children(Const.CLASS.AUTOCOMPLETE_VALUE);
    
    // reset inputs on focus, call removeFunction, and set new autocomplete
    labelInput.focus(function (event) {
        labelInput.val("");
        removeFunction(valueInput.val());
        valueInput.val("");

        // Get the freshest available data
        var selectData = selectSource();

        labelInput.autocomplete({
            autoFocus: true, // autofocus on first value
            delay: 0, // immediately
            source: selectData, // autocomplete on this data
            minLength: 1, // start autocomplete on third character
            appendTo: elem, // append dropdown to input element
            // pushes selection to hidden helper element and shows label
            select: function (event, ui) {
                var selectedItem = ui.item;
                labelInput.val(selectedItem.label);
                valueInput.val(selectedItem.value);
                valueInput.change();
                
                if (selectFunction !== null) {
                    selectFunction(selectedItem, true);
                }

                // unfocus after selection
                labelInput.blur();
                return false;
            },
            // makes changes to display box when opened
            open: function (event, ui) {
                var a = $(elem).children(".ui-autocomplete").css("width", "");
                return false;
            }
        });

        if (renderFunction !== null) {
            labelInput.data("autocomplete")._renderItem = renderFunction;
        }
    });

    // clear label if blur but no selection through autocomplete
    labelInput.blur(function (event) {
        if (valueInput.val() === "") {
            labelInput.val("");
        }
    });
    
}

    
/**
    Provide autcomplete functionality for a Player input.
    @param {Object} elem A $ AutocompleteInput element.
    @param {Array} players A list of objects with keys id, name.
    @param {Object} selectedPlayers A list for storing selected players.
*/
function autocompletePlayers(elem, players, selectedPlayers) {
    autocomplete(
            elem,
            // generate source (players) for autocomplete
            function () {
                // only autocomplete on unselected players
                var unselectedPlayers = [];
                for (var i = 0; i < players.length; i += 1) {
                    var player = players[i];
                    if (!selectedPlayers.hasOwnProperty(player.id)) {
                        unselectedPlayers.push(player);
                    }
                }

                // remap players to generic label/value autocomplete objects
                // and sort
                var selectData = $.map(unselectedPlayers, remapPlayer);
                selectData.sort(sortByLabel);
                return selectData;
            },
            // render an autocomplete item
            function (ul, item) {
                // FIXME put this item together on the server.
                return $('<li class="ui-menu-item-with-thumbnail"></li>')
                    .data("item.autocomplete", item)
                    .append('<a><img src="' + item.thumbnail +
                        '" class="thumbnail"></span>' + item.label + '</a>')
                    .appendTo(ul);

            },
            // handle success of selecting a player
            function (selectedPlayer) {
                // add selected player and set thumbnail
                selectedPlayers[selectedPlayer.value] = selectedPlayer;
                $(elem).children(Const.CLASS.AUTOCOMPLETE_THUMBNAIL)
                    .attr("src", selectedPlayer.thumbnail);
            },
            // handle a player being removed from an autoselect
            function (removedPlayerID) {
                // remove player and thumbnail
                delete selectedPlayers[removedPlayerID];
                $(elem).children(Const.CLASS.AUTOCOMPLETE_THUMBNAIL)
                    .attr("src", "/static/images/thumbnail.jpg");
            });
}
    
        
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
    autocomplete: autocomplete,
    autocompletePlayers: autocompletePlayers
};


});
