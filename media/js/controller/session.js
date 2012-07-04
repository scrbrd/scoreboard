/**
    Handle session events.

    SessionController.controller inherits from BaseController.controller.

    @exports SessionController

    @requires MP
    @requires Event
    @requires BaseController
*/
define(
        [
            "MP",
            "js/event",
            "controller/base"
        ],
        function (MP, Event, BaseController) {


/**
    Controller instance for session event handling.
    @constructor
*/
var sessionController = (function () {
    var that = Object.create(BaseController.controller);

    /**
        Bind UPDATED_SESSION event.
    */
    that.initialize = function () {
        var events = {};

        events[Event.SERVER.UPDATED_SESSION] = that.handleSuccess;
        that.initializeEvents(events);
    };

    /**
        Handle a newly updated session by updating MixPanel identity.
    */
    that.handleSuccess = function (sessionModel) {
        var personID = sessionModel.personID().toString();
        MP.identifyUser(personID);
    };

    return that;
}());

return {
    controller: sessionController
};


});
