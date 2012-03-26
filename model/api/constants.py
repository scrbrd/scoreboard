""" API Constants

...

"""

def constant(f):
    """ Constant Decorator to make constants Final. """
    

    def fset(self, value):
        """ Overload constant function's set to disable."""
        raise SyntaxError
    

    def fget(self):
        """ Overload constant function's get. """
        return f()

    return property(fget, fset)


class _NodeType(object):
    
    """ _NodeType class to hold all Node Types. """


    @constant
    def GAME():
        """ GAME is a Type of Node. """
        return "c_game"


    @constant
    def LEAGUE():
        """ LEAGUE is a Type of Node. """
        return "c_league"


    @constant
    def PLAYER():
        """ PLAYER is a Type of Node. """
        return "c_player"


    @constant
    def TEAM():
        """ TEAM is a Type of Node. """
        return "c_team"


    @constant
    def USER():
        """ USER is a Type of Node. """
        return "c_user"


class _EdgeType(object):

    """ _EdgeType class to hold all Edge Types. """


    @constant
    def IN_LEAGUE():
        """ IN_LEAGUE is a Type of Edge. """
        return "c_in_league"


    @constant
    def HAS_LEAGUE_MEMBER():
        """ HAS_LEAGUE_MEMBER is a Type of Edge. """
        return "c_has_league_member"


    @constant
    def SCHEDULED_IN():
        """ SCHEDULED_IN is a Type of Edge. """
        return "c_scheduled_in"


    @constant
    def HAS_SCHEDULED():
        """ HAS_SCHEDULED is a Type of Edge. """
        return "c_has_scheduled"
    

    @constant
    def WON():
        """ WON is a Type of Edge. """
        return "c_won"


    @constant
    def WON_BY():
        """ WON_BY is a Type of Edge. """
        return "c_won_by"


    @constant
    def LOST():
        """ LOST is a Type of Edge. """
        return "c_lost"


    @constant
    def LOST_BY():
        """ LOST_BY is a Type of Edge. """
        return "c_lost_by"


    @constant
    def TIED():
        """ TIED is a Type of Edge. """
        return "c_tied"


    @constant
    def TIED_BY():
        """ TIED_BY is a Type of Edge. """
        return "c_tied_by"


    @constant
    def PLAYED():
        """ PLAYED is a Type of Edge. """
        return "c_played"


    @constant
    def PLAYED_BY():
        """ PLAYED_BY is a Type of Edge. """
        return "c_played_by"


    @constant
    def CREATED():
        """ CREATED is a Type of Edge. """
        return "c_created"


    @constant
    def CREATED_BY():
        """ CREATED_BY is a Type of Edge. """
        return "c_created_by"


# variables used to refer to Node and Edge Type Constants
# needs to be above _APIConstant and below the Types
NODE_TYPE = _NodeType()
EDGE_TYPE = _EdgeType()


class _NodeProperty(object):

    """ _NodeProperty class to hold all Node Properties. """

    pass


class _EdgeProperty(object):

    """ _EdgeProperty class to hold all Edge Properties. """


    @constant
    def SCORE():
        """ SCORE is a Type of Edge Property. """
        return "c_score"


# variables used to refer to Node and Edge Properties
NODE_PROPERTY = _NodeProperty()
EDGE_PROPERTY = _EdgeProperty()




class _APIConstant(object):

    """ _APIConstant class holds all API constants. """


    @constant
    def OPPONENT_TYPES():
        """ OPPONENT_NODE_TYPES is a list of Opponent Node Types. """
        return [NODE_TYPE.PLAYER, NODE_TYPE.TEAM]


    @constant
    def RESULT_TYPES():
        """ RESULT_TYPES is a list of Result Edge Types. """
        return [
                EDGE_TYPE.WON,
                EDGE_TYPE.WON_BY,
                EDGE_TYPE.LOST,
                EDGE_TYPE.LOST_BY,
                EDGE_TYPE.TIED,
                EDGE_TYPE.TIED_BY,
                EDGE_TYPE.PLAYED,
                EDGE_TYPE.PLAYED_BY]


    @constant
    def EDGE_TYPE_COMPLEMENTS():
        """ EDGE_TYPE_COMPLEMENTS is a dict mapping of Edge Types. """
        return {
                EDGE_TYPE.IN_LEAGUE : EDGE_TYPE.HAS_LEAGUE_MEMBER,
                EDGE_TYPE.HAS_LEAGUE_MEMBER : EDGE_TYPE.IN_LEAGUE,

                EDGE_TYPE.SCHEDULED_IN : EDGE_TYPE.HAS_SCHEDULED,
                EDGE_TYPE.HAS_SCHEDULED : EDGE_TYPE.SCHEDULED_IN,

                EDGE_TYPE.CREATED : EDGE_TYPE.CREATED_BY,
                EDGE_TYPE.CREATED_BY : EDGE_TYPE.CREATED,

                EDGE_TYPE.WON : EDGE_TYPE.WON_BY,
                EDGE_TYPE.WON_BY : EDGE_TYPE.WON,

                EDGE_TYPE.LOST : EDGE_TYPE.LOST_BY,
                EDGE_TYPE.LOST_BY : EDGE_TYPE.LOST,

                EDGE_TYPE.TIED : EDGE_TYPE.TIED_BY,
                EDGE_TYPE.TIED_BY : EDGE_TYPE.TIED,

                EDGE_TYPE.PLAYED : EDGE_TYPE.PLAYED_BY,
                EDGE_TYPE.PLAYED_BY : EDGE_TYPE.PLAYED}


API_CONSTANT = _APIConstant()

