""" Module: connection_manager

Receive database requests, handle neo4j interaction, and
return parsed and formatted nodes, edges, and sets.

All the functions raise DbConnectionError if they can't connect
to the db or if the db returns an error, including a bad id error.

"""

import urllib, urllib2, json
from exceptions import NotImplementedError

from model.constants import NODE_PROPERTY, EDGE_PROPERTY
from model.data import DbConnectionError

from constants import NEO4J, NEO4J_INDEX, GREMLIN
import response_parser


def create_node(base_url, type, properties):
    """ Create, store, and return a new Neo4j node using Gremlin.

    Keys: node_id, type, properties, edges

    Required:
    url     base_url    database url
    str     type        type of neo4j node to create
    dict    properties  properties to set in new neo4j node

    Return:
    dict                properly formatted node

    """

    # add type to properties dictionary before generating script
    properties[NODE_PROPERTY.TYPE] = type

    # TODO: does grabbing the empty edges list take time here?

    # write a gremlin query and specify substitution fields
    script = "g.addVertex({0}).transform{{[it, it.outE()]}}".format(
            NODE_PROPERTY.PROPERTIES)

    # specify substitution values for the gremlin query
    params = {NODE_PROPERTY.PROPERTIES : properties}

    # send a request to the database
    response = gremlin(base_url, script, params)

    # TODO: raise an error if response is empty?

    # format the response as a proper node
    return response_parser.format_node(response[0])


def create_edge(base_url, from_node_id, to_node_id, type, properties):
    """ Create, store, and return a new Neo4j edge using Gremlin.

    Keys: edge_id, from_node_id, to_node_id, type, properties

    Required:
    url     base_url        database url
    id      from_node_id    id of outgoing node
    id      to_node_id      id of incoming node
    str     type            type of neo4j edge to create
    dict    properties      properties to set in new neo4j edge 

    Return:
    dict                    properly formatted edge

    """

    # write a gremlin query and specify substitution fields
    script = "g.addEdge(g.v({0}), g.v({1}), {2}, {3})".format(
            EDGE_PROPERTY.FROM_NODE_ID,
            EDGE_PROPERTY.TO_NODE_ID,
            EDGE_PROPERTY.TYPE,
            EDGE_PROPERTY.PROPERTIES)

    # specify substitution values for the gremlin query
    params = {
            EDGE_PROPERTY.FROM_NODE_ID : from_node_id,
            EDGE_PROPERTY.TO_NODE_ID : to_node_id,
            EDGE_PROPERTY.TYPE : type,
            EDGE_PROPERTY.PROPERTIES : properties,
            }

    # send a request to the database
    response = gremlin(base_url, script, params)

    # TODO: raise an error if response is empty?

    # format the response as a proper edge 
    return response_parser.format_edge(response)


def update_node(base_url, id, properties):
    raise NotImplementedError("NOT IMPLEMENTED...DO NOT CALL!")


def update_edge(base_url, id, properties):
    raise NotImplementedError("NOT IMPLEMENTED...DO NOT CALL!")


def read_node_and_edges(base_url, node_id):
    """ Read and return a Neo4j node and its edges using Gremlin.

    Keys: node_id, type, properties, edges

    Required:
    url     base_url    database url
    id      node_id     id of node to query

    Return:
    dict                properly formatted node

    """

    # write a gremlin query and specify substitution fields
    # [ [ { v }, [ { Pipe }, { Pipe }, { Pipe } ] ] ]
    script = "g.v({0}).transform{{[it, it.outE()]}}".format(NODE_PROPERTY.ID)

    # specify substitution values for the gremlin query
    params = {NODE_PROPERTY.ID : node_id}

    # send a request to the database
    response = gremlin(base_url, script, params)
    
    # if the response isn't empty, format it as a proper node
    if response is None:
        return None
    elif not response:
        return {}
    else:
        return response_parser.format_node(response[0])


