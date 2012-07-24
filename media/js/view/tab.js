/**
    Manage the tab portion of the DOM with Backbone.View.

    @exports TabView

    @requires $
    @requires Backbone
    @requires Const
    @requires DOMUtil
    @requires iScroll
*/
define(
        [
            "jQuery",
            "Backbone",
            "js/constants",
            "util/dom",
            "iScroll"
        ],
        function ($, Backbone, Const, DOMUtil, Scroller) {


var MODEL_EVENT = {
    CHANGE_CONTEXT: "change:" + "context",
    CHANGE_CONTENT: "change:" + "content",
    CHANGE_PAGE_NAME: "change:" + Const.DATA.PAGE_NAME
};

/**
    Manage all DOM manipulation for tab page.
    @constructor
*/
var TabView = Backbone.View.extend({

    // store subViews
    headerView: null,
    contentView: null,
    navView: null,

    /**
        Initialize subViews.
        @param {Object} pageStateModel
    */
    initialize: function (pageStateModel) {
        this.headerView = new HeaderView(pageStateModel);
        this.navView = new NavView(pageStateModel);
        this.contentView = new ContentView(pageStateModel);
    }
});

/**
    Manage all DOM manipulations for header.
    @constructor
*/
var HeaderView = Backbone.View.extend({

    /**
        Setup header portion of DOM and bind to model events.
        @param {Object} model
    */
    initialize: function (model) {
        this.setElement(Const.ID.TAB_HEADER);

        this.model = model;
        this.model.on(MODEL_EVENT.CHANGE_CONTEXT, this.render, this);
    },

    /**
        Render the HeaderView by swapping the new html in.
    */
    render: function () {
        var newEl = $(this.model.header()).insertBefore(this.$el);
        this.$el.remove();
        this.setElement(newEl);

        return this;
    }

});

/**
    Manage all DOM manipulations for nav bar.
    @constructor
*/
var NavView = Backbone.View.extend({
    
    /**
        Setup navigation portion of DOM and bind to model events.
        @param {Object} model
    */
    initialize: function (model) {
        this.setElement(Const.DOM.NAV);

        this.model = model;
        this.model.on(MODEL_EVENT.CHANGE_PAGE_NAME, this.render, this);
    },

    /**
        Render the NavView by updating the active anchor.
    */
    render: function () {
        var activeClass = DOMUtil.getClassFromSelector(
                Const.CLASS.ACTIVE_NAV);
        var inactiveClass = DOMUtil.getClassFromSelector(
                Const.CLASS.INACTIVE_NAV);

        this.$(Const.CLASS.ACTIVE_NAV)
            .removeClass(activeClass) // remove current active nav
            .addClass(inactiveClass); // add inactive nav class

        // TODO change this to an ID (it will make the controller logic
        // simpler
        this.$(DOMUtil.getSelectorFromClass(this.model.pageName()))
            .removeClass(inactiveClass) // remove inactive nav
            .addClass(activeClass); // add active nav

        return this;
    }
});

/**
    Manage all DOM manipulations for the content.
    @constructor
*/
var ContentView = Backbone.View.extend({

    /**
        Setup content portion of DOM and bind to model events.
        @param {Object} model
    */
    initialize: function (model) {
        this.setElement(Const.ID.CONTENT);

        this.model = model;
        this.model.on(MODEL_EVENT.CHANGE_CONTENT, this.render, this);

        this.scroller = Scroller.construct();
    },
    
    /**
        Render the ContentView by updating the content and resetting
        the scroller.
    */
    render: function () {
        this.$el.toggle(false);
        this.scroller.scrollTo(0, 0, 0);  // scroll to x, y, time (ms)
        
        var newEl = $(this.model.content()).insertBefore(this.$el);
        this.$el.remove();
        this.setElement(newEl);
        this.$el.fadeIn('fast');
        this.scroller.refresh();

        return this;
    }
});

return {
    construct: function (options) {
        return new TabView(options);
    }
};


});
