""" Module: sqobject

...
"""

from exceptions import NotImplementedError

class SqObject(object):

    """ SqObject is a subclass of the __new__ python object.

    Provide access to the common attributes of all SqNode and SqEdge
    subclasses.

    Required:
    id   _id            SqObject id
    str  _type          SqObject type
    
    """

    _id = None
    _type = None

    def __init__(self, id, attributes_dict):
        """
        Construct a SqObject extending the __new__ python object and 
        set private members common to all subclasses.
        """
        self._id = id

        self._type = attributes_dict["type"]

    def id(self):
        """ Return a SqObject id. """
        return self._id

    def type(self):
        """ Return a SqObject type. """
        return self._type

    def assert_loaded(self, loaded_data):
        """ Return true if data is loaded, otherwise raise an error. """
        if loaded_data is None:
            raise SqObjectNotLoadedError("SqObject member not loaded")


class SqObjectNotLoadedError(Exception):

    """ SqObjectNotLoadedError is a subclass of Exception.

    Provide an exception to be raised when a member of a SqObject has 
    not yet been loaded from the data layer and an attempt has been 
    made to access it.

    """

    msg = None

    def __init__(self, msg):
        self.msg = msg

class SqNode(SqObject):

    """ SqNode is a subclass of SqObject.

    Provide access to the common attributes of a League, Team, Player,
    User, and Game, including fields and edges connecting to other 
    nodes.

    SqNode's only requirement is at least one set of SqEdges.

    Required:
    dict _edge_ids_dict     {edge_type: [SqNode_id]}

    """

    _edge_ids_dict = {}
    
    def __init__(self, id, attributes_dict):
        """ Construct a SqNode extending SqObject. """
        _edge_ids_dict = attributes_dict["edge_ids_dict"]
        super(SqNode, self).__init__(id, attributes_dict)

    def name(self):
        """ Return a SqNode name. """
        raise NotImplementedError("All SqObject subclasses must override")


class SqEdge(SqObject):

    """ SqEdge is a subclass of SqObject.

    Provide access to the common attributes of Win, Loss, Tie, Member,
    and other edges modeling relationships between SqNodes.

    Required:
    id   _node_id_1     SqNode id at one end of this SqEdge
    id   _node_id_2     SqNode id at the other end of this SqEdge
    bool _is_one_way    does this SqEdge point to both SqNodes?
    bool _is_unique     can more than one SqEdge exist between SqNodes?

    """

    _node_id_1 = None
    _node_id_2 = None
    #_is_one_way = None
    #_is_unique = None

    def __init__(self, id, attributes_dict):
        """ Construct a SqEdge extending SqObject. """
        super(SqEdge, self).__init__(id, attributes_dict)

        self._node_id_1 = attributes_dict["node_id_1"]
        self._node_id_2 = attributes_dict["node_id_2"]
        #self._is_one_way = attributes_dict["is_one_way"]
        #self._is_unique = attributes_dict["is_unique"]

