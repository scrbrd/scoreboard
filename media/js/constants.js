/* Filename: constants.js
 *
 * Hold all multi-module constants
 *
 * All html/css/js constant values should contain dashes.
 *
 */

define(
    [],
    function() {

        return {
            // Dom selectors used by css, js, and jQuery.
            DOM: {
                BODY:                   "body",
                BUTTON:                 "button",
            },

            // Id selectors used by css, js, and jQuery.
            ID: {
                PAGE:                   "#page",
                CONTEXT:                "#context",
                CONTENT:                "#content",
                DIALOG_CONTAINER:       "#dialog-container",
                SCROLLER:               "#iscroll_wrapper",
            },

            // Class selectors used by css, js, and jQuery.
            CLASS: {
                DIALOG_LINK:            ".dialog-link",
                CLOSE:                  ".close",
            },

            // Allowed data-* attribute values.
            DATA: {
                ID:                     "id",
            },
                  
            // Allowed name attribute values. 
            NAME: {
                LEAGUE:                 "[name='league']",
                CREATE_GAME:            "[name='create-game']",
            },
            
            // FIXME XXX - coordinate constants with python, copy system, better
            // js commenting.
            // WARMAN - grab current player id from warman to put in creator
            // input. 
            // mixpanel, autocomplete
        }
    }
);

