""" Module: writer

Provide an API for storing data in a graph database, including create,
update, and delete actions on nodes and edges.

Provides:
    def create_node
    def update_node
    def delete_node
    def create_edge
    def update_edge
    def delete_edge

"""

from model.graph import GraphEdge, GraphNode, GraphInputError
from model.data import db

from time import time


def create_node(type, properties):
    """ Create a node in a graph database.

    Required:
    str     type        type for a new GraphNode
    dict    properties  dict of optional GraphNode properties

    Returns:
    GraphNode           newly created GraphNode

    Raises:
    GraphInputError     bad input

    """

    try:
        node = None

        # make sure callers don't usurp power over the data
        bad_keys = [
                "node_id",
                "type",
                "created_ts",
                "updated_ts",
                "deleted_ts"]

        input_errors = set(bad_keys).intersect(set(properties))

        if input_errors:
            key = input_errors.pop()
            reason = "Invalid input supplied to create_node()."
            raise GraphInputError(key, properties[key], reason)

        # initialize some required properties
        current_ts = int(time())
        properties["created_ts"] = current_ts
        properties["updated_ts"] = current_ts
        properties["deleted_ts"] = None

        # issue a call to the data layer
        node_dict = db.create_node(type, properties)

        node = GraphNode(
                node_dict["node_id"],
                node_dict["type"],
                node_dict["properties"])

    #except DbInputError as e:
        #logger.debug(e.msg)

    #except DbWriteError as e:
        #logger.debug(e.msg)

    finally:
        return node


def update_node(node_id, new_properties):
    """ Update a node in a graph database.

    Required:
    id      node_id     id of the node to update
    dict    properties  dict of optional GraphNode properties

    Returns:
    GraphNode           updated GraphNode

    Raises:
    GraphInputError     bad input

    """

    try:
        node = None

        # make sure callers don't usurp power over the data
        bad_keys = [
                "node_id",
                "type",
                "created_ts",
                "updated_ts",
                "deleted_ts"]
        
        input_errors = set(bad_keys).intersect(set(new_properties))
        
        if input_errors:
            key = input_errors.pop()
            reason = "Invalid input supplied to update_node()."
            raise GraphInputError(key, new_properties[key], reason)

        # make required changes
        new_properties["updated_ts"] = int(time())

        # issue a call to the data layer
        node_dict = db.update_node(node_id, new_properties)

        node = GraphNode(
                node_dict["node_id"],
                node_dict["type"],
                node_dict["properties"])

    #except DbInputError as e:
        #logger.debug(e.msg)

    #except DbWriteError as e:
        #logger.debug(e.msg)

    finally:
        return node


def delete_node(node_id):
    """ Delete a node in a graph database.

    Required:
    id      node_id     id of the node to update

    Returns:
    GraphNode           deleted GraphNode

    """

    try:
        node = None

        # issue a call to the data layer with the required changes
        node_dict = db.delete_node(node_id, {"deleted_ts" : int(time())})

        node = GraphNode(
                node_dict["node_id"],
                node_dict["type"],
                node_dict["properties"])

    #except DbInputError as e:
        #logger.debug(e.msg)

    #except DbWriteError as e:
        #logger.debug(e.msg)

    finally:
        return node


def create_edge(
        from_node_id,
        to_node_id,
        type,
        is_one_way,
        is_unique,
        properties):
    """ Create an edge connecting two nodes in a graph database.

    Required:
    id      from_node_id    id of the node to create the edge from
    id      to_node_id      id of the node to create the edge to
    str     type            type for a new GraphNode
    bool    is_one_way      does the edge point to both nodes?
    bool    is_unique       can nodes have >1 edge of this type
    dict    properties      dict of optional GraphNode properties

    Returns:
    GraphEdge               newly created GraphEdge

    Raises:
    GraphInputError         bad input

    """

    try:
        edge = None

        # make sure callers don't usurp power over the data
        bad_keys = [
                "edge_id",
                "from_node_id",
                "to_node_id",
                "type",
                "is_one_way",
                "is_unique",
                "created_ts",
                "updated_ts",
                "deleted_ts"]

        input_errors = set(bad_keys).intersect(set(properties))

        if input_errors:
            key = input_errors.pop()
            reason = "Invalid input supplied to create_edge()."
            raise GraphInputError(key, properties[key], reason)

        # initialize some required properties

        properties["is_one_way"] = is_one_way
        properties["is_unique"] = is_unique

        current_ts = int(time())
        properties["created_ts"] = current_ts
        properties["updated_ts"] = current_ts
        properties["deleted_ts"] = None

        # issue a call to the data layer
        edge_dict = db.create_edge(from_node_id, to_node_id, type, properties)

        edge = GraphEdge(
                edge_dict["edge_id"],
                edge_dict["from_node_id"],
                edge_dict["to_node_id"],
                edge_dict["type"],
                edge_dict["properties"])

    #except DbInputError as e:
        #logger.debug(e.msg)

    #except DbWriteError as e:
        #logger.debug(e.msg)

    finally:
        return edge


def update_edge(edge_id, new_properties):
    """ Update an edge connecting two nodes in a graph database.

    Required:
    id      edge_id     id of the edge to update
    dict    properties  dict of optional GraphEdge properties

    Returns:
    GraphEdge           updated GraphEdge

    Raises:
    GraphInputError     bad input

    """

    try:
        edge = None

        # make sure callers don't usurp power over the data
        bad_keys = [
                "edge_id",
                "from_node_id",
                "to_node_id",
                "type",
                "is_one_way",
                "is_unique",
                "created_ts",
                "updated_ts",
                "deleted_ts"]

        input_errors = set(bad_keys).intersect(set(new_properties))

        if input_errors:
            key = input_errors.pop()
            reason = "Invalid input supplied to update_edge()."
            raise GraphInputError(key, new_properties[key], reason)

        # make required changes
        new_properties["updated_ts"] = int(time())

        # issue a call to the data layer
        edge_dict = db.update_edge(edge_id, new_properties)

        edge = GraphEdge(
                edge_dict["edge_id"],
                edge_dict["from_node_id"],
                edge_dict["to_node_id"],
                edge_dict["type"],
                edge_dict["properties"])

    #except DbInputError as e:
        #logger.debug(e.msg)

    #except DbWriteError as e:
        #logger.debug(e.msg)

    finally:
        return edge


def delete_edge(edge_id):
    """ Delete an edge connecting two nodes in a graph database.

    Required:
    id      edge_id     id of the edge to update

    Returns:
    GraphEdge           deleted GraphEdge

    """

    try:
        edge = None
        
        # issue a call to the data layer with the required changes 
        edge_dict = db.delete_edge(edge_id, {"deleted_ts" : int(time())})

        edge = GraphEdge(
                edge_dict["edge_id"],
                edge_dict["from_node_id"],
                edge_dict["to_node_id"],
                edge_dict["type"],
                edge_dict["properties"])

    #except DbInputError as e:
        #logger.debug(e.msg)

    #except DbWriteError as e:
        #logger.debug(e.msg)

    finally:
        return edge

