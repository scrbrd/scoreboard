""" Module: stat_computer

...

"""


class StatComputer(object):

    """ StatComputer is an interface for computing stats.

    This is intended to be implemented by SqNode. Its subclasses will utilize
    these generic protected methods.

    Note: StatComputer may become our Sport class, especially is Sport turns
    out to be a collection of Stats or a Stats Config.

    TODO: fill in the generic compute_[count,streak,percentage] methods; they
    can be implemented generically if signatures include a list of Nodes, an
    Edge type to act on, and [optionally] a property of that Edge type to
    modify the computation.

    """


    def __init__(self):
        """ This constructor should never be called. Raise an error. """
        raise NotImplementedError("Interface Constructor: DO NOT CALL")


    def _compute_count(self):
        """ Return a count of a metric. """
        raise NotImplementedError("Interface Constructor: DO NOT CALL")


    def _compute_percentage(self):
        """ Return a percentage of a ratio of one metric to another metric. """
        raise NotImplementedError("Interface Constructor: DO NOT CALL")


    def _compute_streak(self):
        """ Return a streak count for uninterrupted conditions of a series of
        metrics. """
        raise NotImplementedError("Interface Constructor: DO NOT CALL")
