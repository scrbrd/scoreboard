/** 
    A dispatcher for all app-wide event triggers and notifications.

    The EventDispatcher extends Backbone Events, which allows for trigger, on, 
    and off functions to be centrally pooled. This dispatcher provides for 
    inter-module communication.

    The Views are directly bound to model change events and do NOT
    use this framework.

    @exports EventDispatcher

    @requires _
    @requires Backbone
*/
define(
        [
            "Underscore",
            "Backbone",
        ],
        function (_, Backbone) {

    var eventDispatcher = _.extend({}, Backbone.Events);
    return eventDispatcher;
});

