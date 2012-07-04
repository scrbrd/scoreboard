/**
    Represent the User's context - we're talking application logic, not
    View/Page State.

    These Models aren't using Prototypal inheritance to comply with Backbone.

    @exports SessionModel
    
    @requires Const
    @requires Backbone
*/
define(
        [
            "js/constants",
            "Backbone"
        ],
        function (Const, Backbone) {

/**
    Model to hold Session.
    @constructor
*/
var SessionModel = Backbone.Model.extend({
    
    /**
        Provide access to viewer's person id.
    */
    personID: function () {
        return this.get(Const.DATA.PERSON_ID);
    },

    /**
        Provide mutator for viewer's person id.
        @param {number} personID
    */
    setPersonID: function (personID) {
        this.setAttribute(Const.DATA.PERSON_ID, personID);
    },

    /**
        Provide access to viewer's rivals.
    */
    rivals: function () {
        return this.get(Const.DATA.RIVALS);
    },

    /**
        Provide mutator for viewer's rivals.
        @param {Array} rivals an Array of the viewer's Rivals.
    */
    setRivals: function (rivals) {
        this.setAttribute(Const.DATA.RIVALS, rivals);
    },

    // if it's the initial set then don't fire change event
    // FIXME is this needed. Look at pageStateModel
    setAttribute: function (key, value) {
        var silent = false;
        if (this.get(key) === null) {
            silent = true;
        }

        this.set(key, value, {silent: silent});
    }

});

var sessionModel = new SessionModel();
return {
    retrieve: function () {
        return sessionModel;
    }
};

});
