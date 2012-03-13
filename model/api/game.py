""" Module: game

...

"""

from itertools import groupby

from constants import API_CONSTANT, EDGE_TYPE, NODE_TYPE
from sqobject import SqNode
import loader


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
        
        return loader.load_neighbors(
                game_id, 
                API_CONSTANT.RESULT_TYPES, 
                API_CONSTANT.OPPONENT_TYPES)


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
            games[id] = load_opponents(id)

        return games


    @staticmethod
    def calculate_outcome_from_scores(opponent_score_pairs):
        """ Convert opponents and scores to opponents by result. 

        Arguments:
        list opponent_score_pairs   a list of opponents and scores

        If 0 Opponents: {}
        If 1 Opponent: "PLAYED_BY"
        If more Opponents: 
        WON_BY (highest score), LOST_BY, TIED_BY (even)

        Currently, the highest score wins.

        Return {"result": [(score, Opponents)]}

        TODO - change RETURN type {RESULT: [(opponent_id, score)]

        """

        num_of_opponents = len(opponent_score_pairs)
        results_with_opponents_dict = {}

        # if no opponents, then no results
        if num_of_opponents == 0:
            results_with_opponents_dict = {}
        # if one opponent, then no win or loss
        elif num_of_opponents == 1:
            results_with_opponents_dict = {
                    EDGE_TYPE.PLAYED_BY: [(
                        opponent_score_pairs[0][1],
                        opponent_score_pairs[0][0])]}
        # if two or more opponents, then calculate results
        else:
            # opponent lists grouped by score (high to low)
            opponent_score_pairs.sort(key = lambda x:x[1], reverse=True)
            opps_by_score = [(score, [o for o,v in val]) for score, val in
                    groupby(opponent_score_pairs, lambda x:x[1])]

            num_of_results = len(opps_by_score)
            # if 1 result, then the game was a tie
            if num_of_results == 1:
                results_with_opponents_dict = {
                        EDGE_TYPE.TIED_BY: [(
                            opps_by_score[0][0],
                            opps_by_score[0][1])]}
            else:
                # otherwise, win is highest score
                results_with_opponents_dict = {
                        EDGE_TYPE.WON_BY: [(
                            opps_by_score[0][0],
                            opps_by_score[0][1])]}
                # and loss is all the other scores
                losers = []
                for t in opps_by_score[1:]:
                    losers.append((t[0], t[1]))
                results_with_opponents_dict[EDGE_TYPE.LOST_BY] = losers
        return results_with_opponents_dict


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

