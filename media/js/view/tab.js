/**
    Manage the tab portion of the DOM with Backbone.View.

    AppView:
        MainHeader
        Content

    TabView extends AppView:
        TabHeader extends MainHeader
        TabContent extends Content

    DialogView extends AppView
        DialogHeader extends MainHeader
        DialogContent extends Content

    TabContent extends Content
        Properties  [model.context]
        Summary     [model.aggregations(standings, activity)]
        Feed        [model.objects]

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
    CHANGE_AGGREGATIONS: "change:" + "aggregations",
    CHANGE_OBJECTS: "change:" + "objects",
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
    navView: null,
    contentView: null,

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
        @param {Object} pageStateModel
    */
    initialize: function (pageStateModel) {
        this.setElement(Const.ID.TAB_HEADER);

        this.model = pageStateModel;
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
        @param {Object} pageStateModel
    */
    initialize: function (pageStateModel) {
        this.setElement(Const.DOM.NAV);

        this.model = pageStateModel;
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

    // store subViews
    propertiesSection: null,
    summarySection: null,
    feedSection: null,

    /**
        Setup content portion of DOM and bind to model events.
        @param {Object} pageStateModel
    */
    initialize: function (pageStateModel) {
        this.setElement(Const.ID.CONTENT);

        this.model = pageStateModel;
        this.model.on(MODEL_EVENT.CHANGE_CONTENT, this.render, this);

        this.initializeSections(this.model);
        this.scroller = Scroller.construct();
    },

    /**
        Set up sections contained by Content.
        @param {Object} pageStateModel
    */
    initializeSections: function (pageStateModel) {
        // TODO: When do we need these Views (you'll need to add the sections
        // to PageStateModel as well.
        // this.propertiesSection = new PropertiesSection(pageStateModel);
        // this.summarySection = new SummarySection(pageStateModel);
        // this.feedSection = new FeedSection(pageStateModel);
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

/**
    Manage all DOM manipulations for the Properties section.
    @constructor
*/
var PropertiesSection = Backbone.View.extend({

    /**
        Setup Properties section of DOM and bind to model events.
        @param {Object} pageStateModel
    */
    initialize: function (pageStateModel) {
        this.setElement(Const.ID.PROPERTIES);

        //this.model = pageStateModel;
        //this.model.on(MODEL_EVENT.CHANGE_CONTEXT, this.render, this);
    },

    /**
        Render the ContentView by updating the content and resetting
        the scroller.
    */
    render: function () {
        //var newEl = $(this.model.context()).insertBefore(this.$el);
        //this.$el.remove();
        //this.setElement(newEl);

        return this;
    }
});


/**
    Manage all DOM manipulations for the Summary section.
    @constructor
*/
var SummarySection = Backbone.View.extend({

    /**
        Setup Summary section of DOM and bind to model events.
        @param {Object} pageStateModel
    */
    initialize: function (pageStateModel) {
        this.setElement(Const.ID.SUMMARY);

        //this.model = pageStateModel;
        //this.model.on(MODEL_EVENT.CHANGE_AGGREGATE, this.render, this);
    },

    /**
        Render the ContentView by updating the content and resetting
        the scroller.
    */
    render: function () {
        //var newEl = $(this.model.aggregate()).insertBefore(this.$el);
        //this.$el.remove();
        //this.setElement(newEl);

        return this;
    }
});


/**
    Manage all DOM manipulations for the Feed section.
    @constructor
*/
var FeedSection = Backbone.View.extend({

    /**
        Setup Feed section of DOM and bind to model events.
        @param {Object} pageStateModel
    */
    initialize: function (pageStateModel) {
        this.setElement(Const.ID.FEED);

        //this.model = pageStateModel;
        //this.model.on(MODEL_EVENT.CHANGE_OBJECTS, this.render, this);
    },

    /**
        Render the ContentView by updating the content and resetting
        the scroller.
    */
    render: function () {
        //var newEl = $(this.model.objects()).insertBefore(this.$el);
        //this.$el.remove();
        //this.setElement(newEl);

        return this;
    }
});

return {
    construct: function (options) {
        return new TabView(options);
    }
};


});
