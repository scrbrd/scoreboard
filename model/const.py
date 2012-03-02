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
        return "GAME"

    @constant
    def LEAGUE():
        """ LEAGUE is a Type of Node. """
        return "LEAGUE"

    @constant
    def PLAYER():
        """ PLAYER is a Type of Node. """
        return "PLAYER"

    @constant
    def TEAM():
        """ TEAM is a Type of Node. """
        return "TEAM"

    @constant
    def USER():
        """ USER is a Type of Node. """
        return "USER"


class _EdgeType(object):

    """ _EdgeType class to hold all Edge Types. """

    @constant
    def CREATED():
        """ CREATED is a Type of Edge. """
        return "CREATED"

    @constant
    def CREATED_BY():
        """ CREATED_BY is a Type of Edge. """
        return "CREATED_BY"

    @constant
    def LOST():
        """ LOST is a Type of Edge. """
        return "LOST"

    @constant
    def LOST_BY():
        """ LOST_BY is a Type of Edge. """
        return "LOST_BY"

    @constant
    def PLAYED():
        """ PLAYED is a Type of Edge. """
        return "PLAYED"

    @constant
    def PLAYED_BY():
        """ PLAYED_BY is a Type of Edge. """
        return "PLAYED_BY"

    @constant
    def SCHEDULED_IN():
        """ SCHEDULED_IN is a Type of Edge. """
        return "SCHEDULED_IN"

    @constant
    def HAS_SCHEDULED():
        """ HAS_SCHEDULED is a Type of Edge. """
        return "HAS_SCHEDULED"

    @constant
    def TIED():
        """ TIED is a Type of Edge. """
        return "TIED"

    @constant
    def TIED_BY():
        """ TIED_BY is a Type of Edge. """
        return "TIED_BY"
    
    @constant
    def WON():
        """ WON is a Type of Edge. """
        return "WON"

    @constant
    def WON_BY():
        """ WON_BY is a Type of Edge. """
        return "WON_BY"

# variables used to refer to Node and Edge Type Constants
# needs to be above _Constants and below the Types
NODE_TYPE = _NodeType()
EDGE_TYPE = _EdgeType()

class _Const():

    """ _Constants class holds all generic constants. """

    @constant
    def RESULT_TYPES():
        """ RESULT_TYPES is a list of Result Edge Types. """
        return [
                EDGE_TYPE.LOST, EDGE_TYPE.LOST_BY,
                EDGE_TYPE.PLAYED, EDGE_TYPE.PLAYED_BY,
                EDGE_TYPE.TIED, EDGE_TYPE.TIED_BY,
                EDGE_TYPE.WON, EDGE_TYPE.WON_BY]
    
    @constant
    def OPPONENT_TYPES():
        """ OPPOENENT_NODE_TYPES is a list of Opponent Node Types. """
        return = [NODE_TYPE.PLAYER, NODE_TYPE.TEAM]

CONST = _Const

