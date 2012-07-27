""" Module: constants

Provide constants for Page Package.

"""

from util.decorators import constant


class _PageClass(object):

    """ _PageClass holds all the w3c classes for the page package. """


    @constant
    def LOGIN_ANCHOR_WRAPPER(self):
        """ LOGIN_ANCHOR_WRAPPER is a w3c class. """
        return "login-anchor-wrapper"


PAGE_CLASS = _PageClass()


class _PageID(object):

    """ _PageID holds all the w3c ids for the page package. """


    pass


PAGE_ID = _PageID()
