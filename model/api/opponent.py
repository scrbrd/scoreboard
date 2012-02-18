""" Module: Opponent

...
"""

from exceptions import NotImplementedError

class Opponent(object):

    """ Opponent is an interface.

    This is intended to be implemented by Player and Team, which are
    capable of participating in Games.
    
    """

    def __init__(self):
        """ This constructor should never be called. Raise an error. """
        raise NotImplementedError("Interface Constructor: DO NOT CALL")

    def id(self):
        """ Return a node id. """
        raise NotImplementedError("Interface Method: IMPLEMENTOR MUST OVERRIDE")

    def type(self):
        """ Return a node type. """
        raise NotImplementedError("Interface Method: IMPLEMENTOR MUST OVERRIDE")

    def name(self):
        """ Return a SqObject node name. """
        raise NotImplementedError("Interface Method: IMPLEMENTOR MUST OVERRIDE")

    def count_wins(self):
        """ Return an int representing this opponent's win count. """
        raise NotImplementedError("Interface Method: IMPLEMENTOR MUST OVERRIDE")

