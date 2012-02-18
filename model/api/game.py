""" Module: game

...
"""

from itertools import groupby

from model.api import SqNode
from model.api import loader

class Game(SqNode):

    """ Game is a subclass of SqObject for representing games. 

        Provide access to the attributes of a Game, including fields,
        relationships, and nearby nodes.

        Required:
        int _id             super class requirement 
        
        Edges Dict: 
        "WIN": [(opponent_ids, score)]
        "LOSS": [(opponent_ids, score)]
        "TIE": [(opponent_ids, score)]
        "NONE": [(opponent_ids, score)]
        "CREATOR": player_id ***REQUIRED***
        "OPEN_SCHEDULE": [league_ids]
        
        dict _opponents     store loaded Opponents

    """

    _opponents = None

    def __init__(self, game_id, attributes_dict):
        """ Initialize Game class with attributes

        Arguments:
        int game_id             sent to SqObject
        dict attributes_dict    a dictionary of attributes

        """
        super(Game, self).__init__(game_id, attributes_dict)

    def creator_id(self):
        """  Return the Player who created the game. """
        return SqNode._edge_ids_dict["CREATOR"]

    def outcome(self):
        """ Return a dictionary - {opponent_id: score} """
        outcome_dict = {}
        results_list = ["WIN", "LOSS", "TIE", "NONE"]
        for r in results_list:
            for i, s in SqNode._edge_ids_dict[r]
                outcome_dict[i] = s
        return outcome_dict

    def get_opponents(self):
        """ Return a dict of Opponents. """
        return self.assert_loaded(self._opponents) ? self._opponents : {}

    def set_opponents(self, opponents):
        """ Set a Game's loaded Opponents from a dict. """
        self._opponents = opponents

    @staticmethod
    def load_opponents(game_id):
        """
        Load the Game's Opponents and attributes into a Game.
        
        Required:
        int game_id     the id of the Game

        Return Game
        """
        return Loader.loadPath(
                game_id, 
                ["WIN", "LOSS", "TIE", "NONE"], 
                ["PLAYER", "TEAM"])

    @staticmethod
    def multiload_opponents(game_ids):
        """
        Load multiple Games' Opponents and attributes into a list.
        
        Required:
        list game_ids   the ids of the Games

        Return Games list
        """
        games = []
        for id in game_ids:
            games.append(load_opponents(id))
        return games

    @staticmethod
    def calculate_outcome_from_scores(opponent_score_pairs):
        """ Convert opponents and scores to opponents by result. 
        
        Arguments:
        list opponent_score_pairs   a list of opponents and scores
        
        If 0 Opponents: {}
        If 1 Opponent: "None"
        If more Opponents: "WIN" (highest score), "LOSS", "TIE (even)

        Currently, the highest score wins.

        Return {"result": [(score, Opponents)]}
        
        """
        num_of_opponents = len(opponent_score_pairs)
        results_with_opponents_dict = {}

        # if no opponents, then no results
        if num_of_opponents == 0:
            results_with_opponents_dict = {}
        # if one opponent, then no win or loss
        elif num_of_opponents == 1:
            results_with_opponents_dict = {"NONE": 
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
                results_with_opponents_dict = {"TIE": [(opps_by_score[0][0],
                    opps_by_score[0][1])]}
            else:
                # otherwise, win is highest score
                results_with_opponents_dict = {"WIN": [(opps_by_score[0][0], 
                    opps_by_score[0][1])]}
                # and loss is all the other scores
                losers = []
                for t in opps_by_score[1:]:
                    losers.append((t[0], t[1]))
                results_with_opponents_dict["LOSS"] = losers
        return results_with_opponents_dict

