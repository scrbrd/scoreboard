""" Application Constants

Provide constants for view.

    HTML_ID
    HTML_CLASS

"""

from util.decorators import constant


class _AppClass(object):

    """ _AppClass class to hold all defined HTML classes. """


    @constant
    def CLOSE(self):
        """ CLOSE is a html/css/js class. """
        return "close"


    @constant
    def PLAYER_SELECT(self):
        """ PLAYER_SELECT is a html/css/js class. """
        return "player-select"


class _AppID(object):

    """ _AppID class holds all id attributes' possible values. """


    @constant
    def CONTEXT(self):
        """ CONTEXT is the element that stores context data. """
        return "context"


    @constant
    def CONTENT(self):
        """ CONTENT is the element that stores content data. """
        return "content"


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
        return "game_score"


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
FORM_NAME = _FormName()
PAGE_NAME = _PageName()

