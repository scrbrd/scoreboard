""" Module: Player

...
"""

from model.api import SqNode, Game, Opponent
from model.api import editor

class Player(SqNode, Opponent):

    """ Player is a subclass of SqNode.

    Provide access to the attributes of a Player, including fields and 
    edges connecting to other nodes.

    Required:
    id   _id            Player node id
    str  _first_name    Player node first name
    str  _last_name     Player node last name

    Edge Dict:
    "WIN": [(game_ids, score)]
    "LOSS": [(game_ids, score)]
    "TIE": [(game_ids, score)]
    "NONE": [(game_ids, score)]
    "CREATOR": [game_ids]
    "LEAGUE_MEMBER": [league_ids]
 
    dict _games         Dict of Game lists keyed by win/loss/tie
    
    """

    _first_name = None
    _last_name = None
    
    _games = None

    def __init__(self, id, attributes_dict):
        """
        Construct a Player extending SqObject and set any private
        members which are player-specific.
        
        """
        super(Player, self).__init__(id, attributes_dict)

        self._first_name = attributes_dict["first_name"]
        self._last_name = attributes_dict["last_name"]

    def name(self):
        """ Return this Player's name. """
        return self._first_name + " " + self._last_name

    def count_wins(self):
        """ Return the number of Games this Player has won. """
        return len(SqNode._edge_ids_dict["WIN"])
    
    def create_game(self, creator_id, league_id, opponent_scores_dict):
        """ Write Game and corresponding Edges to DB. 
        
        Required:
        int creator_id  id of Player that create the Game
        int league_id   id of League that Game belongs to
        dict opponent_scores_dict   {opponent_id: score}

        Return bool for success/failure
        
        """
        edges_dict = {
                "CREATOR": [{"TO_ID": creator_id}], 
                "OPEN_SCHEDULE": [{"TO_ID": league_id}]}
        # get outcome from opponent scores dict
        outcome = Game.calculate_outcome_from_scores(
                [(o, s) for o, s in opponent_scores_dict])
        # convert output into a format where editor can be blind
        for r, os in outcome:
            edges_dict[r] = [{"TO_ID": o, "SCORE": s} for o, s in os]
 
        return editor.create_and_connect_node("GAME", {}, edges_dict)

