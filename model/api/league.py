""" Module: league

...

"""

from constants import API_CONSTANT, EDGE_TYPE, NODE_TYPE
from sqobject import SqNode, SqObjectNotLoadedError
import loader


class League(SqNode):

    """ League is a subclass of SqNode.

    Provide access to the attributes of a League, including fields and 
    edges connecting to other nodes.

    Required:
    str     _name       League node name

    Optional:
    dict    _opponents  Opponents in this League
    dict    _games      Games played by Opponents in this League

    """

    _name = None
    _opponents = None
    _games = None


    def __init__(self, graph_node):
        """ Construct a League extending SqNode. """
        super(League, self).__init__(graph_node)

        self._name = graph_node.properties()["name"]


    @property
    def name(self):
        """ Return this League's name. """
        return self._name


    def outgoing_edge_types(self):
        """ Return a list of allowed outgoing SqEdge types. """
        return [
                EDGE_TYPE.HAS_LEAGUE_MEMBER,
                EDGE_TYPE.HAS_SCHEDULED]


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


    @property
    def opponents(self):
        """ Return a dict of Opponents. """
        return self.get_opponents()


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


    @property
    def games(self):
        """ Return a dict of Games. """
        return self.get_games()


    """ Static loader wrappers. """


    @staticmethod
    def load_opponents(league_id):
        """ Return a League with opponents loaded from the data layer."""
        return loader.load_neighbors(
                league_id, 
                [EDGE_TYPE.HAS_LEAGUE_MEMBER], 
                API_CONSTANT.OPPONENT_TYPES)


    @staticmethod
    def load_games(league_id):
        """ Return a League with opponents loaded from the data layer."""
        return loader.load_neighbors(
                league_id,
                [EDGE_TYPE.HAS_SCHEDULED]
                [NODE_TYPE.GAME])

