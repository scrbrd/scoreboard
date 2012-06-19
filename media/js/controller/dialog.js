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
        ],
        function (MP, Const) {
      
    function initialize(documentView) {
        documentView.on(
                Const.EVENT.DISPLAY_DIALOG, 
                function (pageName, id, rivals, path) {
                    MP.trackViewDialog(pageName, path);
                });
    }

    return {
        initialize: initialize,
    };
});
