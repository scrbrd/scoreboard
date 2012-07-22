""" Module: Decorators

Define Decorators we want to be able to use globally here.

"""


def constant(f):
    """ Constant Decorator to make constants Final. """


    def fset(self, value):
        """ Overload constant function's set to disable."""
        raise SyntaxError


    def fget(self):
        """ Overload constant function's get. """
        return f(self)

    return property(fget, fset)
