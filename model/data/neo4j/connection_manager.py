""" Module: connection_manager

...
"""
import urllib, urllib2, json, ast

import response_parser

_read_path = "/db/data/cypher"
_write_path = "/db/data"

def create_node(base_url, type, properties):
    url = base_url + _write_path + "/node"

    # add type to properties dictionary
    properties["type"] = type

    #    print("JSON: " + json.dumps(properties))
    response_data = connect(url, json.dumps(properties)) 

    return response_parser.rest_data_to_node(response_data)

def create_edge(base_url, from_node, to_node, type, properties):
    # include from_node in url
    url = "{0}{1}/node/{2}/relationships".format(
            base_url, 
            _write_path, 
            from_node)
   
    # construct edge write data
    data = {}
    to_url = "{0}{1}/node/{2}".format(base_url, _write_path, to_node)
    data["to"] = to_url
    data["type"] = type
    data["data"] = properties 

    response_data = connect(url, json.dumps(data))

    return response_parser.rest_data_to_edge(response_data)

def update_node(base_url, id, properties):
    return None

def update_edge(base_url, id, properties):
    return None

def read_node_and_edges(base_url, id):
    url = base_url + _read_path

    # construct cypher query
    start_val = "n = node({0})".format(id)
    match_val = "n-[r]-(b)"
    return_val = "n, r"
    query_val = "\"start " + start_val
    if match_val != "":
        query_val = query_val + " match " + match_val
    query_val = query_val + " return " + return_val + "\""
    data = "{\"query\": " + query_val + ", \"params\": {}}"
    
    response_data = connect(url, data)
    return response_parser.cypher_data_to_node(response_data)

def read_edge(base_url, id):
    return None

def read_path(
        base_url, 
        start_node, 
        node_return_filter, 
        edge_pruner,
        node_pruner,
        depth):
    return None

def connect(url, data):
    request = urllib2.Request(url, data)
    request.add_header('Content-Type', "application/json")

    # print("DATA: " + data)

    response_data = ""
    try:
        response = urllib2.urlopen(request)
        response_data = response.read()
    except (urllib2.HTTPError, urllib2.URLError) as err:
        print("response: " + str(err.read()))
        response_data = "BAD CONNECTION TO DB OR INVALID RESPONSE" 

    return ast.literal_eval(response_data)

class ConnectionError(Exception):

    """ Exception raised when the database connection breaks. """

    msg = None

    def __init__(self, msg):
        """ Initialize ConnectionError. """
        self.msg = msg

