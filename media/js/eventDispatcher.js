define(
        [
            "Underscore",
            "Backbone",
        ],
        /** 
            A dispatcher for all app-wide event triggers and notifications.

            @exports EventDispatcher

            @requires _
            @requires Backbone
        */
        function (_, Backbone) {

    var eventDispatcher = _.extend({}, Backbone.Events);

    return eventDispatcher;
});

