""" Module: Player

...
"""

from sqobject import SqObject
from opponent import Opponent 

class Player(SqObject, Opponent):

    """ Player is a subclass of SqObject.

    Provide access to the attributes of a Player, including fields and 
    edges connecting to other nodes.
    
    Required:
    id   _id    Player node id

    Optional:
    
    """

    def __init__(self, id, attributes_dict):
        """
        Construct a Player extending SqObject and set any private
        members which are player-specific.
        
        """
        super(Player, self).__init__(id, attributes_dict)
        
    def count_wins(self):
        """ Return a list of Opponent objects. """
        return self._wins_count

