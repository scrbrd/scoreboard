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

    Required:
    dict _node_functions     all the API Node constructors are passed to
                            SqFactory so it doesn't have to import them.
    dict _edge_functions     all the API Edge constructors are passed to
                            SqFactory so it doesn't have to import them.

    """


    def __init__(self, node_functions_dict, edge_functions_dict):
        """ Create the Singleton SqFactory. """
        self._node_functions = node_functions_dict
        self._edge_functions = edge_functions_dict

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
        init_function = self._node_functions[graph_node.type()]
        return init_function(graph_node)


    def construct_edge(self, graph_edge):
        """ Instantiate a subclass of SqEdge from a GraphEdge.

        Required:
        GraphEdge   graph_edge      GraphEdge to convert based on type

        Returns:
        SqEdge                      single instance of concrete subclass

        """
        init_function = self._edge_functions.get(
                graph_edge.type(),
                sqobject.SqEdge)  # remove when all SqEdges are subclasses
        return init_function(graph_edge)


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
