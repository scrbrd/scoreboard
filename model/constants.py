""" Module: Model Constants

Provide a set of constants which is common to the API, Graph, and Data
layers. In particular, note that only a subset of the total list of
properties owned by our nodes and edges is included here.

"""

from util.decorators import constant


class _NodeProperty(object):

    """ _NodeProperty class to hold all Node Properties. """

    @constant
    def ID(self):
        """ ID is a Property of Node. """
        return "id"


    @constant
    def TYPE(self):
        """ TYPE is a Property of Node. """
        return "type"


    @constant
    def PROPERTIES(self):
        """ PROPERTIES is a Property of Node. """
        return "properties"


    @constant
    def EDGES(self):
        """ EDGES is a Property of Node. """
        return "edges"


NODE_PROPERTY = _NodeProperty()


class _EdgeProperty(object):

    """ _EdgeProperty class to hold all Edge Properties. """


    @constant
    def ID(self):
        """ ID is a Property of Edge. """
        return "id"


    @constant
    def TYPE(self):
        """ TYPE is a Property of Edge. """
        return "type"


    @constant
    def PROPERTIES(self):
        """ PROPERTIES is a Property of Edge. """
        return "properties"


    @constant
    def FROM_NODE_ID(self):
        """ FROM_NODE_ID is a Property of Edge. """
        return "from_node_id"


    @constant
    def TO_NODE_ID(self):
        """ TO_NODE_ID is a Property of Edge. """
        return "to_node_id"


EDGE_PROPERTY = _EdgeProperty()


class _PropertyKey(object):

    """ _PropertyKey enumerates some useful values. """


    @constant
    def DELIMITER(self):
        """ DELIMITER is an API Property Key value. """
        return "_"


PROPERTY_KEY = _PropertyKey()


class _PropertyValue(object):

    """ _PropertyValue class to hold all generic Property Values.

    We do this primarily to avoid introducing problematic types to the
    database. For example, Neo4j cannot accept the python value None.
    We also recognize the importance of standardization.

    """


    @constant
    def EMPTY(self):
        """ EMPTY is a generic Property Value. """
        return ""


PROPERTY_VALUE = _PropertyValue()


class _ThirdParty(object):

    """ _ThirdParty defines a set of third party data providers, like
    Facebook, by a key identifier which can also be used as a prefix
    for data storage.

    When adding a constant to this class, be sure to also add it to the
    definition of THIRD_PARTY.ALL to keep users of the list up-to-date.

    """


    @constant
    def FACEBOOK(self):
        """ FACEBOOK is a type of Third Party. """
        return "fb"


    #@constant
    #def TWITTER(self):
    #    """ TWITTER is a type of Third Party. """
    #    return "tw"


    @constant
    def ALL(self):
        """ ALL is a comprehensive list of Third Party types. """
        return [
                self.FACEBOOK,
                #self.TWITTER,
                ]


THIRD_PARTY = _ThirdParty()


class _Gender(object):

    """ _Gender enumerates gender strings. """


    @constant
    def MALE(self):
        """ MALE is a string Gender Type. """
        return "male"

    @constant
    def FEMALE(self):
        """ FEMALE is a string Gender Type. """
        return "female"


GENDER = _Gender()


class _Version(object):

    """ _Version enumerates software version number strings. """


    @constant
    def CURRENT(self):
        """ CURRENT is a string Version Number. """
        return "0.0"


    @constant
    def BETA(self):
        """ BETA is a string Version Number. """
        return "0.0"


    @constant
    def LAST(self):
        """ LAST is a string Version Number. """
        return "0.0"


    @constant
    def LAST_GOOD(self):
        """ LAST_GOOD is a string Version Number. """
        return "0.0"


    @constant
    def OLD(self):
        """ OLD is a string Version Number. """
        return "0.0"


VERSION = _Version()

