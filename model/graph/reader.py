""" Module: reader

Provide an API for retrieving data from a graph database, including 
get and multiget actions on nodes, edges, and paths.

Provides:
    def get_node
    def multiget_node
    def get_edge
    def multiget_edge
    def get_path_to_neighbor_nodes
    def multiget_path_to_neighbor_nodes

"""

from model.graph import GraphEdge, GraphNode, GraphPath, GraphInputError
from model.data import db, DbInputError, DbReadError, DbWriteError


def get_node(node_id):
    """ Return a GraphNode from a graph database.

    Wrap a call to a graph database that returns a dict structured 
    like the following, and parse it into a GraphNode:

    {
        "node_id" : node_id,
        "type" : type,
        "properties" : {"p0" : p0, ..., "pN" : pN},
        "edges" : {edge_id0 : edge_dict0, ..., edge_idN : edge_dictN}
    }

    Required:
    id  node_id     id of node to fetch

    Returns:
    GraphNode       single GraphNode instance

    Raises:
    GraphInputError bad input

    """

    # cases:
    #   1/ success: dict returned;
    #   2/ id was bad: error raised, execution halted;
    #   3/ db fails: error caught, None assigned here.

    try:
        node = None

        node_dict = db.read_node_and_edges(node_id)

        # halts execution and requires API to resend request
        if node_dict is None:
            raise GraphInputError(
                    "node_id",
                    node_id,
                    "Database query failed.")

        node = GraphNode(
                node_dict["node_id"],
                node_dict["type"],
                node_dict["properties"])

    #except DbReadError as e:
        #logger.debug(e.msg)

    finally:
        return node


def multiget_node(node_ids):
    """ Return a dict of GraphNodes from a database keyed on id.

    Wrap a set of calls to a graph database that each return a dict 
    structured like the one referenced in get_node(), and parse them 
    into GraphNodes.

    Required:
    list    node_ids    list of ids of node to fetch

    Returns:
    dict                GraphNodes keyed on node id

    Raises:
    GraphInputError bad input

    """

    nodes = {}
    for node_id in node_ids:
        nodes[node_id] = get_node(node_id)

    return nodes


def get_edge(edge_id):
    """ Return a GraphEdge from a graph database.

    Wrap a call to a graph database that returns a dict structured 
    like the following, and parse it into a GraphEdge:

    {
        "edge_id" : edge_id,
        "from_node_id" : from_node_id,
        "to_node_id" : to_node_id,
        "type" : type,
        "properties" : {"p0" : p0, ..., "pN" : pN}
    }

    Required:
    id  edge_id     id of edge to fetch

    Returns:
    GraphEdge       single GraphEdge instance

    Raises:
    GraphInputError bad input

    """

    # cases:
    #   1/ success: dict returned;
    #   2/ id was bad: error raised, execution halted;
    #   3/ db fails: error caught, None assigned here.

    try:
        edge = None

        edge_dict = db.read_edge(edge_id)

        # halts execution and requires API to resend request
        if edge_dict is None:
            raise GraphInputError(
                    "edge_id",
                    edge_id,
                    "Database query failed.")

        edge = GraphEdge(
                edge_dict["edge_id"],
                edge_dict["from_node_id"],
                edge_dict["to_node_id"],
                edge_dict["type"],
                edge_dict["properties"])

    #except DbReadError as e:
        #logger.debug(e.msg)

    finally:
        return edge


def multiget_edge(edge_ids):
    """ Return a dict of GraphEdges from a database keyed on id.

    Wrap a set of calls to a graph database that each return a dict 
    structured like the one referenced in get_edge(), and parse them 
    into GraphEdges.

    Required:
    list    edge_ids    list of ids of edge to fetch

    Returns:
    dict                GraphEdges keyed on edge id

    Raises:
    GraphInputError bad input

    """

    edges = {}
    for edge_id in edge_ids:
        edges[edge_id] = get_edge(edge_id)

    return edges


#def get_edges_for_node(node_id): pass
#def multiget_edges_for_node(node_ids): pass


def get_path_to_neighbor_nodes(
        start_node_id,
        edge_type_pruner=[],
        node_type_return_filter=[]):
    """ Traverse a depth-1 path from a start node to its neighbors.

    Wrap a call to a graph database that returns a dict structured 
    like the following, and parse it into a GraphPath:

    {
        depth0 : {start_node_id : {start_node_dict}},
        depth1 : {node_id0 : {node_dict0}, ..., node_idN : {node_dictN}}
    }

    Required:
    id   start_node_id           start node id in a depth-1 path

    Optional:
    list edge_type_pruner        list of edge types to traverse
    list node_type_return_filter list of node types to return

    Returns:
    GraphPath                    single GraphPath instance

    Raises:
    GraphInputError bad input

    """

    try:
        path = None

        # issue a db query to generate a path to neighbors
        path_dict = db.read_nodes_from_immediate_path(
                start_node_id, 
                edge_type_pruner,
                node_type_return_filter)

        # should properties be hard-coded like this?
        properties = {
                "edge_types_traversed" : edge_type_pruner, 
                "node_types_returned" : node_type_return_filter
                }
        
        # instantiate all nodes and edges in one fell swoop
        path = GraphPath(start_node_id, path_dict, properties)

    #except DbReadError as e:
        #logger.debug(e.msg)

    finally:
        return path


def multiget_path_to_neighbor_nodes(
        start_node_ids,
        edge_type_pruner=[],
        node_type_return_filter=[]):
    """ Traverse depth-1 paths from start nodes to their neighbors.

    Wrap a set of calls to a graph database that each return a dict 
    structured like the one referenced in get_path_to_neighbor_nodes(), 
    and parse them into GraphPaths.

    Required:
    list    start_node_id           start node id in a depth-1 path

    Optional:
    list    edge_type_pruner        list of edge types to traverse
    list    node_type_return_filter list of node types to return

    Returns:
    dict                            GraphPaths keyed on start node id

    Raises:
    GraphInputError bad input

    """

    paths = {}
    for start_node_id in start_node_ids:
        paths[start_node_id] = get_path_to_neighbor_nodes(start_node_id)

    return paths

