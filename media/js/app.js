/**
    The Sqoreboard mobile client application.

    app.js runs all the application logic. It is to a reusable module but part
    of the load hierarchy. We are using Backbone to create an MVC Framework
    client-side.



    MODELS:
    We are using a very limited model. ViewerContext is being fetched once to
    provide some properties about the user/viewer. PageState is being fetched
    on every page load and keeps track of important contextual information
    as well as providing blocks of html to the Views.

    ROUTER/CRUD:
    We use Backbone's Router for URL updating, but all data fetching is being
    handles by our CRUD (create, read, update, delete) module. This
    architecture makes it easier to have unconventional models and massage
    the incoming data to fit into our framework.

    CONTROLLERS/EVENTS:
    Although Model property changes are bound to View render functions, all
    other inter-module communication is built off a central EventDispatcher.
    Besides View to View triggers, the main consumers of these Events are
    Controllers, that know how to handle both Client and Server triggered
    Events.

    VIEWS:
    The Views create a basic framework. They are very stripped down and expect
    to receive HTML directly from the model instead of using a templating
    framework.



    THIRD-PARTY LIBRARIES:
    1. jQuery: Provides a toolkit for DOM manipulation and other stuff.
    2. Underscore: Provides a functional js toolkit.
    3. Backbone: Provides an MVC framework (limited model usage.)
    4. iScroll: Provides awesome iPhone-like scrolling.
    5. MixPanel: Provides an event drivent testing suite.

    JQUERY PLUGINS:
    1. form2js: Converts form data to JSON for POSTing.
    2. UI: Provides a quite of UI components (including autocomplete.)



    CODING CONVENTIONS:
    1. Check out Douglas Crockford: http://javascript.crockford.com/code.html
    2. We're using JSDocs in a limited capacity for formatting.


    @exports app
    
    @requires jQuery
    @requires Doc
    @requires Router
    @requires LoadPageController
    @requires CreateGameController
    @requires DialogController
    @requires LoginController
    @requires ViewerContextModel
    @requires PageStateModel
*/
require(
[
    'jQuery',
    'view/document',
    'js/router',
    'controller/loadPage',
    'controller/createGame',
    'controller/dialog',
    'controller/login',
    'model/viewerContextModel',
    'model/pageStateModel'
],
function (
        $,
        Doc,
        Router,
        LoadPageController,
        CreateGameController,
        DialogController,
        LoginController,
        ViewerContextModel,
        PageStateModel) {


/**
    Initialize app functionality with default settings.
*/
function initializeApp() {
    // Setup application before DOM loads
    $.ajaxSetup({
        cache: false
    });
    
    // TODO remove facebook's #_=_ insertion that happens at login
    Router.initializeWithPushState();

    initializeControllers();

    // Run DOM dependent logic - Models and Views initialization
    $(document).ready(function () {
        var docView,
            pageStateModel,
            viewerContextModel;

        viewerContextModel = ViewerContextModel.retrieve();
        pageStateModel = PageStateModel.retrieve();
        
        docView = Doc.construct(
                viewerContextModel,
                pageStateModel);

        // initialize pushState in the DOM
        docView.initializePushStateDOM();
                
        // only load dialog after the User has access to the application.
        // FIXME rearchitect how lazy load should work.
        docView.lazyInitialize(viewerContextModel, pageStateModel);
    });
}

/**
    Initialize all controllers.
*/
function initializeControllers() {
    LoadPageController.controller.initialize();
    CreateGameController.controller.initialize();
    DialogController.controller.initialize();
    LoginController.controller.initialize();
}

/**
    Generic object utility functions.
    1. Object.create
*/
var initializeObject = (function () {
    // Adds a create function to every Object, making prototypal
    // inheritance easier.
    // See: http://javascript.crockford.com/prototypal.html
    if (typeof Object.create !== 'function') {
        Object.create = function (o) {
            function F() {}
            F.prototype = o;
            return new F();
        };
    }
}());

initializeApp();


});
