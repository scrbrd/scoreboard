/**
    Handle login events.

    LoginController.controller inherits from BaseController.controller.

    @exports LoginController

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
    Controller instance for login event handling.
    @constructor
*/
var loginController = (function () {
    var that = Object.create(BaseController.controller);

    /**
        Bind REQUEST_FACEBOOK_LOGIN event.
    */
    that.initialize = function () {
        var events = {};

        events[Event.CLIENT.REQUEST_FACEBOOK_LOGIN] = that.handleSubmit;
        events[Event.SERVER.SIGNED_UP] = that.handleSuccess;
        that.initializeEvents(events);
    };

    /**
        Handle Facebook login submission.
    */
    that.handleSubmit = function () {
        console.log("handle request facebook login submit");
        MP.trackRequestFacebookLogin();
    };
    
    /**
        Handle a successful user sign up.
    */
    that.handleSuccess = function () {
        MP.trackSignUpThroughFacebook();
    };

    /**
        Handle an unsuccessful user authorization.
    */
    that.handleError = function () {
        // TODO handle failure events here.
    };

    return that;
}());

return {
    controller: loginController
};


});
