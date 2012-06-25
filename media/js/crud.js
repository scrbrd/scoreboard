define(
        [
            "jQuery",
            "js/constants",
            "js/event",
            "js/eventDispatcher",
        ],
        /** 
            Handle all Create, Read, Update, Delete actions on specific model objects.
           
            @exports Crud

            @requires $
            @requires Const
            @requires Event
            @requires EventDispatcher
        */
        function ($, Const, Event, EventDispatcher) {

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
    var JSON_RESPONSE = "json";

    /** 
        Create a new object.
        @private
        @param {string} type The object type to create.
        @param {Object} objParams The parameters that define this object.
    */
    function create(type, objParams) {

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
                        EventDispatcher.trigger(
                                Event.SERVER.CREATED_GAME,
                                numberOfTags);
                    } else {
                        //TODO: alert user on fail
                        console.log('failed to create game');
                    }
                },
                JSON_RESPONSE);
    }

    function read(url, successFunction) {
        var requestData = {};
        requestData[REQUEST_KEY.ASYNCH] = true; 

        var start = new Date().getTime(); 
        $.get(
                url,
                requestData,
                function (jsonResponse) {
                    var end = new Date().getTime();
                    var time = end - start;
                    console.log("request took " + time + "ms");
                    successFunction(jsonResponse); 
                },
                JSON_RESPONSE);
    }


    function updatePageState(jsonResponse, model) {
        // FIXME have this PageState update viewer context (rivals) too
        var contextID = $(jsonResponse.context_model)
            .data(Const.DATA.ID);
        var pageType= $(jsonResponse.page_state_model)
            .data(Const.DATA.PAGE_TYPE);
        var pageName = $(jsonResponse.page_state_model)
            .data(Const.DATA.PAGE_NAME);
        
        model.setContent(jsonResponse.content);
        model.setContext(jsonResponse.context);
        model.setContextID(contextID);
        model.setPageType(pageType);
        model.setPageName(pageName);
    }

    return /** @lends module:Crud */{
        /**
            Create a new Game.
            @param {Object} gameParams The parameters that define this game.
        */
        createGame: function (gameParams) {
            // TODO: make the gameParams more specific
            create(Const.API_OBJECT.GAME, gameParams);
        },

        fetchTab: function (url, model) {
            read(url, function (response) {
                updatePageState(response, model);
                EventDispatcher.trigger(
                        Event.SERVER.VIEWED_PAGE,
                        model,
                        url);
            });
        },
    };
});

