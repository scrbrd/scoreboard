""" Module: Player

...
"""

from model.const import EDGE_TYPE, NODE_TYPE

from sqobject import SqNode
from game import Game
from opponent import Opponent

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

        self._first_name = graph_node.properties()["first_name"]
        self._last_name = graph_node.properties()["last_name"]

    def name(self):
        """ Return this Player's name. """
        return self._first_name + " " + self._last_name

    def count_wins(self):
        """ Return the number of Games this Player has won. """
        # FIXME: this just counts all the edges, not just EDGE_TYPE.WON
        return len(self.edges())
    
#    def create_game(self, creator_id, league_id, opponent_scores_dict):
#        """ Write Game and corresponding Edges to DB. 
#        
#        Required:
#        int creator_id  id of Player that create the Game
#        int league_id   id of League that Game belongs to
#        dict opponent_scores_dict   {opponent_id: score}
#
#        Return bool for success/failure
#        
#        """
#        edges_dict = {
#                EDGE_TYPE.CREATED: [{"TO_ID": creator_id}], 
#                EDGE_TYPE.IN_LEAGUE: [{"TO_ID": league_id}]}
#        # get outcome from opponent scores dict
#        outcome = Game.calculate_outcome_from_scores(
#                [(o, s) for o, s in opponent_scores_dict])
#        # convert output into a format where editor can be blind
#       for r, os in outcome:
#            edges_dict[r] = [{"TO_ID": o, "SCORE": s} for o, s in os]
# 
#        return editor.create_node_and_edges("GAME", {}, edges_dict)

