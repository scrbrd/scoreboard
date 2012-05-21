define(
        [
            "jQuery",
            "js/constants",
        ],
        /** 
            Handle all Create, Read, Update, Delete actions on specific model objects.
           
            @exports Crud

            @requires $
            @requires Const
        */
        function ($, Const) {

    /**
        Constants for sending server requests.
        @private 
        @enum {string}
        @const
    */
    var REQUEST_KEY = {
        /** Used to indicate XSRF token */
        XSRF:           "_xsrf",
        /** Used to indicate asynchronous request */
        ASYNCH:         "asynch",
        /** Used to indicate object parameters */
        PARAMS:         "parameters",
    };

    /**
        Constants for reading responses from server. <br />
        Note: The values have underscores to match the python conventions.
        @private 
        @enum {string}
        @const
    */
    var RESPONSE_KEY = {
        /** Indicate request sucess */
        IS_SUCCESS:     "is_success",
    };
    
    /**
        URL of create handler.
        @private 
        @type {string}
        @const
    */
    var CREATE_URL = "/create/";

    /**
        JSON posting string.
        @private
        @type {string}
        @const
    */
    var POST_JSON = "json";

    /** 
        Create a new object.
        @private
        @param {string} type The object type to create.
        @param {Object} objParams The parameters that define this object.
        @param {Object} controller The controller that initiated this 
            create request.
    */
    function create(type, objParams, controller) {

        // move xsrf token to request parameters
        var xsrfToken = objParams[REQUEST_KEY.XSRF];
        delete objParams[REQUEST_KEY.XSRF];

        // grab keys that will be used for success function
        var numberOfTags = 0;
        if (objParams.hasOwnProperty(Const.DATA.GAME_SCORE)) {
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
    }

    return /** @lends module:Crud */{
        /**
            Create a new Game.
            @param {Object} gameParams The parameters that define this game.
            @param {Object} controller The controller that initiated this
                create game request.
        */
        createGame: function (gameParams, controller) {
            // TODO: make the gameParams more specific
            create(Const.API_OBJECT.GAME, gameParams, controller);
        },
    };
});

