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
        PLAYER_TAGGED:      "Player Tagged",
        REQUEST_LOGIN:      "Request Login",
        SIGN_UP:            "Sign Up",
        VIEW_PAGE:          "View Page"
    };


    /**
        Enum for all mixpanel properties. (lowercase.)
        @enum {string}
    */
    var PROPERTY = {
        CREATORS_RESULT:   "creator's result",
        DATA_TYPE:          "data type",
        INPUT:              "input", // user input
        IS_SCORED:          "is scored", // true if game has a score
        IS_SELF_TAG:        "is self tag", // is tagger and taggee the same
        LOGIN_TYPE:         "login type",
        NUMBER_OF_TAGS:     "number of tags", // number of tagged folks
        OBJECT_TYPE:        "object type",
        PAGE_NAME:          "page name", // specific name
        PAGE_TYPE:          "page type",
        PATH:               "path", // path to page
        TAGGER_ID:          "tagger id"
    };

    /**
        Enum for all special mixpanel properties.
        @enum {string}
    */
    var MIXPANEL_PROPERTY = {
        DISTINCT_ID:        "distinct_id" // identifier in events
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
            @param {string} isScored Does the object have a score?
            @param {string} creatorsResult The Result of the object's creator.
        */
        that.trackCreateObject = function (
                objectType,
                numberOfTags,
                isScored,
                creatorsResult) {
            var properties = {};
            properties[PROPERTY.OBJECT_TYPE] = objectType;
            properties[PROPERTY.NUMBER_OF_TAGS] = numberOfTags;
            properties[PROPERTY.IS_SCORED] = isScored;
            properties[PROPERTY.CREATORS_RESULT] = creatorsResult;
            // TODO move the game specific properties to the createGame
        
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
            properties[PROPERTY.PAGE_NAME] = pageName;

            that.track(properties);
        };

        return that;
    }());

    /**
        PLAYER_TAGGED event that inherits form mixPanelEvent.
        @constructor
    */
    var playerTagged = (function () {
        var that = Object.create(mixPanelEvent);

        that.mpEvent = EVENT.PLAYER_TAGGED;

        /**
            Track PLAYER_TAGGED event.
            @param {string} distinctID the id to make object player into the
                active user.
            @param {string} objectType object the player is tagged to.
            @param {string} taggerID id of the tagger.
            @param {boolean} isSelfTag True if the tagger and distinct ID are
                the same.
        */
        that.trackPlayerTagged = function (
                distinctID,
                objectType,
                taggerID,
                isSelfTag) {
            var properties = {};
            properties[MIXPANEL_PROPERTY.DISTINCT_ID] = distinctID;
            properties[PROPERTY.OBJECT_TYPE] = objectType;
            properties[PROPERTY.TAGGER_ID] = taggerID; // TODO: needed?
            properties[PROPERTY.IS_SELF_TAG] = isSelfTag;
            
            that.track(properties);
        };

        return that;
    }());

    /**
        SIGN_UP event that inherits from mixPanelEvent.
        @constructor
    */
    var signUp = (function () {
        var that = Object.create(mixPanelEvent);

        that.mpEvent = EVENT.SIGN_UP;

        that.LOGIN_TYPE = {
            FACEBOOK: "facebook"
        };

        /**
            Track SIGN_UP event.
            @param {string} loginTyoe The type of sign up.
        */
       that.trackSignUp = function (loginType) {
           var properties = {};
           properties[PROPERTY.LOGIN_TYPE] = loginType;

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

        that.LOGIN_TYPE = {
            FACEBOOK:        "facebook"
        };

        /**
            Track REQUEST_LOGIN event.
            @param {string} loginType The type of login request.
        */
        that.trackRequestLogin = function (loginType) {
            var properties = {};
            properties[PROPERTY.LOGIN_TYPE] = loginType;
            
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
        
        that.PAGE_TYPE = {
            TAB:        "tab",
            LANDING:    "landing",
            DIALOG:     "dialog"
        };

        that.mpEvent = EVENT.VIEW_PAGE;

        /**
            Track VIEW_PAGE event.
            @param {string} pageType The type of the viewed page.
            @param {string} pageName The name of the viewed page.
            @param {string} path The path (not URL) of the viewed page.
        */
        that.trackViewPage = function (pageType, pageName, path) {
            var properties = {};
            properties[PROPERTY.PAGE_TYPE] = pageType;
            properties[PROPERTY.PAGE_NAME] = pageName;
            properties[PROPERTY.PATH] = path;

            that.track(properties);
        };
        
        return that;
    }());
    
    
    return {
        createObject: createObject,
        enterData: enterData,
        playerTagged: playerTagged,
        requestLogin: requestLogin,
        signUp: signUp,
        viewPage: viewPage
    };
});
