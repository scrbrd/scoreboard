""" Game Module

...
"""

from itertools import groupby

from sqobject import SqObject

class Game(SqObject):

    """ Game is a subclass of SqObject for representing games. 

        Provide access to the attributes of a Game, including fields,
        relationships, and nearby nodes.

        Required:
        int _id                         super class requirement 
        Actor _creator                  who created the game

        Optional:
        list _opponent_result_triples   each entry associates an 
                                        Opponent with a score (int)
    
    """

    _creator = None
    _opponent_result_triples = []

    def __init__(self, game_id, attributes_dict):
        """ Initialize Game class with attributes

        Arguments:
        int game_id         sent to SqObject
        dict attributes_dict     a dictionary of attributes

        """
        super(Game, self).__init__(game_id, attributes_dict)
        self._creator = attributes_dict["creator"]
        self._opponent_result_triples = attributes_dict["opponent_result_triples"]

    def get_creator(self):
        """  Return the User who created the game. """
        return self._creator

    @staticmethod
    def get_opponents_by_result(opponent_score_pairs):
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

