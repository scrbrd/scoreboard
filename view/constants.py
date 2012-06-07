""" Application Constants

Provide constants for view.

    HTML_ID
    HTML_CLASS

"""

from util.decorators import constant


class _AppClass(object):

    """ _AppClass holds all function HTML/js classes. """

    @constant
    def CLOSE_BUTTON(self):
        """ CLOSE_BUTTON is a HTML/js class. """
        return "close-button"

    @constant
    def SUBMIT_BUTTON(self):
        """ SUBMIT_BUTTON is a HTML/js class. """
        return "submit-button"

    @constant
    def PLAYER_SELECT(self):
        """ PLAYER_SELECT is a HTML/js class. """
        return "player-select"

    @constant
    def JS_LINK(self):
        """ JS_LINK is a HTML/js class. """
        return "js-link"

    @constant
    def ROUTE_BYPASS(self):
        """ ROUTE_BYPASS is a HTML/js class. """
        return "route-bypass"

    @constant
    def INACTIVE_NAV(self):
        """ INACTIVE_NAV is a HTML/js class. """
        return "inactive-nav"

    @constant
    def DIALOG_CONTENT(self):
        """ DIALOG_CONTENT is a HTML/js class. """
        return "dialog-content"

    @constant
    def COLUMN_0(self):
        """ COLUMN_0 is a HTML/js class. """
        return "column-0"

    @constant
    def COLUMN_1(self):
        """ COLUMN_1 is a HTML/js class. """
        return "column-1"

    @constant
    def COLUMN_2(self):
        """ COLUMN_2 is a HTML/js class. """
        return "column-2"

    @constant
    def LIST_WITH_HEADERS(self):
        """ LIST_WITH_HEADER is a HTML/js class. """
        return "list-with-headers"

    @constant
    def HEADED_LIST_ITEM(self):
        """ HEADED_LIST_ITEM is a HTML/js class. """
        return "headed-list-item"

    @constant
    def SUBMIT_BUTTON_WRAPPER(self):
        """ SUBMIT_BUTTON_WRAPPER is a HTML/js class. """
        return "submit-button-wrapper"

    @constant
    def ADD_BUTTON(self):
        """ ADD_BUTTON is an HTML class. """
        return "add-button"

    @constant
    def MAIN_HEADER(self):
        """ MAIN_HEADER is a HTML/css class. """
        return "main-header"

    @constant
    def SECOND_HEADER(self):
        """ SECOND_HEADER is a HTML/css class. """
        return "second-header"

    @constant
    def AUTOCOMPLETE_LABEL(self):
        """ AUTOCOMPLETE_LABEL is a HTML/css class. """
        return "autocomplete-label"

    @constant
    def AUTOCOMPLETE_VALUE(self):
        """ AUTOCOMPLETE_VALUE is a HTML/css class. """
        return "autocomplete-value"


class _AppID(object):

    """ _AppID holds all function HTML/js ids. """

    @constant
    def CONTEXT(self):
        """ CONTEXT is the element that stores context data. """
        return "context"

    @constant
    def CONTENT(self):
        """ CONTENT is the element that stores content data. """
        return "content"


class _DesignClass(object):

    """ _DesignClass to hold all design oriented HTML/css classes. """

    @constant
    def ACTIVE_NAV(self):
        """ ACTIVE_NAV is a HTML/css class. """
        return "active-nav"

    @constant
    def COUNTER(self):
        """ COUNTER is a HTML/css class. """
        return "counter"


class _DesignID(object):

    """ _DesignID class to hold all design oriented HTML/js ids. """

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


class _AppData(object):

    """ _AppData class to hold all 'Data-' atttribute keys.

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
    def PAGE_NAME(self):
        """ PAGE_NAME is a key of the HTML attribute Data. """
        return "page-name"


class _PageName(object):

    """ _PageName class to hold all possible values for data-page-name. """

    @constant
    def LANDING(self):
        """ LANDING is the rankings page. """
        return "landing"

    @constant
    def GAMES(self):
        """ GAMES is the rankings page. """
        return "games"

    @constant
    def RANKINGS(self):
        """ RANKINGS is the rankings page. """
        return "rankings"


APP_CLASS = _AppClass()
APP_ID = _AppID()
APP_DATA = _AppData()
DESIGN_CLASS = _DesignClass()
DESIGN_ID = _DesignID()
FORM_NAME = _FormName()
PAGE_NAME = _PageName()
