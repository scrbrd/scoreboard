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
        return "n_id"


    @constant
    def TYPE(self):
        """ TYPE is a Property of Node. """
        return "n_type"


    @constant
    def PROPERTIES(self):
        """ PROPERTIES is a Property of Node. """
        return "n_properties"


    @constant
    def EDGES(self):
        """ EDGES is a Property of Node. """
        return "n_edges"


NODE_PROPERTY = _NodeProperty()


class _EdgeProperty(object):

    """ _EdgeProperty class to hold all Edge Properties. """


    @constant
    def ID(self):
        """ ID is a Property of Edge. """
        return "e_id"


    @constant
    def TYPE(self):
        """ TYPE is a Property of Edge. """
        return "e_type"


    @constant
    def PROPERTIES(self):
        """ PROPERTIES is a Property of Edge. """
        return "e_properties"


    @constant
    def FROM_NODE_ID(self):
        """ FROM_NODE_ID is a Property of Edge. """
        return "e_from_node_id"


    @constant
    def TO_NODE_ID(self):
        """ TO_NODE_ID is a Property of Edge. """
        return "e_to_node_id"


EDGE_PROPERTY = _EdgeProperty()

