""" Module: Player

...
"""

from model.api import Opponent, SqNode

class Player(SqNode, Opponent):

    """ Player is a subclass of SqNode.

    Provide access to the attributes of a Player, including fields and 
    edges connecting to other nodes.

    Required:
    id   _id            Player node id
    str  _first_name    Player node first name
    str  _last_name     Player node last name
    list _game_ids      IDs of Games played by this Player

    Optional:
    dict _games         Dict of Game lists keyed by win/loss/tie
    
    """

    _first_name = None
    _last_name = None
    _game_ids = None
    
    _games = None

    def __init__(self, id, attributes_dict):
        """
        Construct a Player extending SqObject and set any private
        members which are player-specific.
        
        """
        super(Player, self).__init__(id, attributes_dict)

        self._first_name = attributes_dict["first_name"]
        self._last_name = attributes_dict["last_name"]
        self._game_ids = attributes_dict["game_ids"]

    def name(self):
        """ Return this Player's name. """
        return self._first_name + " " + self._last_name

    def count_wins(self):
        """ Return the number of Games this Player has won. """
        return self.assert_loaded(self._games) ? self._games : {}

