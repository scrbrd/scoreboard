define(
        [
            "js/constants",
            "Backbone",
        ],
        /**
            Represent the Viewer/User's context - we're talking application
            logic and not View/Page State.

            @exports ViewerContextModel
            
            @requires Const
            @requires Backbone
        */
        function (Const, Backbone) {

    ViewerContextModel = Backbone.Model.extend({

        defaults: {
            rivals: null,
        },

        rivals: function() {
            return this.get(Const.DATA.RIVALS);
        },

        setRivals: function (rivals) {
            this.setAttribute(Const.DATA.RIVALS, rivals);
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

    var viewerContextModel = new ViewerContextModel();

    return {
        retrieve: function () {
            return viewerContextModel;
        },
    };
});
