""" Module: User

TODO: fill this in with required methods to implement since required
members aren't strictly members [they are pulled from properties].

"""

from time import time

from model.constants import NODE_PROPERTY, THIRD_PARTY, PROPERTY_VALUE

from constants import API_NODE_TYPE, API_EDGE_TYPE, API_NODE_PROPERTY

from sqobject import SqNode
from player import Player
import loader
import editor


class User(SqNode):

    """ User is a subclass of SqNode.

    Provide access to the attributes of a User, including fields and
    edges connecting to other nodes.

    Sqoreboard bases its user and account, for now, on Facebook in order
    to simplify login and credentialing. This represents the basic data
    we can access without asking for any extra permissions.

    TODO: determine if timezone requires a permission...it was unclear.

    From Facebook, the following require no access_token:

    Name        Type    Description

    id          str     user's Facebook ID
    name        str     user's full name
    first_name  str     user's first name
    middle_name str     user's middle name
    last_name   str     user's last name
    link        url     user's profile URL
    username    str     user's Facebook username
    gender      str     user's gender: female or male
    timezone    int     user's timezone offset from UTC
    locale      str     user's locale: ISO language and country code
    picture     url     user's profile pic URL (must set fields=picture)

    https://graph.facebook.com/me

    {
        "id": "1008386",
        "name": "Jon Warman",
        "first_name": "Jon",
        "last_name": "Warman",
        "link": "https://www.facebook.com/warman",
        "username": "warman",
        "gender": "male",
        "timezone": -4,
        "locale": "en_US",
        "picture": "https://fbcdn-profile-a.akamaihd.net/
                    hprofile-ak-ash2/48972_1008386_2741_q.jpg"
    }

    The following represents how we do things at Sqoreboard, some of
    which we do in the Person interface instead of here...

    Required:

    int     _fb_id              Facebook user ID
    str     _fb_name            Facebook user full name
    str     _fb_first_name      Facebook user first name
    str     _fb_middle_name     Facebook user middle name
    str     _fb_last_name       Facebook user last name
    url     _fb_link            Facebook user profile url
    str     _fb_username        Facebook user username
    str     _fb_gender          Facebook user gender: "male"/"female"
    int     _fb_timezone        Facebook current user UTC offset
    str     _fb_locale          Facebook user locale: ISO lang+country
    url     _fb_picture         Facebook user profile picture url

    str     _fb_email           Facebook user contact/login email

    str     _locale                 user locale: ISO lang+country
    str     _last_ip                what was the last session's ip?
    ts      _last_login_ts          when did the last session start?
    ts      _last_authorized_ts     when was an auth token last created?
    ts      _last_deauthorized_ts   when was an auth token last revoked?
    url     _referrer_url           what url, if any, sourced this user?


    TODO: include these member methods:

        def is_new(self):
        def is_active_daily(self):
        def is_active_weekly(self):
        def is_active_monthly(self):
        def is_active_since(self, num_days):
        def is_inactive(self):
        def is_invited(self):
        def is_declined(self):
        def is_authorized(self):
        def is_deauthorized(self):
        def is_deleted(self):

    """


    def outgoing_edge_types(self):
        """ Return a list of allowed outgoing SqEdge types. """
        return [
                API_EDGE_TYPE.SPAWNED,
                API_EDGE_TYPE.OWNS,
                API_EDGE_TYPE.DEFAULTS_TO,
                #API_EDGE_TYPE.INVITED,
                #API_EDGE_TYPE.INVITED_BY,
                ]


    @property
    def timezone(self):
        """ Return this User's timezone as a signed int UTC offset. """
        return self._get_property(API_NODE_PROPERTY.TIMEZONE)


    @property
    def locale(self):
        """ Return a this User's locale string (ISO lang + country). """
        return self._get_property(API_NODE_PROPERTY.LOCALE)


    @property
    def last_ip(self):
        """ Return this User's last ip address. """
        return self._get_property(API_NODE_PROPERTY.LAST_IP)


    @property
    def last_login_ts(self):
        """ Return this User's last login timestamp. """
        return self._get_property(API_NODE_PROPERTY.LAST_LOGIN_TS)


    @property
    def last_authorized_ts(self):
        """ Return this User's last authorization timestamp. """
        return self._get_property(API_NODE_PROPERTY.LAST_AUTHORIZED_TS)


    @property
    def last_deauthorized_ts(self):
        """ Return this User's last deauthorization timestamp. """
        return self._get_property(API_NODE_PROPERTY.LAST_DEAUTHORIZED_TS)


    @property
    def referrer_url(self):
        """ Return the url that referred this User to be created. """
        return self._get_property(API_NODE_PROPERTY.REFERRER_URL)


    """ The below are duplicated in Person for now. """


    @property
    def fb_id(self):
        """ Return this User's Facebook ID. """

        # TODO: for now, we guarantee this is set. later, there may be other
        # third parties and some established hierarchy for checking or we may
        # have implemented our own login system.

        # signal _get_property() to bypass NODE_PROPERTY.ID since that field is
        # guaranteed to always be set and we explicitly want the Facebook ID.
        return self._get_property(NODE_PROPERTY.ID, THIRD_PARTY.FACEBOOK, True)


    @property
    def fb_username(self):
        """ Return this User's Facebook username. """
        return self._get_property(API_NODE_PROPERTY.USERNAME)


    @property
    def email(self):
        """ Return this User's email address. """
        return self._get_property(API_NODE_PROPERTY.EMAIL)


    """ The above are duplicated in Person for now. """


    def get_default_person_id(self):
        """ Return the ID of the Person to default to for this User. """
        return self.get_to_node_ids_by_type(API_EDGE_TYPE.DEFAULTS_TO)[0]


    """ STATIC METHODS """

    @staticmethod
    def property_keys():
        """ Return a list of permitted property fields for User. """
        return [
                API_NODE_PROPERTY.EMAIL,
                API_NODE_PROPERTY.PASSWORD_HASH,
                API_NODE_PROPERTY.USERNAME,
                API_NODE_PROPERTY.TIMEZONE,
                API_NODE_PROPERTY.LOCALE,
                API_NODE_PROPERTY.LAST_IP,
                API_NODE_PROPERTY.LAST_LOGIN_TS,
                API_NODE_PROPERTY.LAST_AUTHORIZED_TS,
                API_NODE_PROPERTY.LAST_DEAUTHORIZED_TS,
                API_NODE_PROPERTY.REFERRER_URL,
                ]


    @staticmethod
    def create_user_and_player(
            email,
            password_hash,
            referrer_url,
            first_name,
            last_name,
            third_parties={},
            inviter_id=None,
            ip=None,
            locale=None):
        """ Create a User and Player atomically and return both.

        Required:
        str     email               created User's email
        str     password_hash       created User's encrypted password
        url     referrer_url        source link clicked to cause this
        str     first_name          created Player's first name
        str     last_name           created Player's last name

        Optional:
        dict    third_parties       key/val dicts keyed on 3rd party
        id      inviter_id          User inviting/spawning User/Player
        str     ip                  User's IP, if logged in
        str     locale              User's locale (ISO language+country)

        Return:
        tuple                       (User, Player)

        Example:
        Optional parameter third_parties should be defined as follows:

        {
            "fb" : {<CONVERT FROM JSON TO DICT AND LEAVE DATA AS IS>},
            "tw" : {<CONVERT FROM JSON TO DICT AND LEAVE DATA AS IS>},
        }

        This will be flattened, validated, and culled by SqNode.

        """

        user = User.create_user(
                email,
                password_hash,
                referrer_url,
                third_parties,
                inviter_id,
                ip,
                locale)

        owner_id = user.id
        spawner_id = inviter_id if inviter_id is not None else owner_id

        player = Player.create_player(
                first_name,
                last_name,
                spawner_id,
                owner_id,
                third_parties)

        return (user, player)


    @staticmethod
    def create_user(
            email,
            password_hash,
            referrer_url,
            third_parties={},
            inviter_id=None,
            ip=PROPERTY_VALUE.EMPTY,
            locale=PROPERTY_VALUE.EMPTY):
        """ Create a User and return it.

        Required:
        str     email           created User's email
        str     password_hash   created User's encrypted password
        url     referrer_url    source link clicked to cause this

        Optional:
        dict    third_parties   key/val dicts keyed on 3rd party
        id      inviter_id      User inviting/spawning User/Person
        str     ip              User's IP, if logged in
        str     locale          User's locale (ISO language+country)

        Return:
        User                    SqNode can log in, act as other SqNodes

        Example:
        Optional parameter third_parties should be defined as follows:

        {
            "fb" : {<CONVERT FROM JSON TO DICT AND LEAVE DATA AS IS>},
            "tw" : {<CONVERT FROM JSON TO DICT AND LEAVE DATA AS IS>},
        }

        This will be flattened, validated, and culled by SqNode.

        """

        # TODO: when there's an alternative to Facebook for login, revisit
        # authorization logic. some of this logic might be context-dependent.

        # email, password_hash, username, timezone, and locale are just being
        # initialized for now; we get these values from Facebook, but they
        # deserve placeholders in case we have to remove third party data.

        # these properties are not explicitly required. one or more third
        # parties may provide them instead.
        raw_properties = {
                API_NODE_PROPERTY.EMAIL: email,
                API_NODE_PROPERTY.PASSWORD_HASH: password_hash,
                }

        # TODO: figure out what else to do with referrer_url

        # no ip address would mean this user isn't logged in at creation time,
        # in which case the initialized empty values suffice.
        if ip:
            current_ts = int(time())

            raw_properties.update({
                API_NODE_PROPERTY.REFERRER_URL: referrer_url,
                API_NODE_PROPERTY.LAST_IP: ip,
                API_NODE_PROPERTY.LOCALE: locale,
                API_NODE_PROPERTY.LAST_LOGIN_TS: current_ts,
                API_NODE_PROPERTY.LAST_AUTHORIZED_TS: current_ts,
                })

        # squash the two into one set of flat, valid node properties
        properties = SqNode.prepare_node_properties(
                User.property_keys(),
                raw_properties,
                third_parties)

        # TODO: add a static method call to generically check required fields
        # against statically defined lists in each class.

        # prepare a node prototype for this user
        prototype_node = editor.prototype_node(
                API_NODE_TYPE.USER,
                properties)

        # TODO: prepare an edge prototype for the inviter_id

        return editor.create_node_and_edges(prototype_node, [])


    @staticmethod
    def load_by_id(id):
        """ Return a User by its id property. """
        return loader.load_node(id)


    @staticmethod
    def load_by_email(email):
        """ Return a User by its indexed email property. """
        return loader.load_node_by_unique_property(
                API_NODE_PROPERTY.EMAIL,
                email,
                [API_NODE_TYPE.USER])


    @staticmethod
    def load_by_external_id(x_id, third_party):
        """ Return a User by its indexed external id property. """
        return loader.load_node_by_unique_property(
                SqNode.third_party_property_key(third_party, NODE_PROPERTY.ID),
                x_id,
                [API_NODE_TYPE.USER])


    @staticmethod
    def load_by_external_email(x_email, third_party):
        """ Return a User by its indexed external email property. """
        key = SqNode.third_party_property_key(third_party, NODE_PROPERTY.EMAIL)

        return loader.load_node_by_unique_property(
                key,
                x_email,
                [API_NODE_TYPE.USER])
