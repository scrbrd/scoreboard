""" Module: game

TODO: fill this in with required methods to implement since required
members aren't strictly members [they are pulled from properties].

"""

from exceptions import NotImplementedError
from itertools import groupby

from constants import API_NODE_TYPE, API_EDGE_TYPE
from constants import API_EDGE_PROPERTY, API_CONSTANT

from sqobject import SqNode
import loader
import editor


class Game(SqNode):

    """ Game is a subclass of SqObject for representing games. 

    Provide access to the attributes of a Game, including fields,
    relationships, and nearby nodes.

    A Game cannot exist without CREATED_BY and SCHEDULED_IN outgoing 
    SqEdges and either a WON_BY and one or more LOST_BY outgoing 
    SqEdges, two or more TIED_BY outgoing SqEdges, or one PLAYED_BY 
    outgoing SqEdge. In all cases, the incoming SqEdge complements 
    are also required.

    Optional:
    dict    _opponents     store loaded Opponents by id

    """

    _opponents = None


    @property
    def name(self):
        """ Games do not have names. Raise an error. """
        raise NotImplementedError("Game does not implement name property.")


    def outgoing_edge_types(self):
        """ Return a list of allowed outgoing SqEdge types. """
        return [
                API_EDGE_TYPE.SCHEDULED_IN,
                API_EDGE_TYPE.CREATED_BY,
                API_EDGE_TYPE.WON_BY,
                API_EDGE_TYPE.LOST_BY,
                API_EDGE_TYPE.TIED_BY,
                API_EDGE_TYPE.PLAYED_BY
                ]


    def creator_id(self):
        """  Return the Player who created the game. """
        return self.get_edges()[API_EDGE_TYPE.CREATED_BY].iterkeys().next()


    def outcome(self):
        """ Return a list of score, opponent_id pairs high to low.

        Return a list of results without result_type.
        [{"id": VALUE, "score": VALUE}]

        """

        outcome = []
 
        for edge_type in API_CONSTANT.RESULT_EDGE_TYPES:
            for edge in self.get_edges().get(edge_type, {}).values():
                score = edge._get_property(API_EDGE_PROPERTY.SCORE)
                opponent_id = edge.to_node_id
                outcome.append({"id": opponent_id, "score": score})
                outcome.sort(key = lambda x: x["score"], reverse=True)

        return outcome


    def get_opponent(self, opp_id):
        """ Return an Opponent by its id. """
        SqNode.assert_loaded(self._opponents)
        return self._opponents.get(opp_id, None)


    def get_opponents(self):
        """ Return a list of Opponents. """
        SqNode.assert_loaded(self._opponents)
        return self._opponents.values()
            
    
    def set_opponents(self, opponents):
        """ Set a Game's loaded Opponents from a dict. """
        self._opponents = opponents


    """ Static loader wrappers. """


    @staticmethod
    def load_opponents(game_id):
        """ Load the Game's Opponents and attributes into a Game.

        Required:
        int game_id     the id of the Game

        Return:
        Game            Game SqNode

        """
        
        (game, opponents) = loader.load_neighbors(
                game_id,
                API_CONSTANT.RESULT_EDGE_TYPES,
                API_CONSTANT.OPPONENT_NODE_TYPES)

        game.set_opponents(opponents)

        return game


    @staticmethod
    def multiload_opponents(game_ids):
        """ Load multiple Games' Opponents and attributes into a dict.

        Required:
        list game_ids   the ids of the Games

        Return:
        dict            Game SqNodes keyed on id

        """

        games = {}

        for id in game_ids:
            games[id] = Game.load_opponents(id)

        return games


    @staticmethod
    def calculate_outcome(game_score):
        """ Calculate Outcome from the Game Score

        Arguments:
        list    game_score      final score of a game
                                [{"id": VALUE, "score": VALUE}]

        If 0 Opponents: {}
        If 1 Opponent: PLAYED_BY
        If more Opponents: 
        WON_BY (highest score), LOST_BY, TIED_BY (even)

        Currently, the highest score wins.

        Return 
        Outcome
        {RESULT_EDGE_TYPE: [{"id": VALUE, "score": VALUE}]}

        """

        num_of_opponents = len(game_score)
        outcome = {}

        # if no opponents, then no results
        if num_of_opponents == 0:
            pass
        # if one opponent, then no win or loss
        elif num_of_opponents == 1:
            outcome[API_EDGE_TYPE.PLAYED_BY] = game_score
        
        # if two or more opponents, then calculate results
        else:
            # sort and group opponents by their scores
            opp_scores_by_score = Game._sort_and_group_opponents_by_score(
                    game_score)
           
            # TIE v WINNER/LOSERS
            num_of_results = len(opp_scores_by_score)
             
            # if 1 result, then the game was a tie
            if num_of_results == 1:
                outcome[API_EDGE_TYPE.TIED_BY] = game_score
           
            # if more results, then win is high score & the rest losses
            else:
                # winners
                winner_scores = opp_scores_by_score[0][1]
                outcome[API_EDGE_TYPE.WON_BY] = winner_scores
               
                # losers
                outcome[API_EDGE_TYPE.LOST_BY] = []
                for score, loser_scores in opp_scores_by_score[1:]:
                    outcome[API_EDGE_TYPE.LOST_BY].extend(loser_scores)
        return outcome


    @staticmethod
    def create_game(league_id, creator_id, game_score):
        """ Create a Game and return it.

        Required:
        id      league_id       league id that game belogs to
        id      creator_id      player id of game's creator
        list    game_score      final score of a game
                                [{"id": id1, "score": score1},
                                 {"id": id2, "score": score2},
                                 ...
                                 {"id": idN, "score": scoreN}]

        Return:
        Game                    newly created Game

        """
        
        # prepare a node prototype for this game
        prototype_node = editor.prototype_node(API_NODE_TYPE.GAME, {})

        prototype_edges = []

        # prepare edge prototypes for schedule edges
        prototype_edges.extend(editor.prototype_edge_and_complement(
                API_EDGE_TYPE.SCHEDULED_IN,
                {},
                league_id))

        # prepare edge prototypes for creator edges
        prototype_edges.extend(editor.prototype_edge_and_complement(
                API_EDGE_TYPE.CREATED_BY,
                {},
                creator_id))

        # get outcome from gamescore
        outcome = Game.calculate_outcome(game_score)

        # prepare edge prototypes for result edges
        for type, result in outcome.items():
            for opponent_score in result:
                prototype_edges.extend(editor.prototype_edge_and_complement(
                    type,
                    {API_EDGE_PROPERTY.SCORE: opponent_score["score"]},
                    opponent_score["id"]))

        return editor.create_node_and_edges(prototype_node, prototype_edges)
    
    @staticmethod
    def _sort_and_group_opponents_by_score(game_score):
        """ Sort and group opponents in game_score by score. 

        itertools.groupby requires a sorted list.

        Required:
        list    game_score      final score of a game
                                [{"id": VALUE, "score": VALUE}]

        Return a sorted list of scores with the relevant portion of the game
        score.
        [(score, [{"id": VALUE, "score": VALUE}])]

        """
        index_field = "score"

        # sort opponents by score  from high to low (needed for groupby)
        game_score.sort(key = lambda x:x[index_field], reverse=True)

        # group opponents by score
        opponent_scores_by_score = []
        for score, result_group in groupby(game_score, lambda x:x[index_field]):
            # get opponent score list for each score
            opponent_scores = [opp_score for opp_score in result_group]
            opponent_scores_by_score.append((score, opponent_scores))

        return opponent_scores_by_score

