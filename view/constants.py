""" Module: constants

Provide Application constants for view.

"""

from util.decorators import constant


class _AppClass(object):

    """ _AppClass holds app-wide w3c classes. """

    @constant
    def INACTIVE_NAV(self):
        return "inactive-nav"

    @constant
    def ACTIVE_NAV(self):
        return "active-nav"

APP_CLASS = _AppClass()


class _AppID(object):

    """ _AppID holds all function w3c ids. """

    pass

APP_ID = _AppID()


class _SqData(object):

    """ _SqData class to hold all possible keys appended to data-*.

    Note: These constants have dashes because the html5 spec says they must.
    Note: These can be used for json data as well.

    """

    @constant
    def ID(self):
        return "id"

    @constant
    def PERSON_ID(self):
        return "person-id"

    @constant
    def NAME(self):
        return "name"

    @constant
    def OBJECT_TYPE(self):
        return "object-type"

    @constant
    def LEAGUE_ID(self):
        return "league-id"

    @constant
    def GAME_TYPE(self):
        return "game-type"

    @constant
    def METRICS_BY_OPPONENT(self):
        return "metrics-by-opponent"

    @constant
    def SPORT_ID(self):
        return "sport-id"

    @constant
    def PICTURE(self):
        return "picture"

    @constant
    def RESULT(self):
        return "result"

    @constant
    def RIVALS(self):
        return "rivals"

    @constant
    def SPORTS(self):
        return "sports"

    @constant
    def SCORE(self):
        return "score"

    @constant
    def PAGE_TYPE(self):
        return "page-type"

    @constant
    def PAGE_NAME(self):
        return "page-name"

SQ_DATA = _SqData()


class _SqValue(object):

    """ _SqValue class to hold all possible values for data-*.

    Note that data-* isn't quite accurate. We explicitly exclude
    data-page-type and data-page-name and count them as special.

    """

    @constant
    def RIVALRY(self):
        """ RIVALRY is a value of the HTML attribute data-game-type. """
        return "rivalry"

    @constant
    def CAMARADERIE(self):
        """ CAMARADERIE is a value of the HTML attribute data-game-type. """
        return "camaraderie"

    # FIXME: DialogModel should populate view.app.dialog with these values.
    # when it does, remove these from here.

    @constant
    def WON(self):
        """ WON is a value of the attribute data-metrics-by-opponent. """
        return "won"

    @constant
    def LOST(self):
        """ LOST is a value of the attribute data-metrics-by-opponent. """
        return "lost"

    @constant
    def PLAYED(self):
        """ PLAYED is a value of the attribute data-metrics-by-opponent. """
        return "played"

SQ_VALUE = _SqValue()


class _PageType(object):

    """ _PageType class to hold all possible values for data-page-type. """

    @constant
    def LANDING(self):
        return "landing"

    @constant
    def TAB(self):
        return "tab"

    @constant
    def DIALOG(self):
        return "dialog"

PAGE_TYPE = _PageType()


class _PageName(object):

    """ _PageName class to hold all possible values for data-page-name. """

    @constant
    def LANDING(self):
        return "landing"

    @constant
    def GAMES(self):
        return "games"

    @constant
    def RANKINGS(self):
        return "rankings"

    @constant
    def LEAGUE(self):
        return "league"

    @constant
    def CREATE_GAME(self):
        return "create-game"

PAGE_NAME = _PageName()


class _ModelID(object):

    """ _ModelID class to hold all IDs that will contain model info. """

    @constant
    def SESSION(self):
        return "model-session"

    @constant
    def CONTEXT(self):
        return "model-context"

    @constant
    def PAGE_STATE(self):
        return "model-page-state"

MODEL_ID = _ModelID()
