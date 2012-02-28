""" Module: response_parser

Parse data lists/dicts from neo4j and return nodes/edges.

"""

def format_path(raw_path):
    """ Convert gremlin depth 1 path into a formatted path dict.

    Required:
    list raw_path   unformmated neo4j path as a pair of lists

    Return dict of start and end nodes keyed on depth and node id.
    {depth:{node_id:node}}

    """
    path = {}
    path[0] = format_nodes(raw_path[0])
    path[1] = format_nodes(raw_path[1])

    return path

def format_nodes(raw_nodes):
    """ Convert gremlin nodes data to a formatted node dict.

    Required:
    list raw_nodes  unformatted neo4j nodes as a list

    Return dict of properly formatted nodes.
    {node_id: node}

    """
    nodes = {}
    for raw_n in raw_nodes:
        node = format_node(raw_n)
        nodes[node["node_id"]] = node
    return nodes

def format_node(raw_node):
    """ Convert gremlin node data to a formatted node.
    
    Required:
    dict raw_node   unformatted neo4j node 
    
    Return node as a dict.
    keys = node_id, type, properties

    """
    node = {}

    node_section = raw_node[0]
    edge_section = raw_node[1]

    node["node_id"] = url_to_id(node_section["self"])

    # its properties 
    properties = node_section["data"]
    node["type"] = properties.pop("type")
    node["properties"] = properties
    
    # grab nodes' edges
    node["edges"] = format_edges(edge_section)

    return node

def format_edges(raw_edges): 
    """ Convert gremlin edges data to a formatted edges dict.

    Required:
    list raw_edges  unformatted neo4j edges as a list

    Return dict of properly formatted edges.
    {edge_id: edge}

    """
    edges= {}
    
    for raw_e in raw_edges:
        edge = format_edge(raw_e)
        edges[edge["edge_id"]] = edge

    return edges

def format_edge(raw_edge):
    """ Convert gremlin edge data to a formatted edge.

    Required:
    dict raw_edge  unformmatted neo4j edge

    Return a properly formatted edge as a dict. 
    keys = edge_id, properties, from_node_id, to_node_id, type

    """
    edge = {}

    edge_id = url_to_id(raw_edge["self"])
    edge["edge_id"] = edge_id
    edge["properties"] = raw_edge["data"]
    edge["from_node_id"] = url_to_id(raw_edge["start"])
    edge["to_node_id"] = url_to_id(raw_edge["end"])
    edge["type"] = raw_edge["type"]

    return edge

def url_to_id(url):
    """ Extract the id from a neo4j url. """
    return int(url.rpartition("/")[2])

