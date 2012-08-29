""" Module: constants

Provide constants for Dialog package.

"""

from util.decorators import constant


class _DialogID(object):

    """ _DialogID holds all w3c ids for the dialog package. """

    @constant
    def DIALOG_HEADER(self):
        return "dialog-header"

    @constant
    def DIALOG_CONTENT(self):
        return "dialog-content"

DIALOG_ID = _DialogID()
