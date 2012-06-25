define(
        [
            "js/constants",
            "Backbone",
        ],
        /**
            Represent a the Page State. A presentation model if you will.

            TODO - the context id should be in a ContextModel, and these models
            should be organized into Collections.

            @exports PageStateModel

            @requires Const
            @requires Backbone
        */
        function (Const, Backbone) {

    CONTEXT = "context";
    CONTENT = "content";

    PageStateModel = Backbone.Model.extend({

        urlRoot: function () {
            console.log("urlRoot");
            return "/" + this.pageName();
        },
        
        url: function () {
            console.log("url");
            console.log("/" + this.pageName());
            return "/" + this.pageName();
        },

        context: function () {
            return this.get(CONTEXT);
        },

        setContext: function (context) {
            this.set(CONTEXT, context);
        },

        content: function () {
            return this.get(CONTENT);
        },

        setContent: function (content) {
            this.set(CONTENT, content);
        },

        contextID: function () {
            return this.get(Const.DATA.ID);
        },

        setContextID: function (id) {
            this.set(Const.DATA.ID, id);
        },

        pageType: function () {
            return this.get(Const.DATA.PAGE_TYPE);
        },

        setPageType: function (pageType) {
            this.set(Const.DATA.PAGE_TYPE, pageType);
        },

        pageName: function () {
            return this.get(Const.DATA.PAGE_NAME);
        },

        setPageName: function (pageName) {
            this.set(Const.DATA.PAGE_NAME, pageName);
        },

        // if it's the initial set then don't fire change event
        setAttribute: function (key, value) {
            var silent = false;
            if (this.get(key) === null) {
                silent = true;
            }

            this.set(key, value, {silent: silent});
        },

    });

    var pageStateModel = new PageStateModel();

    return {
        retrieve: function () {
            return pageStateModel;
        },
    };
});
