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
      
    function initialize(dialog) {
        dialog.on(Const.EVENT.DISPLAYED_DIALOG, function (pageName, path) {
            MP.trackViewDialog(pageName, path);
        });
    }

    return {
        initialize: initialize,
    };
});
