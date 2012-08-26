""" Module: constants

App constants there are used in various areas of the application.

"""
from util.decorators import constant


class _ComponentClass(object):

    """ _ComponentClass class holds App-oriented component w3c constants. """

    @constant
    def COVER_PHOTO(self):
        return "cover-photo"

    @constant
    def HEADLINE(self):
        return "headline"

    @constant
    def SUBHEADLINE(self):
        return "subheadline"

    @constant
    def ICON(self):
        return "icon"

    @constant
    def REMOVE_TAG_BUTTON(self):
        return "remove-tag-button"

    @constant
    def RELATIVE_DATE_COMPONENT(self):
        return "relative-date-component"

COMPONENT_CLASS = _ComponentClass()


class _Image(object):

    """_Image contains the location of a number of static images. """

    @constant
    def DEFAULT_THUMBNAIL(self):
        return "/static/images/thumbnail.jpg"

    @constant
    def DEFAULT_OPPONENT_THUMBNAIL(self):
        return "/static/images/thumbnail.jpg"

    @constant
    def DEFAULT_SPORT_THUMBNAIL(self):
        return "/static/images/thumbnail.jpg"

    @constant
    def TIME_ICON(self):
        return "/static/images/timeIcon.png"

IMAGE = _Image()
