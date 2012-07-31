""" Module: Handler Constants

Provide a set of handler constants for the Controller.

"""

from util.decorators import constant


class _CookieType(object):

    """ _CookieType class to describe all Cookie Types. """


    @constant
    def SESSION(self):
        """ SESSION is a Type of Cookie. """
        return "session"


    @constant
    def AUTH_STATE(self):
        """ AUTH_STATE is a Type of Cookie. """
        return "state"


    # TODO: remove when we start firing off MixPanelSignUp event in python!
    @constant
    def SIGN_UP(self):
        """ SIGN_UP is a Type of Cookie. """
        return "sign_up"


COOKIE_TYPE = _CookieType()


class _Cookie(object):

    """ _Cookie class to describe all Cookie Properties. """


    @constant
    def ACCESS_TOKEN(self):
        """ ACCESS_TOKEN is a Cookie Property. """
        return "access_token"


    @constant
    def USER_ID(self):
        """ USER_ID is a Cookie Property. """
        return "user_id"


    @constant
    def PERSON_ID(self):
        """ PERSON_ID is a Cookie Property. """
        return "person_id"


    @constant
    def FACEBOOK_ID(self):
        """ FACEBOOK_ID is a Cookie Property. """
        return "facebook_id"


    @constant
    def GENDER(self):
        """ GENDER is a Cookie Property. """
        return "gender"


    @constant
    def TIMEZONE(self):
        """ TIMEZONE is a Cookie Property. """
        return "timezone"


    @constant
    def IP(self):
        """ IP is a Cookie Property. """
        return "ip"


    @constant
    def LOCALE(self):
        """ LOCALE is a Cookie Property. """
        return "locale"


    @constant
    def FACEBOOK_LOCALE(self):
        """ FACEBOOK_LOCALE is a Cookie Property. """
        return "facebook_locale"


    @constant
    def VERSION(self):
        """ VERSION is a Cookie Property. """
        return "version"


    # TODO: make this a timestamp instead?
    @constant
    def IS_NEW(self):
        """ IS_NEW is a Cookie Property. """
        return "is_new"


COOKIE = _Cookie()


class _Argument(object):

    """ _Argument class to describe all GET/POST URL Arguments. """


    @constant
    def ASYNCHRONOUS(self):
        """ ASYNCHRONOUS is a Type of URL Argument. """
        return "asynchronous"


    @constant
    def PARAMETERS(self):
        """ PARAMETERS is a Type of URL Argument. """
        return "parameters"


    @constant
    def NEXT(self):
        """ NEXT is a Type of URL Argument. """
        return "next"


    @constant
    def CODE(self):
        """ CODE is a Type of URL Argument. """
        return "code"


    @constant
    def AUTH_STATE(self):
        """ AUTH_STATE is a Type of URL Argument. """
        return "state"


ARGUMENT = _Argument()


class _Parameter(object):

    """ _Parameter class to describe GET/POST URL Argument Parameters. """


    @constant
    def LEAGUE_ID(self):
        """ LEAGUE_ID is a Parameter Property. """
        return "league-id"


    @constant
    def METRICS_BY_OPPONENT(self):
        """ METRICS_BY_OPPONENT is a Parameter Property. """
        return "metrics-by-opponent"


PARAMETER = _Parameter()


class _Setting(object):

    """ _Setting enumerates Controller settings keys. """


    @constant
    def FACEBOOK_API_KEY(self):
        """ FACEBOOK_API_KEY is a Tornado settings property key. """
        return "facebook_api_key"


    @constant
    def FACEBOOK_SECRET(self):
        """ FACEBOOK_SECRET is a Tornado settings property key. """
        return "facebook_secret"


    @constant
    def DEFAULT_LEAGUE_ID(self):
        """ DEFAULT_LEAGUE_ID is a Tornado settings property key. """
        return "league_id"


SETTING = _Setting()


class _FacebookAuth(object):

    """ _FacebookAuth enumerates Facebook Authentication keys. """


    @constant
    def SCOPE(self):
        """ SCOPE is a Facebook Authentication key. """
        return "scope"


    @constant
    def STATE(self):
        """ STATE is a Facebook Authentication key. """
        return "state"


FACEBOOK_AUTH = _FacebookAuth()


class _FacebookAuthScope(object):

    """ _FacebookAuthScope enumerates Facebook Authentication scope keys. """


    @constant
    def ACCESS_TOKEN(self):
        """ ACCESS_TOKEN is a Facebook Authentication scope key. """
        return "access_token"


    @constant
    def GENDER(self):
        """ GENDER is a Facebook Authentication scope key. """
        return "gender"


    @constant
    def EMAIL(self):
        """ EMAIL is a Facebook Authentication scope key. """
        return "email"


    @constant
    def USER_INTERESTS(self):
        """ USER_INTERESTS is a Facebook Authentication scope key. """
        return "user_interests"


FACEBOOK_AUTH_SCOPE = _FacebookAuthScope()


class _Version(object):

    """ _Version enumerates software version number strings. """


    @constant
    def CURRENT(self):
        """ CURRENT is a string Version Number. """
        return "0.0"


    @constant
    def BETA(self):
        """ BETA is a string Version Number. """
        return "0.0"


    @constant
    def LAST(self):
        """ LAST is a string Version Number. """
        return "0.0"


    @constant
    def LAST_GOOD(self):
        """ LAST_GOOD is a string Version Number. """
        return "0.0"


    @constant
    def OLD(self):
        """ OLD is a string Version Number. """
        return "0.0"


VERSION = _Version()
