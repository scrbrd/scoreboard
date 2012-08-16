""" Module: constants

Provide constants for Dialog package.

"""

from util.decorators import constant


class _DialogClass(object):

    """ _DialogClass holds all w3c classes for the dialog package. """

    @constant
    def DIALOG_HEADER(self):
        return "dialog-header"

    @constant
    def DIALOG_CONTENT(self):
        return "dialog-content"

    @constant
    def POST_BUTTON_WRAPPER(self):
        return "post-button-wrapper"

    @constant
    def AUTOCOMPLETE(self):
        return "autocomplete"

    @constant
    def AUTOCOMPLETE_LABEL(self):
        return "autocomplete-label"

    @constant
    def AUTOCOMPLETE_THUMBNAIL(self):
        return "autocomplete-thumbnail"

    @constant
    def AUTOCOMPLETE_VALUE(self):
        return "autocomplete-value"

    @constant
    def AUTOCOMPLETE_TAG(self):
        return "autocomplete-tag"

    @constant
    def AUTOCOMPLETE_PLAYER(self):
        return "autocomplete-player"

    @constant
    def AUTOCOMPLETE_SPORT(self):
        return "autocomplete-sport"

    @constant
    def OPPONENT_TAGS_GROUP(self):
        return "opponent-tags-group"

    @constant
    def OPPONENT_TAGS_LIST(self):
        return "opponent-tags-list"

    @constant
    def OPPONENT_TAG_LIST_ITEM(self):
        return "opponent-tag-list-item"

    @constant
    def OPPONENT_TAGS_HEADLINE(self):
        return "opponent-tags-headline"

    @constant
    def OPPONENT_TAGS_SUBHEADER(self):
        return "opponent-tags-subheader"

    @constant
    def SPORT_TAG_SUBHEADER(self):
        return "sport-tag-subheader"

    @constant
    def GAME_TYPE_SUBHEADER(self):
        return "game-type-subheader"

    #@constant
    #def GAME_TYPE_LABEL(self):
    #    return "game-type-label"

    @constant
    def GAME_TYPE_SWITCH(self):
        return "game-type-switch"

DIALOG_CLASS = _DialogClass()


class _DialogID(object):

    """ _DialogID holds all w3c ids for the dialog package. """

    @constant
    def DIALOG_HEADER(self):
        return "dialog-header"

    @constant
    def DIALOG_CONTENT_WRAPPER(self):
        """ Dialog outer wrapper for iScroll. """
        return "dialog-content-wrapper"

    @constant
    def DIALOG_CONTENT_CONTAINER(self):
        """ Dialog inner wrapper for iScroll. """
        return "dialog-content-container"

DIALOG_ID = _DialogID()
