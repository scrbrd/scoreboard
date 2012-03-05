""" Module: sqfactory

A simple factory pattern implementation for churning out concrete 
instances of SqNode and SqEdge subclasses based on the types stored by 
GraphNodes and GraphEdges.

Provides:
    def SqFactory.construct_node
    def SqFactory.construct_edge
    def SqFactory.construct_edges

"""

from model.api import Game, League, Player
from model.graph import GraphEdge, GraphNode, GraphPath


class SqFactory(object):

    """ SqFactory is a subclass of the __new__ python object.

    Provide a module for  
    """

    def __init__(self):
        """ Dummy constructor cannot be instantiated. """
        raise NotImplementedError("SqFactory cannot be instantiated.")


    @staticmethod
    def construct_node_and_edges(graph_node):
        """ Instantiate a subclass of SqNode from a GraphNode. 
        
        Required:
        GraphNode   graph_node      GraphNode to convert based on type
        
        Returns:
        SqNode                      single instance of concrete subclass
        
        """

        node = SqFactory.construct_node(graph_node)
        node.set_edges(SqFactory.construct_edges(graph_node.get_edges()))

        return node


    @staticmethod
    def construct_node(graph_node)
        node = None

        if graph_node.type() is "LEAGUE":
            node = League(graph_node)

        else if graph_node.type() is "PLAYER":
            node = Player(graph_node)

        else if graph_node.type() is "GAME":
            node = Game(graph_node)

        #else if graph_node.type() is "TEAM":
        #    node = Team.init_from_graph_node(graph_node)
        #
        #else if graph_node.type() is "OPEN_PLAY":
        #    node = OpenPlay.init_from_graph_node(graph_node)
        #
        #else if graph_node.type() is "SEASON":
        #    node = Season.init_from_graph_node(graph_node)
        #
        #else if graph_node.type() is "TOURNAMENT":
        #    node = Tournament.init_from_graph_node(graph_node)
        #
        #else if graph_node.type() is "USER":
        #    node = User.init_from_graph_node(graph_node)

        else:
            # TODO: raise an error...something went terribly wrong.

        return node


    @staticmethod
    def construct_edge(graph_edge):
        """ Instantiate a subclass of SqEdge from a GraphEdge. 
        
        Required:
        GraphEdge   graph_edge      GraphEdge to convert based on type
        
        Returns:
        SqEdge                      single instance of concrete subclass
        
        """

        edge = None

        #if graph_edge.type() is "":
        #    edge = (graph_edge)
        #
        #else if graph_edge.type() is "":
        #    edge = (graph_edge)
        #
        #else if graph_edge.type() is "":
        #    edge = (graph_edge)
        #
        #else if graph_edge.type() is "":
        #    edge = (graph_edge)
        #
        #else if graph_edge.type() is "":
        #    edge = (graph_edge)
        #
        #else if graph_edge.type() is "":
        #    edge = (graph_edge)
        #
        #else:
        #    # TODO: raise an error...something went terribly wrong.
        #
        #return edge

        # TODO: stop returning a GraphEdge when subclasses are implemented
        return graph_edge


    @staticmethod
    def construct_edges(graph_edges):
        """ Instantiate subclasses of SqEdge from GraphEdges. 
        
        Required:
        dict    graph_edges         GraphEdges to convert based on type

        Returns:
        dict                        concrete SqEdge subclass instances

        """

        edges = {}

        for id, graph_edge in graph_edges:
            # TODO: better to return None on any failure?
            edges[id] = SqFactory.construct_edge(graph_edge)

        return edges

