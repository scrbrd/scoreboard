""" Module: league

...

"""

from constants import API_CONSTANT, EDGE_TYPE, NODE_TYPE, NODE_PROPERTY
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

        self._name = graph_node.properties()[NODE_PROPERTY.NAME]


    @property
    def name(self):
        """ Return this League's name. """
        return self._name


    def outgoing_edge_types(self):
        """ Return a list of allowed outgoing SqEdge types. """
        return [
                EDGE_TYPE.HAS_LEAGUE_MEMBER,
                EDGE_TYPE.HAS_SCHEDULED]


    def get_opponent(self, opp_id):
        """ Return an Opponent by its id. """
        SqNode.assert_loaded(self._opponents)
        return self._opponents.get(opp_id, None)


    def get_opponents(self):
        """ Return a list of Opponents. """
        SqNode.assert_loaded(self._opponents)
        return self._opponents.values()
            
    
    def set_opponents(self, opponents):
        """ Set a League's loaded Opponents with a dict. """
        self._opponents = opponents


    def get_game(self, game_id):
        """ Return League's list of Games. """
        SqNode.assert_loaded(self._games)
        return self._games.get(game_id, None)


    def get_games(self):
        """ Return League's list of Games. """
        SqNode.assert_loaded(self._games)
        return self._games.values()


    def set_games(self, games):
        """ Set League's games with a dict. """
        self._games = games


    """ Static loader wrappers. """


    @staticmethod
    def load_opponents(league_id):
        """ Return a League with opponents loaded from the data layer."""
        (league, opponents) = loader.load_neighbors(
                league_id,
                [EDGE_TYPE.HAS_LEAGUE_MEMBER], 
                API_CONSTANT.OPPONENT_TYPES)

        league.set_opponents(opponents)

        return league


    @staticmethod
    def load_games(league_id):
        """ Return a League with opponents loaded from the data layer."""
        (league, games) = loader.load_neighbors(
                league_id,
                [EDGE_TYPE.HAS_SCHEDULED],
                [NODE_TYPE.GAME])

        league.set_games(games)

        return league

