""" Module: editor

... 
"""

from model.graph import writer

def create_and_connect_node(type, properties_dict, edges_dict):
    """ Create a Node for this SqObject and create its edges.

    Required:
    str type                the type/class of the node
    dict properties_dict    the properties of the node {PROP: VALUE}
    dict edges_dict         the edges of the node {TYPE: {PROP: VALUE}}

    Return bool for success/failure

    """
    is_success = false
    new_node_id = create_node(type, properties_dict)
    if new_node_id is not None:
        is_success = true
        new_edge_ids = create_edges(new_node_id, edges_dict)
        if new_edge_ids is None:
            is_success = false
    return is_success

def create_node(type, properties):
    """ Create a Node with the specified properties. 

    Return new node's id or None for failure.

    """
    return write_node(type, properties)

def create_edges(from_node_id, edges_dict):
    """ Create all Edges from specified node.

    Return new edges' ids or None for failure.

    """
