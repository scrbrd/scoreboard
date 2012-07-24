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
# TODO: when SqEdge subclasses exist, uncomment this
# TODO: when SqEdge subclasses exist, don't import SqEdge
import sqobject

# Singleton SqFactory
factory = None


def get_factory():
    """ Get an instance of SqFactory. """
    return factory


class SqFactory(object):

    """ SqFactory constructs all the API Nodes. It's a Singleton.

    dict node_functions     all the API Node constructors are passed to
                            SqFactory so it doesn't have to import them.

    """
    node_functions = {}


    def __init__(self, nodes_functions_dict):
        """ Create the Singleton SqFactory. """
        self.node_functions = nodes_functions_dict
        global factory
        factory = self


    def construct_node_and_edges(self, graph_node):
        """ Construct a SqNode and SqEdges from a GraphNode and GraphEdges.

        Required:
        GraphNode   graph_node      GraphNode to convert based on type

        Returns:
        SqNode                      concrete subclass instance with SqEdges

        """

        node = self.construct_node(graph_node)
        edges = self.construct_edges(graph_node.edges())
        node.set_edges(edges)

        return node


    def construct_node(self, graph_node):
        """ Instantiate a subclass of SqNode from a GraphNode.

        Required:
        GraphNode   graph_node      GraphNode to convert based on type

        Returns:
        SqNode                      single instance of concrete subclass

        """
        node = None
        init_function = self.node_functions[graph_node.type()]
        node = init_function(graph_node)

        return node


    def construct_edge(self, graph_edge):
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
        return sqobject.SqEdge(graph_edge)


    def construct_edges(self, graph_edges):
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
            edges[type][id] = self.construct_edge(graph_edge)

        return edges
