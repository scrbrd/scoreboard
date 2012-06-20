define(
        [], 
        /**
            A module for containing all js, css, and html constants.
            
            Note: All constant values should contain dashes to comply with
            html5 standards. E.g., "class-name".
            
            @exports Const
        */
        function () {
    
    var constants = /** @lends module:Const */ { 

        /**
            Enum for API object types.
            @enum {string} 
            @const
        */
        API_OBJECT: {
            /** @const */ GAME:                 "game",
        },

        /**
            Enum for DOM object selectors.
            @enum {string} 
            @const
        */
        DOM: {
            /** @const */ BODY:                 "body",
            /** @const */ BUTTON:               "button",
            /** @const */ NAV:                  "nav",
        },

        /**
            Enum for ID selectors. (Prefixed with '#')
            @enum {string} 
            @const
        */
        // TODO: make this link sink with Python HTML_ID constants
        ID: {
            /** @const */ TAB:                  "#tab",
            /** @const */ CONTEXT:              "#context",
            /** @const */ CONTENT:              "#content",
            /** @const */ DIALOG_CONTAINER:     "#dialog-container",
            /** @const */ SCROLLER:             "#iscroll-wrapper",
        },


        /**
            Enum for Class selectors. (Prefixed with '.')
            @enum {string}
            @const
        */
        // TODO: make this link sink with Python HTML_CLASS constants
        CLASS: {
            /** @const */ JS_LINK:              ".js-link",
            /** @const */ CLOSE_BUTTON:         ".close-button",
            /** @const */ ACTIVE_NAV:           ".active-nav",
            /** @const */ INACTIVE_NAV:         ".inactive-nav",
            /** @const */ AUTOCOMPLETE_PLAYERS: ".autocomplete-players",
            /** @const */ AUTOCOMPLETE_LABEL:   ".autocomplete-label",
            /** @const */ AUTOCOMPLETE_VALUE:   ".autocomplete-value",
            /** @const */ LIST_WITH_HEADERS:    ".list-with-headers",
        },

        /**
            Enum for data-* attributes, JSON keys, or as form name attribute 
            values.
            @enum {string}
            @const
        */
        // TODO: make this link sink with Python HTML_DATA constants
        DATA: {
            /** @const */ ID:                   "id",
            /** @const */ SCORE:                "score",
            /** @const */ NAME:                 "name",
            /** @const */ RIVALS:               "rivals",
            /** @const */ PAGE_NAME:            "page-name",
            /** @const */ GAME_SCORE:           "game-score",
        },
                
        /**
            Enum for values of name attributes. (Wrapped in [name=VALUE].)
            values.
            @enum {string}
            @const
        */
        // TODO: make this link sink with Python HTML_NAME constants
        NAME: {
            /** @const */ LEAGUE:                 "[name='league']",
            /** @const */ CREATE_GAME:            "[name='create-game']",
        },

        /**
            Enum for page names. 
            @enum {string}
            @const
        */
        PAGE_NAME: {
            /** @const */ RANKINGS:               "rankings",
            /** @const */ GAMES:                  "games",
            /** @const */ LANDING:                "landing",
            /** @const */ CREATE_GAME:            "create-game",
        },

        /**
            Enum for triggerable events. 
            @enum {string}
            @const
        */
        EVENT: {
            /** @const */ DISPLAY_DIALOG:           "display-dialog",
        },
    };

    return constants;
});

