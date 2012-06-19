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
            "iScroll",
        ],
        function(_, $, Backbone, Const, Scroller) {

    
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
            // remove leading period from ".active-nav"
            noPeriodActive = Const.CLASS.ACTIVE_NAV.substr(1);
            noPeriodInactive = Const.CLASS.INACTIVE_NAV.substr(1);

            this.$(Const.CLASS.ACTIVE_NAV)
                .removeClass(noPeriodActive) // remove current active nav
                .addClass(noPeriodInactive); // add inactive nav class

            this.$(activeAnchor)
                .removeClass(noPeriodInactive) // remove inactive nav
                .addClass(noPeriodActive); // add active nav 
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
