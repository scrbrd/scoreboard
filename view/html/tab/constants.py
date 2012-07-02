""" Module: constants

Provide constants for Tab package.

"""
from util.decorators import constant


class _TabClass(object):

    """ _TabClass holds all w3c classes for the tab package. """


    @constant
    def SECOND_HEADER(self):
        """ SECOND_HEADER is a w3c class. """
        return "second-header"


class _TabID(object):

    """ _TabID holds all w3c ids for the tab package. """


    @constant
    def CONTEXT(self):
        """ CONTEXT is the element that stores context data. """
        return "context"


    @constant
    def CONTENT(self):
        """ CONTENT is the element that stores content data. """
        return "content"


TAB_CLASS = _TabClass()
TAB_ID = _TabID()
