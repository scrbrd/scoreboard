"""
Module: League

...
"""

from sqobject import SqObject

class League(SqObject):

    """
    League is a subclass of SqObject

    Provide access to the attributes of a League, including fields and 
    edges connecting to other nodes.
    
    Required:
    id   _id        League node id
    
    Optional:
    list _opponents Opponents in this League
    list _games     Games played by Opponents in this League
    """

    _opponents = None
    _games = None

    def __init__(self, id, attributes_dict):
        """
        Construct a League extending SqObject and set any private
        members which are league-specific.
        """
        super(League, self).__init__(id, attributes_dict)
        
        # opponents/games to be defined in Utils constants
        self._opponents = attributes_dict["opponents"]
        self._games = attributes_dict["games"]

    def get_opponents(self):
        """
        Return a list of Opponent objects
        """
        return self._opponents

    def get_games(self):
        """
        Return a list of Game objects
        """
        return self._games

