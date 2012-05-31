""" Module: sqfactory

A simple factory pattern implementation for churning out concrete 
instances of SqNode and SqEdge subclasses based on the types stored by 
GraphNodes and GraphEdges.

Provides:
    def construct_node_and_edges
    def construct_node
    def construct_edge
    def construct_edges

"""

from model.graph import GraphEdge, GraphNode
from constants import API_NODE_TYPE, API_EDGE_TYPE
# TODO: when SqEdge subclasses exist, don't import SqEdge
from sqobject import SqEdge
import game
import league
import player
import user


def construct_node_and_edges(graph_node, graph_edges):
    """ Construct a SqNode and SqEdges from a GraphNode and GraphEdges.

    Required:
    GraphNode   graph_node      GraphNode to convert based on type
    dict        graph_edges     GraphEdges to convert based on type

    Returns:
    SqNode                      concrete subclass instance with SqEdges

    """

    node = construct_node(graph_node)
    # FIXME: why arent we using graph_edges here? if graph_node already
    # contains a reference to graph_edges, which would be reasonable, then we
    # should fix this method signature and make sure it's not a problem for
    # any of the callers.
    edges = construct_edges(graph_node.edges())
    node.set_edges(edges)

    return node


def construct_node(graph_node):
    """ Instantiate a subclass of SqNode from a GraphNode.

    Required:
    GraphNode   graph_node      GraphNode to convert based on type

    Returns:
    SqNode                      single instance of concrete subclass

    """

    node = None

    if graph_node.type() == API_NODE_TYPE.LEAGUE:
        node = league.League(graph_node)

    elif graph_node.type() == API_NODE_TYPE.PLAYER:
        node = player.Player(graph_node)

    elif graph_node.type() == API_NODE_TYPE.GAME:
        node = game.Game(graph_node)
    
    elif graph_node.type() == API_NODE_TYPE.USER:
        node = user.User(graph_node)

    #elif graph_node.type() == API_NODE_TYPE.TEAM:
    #    node = Team(graph_node)
    #
    #elif graph_node.type() == API_NODE_TYPE.OPEN_PLAY:
    #    node = OpenPlay(graph_node)
    #
    #elif graph_node.type() == API_NODE_TYPE.SEASON:
    #    node = Season(graph_node)
    #
    #elif graph_node.type() == API_NODE_TYPE.TOURNAMENT:
    #    node = Tournament(graph_node)

    else:
    # TODO: raise an error...something went terribly wrong.
        pass

    return node


def construct_edge(graph_edge):
    """ Instantiate a subclass of SqEdge from a GraphEdge.

    Required:
    GraphEdge   graph_edge      GraphEdge to convert based on type

    Returns:
    SqEdge                      single instance of concrete subclass

    """

    #edge = None
    #
    #if graph_edge.type() == API_EDGE_TYPE.:
    #    edge = (graph_edge)
    #
    #else if graph_edge.type() == API_EDGE_TYPE.:
    #    edge = (graph_edge)
    #
    #else:
    #    # TODO: raise an error...something went terribly wrong.
    #
    #return edge
    return SqEdge(graph_edge)


def construct_edges(graph_edges):
    """ Instantiate subclasses of SqEdge from GraphEdges.

    Required:
    dict    graph_edges         GraphEdges to convert based on type

    Returns:
    dict                        concrete SqEdge subclass instances

    """

    edges = {}

    for id, graph_edge in graph_edges.items():
        type = graph_edge.type()

        if type not in edges:
            edges[type] = {}

        # TODO: decide whether returning None on any failure is better?
        edges[type][id] = construct_edge(graph_edge)
    
    return edges

