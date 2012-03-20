""" Module: game

...

"""

from itertools import groupby

from constants import API_CONSTANT, EDGE_TYPE, NODE_TYPE
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
    dict    _opponents     store loaded Opponents

    """

    _opponents = None


    def __init__(self, graph_node):
        """ Initialize Game class with attributes. """
        super(Game, self).__init__(graph_node)


    def outgoing_edge_types(self):
        """ Return a list of allowed outgoing SqEdge types. """
        return [
                EDGE_TYPE.SCHEDULED_IN,
                EDGE_TYPE.CREATED_BY,
                EDGE_TYPE.WON_BY,
                EDGE_TYPE.LOST_BY,
                EDGE_TYPE.TIED_BY,
                EDGE_TYPE.PLAYED_BY]


    def creator_id(self):
        """  Return the Player who created the game. """
        return self.get_edges()[EDGE_TYPE.CREATED_BY].iterkeys().next()


    @property
    def outcome(self):
        """ Return a dictionary - {opponent_id: score} """
        outcome_dict = {}

        for edge_type in API_CONSTANT.RESULT_TYPES:
            for edge in self.get_edges()[edge_type].values():
                outcome_dict[edge.to_node_id()] = edge.properties()["score"]

        return outcome_dict


    def get_opponents(self):
        """ Return a dict of Opponents. """
        return self.assert_loaded(self._opponents) if self._opponents else {}


    def set_opponents(self, opponents):
        """ Set a Game's loaded Opponents from a dict. """
        self._opponents = opponents


    @property
    def opponents(self):
        """ Return a dict of Opponents. """
        return self.get_opponents()


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
                API_CONSTANT.RESULT_TYPES, 
                API_CONSTANT.OPPONENT_TYPES)

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
    def calculate_outcome_from_scores(opponent_score_pairs):
        """ Convert opponents and scores to opponents by result. 

        Arguments:
        list opponent_score_pairs   tuples of opponent ids and scores

        If 0 Opponents: {}
        If 1 Opponent: "PLAYED_BY"
        If more Opponents: 
        WON_BY (highest score), LOST_BY, TIED_BY (even)

        Currently, the highest score wins.

        Return {RESULT: [(opponent_id, score)]

        """

        num_of_opponents = len(opponent_score_pairs)
        results = {}

        # if no opponents, then no results
        if num_of_opponents == 0:
            results = {}

        # if one opponent, then no win or loss
        elif num_of_opponents == 1:
            (id, score) = opponent_score_pairs[0]
            results = {EDGE_TYPE.PLAYED_BY: [(id, score)]}
        
        # if two or more opponents, then calculate results
        else:
            # sort opponents by score from high to low)
            opponent_score_pairs.sort(key = lambda x:x[1], reverse=True)

            # group opponents by their scores
            opps_by_score = Game._group_opponents_by_score(
                    opponent_score_pairs)
           
            
            # TIE v WINNER/LOSERS
            num_of_results = len(opps_by_score)
             
            # if 1 result, then the game was a tie
            if num_of_results == 1:
                (tied_score, tied_ids) = opps_by_score[0]
                tied_result = []
                for id in tied_ids:
                    tied_result.append((id, tied_score))
                results[EDGE_TYPE.TIED_BY] = tied_result
           
            # if more results, then win is high score & the rest losses
            else:
                # winners
                (winner_score, winner_ids) = opps_by_score[0]
                winner_result = []
                for id in winner_ids:
                    winner_result.append((id, winner_score))
                results[EDGE_TYPE.WON_BY] = winner_result
               
                # losers
                loser_result = []
                for loser_score, loser_ids in opps_by_score[1:]:
                    for id in loser_ids:
                        loser_result.append((id, loser_score))
                results[EDGE_TYPE.LOST_BY] = loser_result
        return results


    @staticmethod
    def create_game(league_id, creator_id, opponent_score_pairs):
        """ Create a Game and return it.

        Required:
        id      league_id               league id that game belogs to
        id      creator_id              player id of game's creator
        list    opponent_score_pairs    tuples of opponent ids and score

        Return the created game.

        """
        
        # prepare a node prototype for this game
        prototype_node = editor.prototype_node(NODE_TYPE.GAME, {})

        prototype_edges = []

        # prepare edge prototypes for schedule edges
        prototype_edges.extend(editor.prototype_edge_and_complement(
                EDGE_TYPE.SCHEDULED_IN,
                {},
                league_id))

        # prepare edge prototypes for creator edges
        prototype_edges.extend(editor.prototype_edge_and_complement(
                EDGE_TYPE.CREATED_BY,
                {},
                creator_id))

        # get outcome from opponent score pairs
        outcome = Game.calculate_outcome_from_scores(opponent_score_pairs)

        # prepare edge prototypes for result edges
        for type, result in outcome.items():
            for opponent_id, score in result:
                prototype_edges.extend(editor.prototype_edge_and_complement(
                    type,
                    {"score": score},
                    opponent_id))

        return editor.create_node_and_edges(prototype_node, prototype_edges)
    
    @staticmethod
    def _group_opponents_by_score(opponent_score_pairs):
        """ Group opponents by score. 

        Required:
        list opponent_score_pairs  tuples of ids and scores

        Return (score, [opponent_ids])

        """
        # FIXME make this function more readable
        opps_by_score = [(score, [o for o,v in val]) for score, val in
                    groupby(opponent_score_pairs, lambda x:x[1])]
        return opps_by_score

