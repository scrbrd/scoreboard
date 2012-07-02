/**
    Handle events that relate to the game creation workflow.

    CreateGameController.controller inherits from BaseController.controller.

    @exports CreateGameController

    @requires MP
    @requires Const
    @requires Event
    @requires BaseController
    @requires Crud
    @requires Doc
*/
define(
        [
            "MP",
            "js/constants",
            "js/event",
            "controller/base",
            "js/crud",
            "view/document"
        ],
        function (MP, Const, Event, BaseController, Crud, Doc) {


/**
    Controller instance for creating a game on the server.
    @constructor
*/
var createGameController = (function () {
    var that = Object.create(BaseController.controller);

    /**
        Bind CREATE_GAME and CREATED_GAME events.
    */
    that.initialize = function () {
        var events = {};

        events[Event.CLIENT.CREATE_GAME] = that.handleSubmit;
        events[Event.SERVER.CREATED_GAME] = that.handleSuccess;
        that.initializeEvents(events);
    };

    /**
        Handle creating game form to server processing and submission.
        @param {Object} gameParams All the Game parameters:
            tags, scores, etc.
    */
    that.handleSubmit = function (gameParams) {
        var docView = Doc.retrieve();
        
        // process game data to prepare it for the server.
        gameParams = readyGameForSubmit(gameParams);
        Crud.createGame(gameParams);
        docView.hideDialog();
    };
    
    /**
        Respond to successfull game creation on the server.
        @param {number} numberOfTags number of tagged players
    */
    that.handleSuccess = function (numberOfTags) {
        var docView = Doc.retrieve();
        
        MP.trackCreateGame(
                numberOfTags,
                null,
                null);
        // refresh the Docview with by grabbing new data
        // FIXME trigger RELOAD_PAGE event should accomplish this too.
        docView.refresh();
    };

    /**
        Process and alter Game parameters to ready them for the server.
        @param {Object} gameParams
        @return {Obejct} The altered game parameters.
    */
    function readyGameForSubmit(gameParams) {
        // each player need to have a game score but the checkbox
        // excludes losses, so add them in on that condition.
        var gamescore = gameParams[Const.DATA.GAME_SCORE];
        var i;
        var player;
        for (i = 0; i < gamescore.length; i += 1) {
            player = gamescore[i];
            if (!player.hasOwnProperty(Const.DATA.SCORE)) {
                player[Const.DATA.SCORE] = 0;
            }
        }

        return gameParams;
    }
    return that;
}());

return {
    controller: createGameController
};


});
