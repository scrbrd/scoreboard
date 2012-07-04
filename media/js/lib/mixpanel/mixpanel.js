/**
    Defines the entire MixPanel API that the application can access.

    These events are actually a combination of EVENT and TYPE that we
    use to let an admin see a limited number of events on the surface but also
    break down those events into useful types. By giving each EVENT a
    TYPE we will create a standard that will make it easy for an unfamiliar
    admin to view statistics.

    MixPanel Version: 2?
    See MixPanel: http://mixpanel.com

    event.js and mixpanel.js are the only modules that access the GLOBAL mixpanel.

    @exports MP

    @requires Const
    @requires MPEvent
    @requires mixpanel (non-AMD)

    @return {Object} A set of functions that define the MP API. This decoupling
        stops folks from creating adhoc MP Events, as external users cannot
        call the internal Event objects' track function directly.
*/
define(
        [
            "js/constants",
            "lib/mixpanel/event",
            "order!lib/mixpanel/mixpanel-min"
        ],
        function (Const, MPEvent) {


// Imports
var createObject = MPEvent.createObject;
var enterData = MPEvent.enterData;
var requestLogin = MPEvent.requestLogin;
var viewPage = MPEvent.viewPage;
var GAME = Const.API_OBJECT.GAME;

/**
    Sqoreboard's token from the mixpanel dashboard.
*/
var MIXPANEL_TOKEN =  "21e3cfefb46bbded0d61eb0dca4bcec7";

/**
    Setup mixpanel functionality.
*/
var initializeMixPanel = (function () {
    mixpanel.init(MIXPANEL_TOKEN);
    mixpanel.set_config({
        debug: true // adds a bunch of console.log output
    });
}());

return {
    /**
        Identify the User based on Person ID using Mixpanls' identify.
        @param {string} id The User's Person ID
    */
    identifyUser: function (id) {
        mixpanel.identify(id);
        // insert id as name
        mixpanel.name_tag(id);
        // FIXME remove this property but allow to set elsewhere
        mixpanel.register({"gender": "male"});
    },

    /**
        Track a successfully added Game by wrapping the "Create Object"
        event.
        @param {number} numberOfTags The number of tagged folks.
        @param {boolean} wasScored True if the game was scored.
        @param {string} creatorsOutcome The result of the game's creator.
            (e.g. WON, LOST)
    */
    trackCreateGame: function (numberOfTags, wasScored, creatorsOutcome) {
        createObject.trackCreateObject(
                GAME,
                numberOfTags,
                wasScored,
                creatorsOutcome);
    },

    /**
        Track data entered by the user to construct a game.
        @param {string} dataType The type of inputted data.
        @param {string} inputValue The inputted data.
        @param {string} pageName The page the user is on.
    */
    trackEnterDataForGame: function (dataType, inputValue, pageName) {
        enterData.trackEnterData(
                GAME,
                dataType,
                inputValue,
                pageName);
    },

    /**
        Track a facebook login request by wrapping the "Request Login"
        event.
    */
    trackRequestFacebookLogin: function () {
        requestLogin.trackRequestLogin(requestLogin.TYPE.FACEBOOK);
    },
    
    /**
        Track a landing view by wrapping the "View Page" event.
        @param {string} name The name of the page (e.g., "landing").
        @param {string} path The path to the page (e.g., "/").
    */
    trackViewLanding: function (name, path) {
        viewPage.trackViewPage(viewPage.TYPE.LANDING, name, path);
    },
    
    /**
        Track a dialog view by wrapping the "View Page" event.
        @param {string} name The name of the page (e.g., "create_game").
        @param {string} path The path to the page (e.g., "/rankings").
    */
    trackViewDialog: function (name, path) {
        viewPage.trackViewPage(viewPage.TYPE.DIALOG, name, path);
    },

    /**
        Track a tab view by wrapping the "View Page" event.
        @param {string} name The name of the page (e.g., "games").
        @param {string} path The path to the page (e.g., "/games").
    */
    trackViewTab: function (name, path) {
        viewPage.trackViewPage(viewPage.TYPE.TAB, name, path);
    }
};


});
