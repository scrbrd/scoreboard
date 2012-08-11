/**
    Handle events that relate to the comment creation workflow.

    CreateCommentController.controller inherits fropm BaseController.controller.

    @exports CreateCommentController

    @requires MP
    @requires Const
    @requires Event
    @requires EventDispatcher
    @requires BaseController
    @requires Crud
    @requires Doc
*/
define(
        [
            "MP",
            "js/constants",
            "js/event",
            "js/eventDispatcher",
            "controller/base",
            "js/crud",
            "view/document"
        ],
        function (MP, Const, Event, EventDispatcher, BaseController, Crud, Doc) {


/**
    Controller instance for creating a comment on the server.
    @constructor
*/
var createCommentController = (function () {
    var that = Object.create(BaseController.controller);

    /**
        Bind CREATE_COMMENT and COMMENT_CREATED events.
    */
    that.initialize = function () {
        var events = {};

        events[Event.CLIENT.CREATE_COMMENT] = that.handleSubmit;
        events[Event.SERVER.CREATED_COMMENT] = that.handleSuccess;

        that.initializeEvents(events);
    };

    /**
        Handle creating Comment form to server processing and submission.
        @param {Object} sessionModel
        @param {Object} rawComment raw Comment parameters: game_id, message
    */
    that.handleSubmit = function (sessionModel, rawComment) {
        console.log("in handleSubmit");
        var comment = rawComment; // no preparation needed

        Crud.createComment(comment, function (response) {
            // TODO - update Page State here too.
            EventDispatcher.trigger(
                Event.SERVER.CREATED_COMMENT,
                sessionModel.personID(),
                comment);
        });
    };

    /**
        Respond to successful Comment creation on the server.
        @param {number} commenterID User's person id.
        @param {Object} comment processed Comment.
    */
    that.handleSuccess = function (commenterID, comment) {
        // TODO: add MixPanel stuff here

        // FIXME trigger RELOAD_PAGE event should accomplish this too.
        Doc.retrieve().refresh();
    };

    return that;
}());

return {
    controller: createCommentController
};


});
