""" Module: User

TODO: fill this in with required methods to implement since required
members aren't strictly members [they are pulled from properties].

"""

from model.constants import NODE_PROPERTY

from constants import API_EDGE_TYPE
from person import Person


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

    str     _version                what version is this user seeing?
    int     _account_status         INVITED/DECLINED/NEW/ACTIVE/INACTIVE
    ts      _last_status_change_ts  when did account status last change?
    ts      _last_login_ts          when did the last session start?
    str     _last_login_ip          what was the last session's ip?

    """


    def outgoing_edge_types(self):
        """ Return a list of allowed outgoing SqEdge types. """
        return [
                API_EDGE_TYPE.DEFAULTS_TO
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
    def version(self):
        """ Return our app version string for this User. """

        # TODO: should this be an enum or a float?

        return self._get_property(API_NODE_PROPERTY.VERSION)


    @property
    def account_status(self):
        """ Return this User's account status string.

        Enumeratued Type:
        "e_invited"
        "e_declined"
        "e_new"
        "e_active"
        "e_inactive"

        """

        # TODO: should this be an enum?

        return self._get_property(API_NODE_PROPERTY.ACCOUNT_STATUS)


    @property
    def account_status_ts(self):
        """ Return the last time this User's account status changed. """
        return self._get_property(API_NODE_PROPERTY.ACCOUNT_STATUS_TS)


    @property
    def last_login_ts(self):
        """ Return this User's last login timestamp. """
        return self._get_property(API_NODE_PROPERTY.LAST_LOGIN_TS)


    @property
    def last_login_ip(self):
        """ Return this User's last ip address. """
        return self._get_property(API_NODE_PROPERTY.LAST_LOGIN_IP)


    """ The below are duplicated in Person for now. """


    @property
    def fb_id(self):
        """ Return this User's Facebook ID. """

        # for now, this is guaranteed to be set. later, there may be other
        # third parties and some established hierarchy for checking or we may
        # have implemented our own login system.
        return self._properties.get(
                API_CONSTANT.FACEBOOK_NODE_PROPERTIES[NODE_TYPE.ID],
                None)


    @property
    def fb_username(self):
        """ Return this User's Facebook username. """
        return self._get_property(API_NODE_PROPERTY.USERNAME)


    @property
    def email(self):
        """ Return this User's email address. """
        return self._get_property(API_NODE_PROPERTY.EMAIL)


    """ The above are duplicated in Person for now. """


    # TODO FIXME XXX: convert this to create_user

    #@staticmethod
    #def create_user(league_id, creator_id, game_score):
    #    """ Create a Game and return it.
    #
    #    Required:
    #    id      league_id       league id that game belogs to
    #    id      creator_id      player id of game's creator
    #    list    game_score      final score of a game
    #                            [{"id": VALUE, "score": VALUE}]
    #
    #    Return the created game.
    #
    #    """
    #
    #    # prepare a node prototype for this game
    #    prototype_node = editor.prototype_node(API_NODE_TYPE.GAME, {})
    #
    #    prototype_edges = []
    #
    #    # prepare edge prototypes for schedule edges
    #    prototype_edges.extend(editor.prototype_edge_and_complement(
    #            API_EDGE_TYPE.SCHEDULED_IN,
    #            {},
    #            league_id))
    #
    #    # prepare edge prototypes for creator edges
    #    prototype_edges.extend(editor.prototype_edge_and_complement(
    #            API_EDGE_TYPE.CREATED_BY,
    #            {},
    #            creator_id))
    #
    #    # get outcome from gamescore
    #    outcome = Game.calculate_outcome(game_score)
    #
    #    # prepare edge prototypes for result edges
    #    for type, result in outcome.items():
    #        for opponent_score in result:
    #            prototype_edges.extend(editor.prototype_edge_and_complement(
    #                type,
    #                {API_EDGE_PROPERTY.SCORE: opponent_score["score"]},
    #                opponent_score["id"]))
    #
    #    return editor.create_node_and_edges(prototype_node, prototype_edges)
 
