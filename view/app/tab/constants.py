""" Module: constants

Provide constants for Tab package.

"""

from util.decorators import constant


class _ComponentClass(object):

    """ _ComponentClass holds all w3c classes for the tab components. """


    @constant
    def STORY(self):
        """ STORY is a w3c class. """
        return "story"


    @constant
    def GAME_STORY(self):
        """ GAME_STORY is a w3c class. """
        return "game-story"


    @constant
    def RANKINGS_LIST(self):
        """ RANKINGS_LIST is a w3c class. """
        return "rankings-list"


COMPONENT_CLASS = _ComponentClass()


class _TabClass(object):

    """ _TabClass holds all w3c classes for the tab package. """


    @constant
    def SUMMARY_ITEM(self):
        """ SUMMARY_ITEM is a w3c class. """
        return "summary-item"


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


    @constant
    def PROPERTIES(self):
        """ PROPERTIES is the element that stores properties content. """
        return "properties"


    @constant
    def SUMMARY(self):
        """ SUMMARY is the element that stores summary content. """
        return "summary"


    @constant
    def FEED(self):
        """ FEED is the element that stores feed content. """
        return "feed"


TAB_ID = _TabID()
