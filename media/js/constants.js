/**
    All client side constants.

    w3c constant values should contain dashes to comply with
    html5 standards. E.g., "class-name".
    
    @exports Const
*/
define(
        [],
        function () {


var constants = {

    /**
        Enum for API object types.
        @enum {string}
    */
    API_OBJECT: {
        GAME:                   "game",
        PLAYER:                 "player"
    },

    /**
        Enum for DOM object selectors.
        @enum {string}
    */
    DOM: {
        BODY:                   "body",
        BUTTON:                 "button",
        NAV:                    "nav"
    },

    /**
        Enum for ID selectors. (Prefixed with '#')
        @enum {string}
    */
    // TODO: make this link sync with Python HTML_ID constants
    ID: {
        TAB:                    "#tab",
        TAB_HEADER:             "#tab-header",
        CONTENT:                "#content",
        PROPERTIES:             "#properties",
        SUMMARY:                "#summary",
        FEED:                   "#feed",
        DIALOG_CONTAINER:       "#dialog-container",
        SCROLLER:               "#iscroll-wrapper"
    },

    /**
        Enum for Class selectors. (Prefixed with '.')
        @enum {string}
    */
    // TODO: make this link sync with Python HTML_CLASS constants
    CLASS: {
        JS_LINK:                ".js-link",
        EXTERNAL_LINK:          ".external-link",
        CLOSE_BUTTON:           ".close-button",
        ACTIVE_NAV:             ".active-nav",
        INACTIVE_NAV:           ".inactive-nav",
        AUTOCOMPLETE_PLAYERS:   ".autocomplete-players",
        AUTOCOMPLETE_LABEL:     ".autocomplete-label",
        AUTOCOMPLETE_VALUE:     ".autocomplete-value",
        LIST_WITH_HEADERS:      ".list-with-headers",
        FACEBOOK_LOGIN_BUTTON:  ".facebook-login-button"
    },

    /**
        Enum for data-* attributes, JSON keys, or as form name attribute
        values.
        @enum {string}
        @const
    */
    // TODO: make this link sync with Python HTML_DATA constants
    DATA: {
        ID:                     "id",
        PERSON_ID:              "person-id",
        SCORE:                  "score",
        RESULT:                 "result",
        PLAYER:                 "player",
        NAME:                   "name",
        RIVALS:                 "rivals",
        PAGE_TYPE:              "page-type",
        PAGE_NAME:              "page-name",
        GAME_SCORE:             "game-score"
    },
            
    /** Enum for model ids.
        @enum {string}
    */
    MODEL_ID: {
        SESSION:                "#model-session",
        CONTEXT:                "#model-context",
        PAGE_STATE:             "#model-page-state"
    },

    /**
        Enum for values of name attributes. (Wrapped in attribute selectors.)
        @enum {string}
    */
    // TODO: make this link sync with Python HTML_NAME constants
    NAME: {
        LEAGUE:                 "[name='league']",
        CREATE_GAME:            "[name='create-game']",
        GAME_SCORE_ID:          "[name^='game-score'][name$='[id]']",
        GAME_SCORE_SCORE:       "[name^='game-score'][name$='[score]']"
    },

    /**
        Enum for page types.
        @enum {string}
    */
    PAGE_TYPE: {
        TAB:                    "tab",
        DIALOG:                 "dialog",
        LANDING:                "landing"
    },

    /**
        Enum for page names.
        @enum {string}
    */
    PAGE_NAME: {
        RANKINGS:               "rankings",
        GAMES:                  "games",
        LANDING:                "landing",
        CREATE_GAME:            "create-game"
    }
};

return constants;


});
