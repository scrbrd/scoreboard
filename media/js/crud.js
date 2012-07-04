/**
    Handle ALL server requests and CRUD actions on specific model objects.

    This module takes over a good amount of the model fetching as well. All
    server communications should go through this module, and it is aware
    of the models it interacts with so it can process them. After
    processing the response the CRUD helper methods fire events.

    Only expose specific CRUD actions as opposed to the generic ones.
    
    TODO: If we develop our models more and create better urls for them to
    push/pull to/from then we might be able to get rid of this class.
    
    @exports Crud

    @requires $
    @requires Const
    @requires Event
    @requires EventDispatcher
*/
define(
        [
            "jQuery",
            "js/constants",
            "js/event",
            "js/eventDispatcher"
        ],
        function ($, Const, Event, EventDispatcher) {


var CREATE_URL = "/create/";
var JSON_RESPONSE = "json";

/**
    Constants for server requests parameters.
    @enum {string}
*/
var REQUEST_KEY = {
    XSRF:           "_xsrf",
    ASYNCHRONOUS:   "asynchronous",
    PARAMS:         "parameters"
};

/**
    Constants for reading responses from server.
    Note: The values have underscores to match the python conventions.
    @enum {string}
*/
var RESPONSE_KEY = {
    IS_SUCCESS:         "is_success",
    CONTENT:            "content",
    CONTEXT:            "context",
    CONTEXT_MODEL:      "context_model",
    PAGE_STATE_MODEL:   "page_state_model"
};

/**
    Create a new object on the server.
    @param {string} type The object type to create.
    @param {Object} objParams The parameters that define this object.
    @param {Function} successFunction The function to run on success.
*/
function create(type, objParams, successFunction) {
    var escapedParams = JSON.stringify(objParams);
    var requestData = {};
    var xsrfToken;

    // move xsrf token to request parameters
    xsrfToken = objParams[REQUEST_KEY.XSRF];
    delete objParams[REQUEST_KEY.XSRF];

    requestData[REQUEST_KEY.ASYNCHRONOUS] = true;
    requestData[REQUEST_KEY.XSRF] = xsrfToken;
    requestData[REQUEST_KEY.PARAMS] = escapedParams;

    var start = new Date().getTime();
    $.post(
            CREATE_URL + type,
            requestData,
            function (jsonResponse) {
                var end = new Date().getTime();
                var time = end - start;
                console.log("request took " + time + "ms");
                var success = jsonResponse[RESPONSE_KEY.IS_SUCCESS];
                if (success) {
                    successFunction(jsonResponse);
                } else {
                    //TODO: alert user on fail
                    console.log('failed to create ' + type + '.');
                }
            },
            JSON_RESPONSE);
}

/**
    Read a url from the server.
    @param {string} url The url to fetch.
    @param {Function} successFunction The function to run on success.
*/
function read(url, successFunction) {
    var requestData = {};
    requestData[REQUEST_KEY.ASYNCHRONOUS] = true;

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

/**
    Create a new Game on the server.
    @param {Object} gameParams The parameters that define this game.
    @param {Function} successFunction the function to run upon success.
*/
function createGame(gameParams, successFunction) {
    // TODO: make the gameParams more specific
    create(Const.API_OBJECT.GAME, gameParams, successFunction);
}

/**
    Read a tab from the server, update the model, and fire view event.
    @param {string} tabURL The request URL.
    @param {Obejct} tabModel The pageStateModel for the tab.
*/
function readTab(tabURL, tabModel) {
    read(tabURL, function (response) {
        updatePageState(response, tabModel);
        EventDispatcher.trigger(
                Event.SERVER.VIEWED_PAGE,
                tabModel.pageType(),
                tabModel.pageName(),
                tabURL);
    });
}

/**
    Update the PageState after a server response.
    @param {json} jsonResponse The JSON response from the server.
    @param {Object} pageStateModel The previous PageState to update.
*/
function updatePageState(jsonResponse, pageStateModel) {
    // FIXME have this PageState update viewer context (rivals) too
    var contextID = $(jsonResponse[RESPONSE_KEY.CONTEXT_MODEL])
        .data(Const.DATA.ID);
    var pageType= $(jsonResponse[RESPONSE_KEY.PAGE_STATE_MODEL])
        .data(Const.DATA.PAGE_TYPE);
    var pageName = $(jsonResponse[RESPONSE_KEY.PAGE_STATE_MODEL])
        .data(Const.DATA.PAGE_NAME);
    var context = jsonResponse[RESPONSE_KEY.CONTEXT];
    var content = jsonResponse[RESPONSE_KEY.CONTENT];
    
    pageStateModel.setContextID(contextID);
    pageStateModel.setPageType(pageType);
    pageStateModel.setPageName(pageName);
    pageStateModel.setContext(context);
    pageStateModel.setContent(content);
}

return {
    createGame: createGame,
    readTab: readTab
};


});
