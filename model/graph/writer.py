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

from model.constants import NODE_PROPERTY, EDGE_PROPERTY
from model.data import database_manager
from model.data.data_errors import DbInputError, DbWriteError

from constants import GRAPH_PROPERTY
from model.graph import GraphEdge, GraphNode, GraphInputError


# TODO: change functions and definitions to use GraphProto*

def database():
    """ Get a database from the data layer's database_manager. """
    return database_manager.database()


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
        properties = prototype_node.properties()

        # TODO: move this error checking into GraphPrototype subclasses

        # make sure callers don't usurp power over data input
        bad_properties = [
                NODE_PROPERTY.ID,
                NODE_PROPERTY.TYPE,
                GRAPH_PROPERTY.CREATED_TS,
                GRAPH_PROPERTY.UPDATED_TS,
                GRAPH_PROPERTY.DELETED_TS
                ]

        input_errors = set(bad_properties).intersection(set(properties))

        if input_errors:
            raise GraphInputError(
                    input_errors,
                    "Invalid input supplied to create_node().")

        # initialize some required properties
        current_ts = int(time())
        properties[GRAPH_PROPERTY.CREATED_TS] = current_ts
        properties[GRAPH_PROPERTY.UPDATED_TS] = current_ts
        properties[GRAPH_PROPERTY.DELETED_TS] = False

        # issue a call to the data layer
        node = database().create_node(prototype_node.type(), properties)

        graph_node = GraphNode(
                node[NODE_PROPERTY.ID],
                node[NODE_PROPERTY.TYPE],
                node[NODE_PROPERTY.PROPERTIES],
                node[NODE_PROPERTY.EDGES])

    except DbInputError as e:
        #logger.debug(e.reason)
        print e.reason
        graph_node = None

    except DbWriteError as e:
        #logger.debug(e.reason)
        print e.reason
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
                NODE_PROPERTY.ID,
                NODE_PROPERTY.TYPE,
                GRAPH_PROPERTY.CREATED_TS,
                GRAPH_PROPERTY.UPDATED_TS,
                GRAPH_PROPERTY.DELETED_TS
                ]

        input_errors = set(bad_properties).intersection(set(new_properties))

        if input_errors:
            raise GraphInputError(
                    input_errors,
                    "Invalid input supplied to update_node().")

        # make required changes
        new_properties[GRAPH_PROPERTY.UPDATED_TS] = int(time())

        # issue a call to the data layer
        node = database().update_node(node_id, new_properties)

        graph_node = GraphNode(
                node[NODE_PROPERTY.ID],
                node[NODE_PROPERTY.TYPE],
                node[NODE_PROPERTY.PROPERTIES],
                node[NODE_PROPERTY.EDGES])

    except DbInputError as e:
        #logger.debug(e.reason)
        print(e.reason)
        graph_node = None

    except DbWriteError as e:
        #logger.debug(e.reason)
        print(e.reason)
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
        node = database().delete_node(node_id, {"deleted_ts": int(time())})

        graph_node = GraphNode(
                node[NODE_PROPERTY.ID],
                node[NODE_PROPERTY.TYPE],
                node[NODE_PROPERTY.PROPERTIES],
                node[NODE_PROPERTY.EDGES])

    except DbInputError as e:
        #logger.debug(e.reason)
        print(e.reason)
        graph_node = None

    except DbWriteError as e:
        #logger.debug(e.reason)
        print(e.reason)
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
        properties = prototype_edge.properties()

        # make sure callers don't usurp power over data input
        bad_properties = [
                EDGE_PROPERTY.ID,
                EDGE_PROPERTY.FROM_NODE_ID,
                EDGE_PROPERTY.TO_NODE_ID,
                EDGE_PROPERTY.TYPE,
                #GRAPH_PROPERTY.IS_ONE_WAY,
                #GRAPH_PROPERTY.IS_UNIQUE,
                GRAPH_PROPERTY.CREATED_TS,
                GRAPH_PROPERTY.UPDATED_TS,
                GRAPH_PROPERTY.DELETED_TS
                ]

        input_errors = set(bad_properties).intersection(set(properties))

        if input_errors:
            raise GraphInputError(
                    input_errors,
                    "Invalid input supplied to create_edge().")

        # initialize some required properties

        #properties["is_one_way"] = is_one_way
        #properties["is_unique"] = is_unique

        current_ts = int(time())
        properties[GRAPH_PROPERTY.CREATED_TS] = current_ts
        properties[GRAPH_PROPERTY.UPDATED_TS] = current_ts
        properties[GRAPH_PROPERTY.DELETED_TS] = False

        # issue a call to the data layer
        edge = database().create_edge(
                prototype_edge.from_node_id(),
                prototype_edge.to_node_id(),
                prototype_edge.type(),
                properties)

        graph_edge = GraphEdge(
                edge[EDGE_PROPERTY.ID],
                edge[EDGE_PROPERTY.TYPE],
                edge[EDGE_PROPERTY.PROPERTIES],
                edge[EDGE_PROPERTY.FROM_NODE_ID],
                edge[EDGE_PROPERTY.TO_NODE_ID])

    except DbInputError as e:
        #logger.debug(e.reason)
        print(e.reason)
        graph_edge = None

    except DbWriteError as e:
        #logger.debug(e.reason)
        print(e.reason)
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
                EDGE_PROPERTY.ID,
                EDGE_PROPERTY.FROM_NODE_ID,
                EDGE_PROPERTY.TO_NODE_ID,
                EDGE_PROPERTY.TYPE,
                #GRAPH_PROPERTY.IS_ONE_WAY,
                #GRAPH_PROPERTY.IS_UNIQUE,
                GRAPH_PROPERTY.CREATED_TS,
                GRAPH_PROPERTY.UPDATED_TS,
                GRAPH_PROPERTY.DELETED_TS
                ]

        input_errors = set(bad_properties).intersection(set(new_properties))

        if input_errors:
            raise GraphInputError(
                    input_errors,
                    "Invalid input supplied to update_edge().")

        # make required changes
        new_properties[GRAPH_PROPERTY.UPDATED_TS] = int(time())

        # issue a call to the data layer
        edge = database().update_edge(edge_id, new_properties)

        graph_edge = GraphEdge(
                edge[EDGE_PROPERTY.ID],
                edge[EDGE_PROPERTY.TYPE],
                edge[EDGE_PROPERTY.PROPERTIES],
                edge[EDGE_PROPERTY.FROM_NODE_ID],
                edge[EDGE_PROPERTY.TO_NODE_ID])

    except DbInputError as e:
        #logger.debug(e.reason)
        print(e.reason)
        graph_edge = None

    except DbWriteError as e:
        #logger.debug(e.reason)
        print(e.reason)
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
        edge = database().delete_edge(
                edge_id,
                {GRAPH_PROPERTY.DELETED_TS: int(time())})

        graph_edge = GraphEdge(
                edge[EDGE_PROPERTY.ID],
                edge[EDGE_PROPERTY.TYPE],
                edge[EDGE_PROPERTY.PROPERTIES],
                edge[EDGE_PROPERTY.FROM_NODE_ID],
                edge[EDGE_PROPERTY.TO_NODE_ID])

    except DbInputError as e:
        #logger.debug(e.reason)
        print(e.reason)
        graph_edge = None

    except DbWriteError as e:
        #logger.debug(e.reason)
        print(e.reason)
        graph_edge = None

    return graph_edge
