""" API Constants

...

"""


def api_constant(f):
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


    @api_constant
    def GAME():
        """ GAME is a Type of Node. """
        return "GAME"


    @api_constant
    def LEAGUE():
        """ LEAGUE is a Type of Node. """
        return "LEAGUE"


    @api_constant
    def PLAYER():
        """ PLAYER is a Type of Node. """
        return "PLAYER"


    @api_constant
    def TEAM():
        """ TEAM is a Type of Node. """
        return "TEAM"


    @api_constant
    def USER():
        """ USER is a Type of Node. """
        return "USER"


class _EdgeType(object):

    """ _EdgeType class to hold all Edge Types. """


    @api_constant
    def IN_LEAGUE():
        """ IN_LEAGUE is a Type of Edge. """
        return "IN_LEAGUE"


    @api_constant
    def HAS_LEAGUE_MEMBER():
        """ HAS_LEAGUE_MEMBER is a Type of Edge. """
        return "HAS_LEAGUE_MEMBER"


    @api_constant
    def SCHEDULED_IN():
        """ SCHEDULED_IN is a Type of Edge. """
        return "SCHEDULED_IN"


    @api_constant
    def HAS_SCHEDULED():
        """ HAS_SCHEDULED is a Type of Edge. """
        return "HAS_SCHEDULED"
    

    @api_constant
    def WON():
        """ WON is a Type of Edge. """
        return "WON"


    @api_constant
    def WON_BY():
        """ WON_BY is a Type of Edge. """
        return "WON_BY"


    @api_constant
    def LOST():
        """ LOST is a Type of Edge. """
        return "LOST"


    @api_constant
    def LOST_BY():
        """ LOST_BY is a Type of Edge. """
        return "LOST_BY"


    @api_constant
    def TIED():
        """ TIED is a Type of Edge. """
        return "TIED"


    @api_constant
    def TIED_BY():
        """ TIED_BY is a Type of Edge. """
        return "TIED_BY"


    @api_constant
    def PLAYED():
        """ PLAYED is a Type of Edge. """
        return "PLAYED"


    @api_constant
    def PLAYED_BY():
        """ PLAYED_BY is a Type of Edge. """
        return "PLAYED_BY"


    @api_constant
    def CREATED():
        """ CREATED is a Type of Edge. """
        return "CREATED"


    @api_constant
    def CREATED_BY():
        """ CREATED_BY is a Type of Edge. """
        return "CREATED_BY"


# variables used to refer to Node and Edge Type Constants
# needs to be above _APIConstant and below the Types
NODE_TYPE = _NodeType()
EDGE_TYPE = _EdgeType()


class _APIConstant(object):

    """ _APIConstant class holds all API constants. """


    @api_constant
    def OPPONENT_TYPES():
        """ OPPONENT_NODE_TYPES is a list of Opponent Node Types. """
        return [NODE_TYPE.PLAYER, NODE_TYPE.TEAM]


    @api_constant
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


    @api_constant
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

class _Rankings():

    """ _Rankings class holds Catcher's rankings' constants. """

    @constant
    def RANKS():
        """ RANKS is the ranked objects. """
        return "ranks"

    @constant
    def SORT_FIELD():
        """ SORT_FIELD signifies the ranked objects sort field. """
        return "sort_field"

    @constant
    def RANKED_IN():
        """ RANKED_IN signifies the rankings' container. """
        return "ranked_in"

RANKINGS = _Rankings()

