""" Module: Handler Constants

Provide a set of top-level constants for the Controller.

"""

from util.decorators import constant


class _CookieType(object):

    """ _CookieType class to describe all Cookie Types. """


    @constant
    def USER(self):
        """ USER is a Type of Cookie. """
        return "user"


    @constant
    def STATE(self):
        """ STATE is a Type of Cookie. """
        return "state"


COOKIE_TYPE = _CookieType()


class _CookieKey(object):

    """ _CookieKey class to describe all Cookie Properties. """

    # FIXME: none of this should exist...it should instead be a collaboration
    # of the LoginHandler and AuthCatcher to pre-populate the model on every
    # request with some minimal User/Player. League is just a stopgap.

    @constant
    def USER_ID(self):
        """ USER_ID is a Cookie Property. """
        return "user_id"


    @constant
    def PLAYER_ID(self):
        """ PLAYER_ID is a Cookie Property. """
        return "player_id"


    @constant
    def LEAGUE_ID(self):
        """ LEAGUE_ID is a Cookie Property. """
        return "league_id"


    @constant
    def GENDER(self):
        """ GENDER is a Cookie Property. """
        return "gender"


    @constant
    def TIMEZONE(self):
        """ TIMEZONE is a Type of Cookie. """
        return "timezone"


COOKIE_KEY = _CookieKey()


class _ArgumentType(object):

    """ _ArgumentType class to describe all GET/POST URL Arguments. """


    @constant
    def NEXT(self):
        """ NEXT is a Type of Argument. """
        return "next"


    @constant
    def CODE(self):
        """ CODE is a Type of Argument. """
        return "code"


    @constant
    def STATE(self):
        """ STATE is a Type of Argument. """
        return "state"


ARGUMENT_TYPE = _ArgumentType()

