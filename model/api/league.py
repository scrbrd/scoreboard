""" Module: league

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

    Edges Dict:
    "OPEN_SCHEDULE": [game_ids]
    "LEAGUE_MEMBER": [opponent_ids]

    dict _opponents     Opponents in this League
    dict _games         Games played by Opponents in this League

    """

    _name = None
    
    _opponents = None
    _games = None

    def __init__(self, id, attributes_dict):
        """
        Construct a League extending SqNode and set any private
        members which are league-specific.
        """
        super(League, self).__init__(id, attributes_dict)

        self._name = attributes_dict["name"]

    def name(self):
        """ Return this League's name. """
        return self._name

    def get_opponents(self):
        """ Return a dict of Opponents. """
        try:
            opponents = self._opponents
            self.assert_loaded(opponents)
        except SqObjectNotLoadedError as e:
            # log error and send app empty data
            #logger.debug(e.msg)
            opponents = {}
        
        return opponents

    def set_opponents(self, opponents):
        """ Set a member variable with a dict of Opponents. """
        self._opponents = opponents

    def get_games(self):
        """ Return a dict of Games. """
        try:
            games = self._games
            self.assert_loaded(games)
        except SqObjectNotLoadedError as e:
            # log error and send app empty data
            #logger.debug(e.msg)
            games = {}

        return games

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

