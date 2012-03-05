""" Module: league

...

"""

from sqobject import SqNode
import loader

from model.const import EDGE_TYPE, NODE_TYPE


class League(SqNode):

    """ League is a subclass of SqNode.

    Provide access to the attributes of a League, including fields and 
    edges connecting to other nodes.

    Required:
    id   _id            League node id
    str  _name          League node name

    Edges Dict:
    EDGE_TYPE.HAS_SCHEDULED: [game_ids]
    EDGE_TYPE.HAS_LEAGUE_MEMBER: [opponent_ids]

    dict _opponents     Opponents in this League
    dict _games         Games played by Opponents in this League

    """

    _name = None
    
    _opponents = None
    _games = None


    def __init__(self, graph_node):
        """ Construct a League extending SqNode. """
        super(League, self).__init__(graph_node)

        self._name = graph_node.properties()["name"]


    def name(self):
        """ Return this League's name. """
        return self._name


    def get_opponents(self):
        """ Return a dict of Opponents. """

        opponents = self._opponents

        try:
            self.assert_loaded(opponents)

        except SqObjectNotLoadedError as e:
            #logger.debug(e.reason)
            print e.reason
            opponents = {}

        return opponents


    def set_opponents(self, opponents):
        """ Set a member variable with a dict of Opponents. """
        self._opponents = opponents


    def get_games(self):
        """ Return a dict of Games. """

        games = self._games

        try:
            self.assert_loaded(games)

        except SqObjectNotLoadedError as e:
            #logger.debug(e.reason)
            print e.reason
            games = {}

        return games


    def set_games(self, games):
        """ Set a member variable with a dict of Games. """
        self._games = games


    """ Static loader wrappers. """


    @staticmethod
    def load_opponents(league_id):
        """ Return a League with opponents loaded from the data layer."""
        return loader.load_path(
                league_id, 
                [EDGE_TYPE.HAS_LEAGUE_MEMBER], 
                [NODE_TYPE.PLAYER, NODE_TYPE.TEAM])


    @staticmethod
    def load_games(league_id):
        """ Return a League with opponents loaded from the data layer."""
        return loader.load_path(
                league_id,
                [EDGE_TYPE.HAS_SCHEDULED]
                [NODE_TYPE.GAME])

