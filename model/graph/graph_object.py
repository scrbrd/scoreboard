""" Module: graph_object

GraphObject
    |   |
    |   +-- GraphNode
    |
    +------ GraphEdge

GraphPath

GraphPrototype
    |   |
    |   +-- GraphProtoNode
    |
    +------ GraphProtoEdge

GraphError
    |   |
    |   +-- GraphInputError
    |
    +------ GraphOutputError

"""


class GraphObject(object):
    
    """ GraphObject is a subclass of the __new__ python object.

    Provide access to the common attributes of the GraphNode and 
    GraphEdge subclasses.

    Required:
    id      _id             GraphObject id
    str     _type           GraphObject type
    ts      _created_ts     when was this GraphObject created
    ts      _updated_ts     when was this GraphObject last updated
    ts      _deleted_ts     when, if ever, was this GraphObject deleted
    dict    _properties     GraphObject properties

    """

    _id = None
    _type = None
    _created_ts = None
    _updated_ts = None
    _deleted_ts = None
    _properties = None


    def __init__(self, id, type, properties):
        """ Construct an abstract GraphObject. """
        self._id = id
        self._type = type

        # FIXME: deal with existing bad data in the database. every node 
        # and edge should have a value set for each of these properties.

        self._created_ts = properties.pop("created_ts", False)
        self._created_ts = properties.pop("updated_ts", False)
        self._created_ts = properties.pop("deleted_ts", False)

        self._properties = properties

        # TODO: move as much error checking from reader/writer into here as
        # possible to avoid repetitive code and to grant class hierarchy
        # appropriate knowledge and power over itself.


    def id(self):
        """ Return a GraphObject's id. """
        return self._id


    def type(self):
        """ Return a GraphObject's type. """
        return self._type


    def created_ts(self):
        """ Return a GraphObject's created timestamp. """
        return self._created_ts


    def updated_ts(self):
        """ Return a GraphObject's last updated timestamp. """
        return self._updated_ts


    def deleted_ts(self):
        """ Return a GraphObject's deleted timestamp (or False). """
        return self._deleted_ts


    def properties(self):
        """ Return a GraphObject's properties dict. """
        return self._properties


class GraphNode(GraphObject):

    """ GraphNode is a subclass of GraphObject.

    Provide access to the attributes of a GraphNode not shared with 
    GraphEdge via the superclass GraphObject.

    Required:
    dict    _edges      dict of GraphEdges keyed on id

    """

    _edges = None


    def __init__(self, id, type, properties, edges):
        """ Construct a GraphNode extending GraphObject. """
        super(GraphNode, self).__init__(id, type, properties)

        self._edges = {}

        for edge_id, edge in edges.items():
            self._edges[edge_id] = GraphEdge(
                    edge["edge_id"],
                    edge["type"],
                    edge["properties"],
                    edge["from_node_id"],
                    edge["to_node_id"])


    def edges(self):
        """ Return a GraphNode's dict of GraphEdges. """
        return self._edges


    def set_edges(self, edges):
        """ Set a GraphNode's dict of GraphEdges. """
        self._edges = edges


class GraphEdge(GraphObject):

    """ GraphEdge is a subclass of GraphObject.

    Provide access to the attributes of a GraphEdge not shared with 
    GraphNode via the superclass GraphObject.

    Required:
    id   _from_node_id  GraphNode id at one end of this GraphEdge
    id   _to_node_id    GraphNode id at the other end of this GraphEdge

    """

    _from_node_id = None
    _to_node_id = None
    #_is_one_way = None
    #_is_unique = None


    def __init__(self, id, from_node_id, to_node_id, type, properties):
        """ Construct a GraphEdge extending GraphObject. """
        super(GraphEdge, self).__init__(id, type, properties)

        self._from_node_id = from_node_id
        self._to_node_id = to_node_id

        #self._is_one_way = self._properties.pop("is_one_way", False)
        #self._is_unique = self._properties.pop("is_unique", False)

        # TODO: move as much error checking from reader/writer into here as
        # possible to avoid repetitive code and to grant class hierarchy
        # appropriate knowledge and power over itself.


    def from_node_id(self):
        """ Return the id of the GraphNode a GraphEdge points from. """
        return self._from_node_id


    def to_node_id(self):
        """ Return the id of the GraphNode a GraphEdge points to. """
        return self._to_node_id


    #def is_one_way(self):
    #    """ Return if this GraphEdge points to both its GraphNodes. """
    #    return self._is_one_way
    #
    #
    #def is_unique(self):
    #    """ Return if GraphNodes have at most one of this GraphEdge. """
    #    return self._is_unique


