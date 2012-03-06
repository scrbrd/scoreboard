""" Module: sqfactory

A simple factory pattern implementation for churning out concrete 
instances of SqNode and SqEdge subclasses based on the types stored by 
GraphNodes and GraphEdges.

Provides:
    def SqFactory.construct_node
    def SqFactory.construct_edge
    def SqFactory.construct_edges

"""

from model.const import NODE_TYPE, EDGE_TYPE
from model.graph import GraphEdge, GraphNode
# TODO - do we need to import SqNode?
from sqobject import SqNode, SqEdge
import game
import league
import player

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
    def construct_node(graph_node):
        node = None

        if graph_node.type() is NODE_TYPE.LEAGUE:
            node = league.League(graph_node)

        elif graph_node.type() is NODE_TYPE.PLAYER:
            node = player.Player(graph_node)

        elif graph_node.type() is NODE_TYPE.GAME:
            node = game.Game(graph_node)

        #else if graph_node.type() is NODE_TYPE.TEAM:
        #    node = Team(graph_node)
        #
        #else if graph_node.type() is "OPEN_PLAY":
        #    node = OpenPlay(graph_node)
        #
        #else if graph_node.type() is "SEASON":
        #    node = Season(graph_node)
        #
        #else if graph_node.type() is "TOURNAMENT":
        #    node = Tournament(graph_node)
        #
        #else if graph_node.type() is "USER":
        #    node = User.init_from_graph_node(graph_node)

        else:
            # TODO: raise an error...something went terribly wrong.
            pass

        return node


    @staticmethod
    def construct_edge(graph_edge):
        """ Instantiate a subclass of SqEdge from a GraphEdge. 
        
        Required:
        GraphEdge   graph_edge      GraphEdge to convert based on type
        
        Returns:
        SqEdge                      single instance of concrete subclass
        
        """

        #edge = None
        #
        #if graph_edge.type() is EDGE_TYPE.:
        #    edge = (graph_edge)
        #
        #else if graph_edge.type() is EDGE_TYPE.:
        #    edge = (graph_edge)
        #
        #else:
        #    # TODO: raise an error...something went terribly wrong.
        #
        #return edge

        return SqEdge(graph_edge)


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
            type = graph_edge.type()

            if type not in edges:
                edges[type] = {}

            # TODO: decide whether returning None on any failure is better?
            edges[type][id] = SqFactory.construct_edge(graph_edge)

        return edges

