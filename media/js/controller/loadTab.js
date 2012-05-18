/* 
    Module: loadTab
    Handle tab updating by a returning a stateless object.

    Dependencies:
        view/document
*/
define(
        [
            "MP",
            "view/document",
            "js/constants",
        ],
        function (MP, Doc, Const) {
       
    function handleSubmit() {
        var docView = Doc.retrieve();
        docView.tabView.contentView.hide();
    }
    
    function handleSuccess(context, content) {
        var docView = Doc.retrieve();
        docView.updateTab(context, content);
        this.trackViewPage(docView);
    }

    /*
        Function: trackViewPageByName
        Track the right type of page view by checking the page's name.

        Parameters:
            name - specific name of tab page
            path - path to page
    */
    function trackViewPage(docView) {
        var name = docView.tabView.pageName();
        var path = docView.path();

        if (name === Const.PAGE_NAME.RANKINGS ||
            name === Const.PAGE_NAME.GAMES) {
            MP.trackViewTab(name, path);
        } else if (name === Const.PAGE_NAME.CREATE_GAME) {
            MP.trackViewDialog(name, path);
        } else {
            MP.trackViewLanding(name, path);
        }
    }
    
    return {
        handleSubmit: handleSubmit,
        handleSuccess: handleSuccess,
        trackViewPage: trackViewPage,
    };
});
