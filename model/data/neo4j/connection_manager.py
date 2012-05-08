""" Module: connection_manager

Receive database requests, handle neo4j interaction, and
return parsed and formatted nodes, edges, and sets.

All the functions raise DbConnectionError if they can't connect
to the db or if the db returns an error, including a bad id error.

"""

import urllib, urllib2, json

from model.constants import NODE_PROPERTY, EDGE_PROPERTY
from constants import GREMLIN, NEO4J

import response_parser
from model.data import DbConnectionError



def create_node(base_url, type, properties):
    """ Create a node in the db using gremlin and return created node.

    Required:
    string base_url     url of db
    string type         node's 'type'
    dict properties     node's properties dictionary

    Return node as a dictionary.
    keys = node_id, type, properties, edges
    
    """

    # add type to properties dictionary before generating script
    properties[NODE_PROPERTY.TYPE] = type

    # TODO: does grabbing the empty edges list take time here?
    script = "g.addVertex({0}).transform{{[it, it.outE()]}}".format(
            NODE_PROPERTY.PROPERTIES)
    params = {NODE_PROPERTY.PROPERTIES : properties}

    url = base_url + GREMLIN.PATH
    data = {NEO4J.SCRIPT : script, NEO4J.PARAMS : params}

    response_data = connect(url, json.dumps(data))

    return response_parser.format_node(response_data[0])


def create_edge(base_url, from_node, to_node, type, properties):
    """ Create an edge in the db using gremlin and return created edge.

    Required:
    string base_url     url of db
    int from_node       id of from node
    int to_node         id of to node
    string type         edge's 'type'
    dict properties     edge's properties dictionary

    Return edge as a dictionary.
    keys = edge_id, from_node_id, to_node_id, type, properties
    
    """

    script = "g.addEdge(g.v({0}), g.v({1}), {2}, {3})".format(
            EDGE_PROPERTY.FROM_NODE_ID,
            EDGE_PROPERTY.TO_NODE_ID,
            EDGE_PROPERTY.TYPE,
            EDGE_PROPERTY.PROPERTIES)

    params = {
            EDGE_PROPERTY.FROM_NODE_ID : from_node, 
            EDGE_PROPERTY.TO_NODE_ID : to_node, 
            EDGE_PROPERTY.TYPE : type,
            EDGE_PROPERTY.PROPERTIES : properties
            }

    url = base_url + GREMLIN.PATH
    data = {NEO4J.SCRIPT : script, NEO4J.PARAMS : params}

    response_data = connect(url, json.dumps(data))

    return response_parser.format_edge(response_data)


def update_node(base_url, id, properties):
    return None


def update_edge(base_url, id, properties):
    return None


def read_node_and_edges(base_url, node_id):
    """ Read a node and all its edges from the db using gremlin.

    Required:
    string base_url     url of db
    int node_id         id of requested node

    Return node as a dictionary.
    keys = node_id, type, properties, edges
    
    """

    script = "g.v({0}).transform{{[it, it.outE()]}}".format(NODE_PROPERTY.ID)
    params = {NODE_PROPERTY.ID : node_id}

    url = base_url + GREMLIN.PATH
    data = {NEO4J.SCRIPT : script, NEO4J.PARAMS : params}

    response_data = connect(url, json.dumps(data))

    if response_data is None:
        return None
    else:
        return response_parser.format_node(response_data[0])


def read_edge(base_url, edge_id):
    return None


def read_nodes_from_immediate_path(
        base_url, 
        start_node_id, 
        edge_pruner,
        node_return_filter): 
    """ Read a restricted set of nodes of depth 1 using Gremlin.

    Required:
    string base_url         url of db
    int start_node_id       id of requested node
    list edge_pruner        edges that should be traversed ([]=all)
    list node_return_filter nodes that should be returned ([]=all)

    Return nodes as a dictionary keyed on depth and node_id
    {depth: {node_id: node}}
    
    """

    # TODO: there's got to be a better way to do all of this string formatting

    # format the pruners and filter
    formatted_edge_pruner = ["\"{0}\"".format(f) for f in edge_pruner]
    formatted_edge_pruner = ",".join(formatted_edge_pruner)
    formatted_node_filter = "|".join(node_return_filter)
    return_filter = ""
    if formatted_node_filter != "":
        return_filter = ".filter{{it.{0}.matches({1})}}".format(
                NODE_PROPERTY.TYPE,
                "\"{0}\"".format(formatted_node_filter))

    # all unique nodes depth 1 from start node with restrictions 
    start = "s=g.v({0}).transform{{[it, it.outE()]}}; ".format(
            NODE_PROPERTY.ID)
    path = """
            n=g.v({0}).out({1}).dedup(){2}.transform{{[it, it.outE()]}}; 
            """.format(
                    NODE_PROPERTY.ID,
                    formatted_edge_pruner,
                    return_filter)
    concat = "[s,n]"

    script = start + path + concat
    params = {NODE_PROPERTY.ID : start_node_id} 

    url = base_url + GREMLIN.PATH
    data = {NEO4J.SCRIPT : script, NEO4J.PARAMS : params}

    response_data = connect(url, json.dumps(data))

    if response_data is None:
        return None
    else:
        return response_parser.format_path(response_data)


def gremlin(base_url, script, params):
    """ Read/Write an unrestricted data set using Gremlin.
    
    Required:
    string base_url     url of db
    string script       gremlin script to run
    dict params         parameters referenced in the script

    Return unformatted neo4j response.

    """
    
    url = base_url + GREMLIN.PATH
    data = {NEO4J.SCRIPT : script, NEO4J.PARAMS : params}

    return connect(url, json.dumps(data))


def connect(url, data):
    """ POST data the the url as a JSON request.

    Required:
    string url      url of the connection
    string data     data to POST

    Return unformatted HTTP response.

    Raises:
    DbConnectionError   bad db connection

    """

    request = urllib2.Request(url, data)
    request.add_header(GREMLIN.REQUEST_HEADER_TYPE, GREMLIN.REQUEST_HEADER)

    try:
        response = urllib2.urlopen(request)
        response_data = response.read()

        # object not found
        if GREMLIN.BASE_ERROR + GREMLIN.NULL_ERROR in response_data:
            return None
        elif GREMLIN.BASE_ERROR + GREMLIN.INPUT_ERROR in response_data:
            # TODO - make this a more explicit DbInputError
            raise DbConnectionError(response_data)
        else:
            return json.loads(response_data)
    except (urllib2.HTTPError, urllib2.URLError) as err:
        raise DbConnectionError(err.read())

