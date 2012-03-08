""" Module: loader

Provide a Sqoreboard API for loading graph data into Sqoreboard objects.

Provides:
    def load_node
    def load_edge
    def load_edges
    def load_neighbors

"""

from model.graph import GraphEdge, GraphNode, GraphPath, GraphOutputError
from model.graph import reader
from sqobject import SqNode
import sqfactory


def load_node(node_id):
    """ Return a SqNode subclass for the given id.

    Wrap a call to a Graph API that returns a GraphNode and call on 
    sqfactory to parse it into a SqNode subclass.

    Required:
    id  node_id         id of node to fetch

    Returns:
    SqNode              single instance of concrete SqNode subclass

    """

    node = None

    try:
        node = sqfactory.construct_node_and_edges(reader.get_node(node_id))

    except GraphOutputError as e:
        #logger.debug(e.reason)
        print e.reason

    return node


def load_edge(edge_id):
    """ Return a SqEdge subclass for the given id.

    Wrap a call to a Graph API that returns a GraphEdge and call on 
    sqfactory to parse it into a SqEdge subclass.

    Required:
    id  edge_id         id of edge to fetch

    Returns:
    SqEdge              single instance of concrete SqEdge subclass

    """

    edge = None

    try:
        edge = sqfactory.construct_edge(reader.get_edge(edge_id))

    except GraphOutputError as e:
        #logger.debug(e.reason)
        print e.reason

    return edge


def load_edges(node_id):
    """ Return a SqEdge subclass for the given id.

    Wrap a call to a Graph API that returns a GraphEdge and call on 
    sqfactory to parse it into a SqEdge subclass.

    Required:
    id  edge_id         id of edge to fetch

    Returns:
    SqEdge              single instance of concrete SqEdge subclass

    """

    edge = None

    try:
        graph_node = reader.get_node(node_id)

        edges = {}
        for id, graph_edge in graph_node.edges().items():
            edges[id] = sqfactory.construct_edge(graph_edge)

    except GraphOutputError as e:
        #logger.debug(e.reason)
        print e.reason

    return edges


def load_neighbors(node_id, edge_type_pruner=[], node_type_return_filter=[]):
    """ Load a SqNode and its specified SqEdges and neighbor SqNodes.

    Required:
    id      node_id                 SqNode id

    Optional:
    list    edge_type_pruner        list of SqEdge types to traverse
    list    node_type_return_filter list of SqNode types to return

    Returns:
    SqNode                          specified SqEdges, SqNodes loaded

    """

    path = None

    try:
        # get node, outgoing edges, neighbor nodes
        graph_path = reader.get_path_to_neighbor_nodes(
                node_id,
                edge_type_pruner,
                node_type_return_filter)

        # load nodes and edges into SqNodes and SqEdges
        node = sqfactory.construct_node(graph_path.get_start_node())

        neighbor_nodes = {}
        for id, graph_node in graph_path.get_neighbor_nodes().items():
            neighbor_nodes[id] = sqfactory.construct_node(graph_node)

        node.set_neighbors(neighbor_nodes)

    except GraphOutputError as e:
        #logger.debug(e.reason)
        print e.reason

    return node

