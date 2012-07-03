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


// String used to identify ugly portion of facebook redirect.
var UGLY_PATH = '#_=_';

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
    //remove ugly hash before initializing router
    removeEmptyHash();

    // Backbone using History API's PushState
    var appRouter = new NavRouter();
    var options = {
        silent: true,
        pushState: true
    };
    Backbone.history.start(options);
}

/**
    Remove the empty hash ("#_=_") from facebook login.
*/
function removeEmptyHash() {
    var path = window.location.pathname;
    var hash = window.location.hash;
    var title = document.title;
    if (hash === UGLY_PATH) {
        window.location.hash = ''; // for older browsers
        history.pushState('', title, path); // for pushState browsers
        // TODO test with older browsers and stop page reload.
    }
}

return  {
    initializeWithPushState: initializeWithPushState
};


});
