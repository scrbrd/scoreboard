""" Module: model.constants

...

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


class _Rankings():

    """ _Rankings class holds Catcher's rankings' constants. """


    @constant
    def RANKS():
        """ RANKS is the ranked objects. """
        return "ranks"


    @constant
    def SORT_FIELD():
        """ SORT_FIELD signifies the ranked objects sort field. """
        return "sort_field"


    @constant
    def RANKED_IN():
        """ RANKED_IN signifies the rankings' container. """
        return "ranked_in"


RANKINGS = _Rankings()

