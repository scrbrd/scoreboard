/**
    A list of specific MixPanel events that define how we communicate with
    MixPanel.
    
    These events all have a subcategory called type that mixpanel.js can use
    to create a fairly granular framework of events for the application can
    call. This decoupling stops external users from creating new MixPanel
    events adhoc and disrupting the dataset.
    
    See Douglas Crockford's Prototypal Inheritance:
    http://javascript.crockford.com/prototypal.html

    event.js and mixpanel.js are the only modules that access the GLOBAL mixpanel.

    @exports MPEvent
    
    @return {Object} A set of mixPanelEvents with different track functions.

*/
define(
        [],
        function () {


    /**
        Enum for all mixpanel events. (Capitalized)
        @enum {string}
    */
    var EVENT = {
        CREATE_OBJECT:      "Create Object",
        ENTER_DATA:         "Enter Data",
        REQUEST_LOGIN:      "Request Login",
        VIEW_PAGE:          "View Page"
    };


    /**
        Enum for all mixpanel property parmaeters. (lowercase.)
        @enum {string}
        FIXME XXX make these more descriptive.
    */
    var PROPERTY = {
        DATA_TYPE:          "data type",
        NAME:               "name", // specific name
        NUMBER_OF_TAGS:     "number of tags", // number of tagged folks
        OBJECT_TYPE:        "object type",
        PATH:               "path", // path to page
        TYPE:               "type", // subcategory of event
        INPUT:              "input" // user input
    };
   

    /**
        MixPanel Event prototype object for specific events to subinstance.
        @constructor
    */
    var mixPanelEvent = (function () {
        var that = {};
       
        // Subinstance will have specific event constant.
        that.mpEvent =  null;

        /**
            Wrapper around mixpanel track event.
            @param {Object} eventProperties A dict for the event.
        */
        that.track = function (eventProperties) {
            mixpanel.track(this.mpEvent, eventProperties);
        };

        return that;
    }());
      
    
    /**
        CREATE_OBJECT event that inherits from mixPanelEvent.
        
        This generic event has properties for all object types.
        TODO - Consider if each Object should have its own event.
        @constructor
    */
    var createObject = (function () {
        var that = Object.create(mixPanelEvent);

        that.mpEvent = EVENT.CREATE_OBJECT;

        /**
            Track CREATE_OBJECT event.
            @param {string} objectType The type of object.
            @param {string} numberOfTags The number of folks tagged.
            @param {string} creatorsOutcome The Outcome of the object's creator.
            @param {string} wasScored Was the object given a Score.
        */
        that.trackCreateObject = function (
                objectType,
                numberOfTags,
                creatorsOutcome,
                wasScored) {
            var properties = {};
            properties[PROPERTY.TYPE] = objectType;
            properties[PROPERTY.NUMBER_OF_TAGS] = numberOfTags;
            // TODO: fill in creators_outcome and was_scored
            
            that.track(properties);
        };

        return that;
    }());


    /**
        ENTER_DATA event that inherits from mixPanelEvent.
        @constructor
    */
    var enterData = (function () {
        var that = Object.create(mixPanelEvent);

        that.mpEvent = EVENT.ENTER_DATA;

        /**
            Track ENTER_DATA event.
            @param {string} objectType The object that the data adds to.
            @param {string} dataType The type of inputted data.
            @param {string} inputValue The user inputted data.
            @param {string} pageName The page the user is on.
        */
        that.trackEnterData = function (
                objectType,
                dataType,
                inputValue,
                pageName) {
            var properties = {};
            properties[PROPERTY.OBJECT_TYPE] = objectType;
            properties[PROPERTY.DATA_TYPE] = dataType;
            properties[PROPERTY.INPUT] = inputValue;
            properties[PROPERTY.NAME] = pageName;

            that.track(properties);
        };

        return that;
    }());

    /**
        REQUEST_LOGIN event that inherits from mixPanelEvent.
        @constructor
    */
    var requestLogin = (function () {
        var that = Object.create(mixPanelEvent);

        that.mpEvent = EVENT.REQUEST_LOGIN;

        that.TYPE = {
            FACEBOOK:        "facebook"
        };

        /**
            Track REQUEST_LOGIN event.
            @param {string} loginType The type of login request.
        */
        that.trackRequestLogin = function (loginType) {
            var properties = {};
            properties[PROPERTY.TYPE] = loginType;
            
            that.track(properties);
        };

        return that;
    }());

    
    /**
        VIEW_PAGE event that inherits from mixPanelEvent.
        @constructor
    */
    var viewPage = (function () {
        var that = Object.create(mixPanelEvent);
        
        that.TYPE = {
            TAB:        "tab",
            LANDING:    "landing",
            DIALOG:     "dialog"
        };

        that.mpEvent = EVENT.VIEW_PAGE;

        /**
            Track VIEW_PAGE event.
            @param {string} type The type of the viewed page.
            @param {string} name The name of the viewed page.
            @param {string} path The path (not URL) of the viewed page.
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
    
    
    return {
        createObject: createObject,
        enterData: enterData,
        requestLogin: requestLogin,
        viewPage: viewPage
    };
});
