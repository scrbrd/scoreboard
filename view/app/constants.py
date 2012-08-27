""" Module: constants

App constants there are used in various areas of the application.

"""
from util.decorators import constant


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
