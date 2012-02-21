""" Module: response_parser

...
"""

def cypher_data_to_node(data_dict):
    
    # pull node data from data dictionary
    node_data = data_dict["data"][0][0]

    # get a node dictionary with id, type, properties
    node_dict = node_data_to_node(node_data)
    
    # pull the edge data from the data dictionary
    edges = [v[1] for v in data_dict["data"]]
   
    # get the edge dictionary with ids, type, properties
    node_dict["edges"] = edges_data_to_edges(edges)

    return node_dict

def rest_data_to_node(data_dict):
    node_dict = node_data_to_node(data_dict)
    
    # rest data doesn't have edges included in request
    node_dict["edges"] = {} 

    return node_dict

def rest_data_to_edge(data_dict):
    return edge_data_to_edge(data_dict)

def node_data_to_node(node_data_dict):
    node_dict = {}

    self_url = node_data_dict["self"]
    node_dict["node_id"] = self_url.rpartition("/")[2]

    # its properties 
    properties = node_data_dict["data"]
    node_dict["type"] = properties.pop("type")
    node_dict["properties"] = properties

    return node_dict

def edges_data_to_edges(edges_data_dict_list): 
    edges_dict = {}
    
    for e in edges_data_dict_list:
        temp_edge_dict = edge_data_to_edge(e)
        edge_id = temp_edge_dict["edge_id"]
        edges_dict[edge_id] = temp_edge_dict

    return edges_dict

def edge_data_to_edge(edge_data_dict):
    e_dict = {}

    edge_id = edge_data_dict["self"].rpartition("/")[2]
    e_dict["edge_id"] = edge_id
    e_dict["properties"] = edge_data_dict["data"]
    e_dict["from_node_id"] = edge_data_dict["start"].rpartition("/")[2]
    e_dict["to_node_id"] = edge_data_dict["end"].rpartition("/")[2]
    e_dict["type"] = edge_data_dict["type"]

    return e_dict
