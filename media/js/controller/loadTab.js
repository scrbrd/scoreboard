/* 
    Module: loadTab
    Handle tab updating by a returning a stateless object.

    Dependencies:
        view/document
*/
define(
        [
            "jQuery",
            "MP",
            "view/document",
            "js/constants",
            "js/event",
            "js/eventDispatcher",
        ],
        function ($, MP, Doc, Const, Event, EventDispatcher) {
    
    var router = null;

    function initialize(appRouter) {
        // FIXME XXX - remove router
        router = appRouter;
        EventDispatcher.on(Event.CLIENT.VIEW_PAGE, handleViewPage);
        EventDispatcher.on(Event.CLIENT.RELOAD_PAGE, handleReloadPage);
        EventDispatcher.on(Event.SERVER.VIEWED_PAGE, handleSuccess);
    }

    function handleViewPage(anchor, href, model) {
        var docView = Doc.retrieve();

        // switch active tab
        docView.tabView.navView.render(this, anchor);

        // Update URL
        router.navigate(href, {trigger: false});

        handleSubmit(href, model);
    }

    function handleReloadPage(href, model) {
        handleSubmit(href, model);
    }

    function handleSubmit(href, model) {
        var docView = Doc.retrieve();

        // hide current content
        docView.tabView.contentView.hide();
        
        // update the model by reseting the pagename and fetching
        model.setPageName(href.substring(1));
        var start = new Date().getTime();
        model.fetch({
            data: $.param({
                "asynch": true,
            }),
            success: function (model, response) {
                var end = new Date().getTime();
                var time = end - start;
                console.log("success response: " + time + "ms");
                EventDispatcher.on(
                        Event.SERVER.VIEWED_PAGE,
                        model,
                        response.context_header, 
                        response.content,
                        docView);
            },
            error: function (model, response) {
                console.log("error on model fetch");
            },
        });

    }

    function handleSuccess(model, context, content, docView) {
        setModelFromHTML(
            model,
            context,
            content);
        trackViewPage(docView, model.pageName());
    }

    /*
        Function: trackViewPageByName
        Track the right type of page view by checking the page's name.

        Parameters:
            name - specific name of tab page
            path - path to page
    */
    function trackViewPage(docView, pageName) {
        var path = docView.path();

        if (pageName === Const.PAGE_NAME.RANKINGS ||
            pageName === Const.PAGE_NAME.GAMES) {
            MP.trackViewTab(pageName, path);
        } else if (pageName === Const.PAGE_NAME.CREATE_GAME) {
            MP.trackViewDialog(pageName, path);
        } else {
            MP.trackViewLanding(pageName, path);
        }
    }

    function setModelFromHTML(model, contextHTML, contentHTML) {
        var contextID = $(contextHTML).data(Const.DATA.ID);
        var rivals = $(contextHTML).data(Const.DATA.RIVALS);
        var pageName = $(contentHTML).data(Const.DATA.PAGE_NAME);

        model.setContext(contextHTML);
        model.setContent(contentHTML);
        model.setContextID(contextID);
        model.setRivals(rivals);
        model.setPageName(pageName);
    }

    return {
        initialize: initialize,
    };
});
