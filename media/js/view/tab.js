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
            "jQuery",
            "Backbone",
            "js/constants",
            "iScroll",
        ],
        function($, Backbone, Const, Scroller) {

    
    var TabView = Backbone.View.extend({

        contextView: null,
        contentView: null,
        navView: null,

        initialize: function () {
            this.contextView = new ContextView({el: this.options.context});
            this.navView = new NavView({el: this.options.nav});
            this.contentView = new ContentView({el: this.options.content});
        },

        render: function (newContext, newContent) {
            this.contextView.render(newContext);
            this.contentView.render(newContent);
        },

        pageName: function () {
            return this.contentView.$el.data(Const.DATA.PAGE_NAME);
        },


    });

    var ContextView = Backbone.View.extend({
        render: function (newHTML) {
            var newEl = $(newHTML).insertBefore(this.$el);
            this.$el.remove();
            this.setElement(newEl);
        },

        contextID: function () {
            return this.$el.data(Const.DATA.ID);
        },

        rivals: function () {
            return this.$el.data(Const.DATA.RIVALS);
        },
    });

    var NavView = Backbone.View.extend({
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

        render: function (newHTML) {
            this.$el.toggle(false);
            Scroller.scrollTo(0, 0, 0);  // scroll to x, y, time (ms)

            var newEl = $(newHTML).insertBefore(this.$el);
            this.$el.remove();
            this.setElement(newEl);

            this.$el.fadeIn('fast');
            Scroller.refresh();
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
