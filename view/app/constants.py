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


    @constant
    def OPPONENT_GROUP(self):
        """ OPPONENT_GROUP is a w3c class. """
        return "opponent-group"


    @constant
    def OPPONENT_GROUP_SECTION(self):
        """ OPPONENT_GROUP_SECTION is a w3c class. """
        return "opponent-group-section"


    @constant
    def SINGLE_OPPONENT_GROUP(self):
        """ SINGLE_OPPONENT_GROUP is a w3c class. """
        return "single-opponent-group"


    @constant
    def MULTI_OPPONENT_GROUP(self):
        """ MULTI_OPPONENT_GROUP is a w3c class. """
        return "multi-opponent-group"


COMPONENT_CLASS = _ComponentClass()


class _DefaultImage(object):

    """_DefaultImage contains the location of a number of static images. """

    @constant
    def THUMBNAIL(self):
        return "/static/images/icon.png"


DEFAULT_IMAGE = _DefaultImage()
