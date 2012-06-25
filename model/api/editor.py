""" Module: editor

Provide a Sqoreboard API for editing graph data in Sqoreboard objects.

Provides:
    def create_node_and_edges
    def create_node
    def create_edges
    def create_edge
    def prototype_node
    def prototype_edge_and_complement

"""

from copy import deepcopy

from model.graph import writer, GraphInputError, GraphProtoNode, GraphProtoEdge

from constants import API_CONSTANT
import sqfactory


def create_node_and_edges(prototype_node, prototype_edges):
    """ Create a new SqNode and its SqEdges in the database.

    Required:
    GraphProtoNode  prototype_node  unwritten version of GraphNode
    list            prototype_edges unwritten GraphEdges as GraphProtoEdges

    Return:
    SqNode                          SqNode created or None on failure

    """

    node = None

    try:
        # create and store a new GraphNode
        new_node = create_node(prototype_node)

        # point to/from id in GraphEdges-to-be at the new GraphNode
        for prototype_edge in prototype_edges:
            prototype_edge.set_node_id(new_node.id())

        # TODO: raise an error when incomplete Edge prototypes [meaning, ones
        # missing a to/from node] are passed to create_edge(). this may already
        # be happening, but it certainly isn't a specific enough error.

        # create and store new GraphEdges to/from the new GraphNode
        new_edges = create_edges(prototype_edges)

        # the new GraphNode should contain the new GraphEdges
        new_node.set_edges(new_edges)

        # load the new GraphNode and GraphEdges into SqObjects
        node = sqfactory.construct_node_and_edges(new_node)

    except GraphInputError as e:
        #logger.debug(e.reason)
        print e.reason

    return node


def create_node(prototype_node):
    """ Create a new SqNode in the database.

    This is little more than an intramodule convenience wrapper for
    calling into the graph layer to create and return a GraphNode.

    Note that this returns a technically complete but disconnected
    SqNode. It is technically complete despite not having its edges
    field loaded because it does not yet have any SqEdges at this point.
    It is disconnected because without any SqEdges, it obviously cannot
    be reached by any graph traversal where it is not the root.

    Required:
    GraphProtoNode  prototype_node  unwritten version of GraphNode

    Return:
    SqNode                          SqNode created or None on failure

    """
    return writer.create_node(prototype_node)


def create_edges(prototype_edges):
    """ Create a dict of new SqEdges in the database.

    See create_edge(), which this function wraps directly.

    Required:
    dict    prototype_edges     unwritten versions of GraphEdges

    Return:
    dict                        SqEdges created or None on failure

    """
    graph_edges = {}

    for prototype_edge in prototype_edges:
        graph_edge = create_edge(prototype_edge)
        graph_edges[graph_edge.id()] = graph_edge

    return graph_edges


def create_edge(prototype_edge):
    """ Create a new SqEdge in the database.

    This is little more than an intramodule convenience wrapper for
    calling into the graph layer to create and return a GraphEdge.

    Required:
    GraphProtoEdge  prototype_edge  unwritten version of GraphEdge

    Return:
    SqEdge                          SqEdge created or None on failure

    """
    return writer.create_edge(prototype_edge)


def prototype_node(type, properties):
    """ Prototype a GraphNode for writing out to the database.

    Required:
    str     type        constants.NODE_TYPE
    dict    properties  properties of th GraphNode-to-be {PROP: VALUE}

    Return:
    GraphProtoNode      for instantiating an unwritten SqNode

    """
    return GraphProtoNode(type, properties)


def prototype_edge(type, properties, from_node_id, to_node_id):
    """ Prototype a single GraphEdge for writing to the database.

    If we are preparing to create a SqNode, then we will not know both
    the from and to ID yet when constructing the GraphProtoEdge. It is
    fine to pass None for either from_node_id or to_node_id. Since not
    all scenarios will be symmetric, giving one of them a default value
    and making it optional in the way that we do for the convenience
    function prototype_edge_and_complement() seemed misleading.

    Required:
    str     type            constants.EDGE_TYPE
    dict    properties      properties of GraphEdge-to-be
    id      from_node_id    ID of GraphNode to point from
    id      to_node_id      ID of GraphNode to point to

    Return:
    GraphProtoEdge      unwritten GraphProtoEdge

    """
    return GraphProtoEdge(type, properties, from_node_id, to_node_id)


def prototype_edge_and_complement(
        type,
        properties,
        from_node_id,
        to_node_id=None):
    """ Prototype complementary GraphEdges for writing to the database.

    For convenience, to_node_id is optional, since sometimes we will not
    know both IDs when constructing the prototype.

    Required:
    str     type            constants.EDGE_TYPE
    dict    properties      properties of GraphEdge-to-be
    id      from_node_id    ID of GraphNode to point from

    Optional:
    id      to_node_id      ID of GraphNode to point to

    Return:
    list                complementary unwritten GraphProtoEdges

    """
    outgoing = prototype_edge(type, properties, from_node_id, to_node_id)

    incoming = prototype_edge(
            API_CONSTANT.EDGE_TYPE_COMPLEMENTS[type],
            deepcopy(properties),
            to_node_id,
            from_node_id)

    return [outgoing, incoming]
