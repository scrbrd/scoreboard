define(
        [
            "Backbone",
        ],
        /**
            Represent a generic model for html reader models.

            @exports HTMLReader

            @requires Backbone
        */
       function (Backbone) {

    CONTEXT = "context";
    CONTENT = "content";
    CONTEXT_ID = "context-id";
    RIVALS = "rivals";
    PAGE_NAME = "page-name";

    HTMLReader = Backbone.Model.extend({

        defaults: {
            context: null,
            content: null,
            contextID: null,
            rivals: null,
            pageName: null,
        },

        initialize: function () {
        },

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
            this.setAttribute(CONTEXT, context);
        },

        content: function () {
            return this.get(CONTENT);
        },

        setContent: function (content) {
            this.setAttribute(CONTENT, content);
        },

        contextID: function () {
            return this.get(CONTEXT_ID);
        },

        setContextID: function (id) {
            this.setAttribute(CONTEXT_ID, id);
        },

        rivals: function () {
            return this.get(RIVALS);
        },

        setRivals: function (rivals) {
            this.setAttribute(RIVALS, rivals);
        },

        pageName: function () {
            return this.get(PAGE_NAME);
        },

        setPageName: function (pageName) {
            this.setAttribute(PAGE_NAME, pageName);
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

    return HTMLReader;
});
