""" Module: Player

...

"""

from model.const import EDGE_TYPE, NODE_TYPE
from sqobject import SqNode
from opponent import Opponent
# from game import Game

class Player(SqNode, Opponent):

    """ Player is a subclass of SqNode.

    Provide access to the attributes of a Player, including fields and 
    edges connecting to other nodes.

    Required:
    id   _id            Player node id
    str  _first_name    Player node first name
    str  _last_name     Player node last name

    Edge Dict:
    EDGE_TYPE.WON: [(game_ids, score)]
    EDGE_TYPE.LOST: [(game_ids, score)]
    EDGE_TYPE.TIED: [(game_ids, score)]
    EDGE_TYPE.PLAYED: [(game_ids, score)]
    EDGE_TYPE.CREATED: [game_ids]
    EDGE_TYPE.IN_LEAGUE: [league_ids]
 
    dict _games         Dict of Game lists keyed by win/loss/tie
    
    """
    
    _first_name = None
    _last_name = None
    
    _games = None


    def __init__(self, graph_node):
        """ Construct a Player extending SqNode. """
        super(Player, self).__init__(graph_node)

        self._first_name = self.properties()["first_name"]
        self._last_name = self.properties()["last_name"]


    def name(self, use_last_initial=false):
        """ Return this Player's name. """
        return "{0} {1}".format(
                self.first_name(),
                self.last_name()[0] if use_last_initial else self.last_name())


    def first_name(self):
        """ Return this Player's first name. """
        return self._first_name


    def last_name(self):
        """ Return this Player's last name. """
        return self._last_name


    def shorten_name(self):
        """ Return this Player's first name and last initial. """
        return self.name(true)


    def count_wins(self):
        """ Return the number of Games this Player has won. """
        return len(self.edges()[EDGE_TYPE.WON])

