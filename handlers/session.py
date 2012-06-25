""" Module: session

Provide basic session information related to the viewer and browser to
be available to all parts of the MVC framework.

Much of the information contained here is only being passed around so
that we can fire off events to MixPanel. Otherwise, we would likely only
need User ID, Person ID, and, in the case of third party authentication,
access token.

"""


class Session(object):

    """ Session defines and persists viewer data across requests.

    This class consists only of accessors and mutators and does not
    manipulate information in any way. Rather, it simply makes session
    data captured by the Controller available to the Model and View.

    """

    # required fields
    _user_id = None
    _person_id = None

    # optional fields
    _access_token = None
    _fb_id = None
    _gender = None
    _timezone = None
    _ip = None
    _locale = None
    _version = None


    def __init__(self, user_id, person_id):
        self._user_id = user_id
        self._person_id = person_id


    @property
    def user_id(self):
        """ Return a User ID. """
        return self._user_id


    @property
    def person_id(self):
        """ Return a Person ID. """
        return self._person_id


    def get_access_token(self):
        """ Return a third party access token string for session. """
        return self._access_token


    def set_access_token(self, access_token):
        """ Store a third party access token string for a session. """
        self._access_token = access_token
        

    def get_fb_id(self):
        """ Return a Facebook User ID for a session. """
        return self._fb_id


    def set_fb_id(self, fb_id):
        """ Store a Facebook User ID for a session. """
        self._fb_id = fb_id


    def get_gender(self):
        """ Return a male/female gender string for a session. """
        return self._gender


    def set_gender(self, gender):
        """ Store a male/female gender string for a session. """
        self._gender = gender


    def get_timezone(self):
        """ Return a UTC timezone offset number string for a session. """
        # TODO: make sure this is actually a string and not a signed int.
        return self._timezone


    def set_timezone(self, timezone):
        """ Store a UTC timezone offset number string for a session. """
        # TODO: make sure this is actually a string and not a signed int.
        self._timezone = timezone


    def get_ip(self):
        """ Return an IP address string for a session. """
        return self._ip


    def set_ip(self, ip):
        """ Store an IP address string for a session. """
        self._ip = ip


    def get_locale(self):
        """ Return an ISO language+country string locale for a session. """
        return self._locale


    def set_locale(self, locale):
        """ Store a ISO language+country string locale for a session. """
        self._locale = locale


    def get_version(self):
        """ Return a string application version for a session. """
        return self._version


    def set_version(self, version):
        """ Store a string application version for a session. """
        self._version = version
