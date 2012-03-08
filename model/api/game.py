""" Module: game

...

"""

from itertools import groupby

from model.const import CONST, EDGE_TYPE, NODE_TYPE
from sqobject import SqNode
import loader


class Game(SqNode):

    """ Game is a subclass of SqObject for representing games. 

    Provide access to the attributes of a Game, including fields,
    relationships, and nearby nodes.

    Required:
    int _id             super class requirement 

    Edges Dict: 
    EDGE_TYPE.WON_BY: [(opponent_ids, score)]
    EDGE_TYPE.LOST_BY: [(opponent_ids, score)]
    EDGE_TYPE.TIED_BY: [(opponent_ids, score)]
    EDGE_TYPE.PLAYED_BY: [(opponent_ids, score)]
    EDGE_TYPE.CREATED_BY: player_id ***REQUIRED***
    EDGE_TYPE.SCHEDULED_IN: league_id ***REQUIRED***

    dict _opponents     store loaded Opponents

    TODO - remove complements
    dict _complements   store bi-directional edge complements

    """

    _opponents = None
    _complements = {
            EDGE_TYPE.WON_BY: EDGE_TYPE.WON,
            EDGE_TYPE.LOST_BY: EDGE_TYPE.LOST,
            EDGE_TYPE.TIED_BY: EDGE_TYPE.TIED,
            EDGE_TYPE.PLAYED_BY: EDGE_TYPE.PLAYED,
            EDGE_TYPE.CREATED_BY: EDGE_TYPE.CREATED,
            EDGE_TYPE.SCHEDULED_IN: EDGE_TYPE.HAS_SCHEDULED}


    def __init__(self, graph_node):
        """ Initialize Game class with attributes. """
        super(Game, self).__init__(graph_node)


    def creator_id(self):
        """  Return the Player who created the game. """
        return self.edges()[EDGE_TYPE.CREATED_BY].iterkeys().next()


    @property
    def outcome(self):
        """ Return a dictionary - {opponent_id: score} """
        outcome_dict = {}
        results_list = CONST.RESULT_TYPES
        for r in results_list:
            for i, s in self._edge_ids_dict[r]:
                outcome_dict[i] = s
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
                CONST.RESULT_TYPES, 
                CONST.OPPONENT_TYPES)


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
            results_with_opponents_dict = {EDGE_TYPE.PLAYED_BY: 
                    [(opponent_score_pairs[0][1], opponent_score_pairs[0][0])]}
        # if two or more opponents, then calculate results
        else:
            # opponent lists grouped by score (high to low)
            opponent_score_pairs.sort(key = lambda x:x[1], reverse=True)
            opps_by_score = [(score, [o for o,v in val]) for score, val in
                    groupby(opponent_score_pairs, lambda x:x[1])]

            num_of_results = len(opps_by_score)
            # if 1 result, then the game was a tie
            if num_of_results == 1:
                results_with_opponents_dict = {EDGE_TYPE.TIED_BY: [(opps_by_score[0][0],
                    opps_by_score[0][1])]}
            else:
                # otherwise, win is highest score
                results_with_opponents_dict = {EDGE_TYPE.WON_BY: [(opps_by_score[0][0], 
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
        id league_id                league id that game belogs to
        id creator_id               player id of game's creator
        list opponent_score_pairs   tuples of opponent ids and score

        Return the created game.

        """
        # get outcome from opponent score pairs
        outcome = Game.calculate_outcome_from_scores(opponent_score_pairs)
        
        # create nodes
        properties = {}

        # create edges
        # TODO turn pairs into bi-directional edges
        edges = []

        type = EDGE_TYPE.SCHEDULED_IN
        edges.append({"to_id": league_id, "type": type})
        edges.append({"from_id": league_id, "type": _complements[type]})

        type = EDGE_TYPE.CREATED_BY
        edges.append({"to_id": creator_id, "type": type})
        edges.append({"from_id": creator_id, "type": _complements[type]})

        for type, vals in outcome:
            for o, s in vals:
                properties = {"score": s}
                edges.append({
                    "to_id": o, 
                    "type": type, 
                    "properties": properties})
                edges.append({
                    "from_id": o, 
                    "type": _complements[type], 
                    "properties": properties})

        return editor.create_node_and_edges(NODE_TYPE.GAME, properties, edges)

