""" Module: Neo4j Constants

Provide constants for hardcoded values required by the Neo4j REST
API and the Gremlin plugin.

"""

from util.decorators import constant


class _Neo4j(object):

    """ _Neo4j class to hold all Neo4j constants. """


    @constant
    def SCRIPT(self):
        """ SCRIPT is a Neo4j constant. """
        return "script"


    @constant
    def PARAMS(self):
        """ PARAMS is a Neo4j constant. """
        return "params"


    @constant
    def SELF(self):
        """ SELF is a Neo4j constant. """
        return "self"


    @constant
    def DATA(self):
        """ DATA is a Neo4j constant. """
        return "data"


    @constant
    def START(self):
        """ START is a Neo4j constant. """
        return "start"


    @constant
    def END(self):
        """ END is a Neo4j constant. """
        return "end"


    @constant
    def TYPE(self):
        """ TYPE is a Neo4j constant. """
        return "type"


NEO4J = _Neo4j()


class _Neo4jIndex(object):

    """ _Neo4jIndex class to hold all Neo4j database indices. """


    @constant
    def NODES(self):
        """ NODES is a Neo4j constant. """
        return "vertices"


    @constant
    def EDGES(self):
        """ EDGES is a Neo4j constant. """
        return "edges"


NEO4J_INDEX = _Neo4jIndex()


class _Gremlin(object):

    """ _Gremlin class to hold all Gremlin constants. """


    @constant
    def PATH(self):
        """ PATH is a Gremlin constant. """
        return "/db/data/ext/GremlinPlugin/graphdb/execute_script"


    @constant
    def REQUEST_HEADER_TYPE(self):
        """ REQUEST_HEADER_TYPE is a Gremlin constant. """
        return "Content-type"


    @constant
    def REQUEST_HEADER(self):
        """ REQUEST_HEADER is a Gremlin constant. """
        return "application/json"


    @constant
    def BASE_ERROR(self):
        """ BASE_ERROR is a Gremlin constant. """
        return "javax.script.ScriptException: "


    @constant
    def NULL_ERROR(self):
        """ NULL_ERROR is a Gremlin constant. """
        return "java.lang.NullPointerException"


    @constant
    def INPUT_ERROR(self):
        """ INPUT_ERROR is a Gremlin constant. """
        return "java.lang.IllegalArgumentException"


GREMLIN = _Gremlin()

