""" Module: API Constants

...

"""

from util.decorators import constant
from model.constants import NODE_PROPERTY, EDGE_PROPERTY


class _APINodeType(object):
    
    """ _APINodeType class to hold all Node Types. """


    @constant
    def GAME(self):
        """ GAME is a Type of Node. """
        return "n_game"


    @constant
    def LEAGUE(self):
        """ LEAGUE is a Type of Node. """
        return "n_league"


    @constant
    def PLAYER(self):
        """ PLAYER is a Type of Node. """
        return "n_player"


    @constant
    def TEAM(self):
        """ TEAM is a Type of Node. """
        return "n_team"


    @constant
    def USER(self):
        """ USER is a Type of Node. """
        return "n_user"


class _APIEdgeType(object):

    """ _APIEdgeType class to hold all Edge Types. """


    @constant
    def IN_LEAGUE(self):
        """ IN_LEAGUE is a Type of Edge. """
        return "e_in_league"


    @constant
    def HAS_LEAGUE_MEMBER(self):
        """ HAS_LEAGUE_MEMBER is a Type of Edge. """
        return "e_has_league_member"


    @constant
    def SCHEDULED_IN(self):
        """ SCHEDULED_IN is a Type of Edge. """
        return "e_scheduled_in"


    @constant
    def HAS_SCHEDULED(self):
        """ HAS_SCHEDULED is a Type of Edge. """
        return "e_has_scheduled"
    

    @constant
    def WON(self):
        """ WON is a Type of Edge. """
        return "e_won"


    @constant
    def WON_BY(self):
        """ WON_BY is a Type of Edge. """
        return "e_won_by"


    @constant
    def LOST(self):
        """ LOST is a Type of Edge. """
        return "e_lost"


    @constant
    def LOST_BY(self):
        """ LOST_BY is a Type of Edge. """
        return "e_lost_by"


    @constant
    def TIED(self):
        """ TIED is a Type of Edge. """
        return "e_tied"


    @constant
    def TIED_BY(self):
        """ TIED_BY is a Type of Edge. """
        return "e_tied_by"


    @constant
    def PLAYED(self):
        """ PLAYED is a Type of Edge. """
        return "e_played"


    @constant
    def PLAYED_BY(self):
        """ PLAYED_BY is a Type of Edge. """
        return "e_played_by"


    @constant
    def CREATED(self):
        """ CREATED is a Type of Edge. """
        return "e_created"


    @constant
    def CREATED_BY(self):
        """ CREATED_BY is a Type of Edge. """
        return "e_created_by"


    @constant
    def DEFAULTS_TO(self):
        """ DEFAULTS_TO is a Type of Edge.

        User > Player : DEFAULTS_TO

        """
        return "e_defaults_to"


    @constant
    def HAS_PRIMARY(self):
        """ HAS_PRIMARY is a Type of Edge.

        Player > User : HAS_PRIMARY

        """
        return "e_has_primary"


class _APINodeProperty(object):

    """ _APINodeProperty class to hold all Node Properties. """


    @constant
    def NAME(self):
        """ NAME is a Property of Node. """
        return "n_name"


    @constant
    def FIRST_NAME(self):
        """ FIRST_NAME is a Property of Node. """
        return "n_first_name"


    @constant
    def MIDDLE_NAME(self):
        """ MIDDLE_NAME is a Property of Node. """
        return "n_middle_name"


    @constant
    def LAST_NAME(self):
        """ LAST_NAME is a Property of Node. """
        return "n_last_name"


    @constant
    def LINK(self):
        """ LINK is a Property of Node. """
        return "n_link"


    @constant
    def USERNAME(self):
        """ USERNAME is a Property of Node. """
        return "n_username"


    @constant
    def GENDER(self):
        """ GENDER is a Property of Node. """
        return "n_gender"


    @constant
    def TIMEZONE(self):
        """ TIMEZONE is a Property of Node. """
        return "n_timezone"


    @constant
    def LOCALE(self):
        """ LOCALE is a Property of Node. """
        return "n_locale"


    @constant
    def PICTURE(self):
        """ PICTURE is a Property of Node. """
        return "n_picture"


    @constant
    def EMAIL(self):
        """ EMAIL is a Property of Node. """
        return "n_email"


    @constant
    def VERSION(self):
        """ VERSION is a Property of Node. """
        return "n_version"


    @constant
    def ACCOUNT_STATUS(self):
        """ ACCOUNT_STATUS is a Property of Node. """
        return "n_account_status"


    @constant
    def ACCOUNT_STATUS_TS(self):
        """ ACCOUNT_STATUS_TS is a Property of Node. """
        return "n_account_status_ts"


    @constant
    def LAST_LOGIN_TS(self):
        """ LAST_LOGIN_TS is a Property of Node. """
        return "n_last_login_ts"


    @constant
    def LAST_LOGIN_IP(self):
        """ LAST_LOGIN_IP is a Property of Node. """
        return "n_last_login_ip"


