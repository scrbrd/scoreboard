""" Module: sqobject

SqObject
  |   |
  |   +-- SqNode
  |
  +------ SqEdge

Exception
    |
    +-- SqObjectNotLoadedError

"""

from exceptions import NotImplementedError

from model.graph import GraphEdge, GraphNode
from sqfactory import SqFactory


class SqObject(object):

    """ SqObject is a subclass of the __new__ python object.

    Provide access to the common attributes of all SqNode and SqEdge
    subclasses.

    Required:
    id      _id     SqObject id
    str     _type   SqObject type

    """

    _id = None
    _type = None


    def __init__(self, graph_node):
        """ Construct a SqObject extending the __new__ python object. """
        self._id = graph_node.id()
        self._type = graph_node.type()

        # TODO: decide whether to unset properties copied into members
        self._properties = graph_node.properties()


    def id(self):
        """ Return a SqObject id. """
        return self._id


    def type(self):
        """ Return a SqObject type. """
        return self._type


    def assert_loaded(self, loaded_data):
        """ If data is not loaded, raise an error. """
        if loaded_data is None:
            raise SqObjectNotLoadedError("SqObject member not loaded")


class SqNode(SqObject):

    """ SqNode is a subclass of SqObject.

    Provide access to the common attributes of a League, Team, Player,
    User, and Game, including fields and edges connecting to other 
    nodes.

    SqNode's only requirement is at least one set of SqEdges.

    Optional:
    dict    edges       this SqNode's outgoing SqEdges keyed on id
    dict    neighbors   neighbor SqNodes keyed on id

    """

    _edges = None
    _neighbors = None


    def __init__(self, graph_node):
        """ Construct a SqNode extending SqObject. """
        super(SqNode, self).__init__(graph_node)


    def name(self):
        """ Return a SqNode name. """
        raise NotImplementedError("All SqObject subclasses must override")


    def incoming_edge_types(self):
        """ Return a list of allowed incoming SqEdge types. """
        # TODO: list of edge types, or dict of edge type/node type pairs?
        raise NotImplementedError("Abstract Method: SUBCLASS MUST OVERRIDE!")


    def outgoing_edge_types(self):
        """ Return a list of allowed outgoing SqEdge types. """
        # TODO: list of edge types, or dict of edge type/node type pairs?
        raise NotImplementedError("Abstract Method: SUBCLASS MUST OVERRIDE!")


    def get_edges(self):
        """ Return a dict of outgoing SqEdges. """

        edges = self._edges

        try:
            self.assert_loaded(edges)

        except SqObjectNotLoadedError as e:
            #logger.debug(e.reason)
            print e.reason
            edges = {}

        return edges


    def set_edges(self, edges):
        """ Set a member variable with a dict of outgoing SqEdges. """
        self._neighbors = neighbors


    def get_neighbors(self):
        """ Return a dict of neighbor SqNodes. """

        neighbors = self._neighbors

        try:
            self.assert_loaded(neighbors)

        except SqObjectNotLoadedError as e:
            #logger.debug(e.reason)
            print e.reason
            neighbors = {}

        return neighbors


    def set_neighbors(self, neighbors):
        """ Set a member variable with a dict of neighbor SqNodes. """
        self._neighbors = neighbors


class SqEdge(SqObject):

    """ SqEdge is a subclass of SqObject.

    Provide access to the common attributes of Win, Loss, Tie, Member,
    and other edges modeling relationships between SqNodes.

    Required:
    id      _from_node_id   SqNode id for which this SqEdge is outgoing
    id      _to_node_id     SqNode id for which this SqEdge is incoming
    bool    _is_one_way     does this SqEdge point to both SqNodes?
    bool    _is_unique      can only one of an SqEdge exist for SqNodes?

    """

    _node_id_1 = None
    _node_id_2 = None
    #_is_one_way = None
    #_is_unique = None


    def __init__(self, graph_edge):
        """ Construct a SqEdge extending SqObject. """
        super(SqEdge, self).__init__(graph_edge)

        self._from_node_id = graph_edge.from_node_id()
        self._to_node_id = graph_edge.to_node_id()
        #self._is_one_way = graph_edge.is_one_way()
        #self._is_unique = graph_edge.is_unique()


class SqObjectNotLoadedError(Exception):

    """ SqObjectNotLoadedError is a subclass of Exception.

    Provide an exception to be raised when a member of a SqObject has 
    not yet been loaded from the data layer and an attempt has been 
    made to access it.

    """

    reason = None

    def __init__(self, reason):
        self.reason = reason
