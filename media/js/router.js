define(
        [
            "Backbone",
        ], 
        /**
            A module for server routing.

            @exports Router

            @requires Backbone
        */
        function (Backbone) {

    /**
        Handle all routing interactions with server by using Backbone.
        (Subclasses Backbone.Router.)
        @class NavRouter
    */
    var NavRouter = Backbone.Router.extend(/** @lends NavRouter# */{


        /** 
            List out all routes. 
            @private 
            @type {Object}
        */
        routes: {
            ":tab":             "loadTab",      // load tab
            "*error":           "error"         // error catch all
        },

        loadTab: function (tab) {
            console.log("tab should be loaded without hitting this function");
        },

        error: function (error) {
            console.log("no handler: " + error);
        },
    });


    return /** @lends module:Router */ {
        /**
            Initialize NavRouter's history.
            @param {boolean} pushState Set Router's PushState functionality.
            @returns {NavRouter} An app-wide Router.
        */
        initialize: function (pushState) {
            // Backbone using History API's PushState
            var appRouter = new NavRouter();
            var options = {silent: true};
            if (pushState) {
                options.pushState = true;
            }
            
            Backbone.history.start(options);
        },

    };
});
