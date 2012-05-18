/* 
    Module: Crud
    Handle all Create, Read, Update, Delete actions on specific model objects.
    
    Dependencies:
        $ 
        constants
*/
define(
    [
        "jQuery",
        "js/constants",
    ],
    function ($, Const) {

        /*
            Constants: Request Keys
            XSRF - Used to indicate XSRF token
            ASYNCH - Used to indicate asynchronous request
            PARAMS - Used to indicate object parameters
        */
        var REQUEST_KEY = {
            XSRF:           "_xsrf",
            ASYNCH:         "asynch",
            PARAMS:         "parameters",
        };

        /*
            Constants: Response Keys
            IS_SUCCESS - Indicate request sucess

            Note: The values have underscores to match the python conventions.
        */
        var RESPONSE_KEY = {
            IS_SUCCESS:     "is_success",
        };
        
        // Constant: CREATE_URL
        // URL of create handlers.
        var CREATE_URL = "/create/";

        // Constant: POST_JSON
        // Signify posting type JSON.
        var POST_JSON = "json";

        /* 
            Function: create
            Create a new object.
        
            Parameters:
                type - the object type to create
                parameters - the parameters that define this object
                controller - the controller that initiated this create request
        */
        function create(type, objParams, controller) {

            // move xsrf token to request parameters
            var xsrfToken = objParams[REQUEST_KEY.XSRF];
            delete objParams[REQUEST_KEY.XSRF];

            // grab keys that will be used for success function
            var numberOfTags = 0;
            if (Const.DATA.GAME_SCORE in objParams) {
                numberOfTags = objParams[Const.DATA.GAME_SCORE].length;
            }

            var escapedParams = JSON.stringify(objParams);
            var requestData = {};
            requestData[REQUEST_KEY.ASYNCH] = true; 
            requestData[REQUEST_KEY.XSRF] = xsrfToken;
            requestData[REQUEST_KEY.PARAMS] = escapedParams;
            
            $.post(
                    CREATE_URL + type, 
                    requestData, 
                    function (jsonResponse) {
                        success = jsonResponse[RESPONSE_KEY.IS_SUCCESS];
                        // TODO: send response object to grab relevent MP data
                        // from
                        if (success) {
                            controller.handleSuccess(numberOfTags);
                        } else {
                            //TODO: alert user on fail
                            console.log('failed to create game');
                        }
                    },
                    POST_JSON);
        };

        return {
            /* 
                Function: createGame
                Create a new Game.
            
                Parameters:
                    parameters - the parameters that define this object
            */
            createGame: function (gameParams, controller) {
                // TODO: make the objParams more specific
                create(Const.API_OBJECT.GAME, gameParams, controller);
            },
        };
    }
);

