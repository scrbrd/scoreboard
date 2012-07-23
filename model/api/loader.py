""" Module: loader

Provide a Sqoreboard API for loading graph data into Sqoreboard objects.

Provides:
    def load_node
    def load_node_by_unique_property
    def load_nodes_by_property
    def load_edge
    def load_edges
    def load_neighbors

"""

from model.graph import GraphOutputError
from model.graph import reader

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
        graph_node = reader.get_node(node_id)

        if graph_node:
            node = sqfactory.construct_node_and_edges(graph_node)

    except GraphOutputError as e:
        #logger.debug(e.reason)
        print e.reason

    return node


def load_node_by_unique_property(key, value, node_type_return_filter=None):
    """ Return a single SqNode for a property and node type filter.

    Wrap a call to load_nodes_by_property(). pop and return the first and
    only node returned. The sqfactory module will parse it into a SqNode
    subclass.

    This should only be used for combinations of property key/value and
    return node type which the caller knows to be restricted to exactly
    one stored node. The canonical example is guaranteeing unique email
    address or third party ID in User storage.

    Ideally, this property would be indexed in the database. In fact,
    the underlying graph or data layer may impose this restriction on
    queries and throw an error if no index exists for this property.

    Required:
    str     key                         property to look up
    mixed   value                       property value to look up

    Optional:
    list    node_type_return_filter     node types to filter for

    Returns:
    SqNode                              single SqNode instance

    """

    nodes = load_nodes_by_property(key, value, node_type_return_filter)
    return nodes.values()[0] if nodes else None


def load_nodes_by_property(key, value, node_type_return_filter=None):
    """ Return a list of SqNodes for a given property and node type.

    Wrap a call to a Graph API that returns a GraphNode and call on
    sqfactory to parse it into a SqNode subclass.

    Ideally, this property would be indexed in the database. In fact,
    the underlying graph or data layer may impose this restriction on
    queries and throw an error if no index exists for this property.

    Required:
    str     key                         property key to look up
    mixed   value                       property value to look up

    Optional:
    list    node_type_return_filter     list of SqNode types to return

    Returns:
    dict                                SqNodes keyed on ID (or None)

    """

    nodes = None

    try:
        graph_nodes = reader.get_nodes_by_index(
                key,
                value,
                node_type_return_filter)

        nodes = {}
        for id, graph_node in graph_nodes.items():
            nodes[id] = sqfactory.construct_node_and_edges(graph_node)

    except GraphOutputError as e:
        #logger.debug(e.reason)
        print e.reason

    return nodes


def load_edge(edge_id):
    """ Return a SqEdge subclass for the given id.

    Wrap a call to a Graph API that returns a GraphEdge and call on
    sqfactory to parse it into a SqEdge subclass.

    Required:
    id      edge_id     id of edge to fetch

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
    """ Return a dict of SqEdge subclasses for the given SqNode ID.

    Wrap a call to a Graph API that returns a GraphEdge and call on
    sqfactory to parse it into a SqEdge subclass.

    Required:
    id      node_id     id of edge to fetch

    Returns:
    dict                concrete SqEdge subclasses keyed on ID

    """

    edges = None

    try:
        graph_node = reader.get_node(node_id)

        edges = {}
        for id, graph_edge in graph_node.edges().items():
            edges[id] = sqfactory.construct_edge(graph_edge)

    except GraphOutputError as e:
        #logger.debug(e.reason)
        print e.reason

    return edges


def load_neighbors(
        node_id,
        edge_type_pruner=None,
        node_type_return_filter=None):
    """ Load a SqNode and its specified SqEdges and neighbor SqNodes.

    Required:
    id      node_id                 SqNode id

    Optional:
    list    edge_type_pruner        list of SqEdge types to traverse
    list    node_type_return_filter list of SqNode types to return

    Returns:
    tuple                           (SqNode, dict) => (start, neighbors)

    """

    node = None
    neighbor_nodes = None

    try:
        # get node, outgoing edges, neighbor nodes
        graph_path = reader.get_path_to_neighbor_nodes(
                node_id,
                edge_type_pruner,
                node_type_return_filter)

        # load nodes and edges into SqNodes and SqEdges
        node = sqfactory.construct_node_and_edges(graph_path.get_start_node())

        neighbor_nodes = {}
        for id, graph_node in graph_path.get_neighbor_nodes().items():
            neighbor_nodes[id] = sqfactory.construct_node_and_edges(graph_node)

    except GraphOutputError as e:
        #logger.debug(e.reason)
        print e.reason

    # TODO: this only works for depth-1 queries because of graph fan-out, so
    # we need something different for queries of depth-2 and up.
    return (node, neighbor_nodes)
