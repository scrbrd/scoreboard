""" Module: editor

Provide a Sqoreboard API for editing graph data in Sqoreboard objects.

Provides:
    def create_node_and_edges
    #def create_node
    #def create_edges
    #def create_edge
    def prototype_node
    def prototype_edge_and_complement

"""

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
        new_node = _create_node(prototype_node)

        # TODO: test whether this modifies prototype_edges
        # point to/from id in GraphEdges-to-be at the new GraphNode
        for prototype_edge in prototype_edges:
            prototype_edge.set_node_id(new_node.id())

        # create and store new GraphEdges to/from the new GraphNode
        new_edges = _create_edges(prototype_edges)

        # load the new GraphNode and GraphEdges into SqObjects
        node = sqfactory.construct_node_and_edges(new_node, new_edges)

    except GraphInputError as e:
        #logger.debug(e.reason)
        print e.reason

    return node


#def create_node(prototype_node):
#def create_edges(prototype_edges):
#def create_edge(prototype_edge):


def prototype_node(type, properties):
    """ Prototype a GraphNode for writing out to the database.

    Required:
    str     type        constants.NODE_TYPE
    dict    properties  properties of th GraphNode-to-be {PROP: VALUE}

    Return:
    GraphProtoNode      for instantiating an unwritten SqNode

    """
    
    return GraphProtoNode(type, properties)


def prototype_edge_and_complement(type, properties, node_id):
    """ Prototype complementary GraphEdges for writing to the database.

    Required:
    str     type        constants.EDGE_TYPE
    dict    properties  properties of GraphEdge-to-be
    id      node_id     id of GraphNode to point to/from

    Return:
    list                complementary unwritten GraphProtoEdges

    """

    out_prototype_edge = GraphProtoEdge(
            type,
            properties,
            None,
            node_id)
    in_prototype_edge = GraphProtoEdge(
            API_CONSTANT.EDGE_TYPE_COMPLEMENTS[type],
            properties,
            node_id,
            None)

    return [out_prototype_edge, in_prototype_edge]


def _create_node(prototype_node):
    """ Intramodule Convenience wrapper returning GraphNode. """
    return writer.create_node(prototype_node)


def _create_edges(prototype_edges):
    """ Intramodule Convenience wrapper returning GraphEdges. """

    graph_edges = {}

    for prototype_edge in prototype_edges:
        graph_edge = _create_edge(prototype_edge)
        graph_edges[graph_edge.id()] = graph_edge

    return graph_edges


def _create_edge(prototype_edge):
    """ Intramodule Convenience wrapper returning GraphEdges. """
    return writer.create_edge(prototype_edge)

