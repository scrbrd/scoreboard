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

        initialize: function (model) {
            this.contextView = new ContextView(model);
            this.navView = new NavView();
            this.contentView = new ContentView(model);
        },

    });

    var ContextView = Backbone.View.extend({


        initialize: function (model) {
            this.setElement(Const.ID.CONTEXT);

            this.model = model;
            _.bindAll(this, "render");
            this.model.bind("change:context", this.render);
        },

        render: function () {
            var newEl = $(this.model.context()).insertBefore(this.$el);
            this.$el.remove();
            this.setElement(newEl);
        },

    });

    var NavView = Backbone.View.extend({
       
        initialize: function () {
            this.setElement(Const.DOM.NAV);
        },

        render: function (controller, activeAnchor) {
            // remove leading period from selectors
            activeClass = DOMUtil.getClassFromClassSelector(
                    Const.CLASS.ACTIVE_NAV);
            inactiveClass = DOMUtil.getClassFromClassSelector(
                    Const.CLASS.INACTIVE_NAV);

            this.$(Const.CLASS.ACTIVE_NAV)
                .removeClass(activeClass) // remove current active nav
                .addClass(inactiveClass); // add inactive nav class

            this.$(activeAnchor)
                .removeClass(inactiveClass) // remove inactive nav
                .addClass(activeClass); // add active nav 
        },
    });

    var ContentView = Backbone.View.extend({


        initialize: function (model) {
            this.setElement(Const.ID.CONTENT);

            this.model = model;
            _.bindAll(this, "render");
            this.model.bind("change:content", this.render);
        },
        
        render: function () {
            this.$el.toggle(false);
            Scroller.scrollTo(0, 0, 0);  // scroll to x, y, time (ms)
            
            var newEl = $(this.model.content()).insertBefore(this.$el);
            this.$el.remove();
            this.setElement(newEl);
            this.$el.fadeIn('fast');
            Scroller.refresh();

            return this;
        },

        /*
            Function: hide
            Hide the content and show a loading screen.
        */
        hide: function () {
            var loading = "<span class=\"loading\">Loading...</span>";
            
            this.$el.toggle(false);
            Scroller.scrollTo(0, 0, 0);
            this.$el.html(loading).toggle(true);
        },
    });

    return {
        construct: function (options) {
            return new TabView(options);
        },
    };
});
