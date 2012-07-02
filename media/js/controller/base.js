/**
    Generic Controller for defining how events should be handled.

    All controllers subinstance from this controller. Use 'handleSubmit' and
    'handleSuccess' to keep the subinstances similar. Send a list
    of events to 'initializeEvents'.

    See Douglas Crockford's Prototypal Inheritance:
    http://javascript.crockford.com/prototypal.html
   
    @exports BaseController

    @requires EventDispatcher
*/
define(
        [
            "js/eventDispatcher"
        ],
        function (EventDispatcher) {


/**
    baseController instance for other controllers to subclass.
    @constructor
*/
var baseController = (function () {
    var that = {};

    /**
        Bind events to various functions.
    */
    that.initializeEvents = function (events) {
        var key;
        for (key in events) {
            if (events.hasOwnProperty(key)) {
                EventDispatcher.on(key, events[key], that);
            }
        }
    };

    /**
        Handle submit type events.
    */
    that.handleSubmit = function () {
        console.log("Overwrite handleSubmit in subclass");
    };

    /**
        Handle success type events.
    */
    that.handleSuccess = function () {
        console.log("Overwrite handleSuccess in subclass");
    };

    /**
        Handle error type events.
    */
    that.handleError = function () {
        console.log("Overwrite handleError in subclass");
    };

    return that;
}());

return {
    controller: baseController
};


});
