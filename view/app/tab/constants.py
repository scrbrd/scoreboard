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


TAB_CLASS = _TabClass()


class _TabID(object):

    """ _TabID holds all w3c ids for the tab package. """


    @constant
    def TAB_HEADER(self):
        """ TAB_HEADER is a w3c id. """
        return "tab-header"


    @constant
    def CONTENT(self):
        """ CONTENT is the element that stores content data. """
        return "content"


TAB_ID = _TabID()
