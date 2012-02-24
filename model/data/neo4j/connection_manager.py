""" Module: connection_manager

...
"""
import urllib, urllib2, json, ast

import response_parser

_gremlin_path = "/db/data/ext/GremlinPlugin/graphdb/execute_script"

def create_node(base_url, type, properties):
    url = base_url + _gremlin_path

    # add type to properties dictionary
    properties["type"] = type

    data = {}
    # does grabbing the empty edges list take time here?
    data["script"] = "g.addVertex(properties).transform{[it, it.bothE()]}"
    data["params"] = {"properties": properties}
    
    response_data = connect(url, json.dumps(data))
    return response_parser.format_node(response_data[0])
    
def create_edge(base_url, from_node, to_node, type, properties):
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

def read_node_and_edges(base_url, id):
    url = base_url + _gremlin_path

    data = {}
    data["script"] = "g.v(id).transform{[it, it.bothE()]}"
    data["params"] = {"id":id}
    
    response_data = connect(url, json.dumps(data))
    return response_parser.format_node(response_data[0])

def read_edge(base_url, id):
    return None

def read_nodes_from_immediate_path(
        base_url, 
        start_node_id, 
        edge_pruner,
        node_return_filter): 
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
    start = "s=g.v(id).transform{[it, it.bothE()]}; "
    path = """
            n=g.v(id).both({0}).dedup(){1}.transform{{[it, it.bothE()]}}; 
            """.format(formatted_edge_pruner, return_filter)
    concat = "[s,n]"
    data = {}
    data["script"] = start + path + concat
    data["params"] = {"id": start_node_id} 
  
    response_data = connect(url, json.dumps(data))
    return response_parser.format_path(response_data)

def gremlin(base_url, script, params):
    url = base_url + _gremlin_path

    data = {}
    data["script"] = script
    data["params"] = params
    
    response_data = connect(url, json.dumps(data))
    return response_data

def connect(url, data):
    request = urllib2.Request(url, data)
    request.add_header('Content-Type', "application/json")

    try:
        response = urllib2.urlopen(request)
        response_data = response.read()
        return ast.literal_eval(response_data)
    except (urllib2.HTTPError, urllib2.URLError) as err:
        raise ConnectionError(err.read())

class ConnectionError(Exception):

    """ Exception raised when the database connection breaks. """

    msg = None

    def __init__(self, msg):
        """ Initialize ConnectionError. """
        self.msg = msg

