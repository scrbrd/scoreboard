""" Module: db

Manage incoming db requests and pass them to the proper database.

"""

import urllib2, urllib
from exceptions import NotImplementedError

from model.data import DbInputError, DbReadError, DbWriteError
from model.data import DbConnectionError
from neo4j import connection_manager

HOST = "localhost"
PORT = "7474"
DB = "NEO4J"
BASE_URL = "http://" + HOST + ":" + PORT

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
    if "type" in properties:
        raise DbInputError(
                "properties", 
                properties, 
                "Type included in properties.")
    if type is None:
        raise DbInputError(
                "type", 
                type, 
                "Required 'Type' not inluded.")
    
    try:
        new_node = connection_manager.create_node(BASE_URL, type, properties)
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
    if any(k in properties for k in ("type", "from_node_id", "to_node_id")):
        raise DbInputError(
                k, 
                properties, 
                k + " included in properties.")
    if type is None:
        raise DbInputError(
                "type", 
                type, 
                "Required parameter not included.")
    if from_node_id is None:
        raise DbInputError(
                "from_node_id",
                from_node_id,
                "Required parameter not included.")
    if to_node_id is None:
        raise DbInputError(
                "to_node_id",
                to_node_id,
                "Required parameter not included.")

    try:
        new_edge = connection_manager.create_edge(
                BASE_URL, 
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

    if any(k in properties for k in ("type", "node_id")):
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
                BASE_URL, 
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
        "type", 
        "from_node_id", 
        "to_node_id",
        "edge_id")):
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
                BASE_URL, 
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
        node_data = connection_manager.read_node_and_edges(BASE_URL, node_id)
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
            raise DbInputError(t[0], t[1], "Required parameter not included.")

    try:
        path_data = connection_manager.read_nodes_from_immediate_path(
                BASE_URL,
                start_node_id, 
                edge_pruner,
                node_return_filter)
        return path_data
    except DbConnectionError:
        raise DbReadError("Database read failed.")

def read_node(node_id):
    raise NotImplementedError("TODO - Implement read_node.")
    return None

def read_edge(edge_id):
    raise NotImplementedError("TODO - Implement read_edge.")
    return None


