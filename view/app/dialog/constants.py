""" Module: constants

Provide constants for Dialog package.

"""

from util.decorators import constant


class _DialogClass(object):

    """ _DialogClass holds all w3c classes for the dialog package. """


    @constant
    def DIALOG_CONTENT(self):
        """ DIALOG_CONTENT is a w3c class. """
        return "dialog-content"


    @constant
    def SUBMIT_BUTTON_WRAPPER(self):
        """ SUBMIT_BUTTON_WRAPPER is a w3c class. """
        return "submit-button-wrapper"


    @constant
    def AUTOCOMPLETE(self):
        """ AUTOCOMPLETE is a w3c class. """
        return "autocomplete"


    @constant
    def AUTOCOMPLETE_LABEL(self):
        """ AUTOCOMPLETE_LABEL is a w3c class. """
        return "autocomplete-label"


    @constant
    def AUTOCOMPLETE_VALUE(self):
        """ AUTOCOMPLETE_VALUE is a w3c class. """
        return "autocomplete-value"


    @constant
    def AUTOCOMPLETE_PLAYERS(self):
        """ AUTOCOMPLETE_PLAYERS is a w3c class. """
        return "autocomplete-players"


DIALOG_CLASS = _DialogClass()


class _DialogID(object):

    """ _DialogID holds all w3c ids for the dialog package. """


    @constant
    def DIALOG_HEADER(object):
        """ DIALOG_HEADER is a w3c class. """
        return "dialog-header"


DIALOG_ID = _DialogID()