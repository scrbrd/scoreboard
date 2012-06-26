/**
    Defines the entire MixPanel API that the application can access.

    These events are actually a combination of EVENT and TYPE that we 
    use to let an admin see a limited number of events on the surface but also
    break down those events into useful types. By giving each EVENT a 
    TYPE we will create a standard that will make it easy for an unfamiliar
    admin to view statistics.

    MixPanel Version: 2?
    See MixPanel: http://mixpanel.com 

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
            "order!lib/mixpanel/mixpanel-min",
        ], 
        function (Const, MPEvent) {
    // Imports
    var createObject = MPEvent.createObject;
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
            debug: true, // adds a bunch of console.log output
        });
    }());

    return {
        /**
            Track a successfully added Game by wrapping the "Create Object" 
            event.
            @param {number} numberOfTags The number of tagged folks. 
            @param {string} creatorsOutcome The result of the game's creator.
                (e.g. WIN, LOSS)
            @param {boolean} wasScored True if the game was scored.
        */
        trackCreateGame: function (numberOfTags, creatorsOutcome, wasScored) {
            createObject.trackCreateObject(
                    GAME,
                    numberOfTags,
                    creatorsOutcome,
                    wasScored);
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
        },
    };
});

