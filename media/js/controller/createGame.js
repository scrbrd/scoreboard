/**
    Handle events that relate to the game creation workflow.

    CreateGameController.controller inherits from BaseController.controller.

    @exports CreateGameController

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
        @param {Object} sessionModel
        @param {Object} gameParams All the Game parameters:
            tags, scores, etc.
    */
    that.handleSubmit = function (sessionModel, gameParams) {
        var docView = Doc.retrieve();
        var creatorID = sessionModel.personID();

        // process game data to prepare it for the server.
        gameParams = readyGameParamsForSubmit(gameParams);


        Crud.createGame(gameParams, function (response) {
            // TODO - update Page State here too.
            EventDispatcher.trigger(
                Event.SERVER.CREATED_GAME,
                creatorID,
                gameParams);
        });
        docView.hideDialog();
    };
    
    /**
        Respond to successfull game creation on the server.
        @param {number} creatorID User's person id.
        @param {Object} gameParams game parameters.
    */
    that.handleSuccess = function (
            creatorID,
            gameParams) {

        // set number of tags for MP Create Game event.
        var numberOfTags = 0;
        if (gameParams.hasOwnProperty(Const.DATA.GAME_SCORE)) {
            numberOfTags = gameParams[Const.DATA.GAME_SCORE].length;
        }
    
        // currently there are only W/L/T and no score.
        var isScored = false;
        
        // currently we compute on the server so don't think about creator
        // result.
        var creatorsResult = getCreatorsResult(creatorID, gameParams);
        
        MP.trackCreateGame(
                numberOfTags,
                isScored,
                creatorsResult);

        // go through the tags and create a Player Tagged event for each one.
        var gamescore = gameParams[Const.DATA.GAME_SCORE];
        var i;
        var taggedPlayerID;
        var isSelfTag = false;
        for (i = 0; i < gamescore.length; i += 1) {
            taggedPlayerID = gamescore[i][Const.DATA.ID];
            if (taggedPlayerID === creatorID) {
                isSelfTag = true;
            }
            MP.trackPlayerTaggedToGame(
                    taggedPlayerID.toString(),
                    creatorID.toString(),
                    isSelfTag);
        }

        // refresh the Docview with by grabbing new data
        // FIXME trigger RELOAD_PAGE event should accomplish this too.
        var docView = Doc.retrieve();
        docView.refresh();
    };

    /**
        Process and alter Game parameters to ready them for the server.
        @param {Object} gameParams
        @return {Obejct} The altered game parameters.
    */
    function readyGameParamsForSubmit(gameParams) {
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

    /**
        Process game score and determine if game creator WON or LOST.
        TODO: make this more intelligent. it just responds to a 1 in score.
        @param {number} creatorID
        @param {Object} gameParameters
    */
    function getCreatorsResult(creatorID, gameParameters) {
       var gamescore = gameParameters[Const.DATA.GAME_SCORE];
       // TODO add this to constants if still needed
       var LOST = "lost";
       var WON = "won";
       var i;
       var playerID;
       for (i = 0; i < gamescore.length; i += 1) {
           playerID = gamescore[i][Const.DATA.ID];
           if (playerID === creatorID) {
                if (gamescore[i][Const.DATA.SCORE] === 1) {
                    return WON;
                }
           }
       }
       return LOST;

    }

    return that;
}());

return {
    controller: createGameController
};


});
