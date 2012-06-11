""" Module: component_constants

Provide constants for Components Module.

"""
from util.decorators import constant


class _ComponentClass(object):

    """ _ComponentClass holds all w3c classes for the components module. """


    @constant
    def ADD_BUTTON(self):
        """ ADD_BUTTON is a w3c class. """
        return "add-button"


    @constant
    def CLOSE_BUTTON(self):
        """ CLOSE_BUTTON is a w3c class. """
        return "close-button"


    @constant
    def LOGIN_BUTTON(self):
        """ LOGIN_BUTTON is a w3c class. """
        return "login-button"


    @constant
    def FACEBOOK_LOGIN_BUTTON(self):
        """ FACEBOOK_LOGIN_BUTTON is a w3c class. """
        return "facebook-login-button"


    @constant
    def SUBMIT_BUTTON(self):
        """ SUBMIT_BUTTON is a w3c class. """
        return "submit-button"


    @constant
    def MAIN_HEADER(self):
        """ MAIN_HEADER is a w3c class. """
        return "main-header"


    @constant
    def LIST_COLUMN(self):
        """ LIST_COLUMN is a w3c class. """
        return "list-column"


    @constant
    def NUMBERED_LIST(self):
        """ NUMBERED_LIST is a w3c class. """
        return "numbered-list"


    @constant
    def HEADED_LIST(self):
        """ HEADED_LIST is a w3c class. """
        return "headed-list"


    @constant
    def LIST_HEADER(self):
        """ LIST_HEADER is a w3c class. """
        return "list-header"


    @constant
    def HEADED_LIST_ITEM(self):
        """ HEADED_LIST_ITEM is a w3c class. """
        return "headed-list-item"


COMPONENT_CLASS = _ComponentClass()