class _APIEdgeProperty(object):

    """ _APIEdgeProperty class to hold all Edge Properties. """


    @constant
    def SCORE(self):
        """ SCORE is a Property of Edge. """
        return "e_score"


# these are variables used to refer to the above classes. some of them are used
# in _APINodeTypes and _APIEdgeTypes, so we have to make sure to declare them
# before defining those classes.
API_NODE_TYPE = _APINodeType()
API_EDGE_TYPE = _APIEdgeType()
API_NODE_PROPERTY = _APINodeProperty()
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
    def ACTOR_NODE_TYPES(self):
        """ ACTOR_NODE_TYPES is a list of Actor Node Types. """
        return [
                API_NODE_TYPE.PLAYER
                ]


    @constant
    def FACEBOOK_NODE_PROPERTIES(self):
        """ FACEBOOK_NODE_PROPERTIES is a dict of Facebook Node
        Properties.
        
        """
        
        return {
                NODE_PROPERTY.ID :              "fb_id",
                API_NODE_PROPERTY.NAME :        "fb_name",
                API_NODE_PROPERTY.FIRST_NAME :  "fb_first_name",
                API_NODE_PROPERTY.MIDDLE_NAME : "fb_middle_name",
                API_NODE_PROPERTY.LAST_NAME :   "fb_last_name",
                API_NODE_PROPERTY.LINK :        "fb_link",
                API_NODE_PROPERTY.USERNAME :    "fb_username",
                API_NODE_PROPERTY.GENDER :      "fb_gender",
                API_NODE_PROPERTY.TIMEZONE :    "fb_timezone",
                API_NODE_PROPERTY.LOCALE :      "fb_locale",
                API_NODE_PROPERTY.PICTURE :     "fb_picture",
                API_NODE_PROPERTY.EMAIL :       "fb_email"
                }


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
                API_EDGE_TYPE.IN_LEAGUE : API_EDGE_TYPE.HAS_LEAGUE_MEMBER,
                API_EDGE_TYPE.HAS_LEAGUE_MEMBER : API_EDGE_TYPE.IN_LEAGUE,

                API_EDGE_TYPE.SCHEDULED_IN : API_EDGE_TYPE.HAS_SCHEDULED,
                API_EDGE_TYPE.HAS_SCHEDULED : API_EDGE_TYPE.SCHEDULED_IN,

                API_EDGE_TYPE.CREATED : API_EDGE_TYPE.CREATED_BY,
                API_EDGE_TYPE.CREATED_BY : API_EDGE_TYPE.CREATED,

                API_EDGE_TYPE.WON : API_EDGE_TYPE.WON_BY,
                API_EDGE_TYPE.WON_BY : API_EDGE_TYPE.WON,

                API_EDGE_TYPE.LOST : API_EDGE_TYPE.LOST_BY,
                API_EDGE_TYPE.LOST_BY : API_EDGE_TYPE.LOST,

                API_EDGE_TYPE.TIED : API_EDGE_TYPE.TIED_BY,
                API_EDGE_TYPE.TIED_BY : API_EDGE_TYPE.TIED,

                API_EDGE_TYPE.PLAYED : API_EDGE_TYPE.PLAYED_BY,
                API_EDGE_TYPE.PLAYED_BY : API_EDGE_TYPE.PLAYED
                }


API_CONSTANT = _APIConstant()

