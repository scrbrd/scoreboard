""" Module: connection_manager

Receive database requests, handle neo4j interaction, and
return parsed and formatted nodes, edges, and sets.

All the functions raise DbConnectionError if they can't connect
to the db or if the db returns an error, including a bad id error.

"""

import urllib, urllib2, json

import response_parser
from model.data import DbConnectionError

_gremlin_path = "/db/data/ext/GremlinPlugin/graphdb/execute_script"
_gremlin_base_err = "javax.script.ScriptException: "
_gremlin_null_err = "java.lang.NullPointerException"
_gremlin_input_err = "java.lang.IllegalArgumentException"

def create_node(base_url, type, properties):
    """ Create a node in the db using gremlin and return created node.

    Required:
    string base_url     url of db
    string type         node's 'type'
    dict properties     node's properties dictionary

    Return node as a dictionary.
    keys = node_id, type, properties, edges
    
    """
    url = base_url + _gremlin_path

    # add type to properties dictionary
    properties["type"] = type

    data = {}
    # does grabbing the empty edges list take time here?
    data["script"] = "g.addVertex(properties).transform{[it, it.outE()]}"
    data["params"] = {"properties": properties}
    
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
    url = base_url + _gremlin_path
   
    data = {}
    data["script"] = "g.addEdge(g.v(from),g.v(to),type,properties)"
    data["params"] = {
            "from": from_node, 
            "to": to_node, 
            "type": type,
            "properties": properties}

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
    url = base_url + _gremlin_path

    data = {}
    data["script"] = "g.v(id).transform{[it, it.outE()]}"
    data["params"] = {"id":node_id}
    
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
    url = base_url + _gremlin_path
    
    # formatt the pruners and filter
    formatted_edge_pruner = ["\"{0}\"".format(f) for f in edge_pruner]
    formatted_edge_pruner = ",".join(formatted_edge_pruner)
    formatted_node_filter = "|".join(node_return_filter)
    return_filter = ""
    if formatted_node_filter != "":
        return_filter = ".filter{{it.type.matches({0})}}".format(
                "\"{0}\"".format(formatted_node_filter))

    # all unique nodes depth 1 from start node with restrictions 
    start = "s=g.v(id).transform{[it, it.outE()]}; "
    path = """
            n=g.v(id).out({0}).dedup(){1}.transform{{[it, it.outE()]}}; 
            """.format(formatted_edge_pruner, return_filter)
    concat = "[s,n]"
    data = {}
    data["script"] = start + path + concat
    data["params"] = {"id": start_node_id} 
  
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
    url = base_url + _gremlin_path

    data = {}
    data["script"] = script
    data["params"] = params
    
    response_data = connect(url, json.dumps(data))
    return response_data

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
    request.add_header('Content-Type', "application/json")

    try:
        response = urllib2.urlopen(request)
        response_data = response.read()

        # object not found
        if _gremlin_base_err + _gremlin_null_err in response_data:
            return None
        elif _gremlin_base_err + _gremlin_input_err in response_data:
            # TODO - make this a more explicit DbInputError
            raise DbConnectionError(response_data)
        else:
            loaded_data = json.loads(response_data)
            return loaded_data   
    except (urllib2.HTTPError, urllib2.URLError) as err:
        raise DbConnectionError(err.read())

