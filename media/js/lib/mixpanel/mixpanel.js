/*
    Module: mixpanel
    Mixpanel tracks all page and event actions.

    Version:
        2?

    See:
        http://mixpanel.com 
*/
define(["js/constants", "order!lib/mixpanel/mixpanel-min"], function(Const) {

    // Constant: MIXPANEL_TOKEN
    // Sqoreboard's token from the mixpanel dashboard
    var MIXPANEL_TOKEN =  "21e3cfefb46bbded0d61eb0dca4bcec7";
   
    /*
        Namespace: EVENT
        All mixpanel events.
    
        Mixpanel event values are capitalized.
    */
    var EVENT = {
        // Constants: Mixpanel Events
        // VIEW_PAGE - any view page event.
        // CREATE_OBJECT - any object created.
        VIEW_PAGE:      "View Page", 
        CREATE_OBJECT:  "Create Object",
    }


    /*
        Namepspace: PROPERTY
        All mixpanel property parmaeters.
    
        Mixpanel properties are lowercase.
    */
    var PROPERTY = {
        // Constants: Mixpanel Property Parameters
        // TYPE - Subcategory of event
        // PATH - Path to specific page
        TYPE:           "type",
        NAME:           "name",
        PATH:           "path",
    }

    
    /*
        Namespace: PROPERTY_VALUE
        Values for Properties organized by EVENT and PROPERTY
    */
    var PROPERTY_VALUE = {};
    PROPERTY_VALUE[EVENT.VIEW_PAGE] = {};
    PROPERTY_VALUE[EVENT.VIEW_PAGE][PROPERTY.TYPE] = {
        TAB:            "tab",
        LANDING:        "landing",
        DIALOG:         "dialog",
    };


    /*
        Class: MixPanel
        Wrap around mixpanel functionality and provide event interface.
    */
    function MixPanel() {

        
        /*
            Function: trackViewPageByName
            Determine the type of View Page and track it.

            Parameters:
                name - specific name of tab page
                path - path to page
        */
        this.trackViewPageByName = function(name, path) {
            if (name == Const.PAGE_NAME.RANKINGS ||
                    name == Const.PAGE_NAME.GAMES) {
                this.trackTabViewPage(name, path);
            } else if (name == Const.PAGE_NAME.CREATE_GAME) {
                this.trackDialogViewPage(name, path);
            } else {
                this.trackLandingViewPage(name, path);
            }
        };


        /*
            Function: trackTabViewPage
            Track the Event VIEW_PAGE with Type TAB

            Parameters:
                name - specific name of tab page
                path - path to page
        */
        this.trackTabViewPage = function(name, path) {
            var type_val = PROPERTY_VALUE[EVENT.VIEW_PAGE][PROPERTY.TYPE].TAB;
            trackViewPage(type_val, name, path);
        }

    
        /*
            Function: trackLandingViewPage
            Track the Event VIEW_PAGE with Type LANDING

            Parameters:
                name - specific name of landing page
                path - path to page
        */
        this.trackLandingViewPage = function(name, path) {
            var type_val = PROPERTY_VALUE[EVENT.VIEW_PAGE][PROPERTY.TYPE].LANDING;
            trackViewPage(type_val, name, path);
        }

    
        /*
            Function: trackCreateDialogViewPage
            Track the Event VIEW_PAGE with Type CREATE_DIALOG

            Parameters:
                name - specific name of dialog
                path - path to page
        */
        this.trackDialogViewPage = function(name, path) {
            var type_val = PROPERTY_VALUE[EVENT.VIEW_PAGE][PROPERTY.TYPE].DIALOG;
            trackViewPage(type_val, name, path);
        }

    
        /*
            Function: initialize
            Setup mixpanel functionality.

            PRIVATE
        */
        function initialize() {
            mixpanel.init(MIXPANEL_TOKEN);
            mixpanel.set_config({
                debug: true,
            });
        }


        /* 
            Function: track
            Wrapper around mixpanel track event.

            PRIVATE

            Parameters:
                event - (string) Mixpanel Event.
                event_properties - (dict) Event properties.
        */
        function track(event, event_properties) {
            mixpanel.track(event, event_properties);
        };


        /* 
            Function: trackViewPage
            Track event type VIEW_PAGE.
           
            PRIVATE

            Parameters:
                type - a small selection of possible types
                name - a specific name for the page/dialog
                path - the path to the page
        */
        function trackViewPage(type, name, path) {
            var properties = {};
            properties[PROPERTY.TYPE] = type;
            properties[PROPERTY.NAME] = name;
            properties[PROPERTY.PATH] = path;
            
            track(EVENT.VIEW_PAGE, properties);
        };
        
        initialize();
    }

    var mp = new MixPanel();

    return mp;
});

