""" Module: League

...
"""

from model.api import SqNode
from model.api import loader

class League(SqNode):

    """ League is a subclass of SqNode.

    Provide access to the attributes of a League, including fields and 
    edges connecting to other nodes.

    Required:
    id   _id            League node id
    str  _name          League node name
    list _opponent_ids  Opponent IDs in this League
    list _game_ids      IDs of Games played by Opponents in this League

    Optional:
    dict _opponents     Opponents in this League
    dict _games         Games played by Opponents in this League

    """

    _name = None
    _opponent_ids = None
    _game_ids = None
    
    _opponents = None
    _games = None

    def __init__(self, id, attributes_dict):
        """
        Construct a League extending SqNode and set any private
        members which are league-specific.
        """
        super(League, self).__init__(id, attributes_dict)

        self._name = attributes_dict["name"]
        self._opponent_ids = attributes_dict["opponent_ids"]
        self._game_ids = attributes_dict["game_ids"]

    def name(self):
        """ Return this League's name. """
        return self._name

    def get_opponents(self):
        """ Return a dict of Opponents. """
        return self.assert_loaded(self._opponents) ? self._opponents : {}

    def set_opponents(self, opponents):
        """ Set a member variable with a dict of Opponents. """
        self._opponents = opponents

    def get_games(self):
        """ Return a dict of Games. """
        return self.assert_loaded(self._games) ? self._games : {}

    def set_games(self, games):
        """ Set a member variable with a dict of Games. """
        self._opponents = opponents

    """ Static loader wrappers. """

    @staticmethod
    def load_opponents(league_id):
        """ Return a League with opponents loaded from the data layer."""
        return loader.load_path(
                league_id, 
                ["LEAGUE_MEMBER"], 
                ["PLAYER", "TEAM"])

    @staticmethod
    def load_games(league_id):
        """ Return a League with opponents loaded from the data layer."""
        return loader.load_path(
                league_id,
                ["OPEN_SCHEDULE"]
                ["GAME"])

