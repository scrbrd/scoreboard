""" Module: Player

...

"""

from constants import EDGE_TYPE
from sqobject import SqNode
from opponent import Opponent
#from game import Game


class Player(SqNode, Opponent):

    """ Player is a subclass of SqNode.

    Provide access to the attributes of a Player, including fields and 
    edges connecting to other nodes.

    Required:
    str     _first_name     Player node first name
    str     _last_name      Player node last name

    """
    
    _first_name = None
    _last_name = None


    def __init__(self, graph_node):
        """ Construct a Player extending SqNode. """
        super(Player, self).__init__(graph_node)

        self._first_name = graph_node.properties()["first_name"]
        self._last_name = graph_node.properties()["last_name"]


    @property
    def name(self):
        """ Return this Player's name. """
        return self.short_name


    @property
    def first_name(self):
        """ Return this Player's first name. """
        return self._first_name


    @property
    def last_name(self):
        """ Return this Player's last name. """
        return self._last_name


    @property
    def short_name(self):
        """ Return this Player's first name and last initial. """
        return "{0} {1}".format(
                self.first_name,
                self.last_name[0])


    @property
    def full_name(self):
        """ Return this Player's first and last name. """
        return "{0} {1}".format(
                self.first_name,
                self.last_name)


    def outgoing_edge_types(self):
        """ Return a list of allowed outgoing SqEdge types. """
        return [
                EDGE_TYPE.IN_LEAGUE,
                EDGE_TYPE.CREATED,
                EDGE_TYPE.WON,
                EDGE_TYPE.LOST,
                EDGE_TYPE.TIED,
                EDGE_TYPE.PLAYED]


    def count_wins(self):
        """ Return the number of Games this Player has won. """
        # it's possible for a player not to have any wins, in which case there 
        # won't be an entry in the edges dict, so default to the empty dict
        return len(self.get_edges().get(EDGE_TYPE.WON, {}))


    @property
    def win_count(self):
        """ Alias for count_wins() intended for use as a property. """
        return self.count_wins()


    def outgoing_edge_types(self):
        """ Return a list of allowed outgoing SqEdge types. """
        return [
                EDGE_TYPE.IN_LEAGUE,
                EDGE_TYPE.CREATED,
                EDGE_TYPE.WON,
                EDGE_TYPE.LOST,
                EDGE_TYPE.TIED,
                EDGE_TYPE.PLAYED]


