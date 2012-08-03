""" Module: reader

Provide an API for retrieving data from a graph database, including
get and multiget actions on nodes, edges, and paths.

Provides:
    def get_node
    def get_nodes_by_index
    def multiget_node
    def get_edge
    def multiget_edge
    def get_path_to_neighbor_nodes
    def multiget_path_to_neighbor_nodes

"""
from model.constants import NODE_PROPERTY, EDGE_PROPERTY
from model.data import database_manager
from model.data.data_errors import DbInputError, DbReadError

from constants import GRAPH_PROPERTY
from model.graph import GraphEdge, GraphNode, GraphPath, GraphOutputError


def database():
    """ Get a database from the data layer's database_manager. """
    return database_manager.database()


def get_node(node_id):
    """ Return a GraphNode from a graph database.

    Wrap a call to a graph database that returns a dict structured
    like the following, and parse it into a GraphNode:

    {
        "id" : node_id,
        "type" : type,
        "properties" : {"p0" : p0, ..., "pN" : pN},
        "edges" : {edge_id0 : edge_dict0, ..., edge_idN : edge_dictN}
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

    graph_node = None

    try:
        node_dict = database().read_node_and_edges(node_id)

        if node_dict:
            graph_node = _process_node(node_dict)

    except DbReadError as e:
        print(e.reason)
        #logger.debug(e.reason)

    except DbInputError as e:
        print(e.reason)
        #logger.debug(e.reason)

    return graph_node


def get_nodes_by_index(key, value, node_type_return_filter=None):
    """ Return a dict of GraphNodes from a graph database index.

    Wrap a call to a graph database that returns a dict structured
    like the following, and parse it into a GraphNode:

    {
        "id" : node_id,
        "type" : type,
        "properties" : {"p0" : p0, ..., "pN" : pN},
        "edges" : {edge_id0 : edge_dict0, ..., edge_idN : edge_dictN}
    }

    Required:
    str     key                         indexed property key to look up
    mixed   value                       indexed property value to look up

    Optional:
    list    node_type_return_filter     node types to filter for

    Returns:
    dict                                GraphNodes keyed on ID

    Raises:
    GraphOutputError                    bad input

    """

    # cases:
    #   1/ success: dict returned;
    #   2/ k/v pair was bad: error raised, execution halted;
    #   3/ db fails: error caught, None assigned here.

    graph_nodes = None
    try:
        node_dicts = database().read_nodes_by_index(
                key,
                value,
                node_type_return_filter)
        if node_dicts is None:
            node_dicts = {}

        graph_nodes = {}
        for id, node_dict in node_dicts.items():
            graph_nodes[id] = _process_node(node_dict)

    except DbReadError as e:
        print(e.reason)
        #logger.debug(e.reason)

    except DbInputError as e:
        print(e.reason)
        #logger.debug(e.reason)

    return graph_nodes


def _process_node(node_dict):
    """ Convenience wrapper to validate and convert to a GraphNode. """

    required_fields = set([
            NODE_PROPERTY.ID,
            NODE_PROPERTY.TYPE,
            NODE_PROPERTY.PROPERTIES,
            NODE_PROPERTY.EDGES,
            ])

    required_properties = set([
            GRAPH_PROPERTY.CREATED_TS,
            GRAPH_PROPERTY.UPDATED_TS,
            GRAPH_PROPERTY.DELETED_TS,
            ])

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

    return GraphNode(
            node_dict[NODE_PROPERTY.ID],
            node_dict[NODE_PROPERTY.TYPE],
            node_dict[NODE_PROPERTY.PROPERTIES],
            node_dict[NODE_PROPERTY.EDGES])


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
        "id" : edge_id,
        "type" : type,
        "properties" : {"p0" : p0, ..., "pN" : pN},
        "from_node_id" : from_node_id,
        "to_node_id" : to_node_id
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
        edge_dict = database().read_edge(edge_id)

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
                        "Required fields/properties missing from GraphEdge.")

            edge = GraphEdge(
                    edge_dict[EDGE_PROPERTY.ID],
                    edge_dict[EDGE_PROPERTY.TYPE],
                    edge_dict[EDGE_PROPERTY.PROPERTIES],
                    edge_dict[EDGE_PROPERTY.FROM_NODE_ID],
                    edge_dict[EDGE_PROPERTY.TO_NODE_ID])

    except DbReadError as e:
        print(e.reason)
        #logger.debug(e.reason)

    except DbInputError as e:
        print(e.reason)
        #logger.debug(e.reason)

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
        edge_type_pruner=None,
        node_type_return_filter=None):
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
        path_dict = database().read_nodes_from_immediate_path(
                start_node_id,
                edge_type_pruner,
                node_type_return_filter)

        # FIXME: do similar checking to get_node() for path_dict[0]

        # instantiate all nodes and edges in one fell swoop
        path = GraphPath(start_node_id, path_dict)

    except DbReadError as e:
        print(e.reason)
        #logger.debug(e.reason)

    except DbInputError as e:
        print(e.reason)
        #logger.debug(e.reason)

    return path


def multiget_path_to_neighbor_nodes(
        start_node_ids,
        edge_type_pruner=None,
        node_type_return_filter=None):
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
