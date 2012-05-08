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

from model.data import db, DbInputError, DbReadError, DbWriteError
from model.constants import NODE_PROPERTY, EDGE_PROPERTY

from constants import GRAPH_PROPERTY
from model.graph import GraphEdge, GraphNode, GraphPath, GraphOutputError

def get_node(node_id):
    """ Return a GraphNode from a graph database.

    Wrap a call to a graph database that returns a dict structured 
    like the following, and parse it into a GraphNode:

    {
        "n_id" : node_id,
        "n_type" : type,
        "n_properties" : {"p0" : p0, ..., "pN" : pN},
        "n_edges" : {edge_id0 : edge_dict0, ..., edge_idN : edge_dictN}
    }

    Required:
    id  node_id         id of node to fetch

    Returns:
    GraphNode           single GraphNode instance

    Raises:
    GraphOutputError    bad input

    """

    # cases:
    #   1/ success: dict returned;
    #   2/ id was bad: error raised, execution halted;
    #   3/ db fails: error caught, None assigned here.

    node = None

    required_fields = set([
            NODE_PROPERTY.ID,
            NODE_PROPERTY.TYPE,
            NODE_PROPERTY.PROPERTIES,
            NODE_PROPERTY.EDGES
            ])

    # TODO: deal with existing bad data. every node and edge should have a
    # value set for each of these properties.

    required_properties = set([
            GRAPH_PROPERTY.CREATED_TS,
            GRAPH_PROPERTY.UPDATED_TS,
            GRAPH_PROPERTY.DELETED_TS
            ])

    try:
        node_dict = db.read_node_and_edges(node_id)

        if node_dict:
            # data layer nodes only have fields explicitly required
            errors = required_fields.symmetric_difference(set(node_dict))

            if NODE_PROPERTY.PROPERTIES not in errors:
                # ensure properties the graph layer requires are present too
                properties = set(node_dict[NODE_PROPERTY.PROPERTIES])
                property_errors = required_properties.difference(properties)
                errors = errors.union(property_errors)

            if errors:
                raise GraphOutputError(
                        errors, 
                        "Required fields or properties missing from GraphNode.")

            node = GraphNode(
                    node_dict[NODE_PROPERTY.ID],
                    node_dict[NODE_PROPERTY.TYPE],
                    node_dict[NODE_PROPERTY.PROPERTIES],
                    node_dict[NODE_PROPERTY.EDGES])

    except DbReadError as e:
        print(e.reason)
        #logger.debug(e.reason)
        node = None

    except DbInputError as e:
        print(e.reason)
        #logger.debug(e.reason)
        node = None

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
        "e_id" : edge_id,
        "e_type" : type,
        "e_properties" : {"p0" : p0, ..., "pN" : pN},
        "e_from_node_id" : from_node_id,
        "e_to_node_id" : to_node_id
    }

    Required:
    id  edge_id     id of edge to fetch

    Returns:
    GraphEdge       single GraphEdge instance

    """

    # cases:
    #   1/ success: dict returned;
    #   2/ id was bad: error raised, execution halted;
    #   3/ db fails: error caught, None assigned here.

    edge = None

    required_fields = set([
            EDGE_PROPERTY.ID,
            EDGE_PROPERTY.TYPE,
            EDGE_PROPERTY.PROPERTIES,
            EDGE_PROPERTY.FROM_NODE_ID,
            EDGE_PROPERTY.TO_NODE_ID
            ])

    required_properties = set([
            GRAPH_PROPERTY.CREATED_TS,
            GRAPH_PROPERTY.UPDATED_TS,
            GRAPH_PROPERTY.DELETED_TS
            #GRAPH_PROPERTY.IS_ONE_WAY,
            #GRAPH_PROPERTY.IS_UNIQUE
            ])

    try:
        edge_dict = db.read_edge(edge_id)

        if edge_dict:
            # data layer edges only have fields explicitly required
            errors = required_fields.symmetric_difference(set(edge_dict))

            if EDGE_PROPERTY.PROPERTIES not in errors:
                # ensure properties the graph layer requires are present too
                properties = set(edge_dict[EDGE_PROPERTY.PROPERTIES])
                property_errors = required_properties.difference(properties)
                errors = errors.union(property_errors)

            if errors:
                raise GraphOutputError(
                        errors, 
                        "Required fields or properties missing from GraphEdge.")

            edge = GraphEdge(
                    edge_dict[EDGE_PROPERTY.ID],
                    edge_dict[EDGE_PROPERTY.TYPE],
                    edge_dict[EDGE_PROPERTY.PROPERTIES],
                    edge_dict[EDGE_PROPERTY.FROM_NODE_ID],
                    edge_dict[EDGE_PROPERTY.TO_NODE_ID])

    except DbReadError as e:
        print(e.reason)
        #logger.debug(e.reason)
        edge = None

    except DbInputError as e:
        print(e.reason)
        #logger.debug(e.reason)
        edge = None

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

    """

    path = None

    try:
        # issue a db query to generate a path to neighbors
        path_dict = db.read_nodes_from_immediate_path(
                start_node_id, 
                edge_type_pruner,
                node_type_return_filter)

        # FIXME: do similar checking to get_node() for path_dict[0]

        # instantiate all nodes and edges in one fell swoop
        path = GraphPath(start_node_id, path_dict)

    except DbReadError as e:
        print(e.reason)
        #logger.debug(e.reason)
        path = None

    except DbInputError as e:
        print(e.reason)
        #logger.debug(e.reason)
        path = None

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

    """

    paths = {}

    for start_node_id in start_node_ids:
        paths[start_node_id] = get_path_to_neighbor_nodes(
                start_node_id,
                edge_type_pruner,
                node_type_return_filter)

    return paths

