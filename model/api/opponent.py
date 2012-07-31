""" Module: Opponent

...

"""


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
        raise NotImplementedError(
                "Interface Method: IMPLEMENTOR MUST OVERRIDE")


    def type(self):
        """ Return a node type. """
        raise NotImplementedError(
                "Interface Method: IMPLEMENTOR MUST OVERRIDE")


    def name(self):
        """ Return a SqObject node name. """
        raise NotImplementedError(
                "Interface Method: IMPLEMENTOR MUST OVERRIDE")


    @property
    def loss_count(self):
        """ Return an int representing this opponent's loss count. """
        raise NotImplementedError(
                "Interface Method: IMPLEMENTOR MUST OVERRIDE")


    @property
    def win_count(self):
        """ Return an int representing this opponent's win count. """
        raise NotImplementedError(
                "Interface Method: IMPLEMENTOR MUST OVERRIDE")


    @property
    def loss_percentage(self):
        """ Return a float representing this opponent's loss percentage. """
        raise NotImplementedError(
                "Interface Method: IMPLEMENTOR MUST OVERRIDE")


    @property
    def win_percentage(self):
        """ Return an float representing this opponent's win percentage. """
        raise NotImplementedError(
                "Interface Method: IMPLEMENTOR MUST OVERRIDE")


    @property
    def current_loss_streak(self):
        """ Return an int representing this opponent's loss streak. """
        raise NotImplementedError(
                "Interface Method: IMPLEMENTOR MUST OVERRIDE")


    @property
    def current_win_streak(self):
        """ Return an int representing this opponent's win streak. """
        raise NotImplementedError(
                "Interface Method: IMPLEMENTOR MUST OVERRIDE")
