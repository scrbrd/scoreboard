""" Module: constants

App constants there are used in various areas of the application.

"""
from util.decorators import constant


class _ComponentClass(object):

    """ _ComponentClass class holds App-oriented component constants. """


    @constant
    def COVER_PHOTO(self):
        """ COVER_PHOTO is a w3c class. """
        return "cover-photo"


    @constant
    def HEADLINE(self):
        """ HEADLINE is a w3c class. """
        return "headline"


COMPONENT_CLASS = _ComponentClass()
