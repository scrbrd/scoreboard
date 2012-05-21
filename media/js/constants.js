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
        },

        /**
            Enum for ID selectors. (Prefixed with '#')
            @enum {string} 
            @const
        */
        // TODO: make this link sink with Python HTML_ID constants
        ID: {
            /** @const */ PAGE:                 "#page",
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
            /** @const */ DIALOG_LINK:          ".dialog-link",
            /** @const */ CLOSE:                ".close",
            /** @const */ PLAYER_SELECT:        ".player-select",
        },

        /**
            Enum for data-* attributes, JSON keys, or as form name attribute 
            values.
            @enum {string}
            @const
        */
        // TODO: make this link sink with Python HTML_DATA constants
        DATA: {
            /** @const */ ID:                     "id",
            /** @const */ NAME:                   "name",
            /** @const */ RIVALS:                 "rivals",
            /** @const */ PAGE_NAME:              "page-name",
            /** @const */ GAME_SCORE:             "game-score",
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
            /** @const */ DISPLAYED_DIALOG:       "displayed-dialog",
        },
    };

    return constants;
});

