""" Module: constants

Provide constants for Dialog package.

"""

from util.decorators import constant


class _DialogClass(object):

    """ _DialogClass holds all w3c classes for the dialog package. """


    @constant
    def DIALOG_HEADER(self):
        """ DIALOG_HEADER is a w3c class. """
        return "dialog-header"


    @constant
    def DIALOG_CONTENT(self):
        """ DIALOG_CONTENT is a w3c class. """
        return "dialog-content"


    @constant
    def POST_BUTTON_WRAPPER(self):
        """ POST_BUTTON_WRAPPER is a w3c class. """
        return "post-button-wrapper"


    @constant
    def AUTOCOMPLETE(self):
        """ AUTOCOMPLETE is a w3c class. """
        return "autocomplete"


    @constant
    def AUTOCOMPLETE_LABEL(self):
        """ AUTOCOMPLETE_LABEL is a w3c class. """
        return "autocomplete-label"


    @constant
    def AUTOCOMPLETE_THUMBNAIL(self):
        """ AUTOCOMPLETE_THUMBNAIL is a w3c class. """
        return "autocomplete-thumbnail"


    @constant
    def AUTOCOMPLETE_VALUE(self):
        """ AUTOCOMPLETE_VALUE is a w3c class. """
        return "autocomplete-value"


    @constant
    def AUTOCOMPLETE_PLAYERS(self):
        """ AUTOCOMPLETE_PLAYERS is a w3c class. """
        return "autocomplete-players"


    @constant
    def OPPONENT_TAGS_GROUP(self):
        """ OPPONENT_TAGS_GROUP is a w3c class. """
        return "opponent-tags-group"


    @constant
    def OPPONENT_TAGS_LIST(self):
        """ OPPONENT_TAGS_LIST is a w3c class. """
        return "opponent-tags-list"


    @constant
    def OPPONENT_TAG_LIST_ITEM(self):
        """ OPPONENT_TAG_LIST_ITEM is a w3c class. """
        return "opponent-tag-list-item"


    @constant
    def OPPONENT_TAGS_HEADLINE(self):
        """ OPPONENT_TAGS_HEADLINE is a w3c class. """
        return "opponent-tags-headline"


    @constant
    def OPPONENT_TAGS_SUBHEADER(self):
        """ OPPONENT_TAGS_SUBHEADER is a w3c class. """
        return "opponent-tags-subheader"


    @constant
    def GAME_TYPE(self):
        """ GAME_TYPE is a w3c class. """
        return "game-type"


    @constant
    def GAME_TYPE_LABEL(self):
        """ GAME_TYPE_LABEL is a w3c class. """
        return "game-type-label"


    @constant
    def GAME_TYPE_SWITCH(self):
        """ GAME_TYPE_SWITCH is a w3c class. """
        return "game-type-switch"


DIALOG_CLASS = _DialogClass()


class _DialogID(object):

    """ _DialogID holds all w3c ids for the dialog package. """


    @constant
    def DIALOG_HEADER(self):
        """ DIALOG_HEADER is a w3c class. """
        return "dialog-header"


DIALOG_ID = _DialogID()
