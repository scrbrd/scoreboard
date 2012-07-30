""" Module: API Constants

...

"""

from util.decorators import constant


class _APINodeType(object):

    """ _APINodeType class to hold all Node Types. """


    @constant
    def GAME(self):
        """ GAME is a Type of Node. """
        return "game"


    @constant
    def LEAGUE(self):
        """ LEAGUE is a Type of Node. """
        return "league"


    @constant
    def PLAYER(self):
        """ PLAYER is a Type of Node. """
        return "player"


    @constant
    def TEAM(self):
        """ TEAM is a Type of Node. """
        return "team"


    @constant
    def USER(self):
        """ USER is a Type of Node. """
        return "user"


# intentionally make this declaration now so that we can refer to it below.
API_NODE_TYPE = _APINodeType()


class _APIEdgeType(object):

    """ _APIEdgeType class to hold all Edge Types. """


    @constant
    def IN_LEAGUE(self):
        """ IN_LEAGUE is a Type of Edge. """
        return "in_league"


    @constant
    def HAS_LEAGUE_MEMBER(self):
        """ HAS_LEAGUE_MEMBER is a Type of Edge. """
        return "has_league_member"


    @constant
    def SCHEDULED_IN(self):
        """ SCHEDULED_IN is a Type of Edge. """
        return "scheduled_in"


    @constant
    def HAS_SCHEDULED(self):
        """ HAS_SCHEDULED is a Type of Edge. """
        return "has_scheduled"


    @constant
    def WON(self):
        """ WON is a Type of Edge. """
        return "won"


    @constant
    def WON_BY(self):
        """ WON_BY is a Type of Edge. """
        return "won_by"


    @constant
    def LOST(self):
        """ LOST is a Type of Edge. """
        return "lost"


    @constant
    def LOST_BY(self):
        """ LOST_BY is a Type of Edge. """
        return "lost_by"


    @constant
    def TIED(self):
        """ TIED is a Type of Edge. """
        return "tied"


    @constant
    def TIED_BY(self):
        """ TIED_BY is a Type of Edge. """
        return "tied_by"


    @constant
    def PLAYED(self):
        """ PLAYED is a Type of Edge. """
        return "played"


    @constant
    def PLAYED_BY(self):
        """ PLAYED_BY is a Type of Edge. """
        return "played_by"


    @constant
    def CREATED(self):
        """ CREATED is a Type of Edge. """
        return "created"


    @constant
    def CREATED_BY(self):
        """ CREATED_BY is a Type of Edge. """
        return "created_by"


    @constant
    def SPAWNED(self):
        """ SPAWNED is a Type of Edge.

        User > Person : SPAWNED

        Like CREATED, but functionally the User/Person relationship is
        a bit different than the Person/Entity relationship.

        Like OWNS, but implies creation instead of ownership. For
        example, when Player A owned by User X tags non-existent Player
        B in Game G, User X spawns Player B and invites non-existent
        User Y, and User Y will own Player B.

        """
        return "spawned"


    @constant
    def SPAWNED_BY(self):
        """ SPAWNED_BY is a Type of Edge.

        Person > User : SPAWNED_BY

        Like CREATED_BY, but functionally the Person/User relationship
        is a bit different than the Entity/Person relationship.

        Like OWNED_BY, but implies creation instead of ownership.

        """
        return "spawned_by"


    @constant
    def OWNS(self):
        """ OWNS is a Type of Edge.

        User > Person : OWNS

        """
        return "owns"


    @constant
    def OWNED_BY(self):
        """ OWNED_BY is a Type of Edge.

        Person > User : OWNED_BY

        """
        return "owned_by"


    @constant
    def DEFAULTS_TO(self):
        """ DEFAULTS_TO is a Type of Edge.

        User > Person : DEFAULTS_TO

        Denotes the default owned Person a User controls upon login.

        """
        return "defaults_to"


    @constant
    def HAS_PRIMARY(self):
        """ HAS_PRIMARY is a Type of Edge.

        Person > User : HAS_PRIMARY

        Denotes the primary User among the owners who control a Person.

        """
        return "has_primary"


    #@constant
    #def INVITED(self):
    #    """ INVITED is a Type of Edge.
    #
    #    User > User : INVITED
    #
    #    """
    #    return "invited"
    #
    #
    #@constant
    #def INVITED_BY(self):
    #    """ INVITED_BY is a Type of Edge.
    #
    #    User > User : INVITED_BY
    #
    #    """
    #    return "invited_by"
    #
    #
    #@constant
    #def TAGGED(self):
    #    """ TAGGED is a Type of Edge.
    #
    #    Person > Person : TAGGED
    #
    #    """
    #    return "tagged"
    #
    #
    #@constant
    #def TAGGED_BY(self):
    #    """ TAGGED_BY is a Type of Edge.
    #
    #    Person > Person : TAGGED_BY
    #
    #    """
    #    return "tagged_by"


# intentionally make this declaration now so that we can refer to it below.
API_EDGE_TYPE = _APIEdgeType()


