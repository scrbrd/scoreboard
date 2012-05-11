/*
    Module: mixpanel
    Mixpanel tracks all page and event actions.

    Version:
        2?

    See:
        http://mixpanel.com 

    Dependencies:
        constants
        event
*/
define(
    [
        "js/constants", 
        "lib/mixpanel/event", 
        "order!lib/mixpanel/mixpanel-min",
    ], function (Const, Event) {

    // Constant: MIXPANEL_TOKEN
    // Sqoreboard's token from the mixpanel dashboard
    var MIXPANEL_TOKEN =  "21e3cfefb46bbded0d61eb0dca4bcec7";

    /*
        Function: initializeMixPanel
        Setup mixpanel functionality.
    */
    var initializeMixPanel = (function () {
        mixpanel.init(MIXPANEL_TOKEN);
        mixpanel.set_config({
            debug: true,
        });

    }());

    return {
        /*
            Function: trackViewTab
            Track the Event VIEW_PAGE with Type TAB

            Parameters:
                name - specific name of tab page
                path - path to page
        */
        trackViewTab: function (name, path) {
            Event.viewPage.trackViewPage(
                    Event.viewPage.TYPE.TAB, 
                    name, 
                    path);
        },


        /*
            Function: trackViewLanding
            Track the Event VIEW_PAGE with Type LANDING

            Parameters:
                name - specific name of landing page
                path - path to page
        */
        trackViewLanding: function (name, path) {
            Event.viewPage.trackViewPage(
                    Event.viewPage.TYPE.LANDING, 
                    name, 
                    path);
        },
        
        
        /*
            Function: trackViewDialog
            Track the Event VIEW_PAGE with Type DIALOG

            Parameters:
                name - specific name of dialog
                path - path to page
        */
        trackViewDialog: function (name, path) {
            Event.viewPage.trackViewPage(
                    Event.viewPage.TYPE.DIALOG, 
                    name, 
                    path);
        },


        /*
            Function: trackCreateGame
            Track the Event CREATE_OBJECT with Type GAME

            Parameters:
                name - specific name of dialog
                path - path to page
        */
        trackCreateGame: function (
                number_of_tags, 
                creators_outcome, 
                was_scored) {
            Event.createObject.trackCreateObject(
                    Const.API_OBJECT.GAME,
                    number_of_tags,
                    creators_outcome,
                    was_scored);
        },

    };
});

