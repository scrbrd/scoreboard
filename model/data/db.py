""" Module: db

Manage incoming db requests and pass them to the proper database.

"""

import urllib2, urllib

from neo4j import connection_manager

HOST = "localhost"
PORT = "7474"
DB = "NEO4J"

def write_node(properties_dict):

def read_nodes(ids)

def write_edge(from_id, to_id, properties_dict)

def read_edges_by_id(ids)

def read_edges(node_id, properties_filter_dict)

def read_path(node_id, traversal_filter_dict, return_filter, depth) 
