/* 
    Module: tab
    Manage tab (mainly the content)  portion of the DOM.

    Package:
        view

    Dependencies:
        $
        Backbone
        Const
        Scroller
*/
define(
        [
            "Underscore",
            "jQuery",
            "Backbone",
            "js/constants",
            "util/dom",
            "iScroll",
        ],
        function(_, $, Backbone, Const, DOMUtil, Scroller) {

    
    var TabView = Backbone.View.extend({

        contextView: null,
        contentView: null,
        navView: null,

        initialize: function (pageStateModel) {
            this.contextView = new ContextView(pageStateModel);
            this.navView = new NavView(pageStateModel);
            this.contentView = new ContentView(pageStateModel);
        },

    });

    var ContextView = Backbone.View.extend({

        changeContextEvent: "change:context",

        initialize: function (model) {
            this.setElement(Const.ID.CONTEXT);

            this.model = model;
            this.model.bind(this.changeContextEvent, this.render, this);
        },

        render: function () {
            var newEl = $(this.model.context()).insertBefore(this.$el);
            this.$el.remove();
            this.setElement(newEl);
        },

    });

    var NavView = Backbone.View.extend({
     
        changePageNameEvent: "change:" + Const.DATA.PAGE_NAME,

        initialize: function (model) {
            this.setElement(Const.DOM.NAV);

            this.model = model;
            this.model.bind(this.changePageNameEvent, this.render, this);
        },

        render: function (activeAnchor) {
            activeClass = DOMUtil.getClassFromSelector(
                    Const.CLASS.ACTIVE_NAV);
            inactiveClass = DOMUtil.getClassFromSelector(
                    Const.CLASS.INACTIVE_NAV);

            this.$(Const.CLASS.ACTIVE_NAV)
                .removeClass(activeClass) // remove current active nav
                .addClass(inactiveClass); // add inactive nav class

            // TODO change this to an ID (it will make the controller logic
            // simpler
            this.$(DOMUtil.getSelectorFromClass(this.model.pageName()))
                .removeClass(inactiveClass) // remove inactive nav
                .addClass(activeClass); // add active nav 
        },
    });

    var ContentView = Backbone.View.extend({

        changeContentEvent: "change:content",

        initialize: function (model) {
            this.setElement(Const.ID.CONTENT);

            this.model = model;
            this.model.bind(this.changeContentEvent, this.render, this);

            this.scroller = Scroller.construct();
        },
        
        render: function () {
            this.$el.toggle(false);
            this.scroller.scrollTo(0, 0, 0);  // scroll to x, y, time (ms)
            
            var newEl = $(this.model.content()).insertBefore(this.$el);
            this.$el.remove();
            this.setElement(newEl);
            this.$el.fadeIn('fast');
            this.scroller.refresh();

            return this;
        },

    });

    return {
        construct: function (options) {
            return new TabView(options);
        },
    };
});
