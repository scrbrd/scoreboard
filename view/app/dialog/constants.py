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

    @constant
    def DIALOG_CONTENT_WRAPPER(self):
        """ Dialog outer wrapper for iScroll. """
        return "dialog-content-wrapper"

    @constant
    def DIALOG_CONTENT_CONTAINER(self):
        """ Dialog inner wrapper for iScroll. """
        return "dialog-content-container"

DIALOG_ID = _DialogID()
