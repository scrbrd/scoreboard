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
from model.constants import NODE_PROPERTY, EDGE_PROPERTY

from constants import API_NODE_TYPE, API_EDGE_TYPE
from constants import API_NODE_PROPERTY, API_EDGE_PROPERTY
from constants import API_CONSTANT


class SqObject(object):

    """ SqObject is a subclass of the __new__ python object.

    Provide access to the common attributes of all SqNode and SqEdge
    subclasses.

    Required:
    id      _id             SqObject id
    str     _type           SqObject type
    dict    _properties     SqObject properties from GraphObject 

    """

    _id = None
    _type = None
    _properties = None


    def __init__(self, graph_object):
        """ Construct a SqObject extending the __new__ python object. """
        self._id = graph_object.id()
        self._type = graph_object.type()

        # intentionally not exposed as a property or even as a method since
        # most of the helpers defined by subclasses are access wrappers.
        self._properties = graph_object.properties()

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


    def _get_property(self, key):
        """ Return SqObject property denoted by key. """
        raise NotImplementedError("Abstract Method: SUBCLASS MUST OVERRIDE!")


class SqNode(SqObject):

    """ SqNode is a subclass of SqObject.

    Provide access to the common attributes of a League, Team, Player,
    User, and Game, including fields and edges connecting to other 
    nodes.

    SqNode's only requirement is at least one set of SqEdges.

    Optional:
    dict    edges       this SqNode's outgoing SqEdges keyed on id

    """

    _edges = None


    def __init__(self, graph_object):
        """ Construct a SqNode extending SqObject. """
        super(SqNode, self).__init__(graph_object)

        # TODO: should edges be set here instead of SqFactory?

        # TODO: move as much error checking from reader/writer into here as
        # possible to avoid repetitive code and to grant class hierarchy
        # appropriate knowledge and power over itself.

        # TODO: if neither of the above is necessary remove this empty override


    @property
    def name(self):
        """ Return a SqNode name. """
        raise NotImplementedError("Abstract Method: SUBCLASS MUST OVERRIDE!")


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


    def _get_property(self, key):
        """ Return a GraphObject property as a member.

        If we have data stored for this property key, use it. Otherwise,
        default [for now] to what we get from Facebook. In the future,
        what we default to will depend on some input parameter [likely a
        cookie] describing how this user is logged in.

        """

        property = self._properties.get(
                key,
                self._properties.get(
                    API_CONSTANT.FACEBOOK_NODE_PROPERTIES[key],
                    None))

        if property is None:
            raise SqObjectPropertyError(
                    key,
                    "SqObject property doesn't exist.")

        return property


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
    

    def __init__(self, graph_object):
        """ Construct a SqEdge extending SqObject. """
        super(SqEdge, self).__init__(graph_object)

        self._from_node_id = graph_object.from_node_id()
        self._to_node_id = graph_object.to_node_id()
        #self._is_one_way = graph_object.is_one_way()
        #self._is_unique = graph_object.is_unique()
    
        # FIXME remove whenSqEdges are fully implemented
        self._properties = deepcopy(graph_object.properties())
        
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


    def _get_property(self, key):
        """ Return SqEdge property denoted by key. """
        return self._properties.get(key, None)


class SqObjectPropertyError(Exception):

    """ SqObjectPropertyError is a subclass of Exception.

    Provide an exception to be raised when an attempt is made to access
    a SqObject property which does not exist. Usually this means that
    we failed to retrieve the property from our own database and from
    third party APIs like Facebook as well.

    """

    reason = None


    def __init__(self, parameter, description):
        """ Construct a SqObjectPropertyError extending Exception. """
        self.reason = "SqObjectPropertyError: {0} : {1}".format(
                parameter, 
                description)


class SqObjectNotLoadedError(Exception):

    """ SqObjectNotLoadedError is a subclass of Exception.

    Provide an exception to be raised when a member of a SqObject has 
    not yet been loaded from the data layer and an attempt has been 
    made to access it.

    """

    reason = None


    def __init__(self, reason):
        self.reason = reason

