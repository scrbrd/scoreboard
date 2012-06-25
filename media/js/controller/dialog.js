/* 
    Module: dialog
    Handle all dialog events.

    Dependencies:
        view/document
*/
define(
        [
            "MP",
            "js/constants",
            "js/event",
            "js/eventDispatcher",
        ],
        function (MP, Const, Event, EventDispatcher) {
      
    function initialize() {
        EventDispatcher.on(Event.CLIENT.DISPLAY_DIALOG, handleDisplayDialog);
    }

    function handleDisplayDialog(pageName, path) {
        MP.trackViewDialog(pageName, path);
    }

    return {
        initialize: initialize,
    };
});
