""" Module: constants

Provide Application constants for view.

"""

from util.decorators import constant


class _AppClass(object):

    """ _AppClass holds app-wide w3c classes. """


    @constant
    def INACTIVE_NAV(self):
        """ INACTIVE_NAV is a w3c class. """
        return "inactive-nav"


    @constant
    def ACTIVE_NAV(self):
        """ ACTIVE_NAV is a w3c class. """
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
        """ ID is a key of the HTML attribute Data. """
        return "id"


    @constant
    def PERSON_ID(self):
        """ PERSON_ID is a key of the HTML attribute Data. """
        return "person-id"


    @constant
    def NAME(self):
        """ NAME is a key of the HTML attribute Data. """
        return "name"


    @constant
    def OBJECT_TYPE(self):
        """ OBJECT_TYPE is a key of the HTML attribute Data. """
        return "object-type"


    @constant
    def LEAGUE_ID(self):
        """ LEAGUE_ID is the name of a form element that stores league id. """
        return "league-id"


    @constant
    def GAME_TYPE(self):
        """ GAME_TYPE is a key of the HTML attribute Data. """
        return "game-type"


    @constant
    def METRICS_BY_OPPONENT(self):
        """ METRICS_BY_OPPONENT is a key of the HTML attribute Data. """
        return "metrics-by-opponent"


    @constant
    def PICTURE(self):
        """ PICTURE is a key of the HTML attribute Data. """
        return "picture"


    @constant
    def RESULT(self):
        """ RESULT is a key of the HTML attribute Data. """
        return "result"


    @constant
    def RIVALS(self):
        """ RIVALS is a key of the HTML attribute Data. """
        return "rivals"


    @constant
    def SCORE(self):
        """ SCORE is a key of the HTML attribute Data. """
        return "score"


    @constant
    def PAGE_TYPE(self):
        """ PAGE_TYPE is a key of the HTML attribute Data. """
        return "page-type"


    @constant
    def PAGE_NAME(self):
        """ PAGE_NAME is a key of the HTML attribute Data. """
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


PAGE_TYPE = _PageType()


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
    def LEAGUE(self):
        """ LEAGUE is the league tab page. """
        return "league"


    @constant
    def CREATE_GAME(self):
        """ CREATE_GAME is the create game dialog page. """
        return "create-game"


PAGE_NAME = _PageName()


class _ModelID(object):

    """ _ModelID class to hold all IDs that will contain model info. """


    @constant
    def SESSION(self):
        """ SESSION is and w3c id for storing data. """
        return "model-session"


    @constant
    def CONTEXT(self):
        """ CONTEXT is and w3c id for storing data. """
        return "model-context"


    @constant
    def PAGE_STATE(self):
        """ PAGE_STATE is and w3c id for storing data. """
        return "model-page-state"


MODEL_ID = _ModelID()
