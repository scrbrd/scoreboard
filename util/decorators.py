""" Module: Decorators

Define Decorators we want to be able to use globally here.

"""
import os


def constant(f):
    """ Constant Decorator to make constants Final. """


    def fset(self, value):
        """ Overload constant function's set to disable."""
        raise SyntaxError


    def fget(self):
        """ Overload constant function's get. """
        return f(self)

    return property(fget, fset)


def print_timing(func):
    """ Debug decorator to see how long functions take. """


    def wrapper(*arg):
        t1 = os.times()[4]
        return_value = func(*arg)
        t2 = os.times()[4]
        print "{0} took {1}ms".format(func.func_name, (t2 - t1) * 1000.0)
        return return_value
    return wrapper
