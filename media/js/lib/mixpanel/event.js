/*
    Module: event
    All Mixpanel events are specified here.

    Dependencies:
       constants
       
    Global:
        mixpanel
*/
define(["js/constants"], function (Const) {

    // TODO: put this Object.create method in a util package
    /*
        Function: Object.create
        Adds a create function to every Object, making prototypal inheritance
        easier.
        
        See:
            http://javascript.crockford.com/prototypal.html
    */
    if (typeof Object.create !== 'function') {
        Object.create = function (o) {
            function F() {}
            F.prototype = o;
            return new F();
        };
    }
    
    
    /*
        Class: EVENT
        All mixpanel events.
    
        Mixpanel event values are capitalized.
    */
    var EVENT = {
        // Constants: Mixpanel Events
        // VIEW_PAGE - any view page event.
        // CREATE_OBJECT - any object created.
        VIEW_PAGE:      "View Page", 
        CREATE_OBJECT:  "Create Object",
    };


    /*
        Class: PROPERTY
        All mixpanel property parmaeters.
    
        Mixpanel properties are lowercase.
    */
    var PROPERTY = {
        // Constants: Mixpanel Property Parameters
        // TYPE - Subcategory of event
        // NAME - the specific name 
        // PATH - Path to specific page
        // NUMBER_OF_TAGS - number of folks tagged in an object
        TYPE:               "type",
        NAME:               "name",
        PATH:               "path",
        NUMBER_OF_TAGS:     "number of tags"
    };
    
    
    /*
        Object: MixPanelEvent
        Prototype object for specific Mix Panels events to subclass.
    */
    var mixPanelEvent = (function () {
        var that = {};
        
        // Variable: mpEvent
        // (string) the selector for the mixpanel event.
        that.mpEvent =  null;

        /* 
            Function: track
            Wrapper around mixpanel track event.

            Parameters:
                eventProperties - (dict) Event properties.
        */
        that.track = function (eventProperties) {
            mixpanel.track(this.mpEvent, eventProperties);
        };

        return that;
    }());


    /*
        Object: viewPage 
        A Singleton for tracking VIEW_PAGE.

        Subclass from mixPanelEvent.
    */
    var viewPage = (function () {
        // viewPage inherits from mixPanelEvent
        var that = Object.create(mixPanelEvent); 
        
        // Class: TYPE
        // The page type of the VIEW_PAGE event.
        // TODO: make this part of the presentation model
        // e.g., pages should know what type they are (like PAGE_NAME)
        that.TYPE = {
            /*
                Constants: Page Types
                TAB - a tab page is a view for a logged in user
                LANDING - a landing page is the initial marketing page
                DIALOG - a dialog page is an interface for user response
            */
            TAB:        "tab",
            LANDING:    "landing",
            DIALOG:     "dialog",
        };

        that.mpEvent = EVENT.VIEW_PAGE;


        /* 
            Function: trackViewPage
            Track event type VIEW_PAGE.
         
            Parameters:
                type - a small selection of possible types
                name - a specific name for the page/dialog
                path - the path to the page
        */
        that.trackViewPage = function (type, name, path) {
            var properties = {};
            properties[PROPERTY.TYPE] = type;
            properties[PROPERTY.NAME] = name;
            properties[PROPERTY.PATH] = path;

            that.track(properties);
        };
        
        return that;
    }());
      
    
    /*
        Object: createObject 
        A Singleton for tracking CREATE_OBJECT
    */
    var createObject = (function () {
        // createObject inherits from mixPanelEvent
        var that = Object.create(mixPanelEvent); 

        that.mpEvent = EVENT.CREATE_OBJECT;


        /*
            Function: trackCreateObject
            Track event type CREATE_OBJECT

            Parameters:
                type - (string) the type of object being created
                numer_of_tags - (int) number of players tagged
                creators_outcome - (string) the player WON, LOST, or TIED
                was_scored - (boolean) if a score was attached to the game
        */
        that.trackCreateObject = function (
                type, 
                number_of_tags, 
                creators_outcome, 
                was_scored) {
            var properties = {};
            properties[PROPERTY.TYPE] = type;
            properties[PROPERTY.NUMBER_OF_TAGS] = number_of_tags;
            // TODO: fill in creators_outcome and was_scored
            
            that.track(properties);
        };

        return that;
    }());

    return {
        viewPage: viewPage, 
        createObject: createObject,
    };


});
