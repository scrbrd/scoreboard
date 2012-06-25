/* 
    Module: login
    Manage any login events

    Dependencies:
        view/document
*/
define(
        [
            "jQuery",
            "Backbone",
            "MP",
            "view/document",
            "js/constants",
            "js/event",
            "js/eventDispatcher",
        ],
        function ($, Backbone, MP, Doc, Const, Event, EventDispatcher) {
    

    function initialize() {
        EventDispatcher.on(Event.CLIENT.REQUEST_FACEBOOK_LOGIN, handleSubmit);
    }


    function handleSubmit() {
        console.log("handle request facebook login submit");
        MP.trackRequestFacebookLogin();
    }

    function handleSuccess() {
    }

    return {
        initialize: initialize,
    };
});
