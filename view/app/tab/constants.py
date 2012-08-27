""" Module: constants

Provide constants for Tab package.

"""

from util.decorators import constant


class _TabID(object):

    """ _TabID holds all w3c ids for the tab package. """

    @constant
    def TAB_HEADER(self):
        return "tab-header"

    @constant
    def CONTENT(self):
        return "content"

    @constant
    def PROPERTIES(self):
        return "properties"

    @constant
    def SUMMARY(self):
        return "summary"

    @constant
    def FEED(self):
        return "feed"

    @constant
    def TAB_CONTENT_WRAPPER(self):
        """ Tab outer wrapper for iScroll. """
        return "content-container-wrapper"

    @constant
    def TAB_CONTENT_CONTAINER(self):
        """ Tab inner wrapper for iScroll. """
        return "content-container"

TAB_ID = _TabID()