def read_nodes_by_index(base_url, key, value, node_return_filter=None):
    """ Read and return a Neo4j node and its edges using Gremlin.

    Perform this lookup from a database index rather than by ID.

    Keys: node_id, type, properties, edges

    Required:
    url     base_url            database url
    str     key                 indexed node property to look up
    mixed   value               value (ideally unique) to look up

    Optional:
    list    node_return_filter  node types to filter for

    Return:
    dict                        properly formatted node

    """

    # write a gremlin query

    filter = ""
    if node_return_filter:
        filter = ".filter{{it.{0}.matches({1})}}".format(
                NODE_PROPERTY.TYPE,
                "\"{0}\"".format("|".join(node_return_filter)))

    # specify substitution fields
    # [ { v }, [ { Pipe }, { Pipe } ] ]
    script = """
    g.idx(\"{0}\").get({1}, {2})._(){3}.transform{{[it, it.outE()]}}
    """.format(
            NEO4J_INDEX.NODES,
            key,
            value,
            filter)

    # specify substitution values for the gremlin query
    params = {
            key : key,
            value : value,
            NODE_PROPERTY.TYPE : NODE_PROPERTY.TYPE,
            }

    # send a request to the database
    response = gremlin(base_url, script, params)

    # if the response isn't empty, format it as a proper node
    if response is None:
        return None
    elif not response:
        return {}
    else:
        return response_parser.format_nodes(response)


def read_edge(base_url, edge_id):
    raise NotImplementedError("NOT IMPLEMENTED...DO NOT CALL!")


def read_nodes_from_immediate_path(
        base_url, 
        start_node_id, 
        edge_pruner,
        node_return_filter): 
    """ Read and return a depth-1 set of Neo4j nodes using Gremlin.

    Use edge_pruner and node_return_filter to impose path constraints.

    {depth: {node_id: node}}

    Required:
    url     base_url            database url
    id      start_node_id       id of requested neo4j node
    list    edge_pruner         edges to traverse (None=all)
    list    node_return_filter  nodes to return (None=all)

    Return:
    dict                        formatted nodes keyed on depth and id

    """

    # None is standard for specifying no filter (or, filter for all types"). an
    # empty list would be the correct way to ask for no return types, but we
    # consider that to be an obvious error, which is raised a layer above by
    # the generic model.db, which has no knowledge of or interest in how we
    # format these filters here.

    if edge_pruner is None:
        edge_pruner = []

    if node_return_filter is None:
        node_return_filter = []

    # TODO: there's got to be a better way to do all of this string formatting

    # format the pruners and filter
    edge_pruner = ",".join(["\"{0}\"".format(f) for f in edge_pruner])

    return_filter = ""
    if node_return_filter:
        return_filter = ".filter{{it.{0}.matches({1})}}".format(
                NODE_PROPERTY.TYPE,
                "\"{0}\"".format("|".join(node_return_filter)))

    # all unique nodes depth 1 from start node with restrictions 
    start = "s=g.v({0}).transform{{[it, it.outE()]}}; ".format(
            NODE_PROPERTY.ID)
    path = """
            n=g.v({0}).out({1}).dedup(){2}.transform{{[it, it.outE()]}}; 
            """.format(
                    NODE_PROPERTY.ID,
                    edge_pruner,
                    return_filter)
    concat = "[s,n]"

    # write a gremlin query and specify substitution fields
    script = start + path + concat

    # specify substitution values for the gremlin query
    params = {NODE_PROPERTY.ID : start_node_id} 

    # send a request to the database
    response = gremlin(base_url, script, params)

    # if the response isn't empty, format it as a proper edge
    if response is None:
        return None
    else:
        return response_parser.format_path(response)


def gremlin(base_url, script, params):
    """ POST a Gremlin JSON request to a URL and handle the response.
    
    Script and parameters describe the JSON request, and base_url and the
    Gremlin path describe the database to send it to.

    Required:
    url     base_url    database url
    str     script      gremlin script query
    dict    params      paramters to substitute in script

    Return:
    json                unformatted HTTP response.

    Raises:
    DbConnectionError   bad db connection

    """

    request = urllib2.Request(
            base_url + GREMLIN.PATH,
            json.dumps({NEO4J.SCRIPT : script, NEO4J.PARAMS : params}))

    request.add_header(GREMLIN.REQUEST_HEADER_TYPE, GREMLIN.REQUEST_HEADER)

    response = None

    try:
        serialized_response = urllib2.urlopen(request).read()

        # object not found
        if GREMLIN.BASE_ERROR + GREMLIN.NULL_ERROR in serialized_response:
            # TODO: raise an error? when do we get to this case?
            response = None

        # input failed
        elif GREMLIN.BASE_ERROR + GREMLIN.INPUT_ERROR in serialized_response:
            # TODO: make this a more explicit DbInputError
            raise DbConnectionError(serialized_response)

        # success!
        else:
            response = json.loads(serialized_response)

    except (urllib2.HTTPError, urllib2.URLError) as err:
        raise DbConnectionError(err.read())

    return response

