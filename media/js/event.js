define(
        [], 
        /**
            Event Constants

            Client events are usually in present tense to indicate that the 
            handler is responsible for creating the functionality of event. 
            In general, try to handle eveything at trigger time so a second 
            past tense event isn't required.

            Server events are typically past tense to indicate that the main
            handlers will be responding to events that happened elsewhere.

            @exports Event
        */
        function () {
    
    var event = /** @lends module:Event */ { 

        /**
            Enum for client initiated events. 
            @enum {string}
            @const
        */
        CLIENT: {
            /** @const */ DISPLAY_DIALOG: "client-display-dialog",
            /** @const */ CREATE_GAME: "client-create-game",
            /** @const */ VIEW_PAGE: "client-view-page",
            /** @const */ RELOAD_PAGE: "client-reload-page",
            /** @const */ REQUEST_FACEBOOK_LOGIN:
                "client-request-facebook-login",
        },
        
        
        /**
            Enum for server initiated events. 
            @enum {string}
            @const
        */
        SERVER: {
            /** @const */ CREATED_GAME: "server-created-game",
            /** @const */ VIEWED_PAGE: "server-viewed-page",
        },
    };

    return event;
});

