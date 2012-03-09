""" Module: editor

Provide a Sqoreboard API for editing graph data in Sqoreboard objects.

Provides:
    def create_node_and_edges
    #def create_node
    #def create_edges
    #def create_edge

"""

from model.graph import reader, writer, GraphInputError, GraphOutputError
import sqfactory


def create_node_and_edges(type, properties, edges):
    """ Create a Node for this SqObject and create its edges.

    Required:
    str type            the type/class of the node
    dict properties     the properties of the node {PROP: VALUE}
    list edges          list of edge dicts

    edges list's dicts' keys: "from_id", "type", "properties"

    Return new SqNode if success and None if failure

    """

    node = None

    try:
        # create and store a new GraphNode
        new_node = _create_node(type, properties)

        # create and store new GraphEdges to/from the new GraphNode
        _create_edges(new_node.id(), edges)

        # read the new GraphNode with GraphEdges loaded
        graph_node = reader.get_node(new_node.id())

        # load the new GraphNode and GraphEdges into SqObjects
        node = sqfactory.construct_node_and_edges(graph_node)

    except GraphOutputError as e:
        #logger.debug(e.reason)
        print e.reason

    except GraphInputError as e:
        #logger.debug(e.reason)
        print e.reason

    return node


#def create_node(type, properties):
#def create_edge(type, properties):
#def create_edges(type, properties):


def _create_node(type, properties):
    """ Intramodule Convenience wrapper returning GraphNode. """
    return writer.create_node(type, properties)


def _create_edges(connecting_node_id, edges):
    """ Intramodule Convenience wrapper returning GraphEdges. """

    graph_edges = {}

    for edge in edges:
        graph_edge = _create_edge(connecting_node_id, edge)
        graph_edges[graph_edge.id()] = graph_edge

    return graph_edges


def _create_edge(connecting_node_id, edge):
    """ Intramodule Convenience wrapper returning GraphEdges. """

    from_node_id = edge.get("from_node_id", connecting_node_id)
    to_node_id = edge.get("to_node_id", connecting_node_id)

    is_one_way = True
    is_unique = False

    return writer.create_edge(
            from_node_id,
            to_node_id,
            edge["type"],
            is_one_way,
            is_unique,
            edge["properties"])

