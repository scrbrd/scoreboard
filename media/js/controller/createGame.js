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
        Handle creating Game form to server processing and submission.
        @param {Object} sessionModel
        @param {Object} rawGame raw Game parameters: tags, metrics, etc.
    */
    that.handleSubmit = function (sessionModel, rawGame) {
        var game = prepareGameForSubmit(rawGame);

        Crud.createGame(game, function (response) {
            // TODO - update Page State here too.
            EventDispatcher.trigger(
                Event.SERVER.CREATED_GAME,
                sessionModel.personID(),
                game);
        });

        Doc.retrieve().hideDialog();
    };
    
    /**
        Respond to successful Game creation on the server.
        @param {number} creatorID User's person id.
        @param {Object} game processed Game.
    */
    that.handleSuccess = function (creatorID, game) {
        MP.trackCreateGame(
            countTagsInGame(game),
            isGameScored(game),
            getResultForCreator(creatorID, game));

        var metrics = game[Const.DATA.OPPONENT_METRICS];

        var opponentID;
        for (opponentID in metrics) {
            if (metrics.hasOwnProperty(opponentID)) {
                MP.trackPlayerTaggedToGame(
                    opponentID.toString(),
                    creatorID.toString(),
                    (opponentID === creatorID));
            }
        }

        // FIXME trigger RELOAD_PAGE event should accomplish this too.
        Doc.retrieve().refresh();
    };

    /**
        Process a raw game object into a Game prepared to send to the server.

        rawGame = {
             "league-id":        <LEAGUE_ID>,
             "creator-id":       <CREATOR_ID>,
             "opponent-metrics": {
                 0: {<EDGE_TYPE0>: <OPPONENT_ID0>},
                 1: {<EDGE_TYPE1>: <OPPONENT_ID1>},
                 }
             }
        game = {
             "leagueID":        <LEAGUE_ID>,
             "creatorID":       <CREATOR_ID>,
             "opponentMetrics": {
                 <OPPONENT_ID0>: {"result": <EDGE_TYPE0>, "score": <#0>},
                 <OPPONENT_ID1>: {"result": <EDGE_TYPE1>, "score": <#1>}
                 }
             }

        @param {Object} rawGame
        @return {Obejct} The altered game parameters.
    */
    function prepareGameForSubmit(rawGame) {
        var rawMetrics = rawGame[Const.DATA.METRICS_BY_OPPONENT];

        var metrics = {};

        var i;
        for (i = 0; i < rawMetrics.length; i += 1) {

            var metric;
            for (metric in rawMetrics[i]) {

                if (rawMetrics[i].hasOwnProperty(metric)) {

                    // TODO: the only value type right now is RESULT, but
                    // when others exist, we won't know which type this is.

                    var opponentID = rawMetrics[i][metric];
                    var result = Const.DATA.RESULT;

                    metrics[opponentID] = {
                        result: metric
                    };
                }
            }
        }

        rawGame[Const.DATA.METRICS_BY_OPPONENT] = metrics;

        return rawGame;
    }

    /**
        Count the number of tags in the newly created Game.
        @param {Object} game processed Game.
        @return {number} number of tags in a new Game.
    */
    function countTagsInGame(game) {
        return game[Const.DATA.METRICS_BY_OPPONENT].length;
    }

    /**
        Is the newly created Game scored?
        @param {Object} game processed Game.
        @return {boolean} does the new Game have a score?
    */
    function isGameScored(game) {
        var metrics = game[Const.DATA.METRICS_BY_OPPONENT];

        var opponentID;
        for (opponentID in metrics) {
            if (metrics.hasOwnProperty(opponentID)) {
                return (metrics[opponentID].hasOwnProperty(Const.DATA.SCORE));
            }
        }

        return false;
    }

    /**
        Is the creator tagging him/herself in the newly created Game?
        @param {Object} game processed Game.
        @return {boolean} does the new Game have a score?
    */
    function isCreatorTagged(creatorID, game) {
        var metrics = game[Const.DATA.METRICS_BY_OPPONENT];
        return metrics.hasOwnProperty(creatorID);
    }

    /**
        Process game score and determine if game creator WON or LOST.
        TODO: make this more intelligent. it just responds to a 1 in score.
        @param {number} creatorID Game creator ID
        @param {Object} game processed Game
    */
    function getResultForCreator(creatorID, game) {
        var metrics = game[Const.DATA.METRICS_BY_OPPONENT];

        var result = "";
        if (metrics.hasOwnProperty(creatorID)) {
            result = metrics[creatorID][Const.DATA.RESULT];
        }

        return result;
    }

    return that;
}());

return {
    controller: createGameController
};


});
