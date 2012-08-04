""" Module: auth

Define an AuthModel providing the read/write interface to validate
credentials and establish a Session. If we choose to implement our own
authentication system, this should provide the stub to make that easy.

Also define a FacebookAuthModel subclass which, for now, is the only
actual way to authenticate. Override some basic AuthModel functionality
to make use of Facebook's authentication system.

"""

import tornado.web

from model.constants import NODE_PROPERTY, PROPERTY_VALUE, THIRD_PARTY
from model.api.user import User
from model.api.person import Person

from base import BaseModel


class AuthModel(BaseModel):

    """ Authenticate a User.

    Create, fetch, and/or prepare all necessary data for storing a
    cookie that can be used for authentication and analytics tracking on
    future requests. On first login, Create and store a new User.

    This is set up so that there should be a subclass for each third
    party login implementation we support. These Subclasses need only
    override the credentials-related methods described herein. Further,
    to implement our own login, we need only implement those same
    credentials-related methods here.

    Required:

    Optional:
    User    _existing_user      the User object that corresponds to the
                                raw_user
    User    _user               the User object for this raw_user
    Person  _person             the Person object for this raw_user
    boolean _is_new             True if the User has just been created
    str     _ip                 the ip of the user
    str     _locale             the locale of the user

    Constants:
    int     MAX_ATTEMPTS        the number of tries to see if the user is in
                                our database already

    """

    MAX_ATTEMPTS = 5


    def __init__(self, session, raw_user):
        """ Construct a model that authenticates a user.

        Required:
        dict    session     a dictionary representation of the user's session
        ???     raw_user    a raw user object from authentication

        """
        super(AuthModel, self).__init__(session)

        self._raw_user = raw_user

        self._existing_user = None
        self._user = None
        self._person = None
        self._is_new = False
        self._ip = None
        self._locale = None

        # TODO: remove this when removing default league!
        self._default_league_id = None


    def set_ip(self, ip):
        """ Set the IP address for the Session to be created. """
        self._ip = ip


    def set_locale(self, locale):
        """ Set the browser locale for the Session to be created. """
        self._locale = locale


    # TODO: remove this when no longer needed!
    def set_default_league_id(self, default_league_id):
        """ Set the default League ID to join for new Users. """
        self._default_league_id = default_league_id


    def load_and_dispatch(self):
        """ Load a User from credentials and dispatch creates/updates. """
        self.load()
        self.dispatch()


    def load(self):
        """ Load an existing User from supplied login credentials. """
        # retry lookup from credentials a couple times to avoid duplicates.
        # this is an absolute and utter hackjob!
        for attempt in range(self.MAX_ATTEMPTS):
            self._existing_user = self._load_credentials(self._raw_user)
            if self._existing_user:
                break


    def dispatch(self):
        """ Dispatch a create/update based on whether a User exists. """

        # this User/Person exists; update our data with raw data.
        if self._existing_user:
            (self._user, self._person) = self._update_credentials(
                    self._raw_user,
                    self._existing_user)

        # this User/Person is new; create new ones!
        else:
            (self._user, self._person) = self._create_credentials(
                    self._raw_user,
                    self._default_league_id)

            # set a flag to alert subscribers that a new user was created!
            self._is_new = all([self._user, self._person])


    def _load_credentials(self, raw_user):
        """ Try to return an existing user for a set of credentials. """
        raise NotImplementedError("Not Yet Implemented: SUBCLASS, OVERRIDE!")


    def _update_credentials(self, old_user, raw_user):
        """ Update an existing User with new raw user credentials. """
        raise NotImplementedError("Not Yet Implemented: SUBCLASS, OVERRIDE!")


    # TODO: drop league_id from this signature when leagues are better!
    def _create_credentials(self, raw_user, league_id=None):
        """ Create a new User and Player from raw user credentials. """
        raise NotImplementedError("Not Yet Implemented: SUBCLASS, OVERRIDE!")


    def _set_raw_user(self, raw_user):
        """ Set the User for the Session to be created. """
        self.set_raw_user(raw_user)

    @property
    def user(self):
        """ Return the User for this request. """
        return self._user


    @property
    def person(self):
        """ Return the Person for this request. """
        return self._person


    @property
    def is_new(self):
        """ Return whether this User/Person is newly created. """
        return self._is_new


class FacebookAuthModel(AuthModel):

    """ Authenticate a Facebook User, and potentially have them authorize our
    application to get that authentication.

    Lookup and/or create/update a User on login with Facebook.

    On Facebook login, we attempt to fetch a User and potentially create
    or update our database with the user information supplied.

    """


    def _load_credentials(self, raw_user):
        """ Return an existing user for a set of credentials. """
        fb_id = raw_user.get(NODE_PROPERTY.ID)

        if fb_id is None:
            raise tornado.web.HTTPError(500, "No Facebook User ID.")

        return User.load_by_external_id(fb_id, THIRD_PARTY.FACEBOOK)


    def _update_credentials(self, raw_user, user):
        """ Update an existing User with new raw user credentials. """
        # TODO: implement update and use it here!
        #return User.update_user_and_player(user, raw_user)
        return (user, Person.load_leagues(user.get_default_person_id()))


    # TODO: drop league_id from this signature when leagues are better!
    def _create_credentials(self, raw_user, league_id=None, inviter_id=None):
        """ Create a new User and Player from raw user credentials. """

        # TODO: there are a lot of open questions here:
        # 1/ maybe fix this parameter list...it's ridiculous!
        # 2/ what about when we want to create a Person who isn't a Player?
        # 3/ when other credentialing options exist, it might not be good to
        #    assume exclusively.
        # 4/ is it more sensible to keep these methods separate if it turns out
        #    we can't easily generalize across other Person subclasses?

        (user, player) = User.create_user_and_player(
                PROPERTY_VALUE.EMPTY,
                PROPERTY_VALUE.EMPTY,
                None,
                PROPERTY_VALUE.EMPTY,
                PROPERTY_VALUE.EMPTY,
                {THIRD_PARTY.FACEBOOK: raw_user},
                inviter_id,
                self._ip,
                self._locale)

        # TODO: uncomment TAGGED SqEdge type and pass optional third argument.
        if league_id is not None:
            Person.join_league(player.id, league_id)

        return (user, player)
