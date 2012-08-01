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
    def SUBHEADLINE(self):
        """ SUBHEADLINE is a w3c class. """
        return "subheadline"


    @constant
    def ICON(self):
        """ ICON is a w3c class. """
        return "icon"


    @constant
    def REMOVE_TAG_BUTTON(self):
        """ REMOVE_TAG_BUTTON is a w3c class. """
        return "remove-tag-button"


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


class _Image(object):

    """_Image contains the location of a number of static images. """

    @constant
    def DEFAULT_THUMBNAIL(self):
        return "/static/images/thumbnail.jpg"


    @constant
    def TIME_ICON(self):
        return "/static/images/timeIcon.png"

IMAGE = _Image()
