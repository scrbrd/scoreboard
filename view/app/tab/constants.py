""" Module: constants

Provide constants for Tab package.

"""

from util.decorators import constant


class _ComponentClass(object):

    """ _ComponentClass holds all w3c classes for the tab components. """

    @constant
    def STORY(self):
        return "story"

    @constant
    def GAME_STORY(self):
        return "game-story"

    @constant
    def MAIN_STORY_SECTION(self):
        return "main-story-section"

    @constant
    def SPORT_STORY_COMPONENT(self):
        return "sport-story-component"

    @constant
    def COMMENTS_SECTION(self):
        return "comments-section"

    @constant
    def RANKINGS_LIST(self):
        return "rankings-list"

    @constant
    def COMMENT_FORM(self):
        return "comment-form"


COMPONENT_CLASS = _ComponentClass()


class _TabClass(object):

    """ _TabClass holds all w3c classes for the tab package. """

    @constant
    def TAB_HEADER(self):
        return "tab-header"

    @constant
    def SUMMARY_ITEM(self):
        return "summary-item"

    @constant
    def SECOND_HEADER(self):
        return "second-header"

TAB_CLASS = _TabClass()


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

TAB_ID = _TabID()
