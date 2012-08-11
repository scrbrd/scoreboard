""" Module: Handler Constants

Provide a set of handler constants for the Controller.

"""

from util.decorators import constant


class _CookieType(object):

    """ _CookieType class to describe all Cookie Types. """

    @constant
    def SESSION(self):
        return "session"

    @constant
    def AUTH_STATE(self):
        return "state"

    # TODO: remove when we start firing off MixPanelSignUp event in python!
    @constant
    def SIGN_UP(self):
        return "sign_up"

COOKIE_TYPE = _CookieType()


class _Cookie(object):

    """ _Cookie class to describe all Cookie Properties. """

    @constant
    def ACCESS_TOKEN(self):
        return "access_token"

    @constant
    def USER_ID(self):
        return "user_id"

    @constant
    def PERSON_ID(self):
        return "person_id"

    @constant
    def FACEBOOK_ID(self):
        return "facebook_id"

    @constant
    def GENDER(self):
        return "gender"

    @constant
    def TIMEZONE(self):
        return "timezone"

    @constant
    def IP(self):
        return "ip"

    @constant
    def LOCALE(self):
        return "locale"

    @constant
    def FACEBOOK_LOCALE(self):
        return "facebook_locale"

    @constant
    def VERSION(self):
        return "version"

    # TODO: make this a timestamp instead?
    @constant
    def IS_NEW(self):
        return "is_new"

COOKIE = _Cookie()


class _Argument(object):

    """ _Argument class to describe all GET/POST URL Arguments. """

    @constant
    def ASYNCHRONOUS(self):
        return "asynchronous"

    @constant
    def PARAMETERS(self):
        return "parameters"

    @constant
    def NEXT(self):
        return "next"

    @constant
    def CODE(self):
        return "code"

    @constant
    def AUTH_STATE(self):
        return "state"

ARGUMENT = _Argument()


class _Parameter(object):

    """ _Parameter class to describe GET/POST URL Argument Parameters. """


    @constant
    def LEAGUE_ID(self):
        return "league-id"

    @constant
    def GAME_ID(self):
        return "game-id"

    @constant
    def MESSAGE(self):
        return "message"

    @constant
    def METRICS_BY_OPPONENT(self):
        return "metrics-by-opponent"

    @constant
    def SPORT_ID(self):
        return "sport-id"

PARAMETER = _Parameter()


class _Setting(object):

    """ _Setting enumerates Tornado Controller settings keys. """

    @constant
    def FACEBOOK_API_KEY(self):
        return "facebook_api_key"

    @constant
    def FACEBOOK_SECRET(self):
        return "facebook_secret"

    @constant
    def DEFAULT_LEAGUE_ID(self):
        return "league_id"

SETTING = _Setting()


class _FacebookAuth(object):

    """ _FacebookAuth enumerates Facebook Authentication keys. """

    @constant
    def SCOPE(self):
        return "scope"

    @constant
    def STATE(self):
        return "state"

FACEBOOK_AUTH = _FacebookAuth()


class _FacebookAuthScope(object):

    """ _FacebookAuthScope enumerates Facebook Authentication scope keys. """

    @constant
    def ACCESS_TOKEN(self):
        return "access_token"

    @constant
    def GENDER(self):
        return "gender"

    @constant
    def EMAIL(self):
        return "email"

    @constant
    def USER_INTERESTS(self):
        return "user_interests"


FACEBOOK_AUTH_SCOPE = _FacebookAuthScope()


class _Version(object):

    """ _Version enumerates software version number strings. """

    @constant
    def CURRENT(self):
        return "0.0"

    @constant
    def BETA(self):
        return "0.0"

    @constant
    def LAST(self):
        return "0.0"

    @constant
    def LAST_GOOD(self):
        return "0.0"

    @constant
    def OLD(self):
        return "0.0"

VERSION = _Version()
