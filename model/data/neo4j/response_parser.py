""" Module: response_parser

Parse data lists/dicts from neo4j and return nodes/edges.

"""

from model.constants import NODE_PROPERTY, EDGE_PROPERTY

from constants import NEO4J


def format_path(raw_path):
    """ Convert gremlin depth 1 path into a formatted path dict.

    {depth:{node_id:node}}

    Required:
    list    raw_path    unformmated neo4j path as a pair of lists

    Return:
    dict                start, end nodes keyed on depth, node id

    """
    return {
            0 : format_nodes(raw_path[0]),
            1 : format_nodes(raw_path[1]),
            }


def format_nodes(raw_nodes):
    """ Convert gremlin nodes data to a formatted node dict.

    {node_id: node}

    Required:
    list    raw_nodes   unformatted neo4j nodes

    Return:
    dict                properly formatted neo4j nodes

    """
    nodes = {}

    for raw_node in raw_nodes:
        node = format_node(raw_node)
        nodes[node[NODE_PROPERTY.ID]] = node

    return nodes


def format_node(raw_node):
    """ Convert gremlin node data to a formatted node.

    keys = node_id, type, properties

    Required:
    dict    raw_node    unformatted neo4j node 
    
    Return:
    dict                formatted neo4j node

    """
    node = {}

    node_section = raw_node[0]
    edge_section = raw_node[1]

    node[NODE_PROPERTY.ID] = url_to_id(node_section[NEO4J.SELF])

    # its properties 
    properties = node_section[NEO4J.DATA]
    node[NODE_PROPERTY.TYPE] = properties.pop(NODE_PROPERTY.TYPE)
    node[NODE_PROPERTY.PROPERTIES] = properties

    # grab nodes' edges
    node[NODE_PROPERTY.EDGES] = format_edges(edge_section)

    return node


def format_edges(raw_edges): 
    """ Convert gremlin edges data to a formatted edges dict.

    {edge_id: edge}

    Required:
    list    raw_edges   unformatted neo4j edges as a list

    Return:
    dict                properly formatted neo4j edges

    """
    edges= {}
    
    for raw_edge in raw_edges:
        edge = format_edge(raw_edge)
        edges[edge[EDGE_PROPERTY.ID]] = edge

    return edges


def format_edge(raw_edge):
    """ Convert gremlin edge data to a formatted edge.

    keys = edge_id, properties, from_node_id, to_node_id, type

    Required:
    dict    raw_edge    unformmatted neo4j edge

    Return:
    dict                properly formatted neo4j edge

    """
    return {
            EDGE_PROPERTY.ID : url_to_id(raw_edge[NEO4J.SELF]),
            EDGE_PROPERTY.PROPERTIES : raw_edge[NEO4J.DATA],
            EDGE_PROPERTY.FROM_NODE_ID : url_to_id(raw_edge[NEO4J.START]),
            EDGE_PROPERTY.TO_NODE_ID : url_to_id(raw_edge[NEO4J.END]),
            EDGE_PROPERTY.TYPE : raw_edge[NEO4J.TYPE],
            }


def url_to_id(url):
    """ Extract the id from a neo4j url. """
    return int(url.rpartition("/")[2])

