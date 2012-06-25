""" Module: league

TODO: fill this in with required methods to implement since required
members aren't strictly members [they are pulled from properties].

"""

from constants import API_NODE_TYPE, API_EDGE_TYPE
from constants import API_NODE_PROPERTY, API_CONSTANT

from sqobject import SqNode, SqObjectNotLoadedError
import loader, editor


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

    _opponents = None
    _games = None


    def _get_property(self, key):
        """ Return League property denoted by key. """
        return self._properties.get(key, None)


    @property
    def name(self):
        """ Return this League's name. """
        # TODO: this wouldn't have to be defined here or in Person if it were
        # instead defined in SqNode, but this seems less confusing for now.
        return self._get_property(API_NODE_PROPERTY.NAME)


    def outgoing_edge_types(self):
        """ Return a list of allowed outgoing SqEdge types. """
        return [
                API_EDGE_TYPE.HAS_LEAGUE_MEMBER,
                API_EDGE_TYPE.HAS_SCHEDULED
                ]


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
    def property_keys():
        """ Return a list of permitted property fields for Game. """
        return [
                API_NODE_PROPERTY.NAME,
                ]


    @staticmethod
    def load_opponents(league_id):
        """ Return a League with Opponents loaded from the data layer."""
        (league, opponents) = loader.load_neighbors(
                league_id,
                [API_EDGE_TYPE.HAS_LEAGUE_MEMBER], 
                API_CONSTANT.OPPONENT_NODE_TYPES)

        league.set_opponents(opponents)

        return league


    @staticmethod
    def load_games(league_id):
        """ Return a League with opponents loaded from the data layer."""
        (league, games) = loader.load_neighbors(
                league_id,
                [API_EDGE_TYPE.HAS_SCHEDULED],
                [API_NODE_TYPE.GAME])

        league.set_games(games)

        return league


    @staticmethod
    def create_league(name, creator_id, opponent_ids=[]):
        """ Create and return a League.

        Required:
        str     name            name of League to be created
        id      creator_id      id of Person creating this League

        Optional:
        list    opponent_ids    ids of Teams/Players to add by default

        Return:
        League                  SqNode of Teams, Players, Schedules

        """

        raw_properties = {
                API_NODE_PROPERTY.NAME : name,
                }

        # squash the two into one set of flat, valid node properties
        properties = SqNode.prepare_node_properties(
                League.property_keys(),
                raw_properties)

        # prepare a node prototype for this league
        prototype_node = editor.prototype_node(
                API_NODE_TYPE.LEAGUE,
                properties)

        # prepare edge prototypes for creator edges
        prototype_edges = editor.prototype_edge_and_complement(
            API_EDGE_TYPE.CREATED,
            {},
            creator_id)

        # prepare edge prototypes for default opponents
        for opponent_id in opponent_ids:
            prototype_edges.extend(editor.prototype_edge_and_complement(
                API_EDGE_TYPE.IN_LEAGUE,
                {},
                opponent_id))

        return editor.create_node_and_edges(prototype_node, prototype_edges)
