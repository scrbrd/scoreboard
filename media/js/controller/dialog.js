/** 
    Handle events that relate to the dialog actions.

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
            "controller/base",
        ],
        function (MP, Const, Event, BaseController) {
      
    /**
        Controller instance for responding to dialog actions.
        @constructor
    */
    var dialogController = (function () {
        var that = Object.create(BaseController.controller);

        /** 
            Bind DISPLAY_DIALOG event.
        */
        that.initialize = function () {
            var events = {};

            events[Event.CLIENT.DISPLAY_DIALOG] = that.handleSubmit;
            that.initializeEvents(events);
        };

        /**
            Handle event tracking for dialog display.
            @param {string} pageName name of the dialog
            @param {string} path path to url of the tab that the dialog's on.
        */
        that.handleSubmit = function(pageName, path) {
            MP.trackViewDialog(pageName, path);
        };
        
        return that;
    }());

    return {
        controller: dialogController,
    };
});
