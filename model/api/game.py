""" Game Module

...
"""
from itertools import groupby

from sqobject import SqObject
#import utils

class Game(SqObject):

    """ Game is a subclass of SqObject for representing games. 

        Provide access to the attributes of a Game, including fields,
        relationships, and nearby nodes.

        Required:
        int _id                     super class requirement 
        Actor _creator              who created the game

        Optional:
        list _opponent_score_tuples each entry associates an Opponent 
                                    with a score (int)
    
    """

    _creator = None
    _opponent_score_pairs = []

    # ALPHA RULE - high score is always the winner, tie scores are ties
    
    def __init__(self, game_id, attributes):
        """ Initializes Game class with attributes

        Arguments:
        int game_id         sent to SqObject
        dict attributes     a dictionary of attributes

        """
        super(Game, self).__init__(game_id, attributes)
        self._creator = attributes["creator"]
        self._opponents_list = attributes["opponent_score_pairs"]

    def get_creator(self):
        """  Returns the User who created the game. """
        return self._creator

    def get_opponents_by_result(self):
        """ Provides access to all results with corresponding opponents. 
        
        If 0 Opponents: {}
        If 1 Opponent: "None"
        If more Opponents: "WIN" (highest score), "LOSS", "TIE (even)

        Returns {"result": Opponents}
        
        """
        num_of_opponents = len(_opponent_score_pairs)
        
        if num_of_opponents == 0:
            return {}
        elif num_of_opponents == 1:
            return {"NONE": _opponent_score_pairs[0]}
        else:
            opps_by_score = [(score, [o for o,v in val]) for score, val in
                    groupby(_opponent_score_pairs, lambda x:x[1])]
            opps_by_score.sort(reverse=True)

            num_of_results = len(opps_by_score)
            if num_of_results == 1:
                return {"TIE": [opps[0] for opps in _opponent_score_pairs]}
            else:
                d = {"WIN": opps_by_score[0][1]}
                losers = []
                for t in opps_by_score[1:]
                    losers.append(t[1])
                d["LOSS"] = losers
                return d

