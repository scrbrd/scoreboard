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
        COMMENT:                "comment",
        PLAYER:                 "player"
    },

    /**
        Enum for DOM object selectors.
        @enum {string}
    */
    DOM: {
        BODY:                   "body",
        NAV:                    "nav"
    },

    /**
        Enum for ID selectors. (Prefixed with '#')
        @enum {string}
    */
    // TODO: make this link sync with Python HTML_ID constants
    ID: {
        TAB:                        "#tab",
        TAB_HEADER:                 "#tab-header",
        CONTENT:                    "#content",
        PROPERTIES:                 "#properties",
        SUMMARY:                    "#summary",
        FEED:                       "#feed",
        TAB_OUTER_CONTENT_CONTAINER: "#tab-outer-content-container",
        DIALOG_OUTER_CONTENT_CONTAINER: "#dialog-outer-content-container",
        CREATE_GAME:                "#create-game"
    },

    /**
        Enum for Class selectors. (Prefixed with '.')
        @enum {string}
    */
    // TODO: make this link sync with Python HTML_CLASS constants
    CLASS: {
        NON_ROUTING_ANCHOR:     ".non-routing-anchor",
        ANCHOR:                 ".anchor",
        BUTTON:                 ".button",
        CLOSE_BUTTON:           ".close-button",
        CREATE_BUTTON:          ".create-button",
        MENU_BUTTON:            ".menu-button",
        REMOVE_TAG_BUTTON:      ".remove-tag-button",
        ACTIVE_NAV:             ".active-nav",
        INACTIVE_NAV:           ".inactive-nav",
        AUTOCOMPLETE:           ".autocomplete",
        AUTOCOMPLETE_TAG:       ".autocomplete-tag",
        AUTOCOMPLETE_PLAYER:    ".autocomplete-player",
        AUTOCOMPLETE_SPORT:     ".autocomplete-sport",
        AUTOCOMPLETE_LABEL:     ".autocomplete-label",
        AUTOCOMPLETE_THUMBNAIL: ".autocomplete-thumbnail",
        AUTOCOMPLETE_VALUE:     ".autocomplete-value",
        SWITCH_CONTROL:         ".switch-control",
        SWITCH_ON:              ".switch-on",
        SWITCH_KNOB:            ".switch-knob",
        SWITCH_CHECKBOX:        ".switch-checkbox",
        LIST_WITH_HEADERS:      ".list-with-headers",
        FACEBOOK_LOGIN_ANCHOR:  ".facebook-login-anchor",
        OPPONENT_TAGS_GROUP:    ".opponent-tags-group",
        COMMENT_FORM:           ".comment-form"
    },

    /**
        Enum for data-* attributes, JSON keys, or as form name attribute
        values.
        @enum {string}
        @const
    */
    // TODO: make this sync with Python SQ_DATA constants.
    DATA: {
        ID:                     "id",
        PERSON_ID:              "person-id",
        NAME:                   "name",
        LEAGUE_ID:              "league-id",
        GAME_TYPE:              "game-type",
        SCORE:                  "score",
        RESULT:                 "result",
        METRICS_BY_OPPONENT:    "metrics-by-opponent",
        PICTURE:                "picture",
        RIVALS:                 "rivals",
        SPORTS:                 "sports",
        PLAYER:                 "player",
        PAGE_TYPE:              "page-type",
        PAGE_NAME:              "page-name"
    },

    /**
        Enum for data-* values or JSON values corresponding to Data.
        @enum {string}
        @const
    */
    // TODO: make this sync with Python SQ_DATA constants.
    // TODO FIXME XXX: REMOVE W/L/P OR FIGURE OUT THE RIGHT WAY TO DO THIS!
    VALUE: {
        RIVALRY:                "rivalry",
        CAMARADERIE:            "camaraderie",
        WON:                    "won",
        LOST:                   "lost",
        PLAYED:                 "played"
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
    // TODO: make this sync with Python HTML_NAME constants
    NAME: {
        LEAGUE_ID:      "[name='league-id']",
        CREATE_GAME:    "[name='create-game']",
        // FIXME: this probably doesn't work anymore.
        OPPONENT_ID:    "[name^='metrics-by-opponent'][name$='[id]']",
        RESULT:         "[name^='metrics-by-opponent'][name$='[result]']"
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
