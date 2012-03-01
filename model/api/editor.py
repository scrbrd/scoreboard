""" Module: editor

... 
"""

from model.graph import writer
from model.api import SqFactory

def create_node(type, properties, edges):
    """ Create a Node for this SqObject and create its edges.

    Required:
    str type            the type/class of the node
    dict properties     the properties of the node {PROP: VALUE}
    list edges          list of edges as dict
    
    edges list's dicts' keys: "from_id", "type", "properties"

    Return new SqNode if success and None if failure

    """
    is_one_way = true
    is_unique = false
    
    try:
        # new_node of type GraphNode
        new_node = writer.create_node(type, properties)
        new_edges = []
        if new_node is not None:
            node_id = new_node["node_id"]

            for e in edges:
                from_id = node_id
                to_id = node_id
                if "from_id" is in e:
                    from_id = e["from_id"]
                if "to_id" is in e:
                    to_id = e["to_id"]
                type = e["type"]
                properties = e["properties"]
                # new_edge of type GraphEdge
                new_edge = writer.create_edges(
                        from_id,
                        to_id,
                        type,
                        is_one_way,
                        is_unique,
                        properties)
                if new_edge is None:
                    return None
                new_edges.append(new_edge)
    
        return SqFactory.getClass(new_node, new_edges)
    except:
        return None

#def create_node(type, properties):
#    """ Create a Node with the specified properties. 
#
#    Return new node's id or None for failure.
#
#    """
#    return write_node(type, properties)
#
#def create_edges(from_node_id, edges_dict):
#    """ Create all Edges from specified node.
#
#    Return new edges' ids or None for failure.
#
#    """
