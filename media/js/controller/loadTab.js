/* 
    Module: loadTab
    Handle tab updating by a returning a stateless object.

    Dependencies:
        view/document
*/
define(
        [
            "jQuery",
            "Backbone",
            "MP",
            "js/constants",
            "js/event",
            "js/eventDispatcher",
            "js/crud",
        ],
        function ($, Backbone, MP, Const, Event, EventDispatcher, Crud) {
    

    function initialize() {
        EventDispatcher.on(Event.CLIENT.VIEW_PAGE, handleViewPage);
        EventDispatcher.on(Event.CLIENT.RELOAD_PAGE, handleReloadPage);
        EventDispatcher.on(Event.SERVER.VIEWED_PAGE, handleSuccess);
    }

    function handleViewPage(anchor, href, pageStateModel) {
        // switch active tab
        var pageName = "";
        if ($(anchor).hasClass(Const.PAGE_NAME.RANKINGS)) {
            pageName = Const.PAGE_NAME.RANKINGS;
        } else if ($(anchor).hasClass(Const.PAGE_NAME.GAMES)) {
            pageName = Const.PAGE_NAME.GAMES;
        }
        pageStateModel.setPageName(pageName);

        // Update URL
        Backbone.history.navigate(href, {trigger: false});

        handleSubmit(href, pageStateModel);
    }

    function handleReloadPage(href, pageStateModel) {
        handleSubmit(href, pageStateModel);
    }

    function handleSubmit(href, pageStateModel) {
        // set loading screen
        var loading = "<div class=\"loading\">Loading...</div>";
        pageStateModel.setContent(loading);
        
        Crud.fetchTab(href, pageStateModel);

    }

    function handleSuccess(model, path) {
        trackViewPage(model.pageName(), path);
    }

    /*
        Function: trackViewPageByName
        Track the right type of page view by checking the page's name.

        Parameters:
            name - specific name of tab page
            path - path to page
    */
    function trackViewPage(pageName, path) {
        // FIXME check Page Type
        if (pageName === Const.PAGE_NAME.RANKINGS ||
            pageName === Const.PAGE_NAME.GAMES) {
            MP.trackViewTab(pageName, path);
        } else if (pageName === Const.PAGE_NAME.CREATE_GAME) {
            MP.trackViewDialog(pageName, path);
        } else  {
            // TODO add in landing page qualifier
            console.log("landing page viewed");
            MP.trackViewLanding(pageName, path);
        } 
    }

    return {
        initialize: initialize,
    };
});
