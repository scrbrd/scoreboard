/* 
    Module: Constants
    Hold all multi-module constants used by html, css, and js.
    
    Types:     
        DOM - DOM Selectors
        ID - ID Selectors
        CLASS - Class Selectors
        DATA - Data Values (JSON, data-*)
        NAME - Name Values

    Note:
        All constant values should contain dashes to comply
        with html5 standards. E.g., "class-name".
*/
define(
    [],
    function() {

        return {

            // Type: DOM
            // All DOM Constants correspond to DOM tags.
            DOM: {
                BODY:                   "body",
                BUTTON:                 "button",
            },


            // Type: ID
            // All ID Constants are prefixed with "#" for selection.
            // TODO: make this link sink with Python HTML_ID constants
            ID: {
                PAGE:                   "#page",
                CONTEXT:                "#context",
                CONTENT:                "#content",
                DIALOG_CONTAINER:       "#dialog-container",
                SCROLLER:               "#iscroll_wrapper",
            },


            // Type: CLASS
            // All Class Constants are prefixed with "." for selection.
            // TODO: make this link sink with Python HTML_CLASS constants
            CLASS: {
                DIALOG_LINK:            ".dialog-link",
                CLOSE:                  ".close",
                PLAYER_SELECT:          ".player-select",
            },


            // Type: DATA
            // These constants should be used with "data-*" attributes,
            // as JSON keys, or as form name attribute values.
            // TODO: make this link sink with Python HTML_DATA constants
            DATA: {
                ID:                     "id",
                NAME:                   "name",
                RIVALS:                 "rivals",
            },
                  

            // Type: NAME
            // These constants are used as possible values for form tag names.
            // They are all of the format "[name='CONST']".
            // TODO: make this link sink with Python HTML_NAME constants
            NAME: {
                LEAGUE:                 "[name='league']",
                CREATE_GAME:            "[name='create-game']",
            },
        }
    }
);

