/**
    Manage the LeagueTab portion of the DOM with Backbone.View.

    @exports LeagueView

    @requires $
    @requires Backbone
    @requires Const
    @requires TabView

*/
define(
        [
            "jQuery",
            "Backbone",
            "js/constants",
            "view/tab"
        ],
        function ($, Backbone, Const, TabView) {


/**
    Manage all DOM manipulation for league tab page.
    @constructor
*/
var LeagueView = TabView.extend({

    /**
        Initialize subViews.
        @param {Object} pageStateModel
    */
    initialize: function (pageStateModel) {
        TabView.prototype.initialize.call(this, pageStateModel);
    }

});

return {
    construct: function (options) {
        return new LeagueView(options);
    }
};


});
