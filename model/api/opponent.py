""" Module: Opponent

...
"""

import exceptions

class Opponent(object):

    """ Opponent is an interface.

    This is intended to be implemented by Player and Team, which are
    capable of participating in Games.
    
    """

    def __init__(self):
        """ This constructor should never be called. Raise an error. """
        raise NotImplementedError("Interface Constructor: DO NOT CALL")

    def count_wins(self):
        """ Return an int representing this opponent's win count. """
        raise NotImplementedError("Interface Method: DO NOT CALL")

