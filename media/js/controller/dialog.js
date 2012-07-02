/**
    Handle events that relate to the dialog pages.

    DialogController.controller inherits from BaseController.controller.

    @exports DialogController

    @requires MP
    @requires Const
    @requires Event
    @requires BaseController
*/
define(
        [
            "MP",
            "js/constants",
            "js/event",
            "controller/base"
        ],
        function (MP, Const, Event, BaseController) {
      

/**
    Controller instance for responding to dialog actions.
    @constructor
*/
var dialogController = (function () {
    var that = Object.create(BaseController.controller);

    /**
        Bind ENTER_DATA event.
    */
    that.initialize = function () {
        var events = {};

        events[Event.CLIENT.ENTER_GAME_DATA] = that.handleSubmit;
        that.initializeEvents(events);
    };

    /**
        Handle tracking data input as a user types.

        The pageName should be the dialog if it's on a dialog and not
        the page that the dialog is on.
        @param {string} dataType the DATA type of the input
        @param {string} inputValue the actual inputted data
        @param {string} pageName the page that the data's on
    */
    that.handleSubmit = function (dataType, inputValue, pageName) {
        MP.trackEnterDataForGame(dataType, inputValue, pageName);
    };
    
    return that;
}());

return {
    controller: dialogController
};


});
