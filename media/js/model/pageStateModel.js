/**
    Represent the Page State. A presentation model if you will.

    These Models aren't using Prototypal inheritance to comply with Backbone.
    
    TODO - the context id should be in a ContextModel, and these models
    should be organized into Collections.

    @exports PageStateModel

    @requires Const
    @requires Backbone
*/
define(
        [
            "js/constants",
            "Backbone"
        ],
        function (Const, Backbone) {


var HEADER = "header";
var CONTENT = "content";

/**
    Model to hold Page State and replacable html chunks.
    @constructor
*/
var PageStateModel = Backbone.Model.extend({

    /**
        Provide access to url for CRUD operations.

        Only used when the Model is part of a collection.
    */
    urlRoot: function () {
        console.log("urlRoot");
        return "/" + this.pageName();
    },
    
    /**
        Provide access to url for CRUD operations.
    */
    url: function () {
        console.log("url");
        console.log("/" + this.pageName());
        return "/" + this.pageName();
    },

    /**
        Provide access to the current header html.
    */
    header: function () {
        return this.get(HEADER);
    },

    /**
        Provide mutator for header html.
        @param {string} header
    */
    setHeader: function (header) {
        this.set(HEADER, header);
    },

    /**
        Provide access to the current content html.
    */
    content: function () {
        return this.get(CONTENT);
    },

    /**
        Provide mutator for content html.
        @param {string} content
    */
    setContent: function (content) {
        this.set(CONTENT, content);
    },

    /**
        Provide access to the page's context ID.
    */
    contextID: function () {
        return this.get(Const.DATA.ID);
    },

    /**
        Provide mutator for the page's context ID.
        @param {string} id
    */
    setContextID: function (id) {
        this.set(Const.DATA.ID, id);
    },

    /**
        Provide access to the page type. (e.g. dialog, tab, etc.)
    */
    pageType: function () {
        return this.get(Const.DATA.PAGE_TYPE);
    },

    /**
        Provide mutator for the page's type
        @param {string} pageType
    */
    setPageType: function (pageType) {
        this.set(Const.DATA.PAGE_TYPE, pageType);
    },

    /**
        Provide access to the page's name.
    */
    pageName: function () {
        return this.get(Const.DATA.PAGE_NAME);
    },

    /**
        Provide mutator for the page's name.
        @param {string} pageName
    */
    setPageName: function (pageName) {
        this.set(Const.DATA.PAGE_NAME, pageName);
    }

});

var pageStateModel = new PageStateModel();
return {
    retrieve: function () {
        return pageStateModel;
    }
};


});
