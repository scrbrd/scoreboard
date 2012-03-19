""" Module: model.constants

Constants for communicating inside and outside of Model

"""

def constant(f):
    """ Constant Decorator to make constants Final. """


    def fset(self, value):
        """ Overload constant function's set to disable."""
        raise SyntaxError


    def fget(self):
        """ Overload constant function's get. """
        return f()


    return property(fget, fset)


class _Games():

    """ _Games class holds Catcher's games' constants. """


    @constant
    def GAMES():
        """ GAMES is the Games objects. """
        return "GAMES"


    @constant
    def PLAYED_IN():
        """ PLAYED_IN signifies the games' league. """
        return "PLAYED_IN"


GAMES = _Games()


class _Rankings():

    """ _Rankings class holds Catcher's rankings' constants. """


    @constant
    def RANKS():
        """ RANKS is the ranked objects. """
        return "RANKS"


    @constant
    def SORT_FIELD():
        """ SORT_FIELD signifies the ranked objects sort field. """
        return "SORT_FIELD"


    @constant
    def RANKED_IN():
        """ RANKED_IN signifies the rankings' container. """
        return "RANKED_IN"


RANKINGS = _Rankings()

