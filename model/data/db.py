""" Module: db

Manage incoming db requests and pass them to the proper database.

"""

import urllib2, urllib
from exceptions import NotImplementedError

from model.constants import NODE_PROPERTY, EDGE_PROPERTY
from model.data.constants import DATABASE

from model.data import DbInputError, DbReadError, DbWriteError
from model.data import DbConnectionError
from neo4j import connection_manager


def create_node(type, properties):
    """ Create a new node and return it.
    
    Checks for valid input and if valid, writes node to db.

    Required:
    string type         type of node
    dict properties     a dict of all the node's properties
    
    Returns the created Node.

    Raises:
    DbInputError        bad input
    DbWriteError        failed to write to database

    """
    
    _validate_input(properties, {NODE_PROPERTY.TYPE : type})
    
    try:
        new_node = connection_manager.create_node(
                DATABASE.BASE_URL, 
                type, 
                properties)
        if new_node is None:
            raise DbWriteError(
                    "create_node", 
                    "No new node returned from database.")
        return new_node
    except DbConnectionError:
        raise DbWriteError("create_node", "Database write failed.")


def create_edge(from_node_id, to_node_id, type, properties):
    """ Create a new edge and return it.
    
    Checks for valid input and if valid, writes edge to db.

    Required:
    int from_node_id    id of start node
    int to_node_id      if of end node
    string type         type of edge
    dict properties     a dict of all the edge's properties
    
    Returns the created edge.

    Raises:
    DbInputError        bad input
    DbWriteError        failed to write to database

    """

    special_params = {
            EDGE_PROPERTY.TYPE : type, 
            EDGE_PROPERTY.FROM_NODE_ID : from_node_id, 
            EDGE_PROPERTY.TO_NODE_ID : to_node_id 
            }
    _validate_input(properties, special_params)

    try:
        new_edge = connection_manager.create_edge(
                DATABASE.BASE_URL, 
                from_node_id,
                to_node_id,
                type, 
                properties)
        if new_edge is None:
            raise DbWriteError(
                    "create_edge", 
                    "No new edge returned from database.")
        return new_edge
    except DbConnectionError:
        raise DbWriteError("create_edge", "Database write failed.")


def update_node(node_id, properties):
    """ Update existing node and return it.

    NOT IMPLEMENTED

    Required:
    int node_id         id of node to update
    dict properties     dictionary of new/updated properties
    
    Returns the node with updated properties.

    Raises:
    DbInputError    bad input
    DbWriteError    failed to write to database

    """
    raise NotImplementedError("TODO - Implement update_node.")

    if any(k in properties for k in (NODE_PROPERTY.TYPE, NODE_PROPERTY.ID)):
        raise DbInputError(
                k, 
                properties, 
                k + " included in properties.")
    if node_id is None:
        raise DbInputError(
                "node_id".
                node_id,
                "Required parameter not included.")
    
    try:
        updated_node = connection_manager.update_node(
                DATABASE.BASE_URL, 
                node_id, 
                properties)
        if updated_node is None:
            raise DbWriteError(
                    "update_node", 
                    "No updated node returned from database.")
        return updated_node
    except DbConnectionError:
        raise DbWriteError("update_node", "Database write failed.")


def update_edge(edge_id, properties):
    """ Update existing edge and return it.

    Required:
    int edge_id     id of edge to update
    dict properties dictionary of new/updated properties

    Returns the edge with updated properties.

    Raises:
    DbInputError    bad input
    DbWriteError    failed to write to database
    
    """
    raise NotImplementedError("TODO - Implement update_edge.")
    
    if any(k in properties for k in (
        EDGE_PROPERTY.TYPE,
        EDGE_PROPERTY.FROM_NODE_ID,
        EDGE_PROPERTY.TO_NODE_ID,
        EDGE_PROPERTY.ID)):
        raise DbInputError(
            k,
            properties,
            k + " included in properties.")
    if edge_id is None:
        raise DbInputError(
                "edge_id".
                edge_id,
                "Required parameter not included.")
    try:
        updated_edge = connection_manager.update_edge(
                DATABASE.BASE_URL, 
                edge_id, 
                properties)
        if updated_edge is None:
            raise DbWriteError(
                    "update_edge", 
                    "No updated edge returned from database.")
        return updated_node
    except DbConnectionError:
        raise DbWriteError("update_edge", "Database write failed.")


def delete_node(node_id, properties):
    raise NotImplementedError("TODO - Implement delete_node.")
    return None


def delete_edge(edge_id, properties):
    raise NotImplementedError("TODO - Implement delete_edge.")
    return None


def read_node_and_edges(node_id):
    """ Read a node and its edges. 
    
    Required:
    int node_id     id of requested Node

    Returns node as a dictionary or None if node not found

    Raises:
    DbReadError     db threw error

    """
    try:
        node_data = connection_manager.read_node_and_edges(
                DATABASE.BASE_URL, 
                node_id)
        return node_data
    except DbConnectionError:
        raise DbReadError("Database read failed.")


def read_nodes_from_immediate_path(
        start_node_id, 
        edge_pruner,
        node_return_filter):
    """ Read a pruned path from the database and return a filtered dict.

    Prune the path based on the edges list. Restrict the returned nodes 
    to the filtered dictionary and the starting node.

    No duplicate edges in traversal. No duplicates in node lists.

    Returns path    {depth:{id:node}}

    Raises:
    DbInputError    if parameters are missing or incorrect
    DbReadError     db threw error

    """
    required = ((start_node_id, "start_node_id"),
            (node_return_filter, "return_node_filter"),
            (edge_pruner, "edge_pruner"))
    for t in required:
        if t[0] is None:
            raise DbInputError(
                    t[0], 
                    t[1], 
                    "Required parameter not included.")

    try:
        return connection_manager.read_nodes_from_immediate_path(
                DATABASE.BASE_URL,
                start_node_id, 
                edge_pruner,
                node_return_filter)

    except DbConnectionError:
        raise DbReadError("Database read failed.")


def read_node(node_id):
    raise NotImplementedError("TODO - Implement read_node.")
    return None


def read_edge(edge_id):
    raise NotImplementedError("TODO - Implement read_edge.")
    return None


def _validate_input(properties, special_params):
    """ Validate the input properties. 
    
    Check for both disallowed keys and null values.

    Required:
    dict properties         dict for all properties
    dict special_params     dict for required non-props params
    
    Return True for validation or raise error.

    Raises:
    DbInputError    bad input
    
    """
    # check each property for being a special key and for no value
    for prop, value in properties.items():
        # check each special key against props and for no value
        for special_key, special_val in special_params.items():
            if prop == special_key:
                raise DbInputError(
                        special_key, 
                        properties, 
                        special_key + " included in properties.")
            if special_val is None:
                raise DbInputError(
                        special_key, 
                        "None", 
                        "Required parameter not included.")

        # check each prop for no value
        if value is None:
            raise DbInputError(
                    prop,
                    value,
                    "Null/None properties not allowed.")

    # if no properties still check special keys
    if len(properties) == 0:
        for special_key, special_val in special_params.items():
            if special_val is None:
                raise DbInputError(
                        special_key, 
                        "None", 
                        "Required parameter not included.")
    return True