class _APINodeProperty(object):

    """ _APINodeProperty class to hold all Node Properties. """


    @constant
    def NAME(self):
        """ NAME is a Property of Node. """
        return "name"


    @constant
    def FIRST_NAME(self):
        """ FIRST_NAME is a Property of Node. """
        return "first_name"


    @constant
    def MIDDLE_NAME(self):
        """ MIDDLE_NAME is a Property of Node. """
        return "middle_name"


    @constant
    def LAST_NAME(self):
        """ LAST_NAME is a Property of Node. """
        return "last_name"


    @constant
    def LINK(self):
        """ LINK is a Property of Node. """
        return "link"


    @constant
    def USERNAME(self):
        """ USERNAME is a Property of Node. """
        return "username"


    @constant
    def GENDER(self):
        """ GENDER is a Property of Node. """
        return "gender"


    @constant
    def TIMEZONE(self):
        """ TIMEZONE is a Property of Node. """
        return "timezone"


    @constant
    def LOCALE(self):
        """ LOCALE is a Property of Node. """
        return "locale"


    @constant
    def PICTURE(self):
        """ PICTURE is a Property of Node. """
        return "picture"


    @constant
    def EMAIL(self):
        """ EMAIL is a Property of Node. """
        return "email"


    @constant
    def PASSWORD_HASH(self):
        """ PASSWORD_HASH is a Property of Node. """
        return "password_hash"


    @constant
    def LAST_IP(self):
        """ LAST_IP is a Property of Node. """
        return "last_ip"


    @constant
    def LAST_LOGIN_TS(self):
        """ LAST_LOGIN_TS is a Property of Node. """
        return "last_login_ts"


    @constant
    def LAST_AUTHORIZED_TS(self):
        """ LAST_AUTHORIZED_TS is a Property of Node. """
        return "last_authorized_ts"


    @constant
    def LAST_DEAUTHORIZED_TS(self):
        """ LAST_DEAUTHORIZED_TS is a Property of Node. """
        return "last_deauthorized_ts"


    @constant
    def REFERRER_URL(self):
        """ REFERRER_URL is a Property of Node. """
        return "referrer_url"


API_NODE_PROPERTY = _APINodeProperty()


class _APIEdgeProperty(object):

    """ _APIEdgeProperty class to hold all Edge Properties. """


    @constant
    def SCORE(self):
        """ SCORE is a Property of Edge. """
        return "score"


API_EDGE_PROPERTY = _APIEdgeProperty()


class _APIConstant(object):

    """ _APIConstant defines other Node and Edge Type and Property
    constants.

    """


    @constant
    def OPPONENT_NODE_TYPES(self):
        """ OPPONENT_NODE_TYPES is a list of Opponent Node Types. """
        return [
                API_NODE_TYPE.PLAYER,
                API_NODE_TYPE.TEAM
                ]


    @constant
    def RESULT_EDGE_TYPES(self):
        """ RESULT_EDGE_TYPES is a list of Result Edge Types. """
        return [
                API_EDGE_TYPE.WON,
                API_EDGE_TYPE.WON_BY,
                API_EDGE_TYPE.LOST,
                API_EDGE_TYPE.LOST_BY,
                API_EDGE_TYPE.TIED,
                API_EDGE_TYPE.TIED_BY,
                API_EDGE_TYPE.PLAYED,
                API_EDGE_TYPE.PLAYED_BY
                ]


    @constant
    def EDGE_TYPE_COMPLEMENTS(self):
        """ EDGE_TYPE_COMPLEMENTS is a dict mapping of Edge Types. """
        return {
                API_EDGE_TYPE.IN_LEAGUE: API_EDGE_TYPE.HAS_LEAGUE_MEMBER,
                API_EDGE_TYPE.HAS_LEAGUE_MEMBER: API_EDGE_TYPE.IN_LEAGUE,

                API_EDGE_TYPE.SCHEDULED_IN: API_EDGE_TYPE.HAS_SCHEDULED,
                API_EDGE_TYPE.HAS_SCHEDULED: API_EDGE_TYPE.SCHEDULED_IN,

                API_EDGE_TYPE.WON: API_EDGE_TYPE.WON_BY,
                API_EDGE_TYPE.WON_BY: API_EDGE_TYPE.WON,

                API_EDGE_TYPE.LOST: API_EDGE_TYPE.LOST_BY,
                API_EDGE_TYPE.LOST_BY: API_EDGE_TYPE.LOST,

                API_EDGE_TYPE.TIED: API_EDGE_TYPE.TIED_BY,
                API_EDGE_TYPE.TIED_BY: API_EDGE_TYPE.TIED,

                API_EDGE_TYPE.PLAYED: API_EDGE_TYPE.PLAYED_BY,
                API_EDGE_TYPE.PLAYED_BY: API_EDGE_TYPE.PLAYED,

                API_EDGE_TYPE.CREATED: API_EDGE_TYPE.CREATED_BY,
                API_EDGE_TYPE.CREATED_BY: API_EDGE_TYPE.CREATED,

                API_EDGE_TYPE.SPAWNED: API_EDGE_TYPE.SPAWNED_BY,
                API_EDGE_TYPE.SPAWNED_BY: API_EDGE_TYPE.SPAWNED,

                API_EDGE_TYPE.OWNS: API_EDGE_TYPE.OWNED_BY,
                API_EDGE_TYPE.OWNED_BY: API_EDGE_TYPE.OWNS,

                }


API_CONSTANT = _APIConstant()
