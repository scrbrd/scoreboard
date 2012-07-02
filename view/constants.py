""" Module: constants

Provide Application constants for view.

    HTML_ID
    HTML_CLASS

"""
from util.decorators import constant


class _AppClass(object):

    """ _AppClass holds app-wide w3c classes. """


    @constant
    def JS_LINK(self):
        """ JS_LINK is a w3c class. """
        return "js-link"


    @constant
    def EXTERNAL_LINK(self):
        """ EXTERNAL_LINK is a w3c class. """
        return "external-link"


    @constant
    def ROUTE_BYPASS(self):
        """ ROUTE_BYPASS is a w3c class. """
        return "route-bypass"


    @constant
    def INACTIVE_NAV(self):
        """ INACTIVE_NAV is a w3c class. """
        return "inactive-nav"


    @constant
    def ACTIVE_NAV(self):
        """ ACTIVE_NAV is a w3c class. """
        return "active-nav"


class _AppID(object):

    """ _AppID holds all function w3c ids. """

    pass


class _FormName(object):

    """ _FormName class holds all name attributes' possible values. """


    @constant
    def LEAGUE(self):
        """ LEAGUE is the name of a form element that stores league id. """
        return "league"


    @constant
    def CREATOR(self):
        """ CREATOR is the name of a form element that stores creator id. """
        return "creator"


    @constant
    def GAME_SCORE(self):
        """ GAME_SCORE is the name of a set of form elements. """
        return "game-score"


class _SqData(object):

    """ _SqData class to hold all 'Data-' atttribute keys.

    Note: These constants have dashes because the html5 spec says they must.
    Note: These can be used for json data as well.

    """


    @constant
    def ID(self):
        """ ID is a key of the HTML attribute Data. """
        return "id"


    @constant
    def NAME(self):
        """ NAME is a key of the HTML attribute Data. """
        return "name"


    @constant
    def OBJECT_TYPE(self):
        """ OBJECT_TYPE is a key of the HTML attribute Data. """
        return "object-type"


    @constant
    def SCORE(self):
        """ SCORE is a key of the HTML attribute Data. """
        return "score"


    @constant
    def RIVALS(self):
        """ RIVALS is a key of the HTML attribute Data. """
        return "rivals"


    @constant
    def PAGE_TYPE(self):
        """ PAGE_TYPE is a key of the HTML attribute Data. """
        return "page-type"


    @constant
    def PAGE_NAME(self):
        """ PAGE_NAME is a key of the HTML attribute Data. """
        return "page-name"


class _PageType(object):

    """ _PageType class to hold all possible values for data-page-type. """


    @constant
    def LANDING(self):
        """ LANDING is a page type. """
        return "landing"


    @constant
    def TAB(self):
        """ TAB is a page type. """
        return "tab"


    @constant
    def DIALOG(self):
        """ DIALOG is a page type. """
        return "dialog"


class _PageName(object):

    """ _PageName class to hold all possible values for data-page-name. """


    @constant
    def LANDING(self):
        """ LANDING is the landing page. """
        return "landing"


    @constant
    def GAMES(self):
        """ GAMES is the games tab page. """
        return "games"


    @constant
    def RANKINGS(self):
        """ RANKINGS is the rankings tab page. """
        return "rankings"


    @constant
    def CREATE_GAME(self):
        """ CREATE_GAME is the create game dialog page. """
        return "create-game"


class _ModelID(object):

    """ _ModelID class to hold all IDs that will contain model info. """


    @constant
    def VIEWER_CONTEXT(self):
        """ VIEWER_CONTEXT is and w3c id for storing data. """
        return "model-viewer-context"


    @constant
    def CONTEXT(self):
        """ CONTEXT is and w3c id for storing data. """
        return "model-context"


    @constant
    def PAGE_STATE(self):
        """ PAGE_STATE is and w3c id for storing data. """
        return "model-page-state"


APP_CLASS = _AppClass()
APP_ID = _AppID()
SQ_DATA = _SqData()
FORM_NAME = _FormName()
PAGE_TYPE = _PageType()
PAGE_NAME = _PageName()
MODEL_ID = _ModelID()
