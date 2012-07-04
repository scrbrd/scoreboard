/**
    All triggerable application events for publish/subscribe.

    Events are triggered by any module that needs to send out an
    app-wide alert. Then other modules can subscribe to these events.

    The Views are directly bound to model change events. That communication
    does not use this framework. Also, these events do not need to
    correspond to mixpanel events, though they usually do.

    I've used present tense for Client events and past tense for Server
    events. This respects how the handlers typically respond to these events
    and also make it easy to connect initial Client events and later Server
    response events.

    TODO: Make Events objects with initialization parameters.

    @exports Event
*/
define(
        [],
        function () {
    

var event = {

    /**
        Enum for client initiated events.
        @enum {string}
    */
    CLIENT: {
        DISPLAY_DIALOG:         "client-display-dialog",
        ENTER_GAME_DATA:        "client-enter-game-data",
        CREATE_GAME:            "client-create-game",
        VIEW_PAGE:              "client-view-page",
        RELOAD_PAGE:            "client-reload-page",
        REQUEST_FACEBOOK_LOGIN: "client-request-facebook-login"
    },
    
    
    /**
        Enum for server initiated events.
        @enum {string}
    */
    SERVER: {
        CREATED_GAME:           "server-created-game",
        UPDATED_SESSION:        "server-updated-session",
        VIEWED_PAGE:            "server-viewed-page"
    }
};

return event;


});
