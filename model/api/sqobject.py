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
from copy import deepcopy

from model.graph import GraphEdge, GraphNode
from constants import API_CONSTANT, NODE_TYPE, EDGE_TYPE

class SqObject(object):

    """ SqObject is a subclass of the __new__ python object.

    Provide access to the common attributes of all SqNode and SqEdge
    subclasses.

    Required:
    id      _id             SqObject id
    str     _type           SqObject type
    
    """

   
    _id = None
    _type = None

    def __init__(self, graph_node):
        """ Construct a SqObject extending the __new__ python object. """
        self._id = graph_node.id()
        self._type = graph_node.type()

        # TODO: move as much error checking from reader/writer into here as
        # possible to avoid repetitive code and to grant class hierarchy
        # appropriate knowledge and power over itself.


    @property
    def id(self):
        """ Return a SqObject id. """
        return self._id


    @property
    def type(self):
        """ Return a SqObject type. """
        return self._type


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


    def __init__(self, graph_node):
        """ Construct a SqNode extending SqObject. """
        super(SqNode, self).__init__(graph_node)

        # TODO: should edges be set here instead of SqFactory?

        # TODO: move as much error checking from reader/writer into here as
        # possible to avoid repetitive code and to grant class hierarchy
        # appropriate knowledge and power over itself.


    @property
    def name(self):
        """ Return a SqNode name. """
        raise NotImplementedError("All SqObject subclasses must override")


    def outgoing_edge_types(self):
        """ Return a list of allowed outgoing SqEdge types. """
        raise NotImplementedError("Abstract Method: SUBCLASS MUST OVERRIDE!")


    def incoming_edge_types(self):
        """ Return a list of allowed incoming SqEdge types. """
        
        edge_types = []

        for edge_type in self.outgoing_edge_types():
            edge_types.append(API_CONSTANT.EDGE_TYPE_COMPLEMENTS[edge_type])

        return edge_types


    def get_edges(self):
        """ Return a dict of outgoing SqEdges. """

        edges = self._edges

        try:
            self.assert_loaded(edges)

        except SqObjectNotLoadedError as e:
            print e.reason
            edges = {}
        
        return edges


    def set_edges(self, edges):
        """ Set a member variable with a dict of outgoing SqEdges. """
        self._edges = edges

    
    @staticmethod
    def assert_loaded(loaded_data):
        """ If data is not loaded, raise an error. """
        if loaded_data is None:
            raise SqObjectNotLoadedError("SqObject member not loaded")


class SqEdge(SqObject):

    """ SqEdge is a subclass of SqObject.

    Provide access to the common attributes of Win, Loss, Tie, Member,
    and other edges modeling relationships between SqNodes.

    Required:
    id      _from_node_id   SqNode id for which this SqEdge is outgoing
    id      _to_node_id     SqNode id for which this SqEdge is incoming
    dict    _properties     all edge properties (temporary)

    """

    _from_node_id = None
    _to_node_id = None
    #_is_one_way = None
    #_is_unique = None

    # FIXME remove this variable when SqEdges are fully implemented
    _properties = {}
    

    def __init__(self, graph_edge):
        """ Construct a SqEdge extending SqObject. """
        super(SqEdge, self).__init__(graph_edge)

        self._from_node_id = graph_edge.from_node_id()
        self._to_node_id = graph_edge.to_node_id()
        #self._is_one_way = graph_edge.is_one_way()
        #self._is_unique = graph_edge.is_unique()
    
        # FIXME remove whenSqEdges are fully implemented
        self._properties = deepcopy(graph_edge.properties())
        
        # TODO: move as much error checking from reader/writer into here as
        # possible to avoid repetitive code and to grant class hierarchy
        # appropriate knowledge and power over itself.


    @property
    def from_node_id(self):
        """ Return the SqNode id for which this SqEdge is outgoing. """
        return self._from_node_id


    @property
    def to_node_id(self):
        """ Return the SqNode id for which this SqEdge is incoming. """
        return self._to_node_id


    # FIXME remove when SqEdges are implemented
    def properties(self):
        """ Return dictionary of SqObject properties. """
        return self._properties


    def get_property(self, key):
        """ Return value of requested SqObject property. """
        return self._properties.get(key, None)


class SqObjectNotLoadedError(Exception):

    """ SqObjectNotLoadedError is a subclass of Exception.

    Provide an exception to be raised when a member of a SqObject has 
    not yet been loaded from the data layer and an attempt has been 
    made to access it.

    """

    reason = None

    def __init__(self, reason):
        self.reason = reason