class GraphPath(object):

    """ GraphPath is a subclass of GraphObject.

    Provide access to the attributes of a GraphPath not shared with 
    GraphObjects via the superclass GraphObject.

    Required:
    int     _depth                      degrees separating start and end
    dict    _path                       GraphNodes keyed on depth and id

    Optional:
    list    _edge_type_pruner           GraphEdge types pruned on path
    list    _node_type_return_filter    GraphNode types returned in path

    """

    _depth = None
    _path = None
    _edge_type_pruner = None
    _node_type_return_filter = None


    def __init__(self, id, path, properties):
        """ Construct a GraphNode extending GraphObject. """
        super(GraphPath, self).__init__(id, properties)

        # TODO: determine whether these are necessary members.

        # make traversal pruner a member
        self._edge_type_pruner = self._properties.pop(
                "edge_type_pruner",
                [])

        # make return filter a member
        self._node_type_return_filter = self._properties.pop(
                "node_type_return_filter",
                [])

        # infer depth member from path dict
        self._depth = (len(path) - 1)

        # TODO: determine whether to keep path or just rely on convenience
        # methods, since they are more explicit and easier to read.

        self._path = {}

        # load nodes and edges at each depth
        for depth in range(self._depth + 1):
            self._path[depth] = {}

            for node_id, node_dict in path[depth].items():
                self._path[depth][node_id] = GraphNode(
                        node_dict["node_id"],
                        node_dict["type"],
                        node_dict["properties"],
                        node_dict["edges"])


    def edge_type_pruner(self):
        """ Return GraphEdge types pruned when traversing. """
        return self._edge_type_pruner


    def node_type_return_filter(self):
        """ Return GraphNode types filtered when returning the path. """
        return self._node_type_return_filter


    def depth(self):
        """ Return an int for this GraphPath's traversal depth. """
        return self._depth


    def path(self):
        """ Return a dict describing a path from start node. """
        return self._path


    def get_nodes_at_depth(self, depth):
        """ Return the dict of GraphNodes at a specific depth. """
        return self.path()[depth]


    def count_nodes_at_depth(self, depth):
        """ Return the number of GraphNodes at a specific depth. """
        return len(self.path()[depth])


    def start_node_id(self):
        """ Alias for self.id(). """
        return self.id()


    def get_start_node(self):
        """ Convenience method wrapping self.get_nodes_at_depth(). """
        return self.get_nodes_at_depth(0)[self.start_node_id()]


    def get_neighbor_nodes(self):
        """ Convenience method to get start node's neighbors. """
        return self.get_nodes_at_depth(1)


    def count_neighbor_nodes(self):
        """ Convenience method to count start node's neighbors. """
        return self.count_nodes_at_depth(1)


class GraphPrototype(object):

    """ GraphPrototype is a subclass of the __new__ python object.

    Provide an abstract superclass representing a model for a 
    GraphObject before it has been written out to a database. The 
    main difference between them is that a GraphPrototype has no id.

    Required:
    str     _type           see GraphObject type
    dict    _properties     see GraphObject properties

    """

    _type = None
    _properties = None


    def __init__(self, type, properties):
        """ Construct an abstract GraphPrototype. """
        self._type = type
        self._properties = properties

        # TODO: raise GraphInputError on failure to provide required field
        # TODO: raise GraphInputError when disallowed fields are provided


    def type(self):
        """ Return a GraphPrototype's type. """
        return self._type


    def properties(self):
        """ Return a GraphPrototype's properties dict. """
        return self._properties


class GraphProtoNode(GraphPrototype):
    
    """ GraphProtoNode is a subclass of GraphPrototype.

    Provide access to the attributes of GraphProtoNode not shared with 
    GraphProtoEdge via the superclass GraphPrototype. There is no edges 
    requirement because GraphPrototypes are only intended to be useful 
    before data is written, and nodes have no associated edges until 
    after they have been stored.

    """


    def __init__(self, type, properties, edges=[]):
        """ Construct a GraphProtoNode extending GraphPrototype. """
        super(GraphProtoNode, self).__init__(type, properties)

        # TODO: raise GraphInputError on failure to provide required field
        # TODO: raise GraphInputError when disallowed fields are provided


class GraphProtoEdge(GraphPrototype):

    """ GraphProtoEdge is a subclass of GraphPrototype.

    Provide access to the attributes of GraphProtoEdge not shared with 
    GraphProtoNode via the superclass GraphPrototype.

    Required:
    id   _from_node_id  see GraphEdge from_node_id
    id   _to_node_id    see GraphEdge to_node_id

    """

    _from_node_id = None
    _to_node_id = None


    def __init__(self, type, properties, from_node_id, to_node_id):
        """ Construct a GraphProtoEdge extending GraphPrototype. """
        super(GraphProtoEdge, self).__init__(type, properties)

        self._from_node_id = from_node_id
        self._to_node_id = to_node_id

        # TODO: raise GraphInputError on failure to provide required field
        # TODO: raise GraphInputError when disallowed fields are provided

    
    def from_node_id(self):
        """ Return the GraphProtoNode id a GraphProtoEdge points from. """
        return self._from_node_id


    def to_node_id(self):
        """ Return the GraphProtoNode id a GraphProtoEdge points to. """
        return self._to_node_id


    def set_node_id(self, node_id):
        """ Set the from and/or to node id in a GraphProtoEdge. """

        # during node creation, one of these [rarely both] will not yet be set
        if self._from_node_id is None:
            self._from_node_id = node_id

        # don't use elif, since it's valid to point a node at itself
        if self._to_node_id is None:
            self._to_node_id = node_id


class GraphError(Exception):
    """ GraphError is a subclass of Exception.

    Provide an exception superclass from which all graph-related
    errors should inherit.

    Required:
    str     reason      what went wrong?
    
    """

    reason = None


    def __init__(self, error, parameters, description):
        """ Construct a generic but not quite abstract GraphError. """
        self.reason = "{0}: [{1}] : {2}".format(
                error,
                ", ".join(parameters),
                description)


class GraphInputError(GraphError):

    """ GraphInputError is a subclass of Exception.

    Provide an exception to be raised when an input parameter supplied 
    to this graph API is invalid.

    """

    def __init__(self, parameters, description):
        """ Construct a GraphInputError extending GraphError. """
        super(GraphInputError, self).__init__(
                "GraphInputError",
                parameters,
                description)


class GraphOutputError(GraphError):

    """ GraphOutputError is a subclass of Exception.

    Provide an exception to be raised when output from the data layer 
    supplied to this graph API is invalid.

    """

    def __init__(self, parameters, description):
        """ Construct a GraphOutputError extending GraphError. """
        super(GraphInputError, self).__init__(
                "GraphOutputError",
                parameters,
                description)

