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

from time import time

from model.data import db, DbInputError, DbReadError, DbWriteError
from model.graph import GraphEdge, GraphNode, GraphInputError


# TODO: change functions and definitions to use GraphProto*

def create_node(prototype_node):
    """ Create a node in a graph database.

    Required:
    GraphProtoNode  prototype_node  unwritten version of GraphNode 

    Returns:
    GraphNode                       newly created GraphNode

    Raises:
    GraphInputError                 bad input

    """

    graph_node = None

    try:

        # isolate the GraphProtoNode members we need
        type = prototype_node.type()
        properties = prototype_node.properties()

        # TODO: move this error checking into GraphPrototype subclasses

        # make sure callers don't usurp power over data input
        bad_properties = [
                "node_id",
                "type",
                "created_ts",
                "updated_ts",
                "deleted_ts"]

        input_errors = set(bad_properties).intersection(set(properties))

        if input_errors:
            raise GraphInputError(
                    input_errors,
                    "Invalid input supplied to create_node().")

        # initialize some required properties
        current_ts = int(time())
        properties["created_ts"] = current_ts
        properties["updated_ts"] = current_ts
        properties["deleted_ts"] = False

        # issue a call to the data layer
        node = db.create_node(type, properties)

        graph_node = GraphNode(
                node["node_id"],
                node["type"],
                node["properties"],
                node["edges"])

    except DbInputError as e:
        #logger.debug(e.reason)
        graph_node = None

    except DbWriteError as e:
        #logger.debug(e.reason)
        graph_node = None

    return graph_node


# TODO: replace new_properties with GraphProtoEdge
def update_node(node_id, new_properties):
    """ Update a node in a graph database.

    Required:
    id      node_id         id of the node to update
    dict    new_properties  dict of optional GraphNode properties

    Returns:
    GraphNode               updated GraphNode

    Raises:
    GraphInputError         bad input

    """

    graph_node = None

    try:
        # make sure callers don't usurp power over data input
        bad_properties = [
                "node_id",
                "type",
                "created_ts",
                "updated_ts",
                "deleted_ts"]
        
        input_errors = set(bad_properties).intersection(set(new_properties))
        
        if input_errors:
            raise GraphInputError(
                    input_errors,
                    "Invalid input supplied to update_node().")

        # make required changes
        new_properties["updated_ts"] = int(time())

        # issue a call to the data layer
        node = db.update_node(node_id, new_properties)

        graph_node = GraphNode(
                node["node_id"],
                node["type"],
                node["properties"],
                node["edges"])

    except DbInputError as e:
        #logger.debug(e.reason)
        graph_node = None

    except DbWriteError as e:
        #logger.debug(e.reason)
        graph_node = None

    return graph_node


def delete_node(node_id):
    """ Delete a node in a graph database.

    Required:
    id          node_id     id of the node to update

    Returns:
    GraphNode               deleted GraphNode

    """

    graph_node = None

    try:
        # issue a call to the data layer with the required changes
        node = db.delete_node(node_id, {"deleted_ts" : int(time())})

        graph_node = GraphNode(
                node["node_id"],
                node["type"],
                node["properties"],
                node["edges"])

    except DbInputError as e:
        #logger.debug(e.reason)
        graph_node = None

    except DbWriteError as e:
        #logger.debug(e.reason)
        graph_node = None

    return graph_node


def create_edge(prototype_edge):
    """ Create an edge connecting two nodes in a graph database.

    Required:
    GraphProtoEdge  prototype_edge  unwritten version of GraphEdge

    Returns:
    GraphEdge                       newly created GraphEdge

    Raises:
    GraphInputError                 bad input

    """

    graph_edge = None

    try:
        # make sure callers don't usurp power over data input
        bad_properties = [
                "edge_id",
                "from_node_id",
                "to_node_id",
                "type",
                "is_one_way",
                "is_unique",
                "created_ts",
                "updated_ts",
                "deleted_ts"]

        input_errors = set(bad_properties).intersection(set(properties))

        if input_errors:
            raise GraphInputError(
                    input_errors,
                    "Invalid input supplied to create_edge().")

        # initialize some required properties

        properties["is_one_way"] = is_one_way
        properties["is_unique"] = is_unique

        current_ts = int(time())
        properties["created_ts"] = current_ts
        properties["updated_ts"] = current_ts
        properties["deleted_ts"] = False

        # issue a call to the data layer
        edge = db.create_edge(from_node_id, to_node_id, type, properties)

        graph_edge = GraphEdge(
                edge["edge_id"],
                edge["type"],
                edge["properties"],
                edge["from_node_id"],
                edge["to_node_id"])

    except DbInputError as e:
        #logger.debug(e.reason)
        graph_edge = None

    except DbWriteError as e:
        #logger.debug(e.reason)
        graph_edge = None

    return graph_edge

# TODO: replace new_properties with GraphProtoEdge
def update_edge(edge_id, new_properties):
    """ Update an edge connecting two nodes in a graph database.

    Required:
    id          edge_id         id of the edge to update
    dict        new_properties  dict of optional GraphEdge properties

    Returns:
    GraphEdge                   updated GraphEdge

    Raises:
    GraphInputError             bad input

    """

    graph_edge = None

    try:
        # make sure callers don't usurp power over data input
        bad_properties = [
                "edge_id",
                "from_node_id",
                "to_node_id",
                "type",
                "is_one_way",
                "is_unique",
                "created_ts",
                "updated_ts",
                "deleted_ts"]

        input_errors = set(bad_properties).intersection(set(new_properties))

        if input_errors:
            raise GraphInputError(
                    input_errors,
                    "Invalid input supplied to update_edge().")

        # make required changes
        new_properties["updated_ts"] = int(time())

        # issue a call to the data layer
        edge = db.update_edge(edge_id, new_properties)

        graph_edge = GraphEdge(
                edge["edge_id"],
                edge["type"],
                edge["properties"],
                edge["from_node_id"],
                edge["to_node_id"])

    except DbInputError as e:
        #logger.debug(e.reason)
        graph_edge = None

    except DbWriteError as e:
        #logger.debug(e.reason)
        graph_edge = None

    return graph_edge


def delete_edge(edge_id):
    """ Delete an edge connecting two nodes in a graph database.

    Required:
    id          edge_id     id of the edge to update

    Returns:
    GraphEdge               deleted GraphEdge

    """

    graph_edge = None
        
    try:
        # issue a call to the data layer with the required changes 
        edge = db.delete_edge(edge_id, {"deleted_ts" : int(time())})

        graph_edge = GraphEdge(
                edge["edge_id"],
                edge["type"],
                edge["properties"],
                edge["from_node_id"],
                edge["to_node_id"])

    except DbInputError as e:
        #logger.debug(e.reason)
        graph_edge = None

    except DbWriteError as e:
        #logger.debug(e.reason)
        graph_edge = None

    return graph_edge

