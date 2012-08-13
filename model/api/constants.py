""" Module: API Constants

...

"""

from util.decorators import constant


class _APINodeType(object):

    """ Hold all Node Types. """

    @constant
    def GAME(self):
        return "game"

    @constant
    def LEAGUE(self):
        return "league"

    @constant
    def PLAYER(self):
        return "player"

    @constant
    def TEAM(self):
        return "team"

    @constant
    def USER(self):
        return "user"


API_NODE_TYPE = _APINodeType()


class _APIEdgeType(object):

    """ Hold all Edge Types. """

    @constant
    def COMMENTED_ON(self):
        return "commented_on"

    @constant
    def HAS_COMMENT_FROM(self):
        return "has_comment_from"

    @constant
    def IN_LEAGUE(self):
        return "in_league"

    @constant
    def HAS_LEAGUE_MEMBER(self):
        return "has_league_member"

    @constant
    def SCHEDULED_IN(self):
        return "scheduled_in"

    @constant
    def HAS_SCHEDULED(self):
        return "has_scheduled"

    @constant
    def WON(self):
        return "won"

    @constant
    def WON_BY(self):
        return "won_by"

    @constant
    def LOST(self):
        return "lost"

    @constant
    def LOST_BY(self):
        return "lost_by"

    @constant
    def TIED(self):
        return "tied"

    @constant
    def TIED_BY(self):
        return "tied_by"

    @constant
    def PLAYED(self):
        return "played"

    @constant
    def PLAYED_BY(self):
        return "played_by"

    @constant
    def CREATED(self):
        return "created"

    @constant
    def CREATED_BY(self):
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


API_EDGE_TYPE = _APIEdgeType()


class _APINodeProperty(object):

    """ Hold all Node Properties. """

    @constant
    def NAME(self):
        return "name"

    @constant
    def FIRST_NAME(self):
        return "first_name"

    @constant
    def MIDDLE_NAME(self):
        return "middle_name"

    @constant
    def LAST_NAME(self):
        return "last_name"

    @constant
    def LINK(self):
        return "link"

    @constant
    def USERNAME(self):
        return "username"

    @constant
    def GENDER(self):
        return "gender"

    @constant
    def TIMEZONE(self):
        return "timezone"

    @constant
    def LOCALE(self):
        return "locale"

    @constant
    def PICTURE(self):
        return "picture"

    @constant
    def BIG_PICTURE(self):
        return "big_picture"

    @constant
    def EMAIL(self):
        return "email"

    @constant
    def PASSWORD_HASH(self):
        return "password_hash"

    @constant
    def LAST_IP(self):
        return "last_ip"

    @constant
    def LAST_LOGIN_TS(self):
        return "last_login_ts"

    @constant
    def LAST_AUTHORIZED_TS(self):
        return "last_authorized_ts"

    @constant
    def LAST_DEAUTHORIZED_TS(self):
        return "last_deauthorized_ts"

    @constant
    def REFERRER_URL(self):
        return "referrer_url"

    @constant
    def SPORT_ID(self):
        return "sport_id"


API_NODE_PROPERTY = _APINodeProperty()


class _APIEdgeProperty(object):

    """ Hold all Edge Properties. """

    @constant
    def SCORE(self):
        return "score"


    @constant
    def MESSAGE(self):
        return "message"


API_EDGE_PROPERTY = _APIEdgeProperty()


class _APIConstant(object):

    """ _APIConstant defines other Node and Edge Type and Property
    constants. """

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

                API_EDGE_TYPE.COMMENTED_ON: API_EDGE_TYPE.HAS_COMMENT_FROM,
                API_EDGE_TYPE.HAS_COMMENT_FROM: API_EDGE_TYPE.COMMENTED_ON,
                }


API_CONSTANT = _APIConstant()
