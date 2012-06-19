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
        ],
        function ($, MP, Doc, Const) {
    
    var router = null;

    function initialize(appRouter) {
        router = appRouter;
    }

    function handleSubmit(anchor, href, model) {
        var docView = Doc.retrieve();

        // switch active tab
        if (anchor !== null) {
            docView.tabView.navView.render(this, anchor);
        }

        // hide current content
        docView.tabView.contentView.hide();

        // send request to server
        router.navigate(href, {trigger: false});

        // update the model by reseting the pagename and fetching
        model.setPageName(href.substring(1));
        var start = new Date().getTime();
        var loadTabCont = this;
        model.fetch({
            data: $.param({
                "asynch": true,
            }),
            success: function (model, response) {
                var end = new Date().getTime();
                var time = end - start;
                console.log("success response: " + time + "ms");
                loadTabCont.setModelFromHTML(
                    model,
                    response.context_header,
                    response.content);
                loadTabCont.trackViewPage(Doc.retrieve(), model.pageName());
            },
            error: function (model, response) {
                console.log("error on model fetch");
            },
        });
    }

    
    function handleSuccess(context, content) {
        // FIXME DELETE THIS FUNCTION
        console.log("DELETE THIS FUNCTION NOW!!!");
        var docView = Doc.retrieve();
        var currModel = docView.model;
        this.setModelFromHTML(currModel, context, content);
        //docView.updateTab(context, content);
        this.trackViewPage(docView, currModel.pageName);
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
        handleSubmit: handleSubmit,
        handleSuccess: handleSuccess,
        trackViewPage: trackViewPage,
        setModelFromHTML: setModelFromHTML,
    };
});
