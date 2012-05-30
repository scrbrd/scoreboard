""" Application Constants

Provide constants for view.

    HTML_ID
    HTML_CLASS

"""

from util.decorators import constant


class _AppClass(object):

    """ _AppClass holds all function HTML/js classes. """

    @constant
    def CLOSE(self):
        """ CLOSE is a HTML/js class. """
        return "close"

    @constant
    def PLAYER_SELECT(self):
        """ PLAYER_SELECT is a HTML/js class. """
        return "player-select"


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
    def HEADER_SECTION(self):
        """ HEADER_SECTION is a HTML/css class. """
        return "header-section"

    @constant
    def MAIN_HEADER(self):
        """ MAIN_HEADER is a HTML/css class. """
        return "main-header"

    @constant
    def SECOND_HEADER(self):
        """ SECOND_HEADER is a HTML/css class. """
        return "second-header"

    @constant
    def ACTIVE_NAV(self):
        """ ACTIVE_NAV is a HTML/css class. """
        return "active-nav"

    @constant
    def INACTIVE_NAV(self):
        """ INACTIVE_NAV is a HTML/css class. """
        return "inactive-nav"

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
