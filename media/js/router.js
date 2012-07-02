/**
    A limited Backbone Router for updating the browser.

    Unlike typical Backbone setups, we don't use the router to communicate
    with the server. Our architecture makes it easier to use a PageStateModel
    with html responses from the server, and keep things updated during
    static refreshes. (As Backbone's router ignores navigating to
    the current URL.)

    @exports Router

    @requires Backbone
*/
define(
        [
            "Backbone"
        ],
        function (Backbone) {


/**
    Handle all routing interactions with browser by extending Backbone
    Router.
*/
var NavRouter = Backbone.Router.extend({
    routes: {
        ":tab":             "loadTab",      // load tab
        "*error":           "error"         // error catch all
    },

    loadTab: function (tab) {
        console.log("tab should be loaded without hitting this function");
    },

    error: function (error) {
        console.log("no handler: " + error);
    }
});

/**
    Initialize NavRouter's history using History API's PushState, which
    effectively allows you to not use hash tags for AJAX requests.
*/
function initializeWithPushState() {
    // Backbone using History API's PushState
    var appRouter = new NavRouter();
    var options = {
        silent: true,
        pushState: true
    };
    
    Backbone.history.start(options);
}

return  {
    initializeWithPushState: initializeWithPushState
};


});
