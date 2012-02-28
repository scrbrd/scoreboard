""" Module: graph_object

GraphObject
    |   |
    |   +-- GraphPath
    |
    +------ GraphPrimitive
                |   |
                |   +-- GraphEdge
                |
                +------ GraphNode

Exception
    |   |
    |   +-- GraphInputError
    |
    +------ GraphOutputError

"""


class GraphObject(object):
    
    """ GraphObject is a subclass of the __new__ python object.

    Provide access to the most basic common attributes of all
    GraphPrimitive and GraphPath subclasses.

    Required:
    id      _id             GraphObject id
    dict    _properties     GraphObject properties

    """

    _id = None
    _properties = None

    def __init__(self, id, properties):
        """ Construct an abstract GraphObject. """

        # TODO: remove int() when data layer returns the right type!

        self._id = int(id)
        self._properties = properties

    def id(self):
        """ Return a GraphObject id. """
        return self._id

    def properties(self):
        """ Return a GraphObject's properties dict. """
        return self._properties


class GraphPrimitive(GraphObject):

    """ GraphPrimitive is a subclass of GraphObject. 

    Provide access to the common attributes of all GraphNode and 
    GraphEdge subclasses.

    Required:
    str     _type           GraphObject type
    ts      _created_ts     when was this GraphObject created
    ts      _updated_ts     when was this GraphObject last updated
    ts      _deleted_ts     when, if ever, was this GraphObject deleted

    """

    _type = None
    _created_ts = None
    _updated_ts = None
    _deleted_ts = None

    def __init__(self, id, type, properties):
        """ Construct a GraphPrimitive extending GraphObject. """
        super(GraphPrimitive, self).__init__(id, properties)

        self._type = type

        # TODO: move as much error checking from reader/writer into here as
        # possible to avoid repetitive code and to grant class hierarchy
        # appropriate knowledge and power over itself.

        # TODO: deal with existing bad data. every node and edge should have a
        # value set for each of these properties.

        # TODO: remove int() when data layer returns the right type!

        if "created_ts" in self._properties:
            self._created_ts = int(self._properties.pop("created_ts"))
        else:
            self._created_ts = 0

        if "updated_ts" in self._properties:
            self._updated_ts = int(self._properties.pop("updated_ts"))
        else:
            self._updated_ts = 0

        if "deleted_ts" in self._properties:
            self._deleted_ts = int(self._properties.pop("deleted_ts"))
        else:
            self._deleted_ts = None

    def type(self):
        """ Return a GraphObject type. """
        return self._type

    def created_ts(self):
        """ Return a GraphObject's created timestamp. """
        return self._created_ts

    def updated_ts(self):
        """ Return a GraphObject's last updated timestamp. """
        return self._updated_ts

    def deleted_ts(self):
        """ Return a GraphObject's deleted timestamp (or None). """
        return self._deleted_ts


class GraphNode(GraphPrimitive):

    """ GraphNode is a subclass of GraphPrimitive.

    Provide access to the attributes of a GraphNode not shared with 
    GraphEdge via the superclass GraphPrimitive.

    Required:
    dict    _edges      dict of GraphEdges keyed on edge id

    """

    _edges = None

    def __init__(self, id, type, properties, edges):
        """ Construct a GraphNode extending GraphPrimitive. """
        super(GraphNode, self).__init__(id, type, properties)

        self._edges = {}
        for edge_id, edge in edges.items():

            # TODO: remove int() when data layer returns the right type!

            self._edges[int(edge_id)] = GraphEdge(
                    edge["edge_id"],
                    edge["type"],
                    edge["properties"],
                    edge["from_node_id"],
                    edge["to_node_id"])

    def edges(self):
        """ Return a GraphNode's dict of GraphEdges. """
        return self._edges


class GraphEdge(GraphPrimitive):

    """ GraphEdge is a subclass of GraphPrimitive.

    Provide access to the attributes of a GraphEdge not shared with 
    GraphNode via the superclass GraphPrimitive.

    Required:
    id   _from_node_id  GraphNode id at one end of this GraphEdge
    id   _to_node_id    GraphNode id at the other end of this GraphEdge
    bool _is_one_way    does this GraphEdge point to both GraphNodes?
    bool _is_unique     can GraphNodes have >1 GraphEdges of this type?

    """

    _from_node_id = None
    _to_node_id = None
    _is_one_way = None
    _is_unique = None

    def __init__(self, id, type, properties, from_node_id, to_node_id):
        """ Construct a GraphEdge extending GraphPrimitive. """
        super(GraphEdge, self).__init__(id, type, properties)

        # TODO: remove int() when data layer returns the right type!

        self._from_node_id = int(from_node_id)
        self._to_node_id = int(to_node_id)

        # TODO: move as much error checking from reader/writer into here as
        # possible to avoid repetitive code and to grant class hierarchy
        # appropriate knowledge and power over itself.

        # TODO: deal with existing bad data. every node and edge should have a
        # value set for each of these properties.

        # TODO: remove bool() when data layer returns the right type!

        if "is_one_way" in self._properties:
            self._is_one_way = bool(self._properties.pop("is_one_way"))
        else:
            self._is_one_way = False

        if "is_unique" in self._properties:
            self._is_unique = bool(self._properties.pop("is_unique"))
        else:
            self._is_unique = False

    def from_node_id(self):
        """ Return the id of the GraphNode a GraphEdge points from. """
        return self._from_node_id

    def to_node_id(self):
        """ Return the id of the GraphNode a GraphEdge points to. """
        return self._to_node_id

    def is_one_way(self):
        """ Return if this GraphEdge points to both its GraphNodes. """
        return self._is_one_way

    def is_unique(self):
        """ Return if GraphNodes have at most one of this GraphEdge. """
        return self._is_unique


class GraphPath(GraphObject):

    """ GraphPath is a subclass of GraphObject.

    Provide access to the attributes of a GraphPath not shared with 
    GraphPrimitives via the superclass GraphObject.

    Required:
    dict    _path                       GraphNodes keyed on depth and id

    Optional:
    list    _edge_type_pruner           GraphEdge types pruned on path
    list    _node_type_return_filter    GraphNode types returned in path

    """

    _path = None
    _depth = None
    _edge_type_pruner = None
    _node_type_return_filter = None

    def __init__(self, id, path, properties):
        """ Construct a GraphNode extending GraphObject. """
        super(GraphPath, self).__init__(id, properties)

        # TODO: determine whether these are necessary members.

        # make traversal pruner a member
        key = "edge_type_pruner"
        if key in properties:
            self._edge_type_pruner = self._properties.pop(key)
        else:
            self._edge_type_pruner = []

        # make return filter a member
        key = "node_type_return_filter"
        if key in properties:
            self._node_type_return_filter = self._properties.pop(key)
        else:
            self._node_type_return_filter = []

       # infer depth member from path dict
        self._depth = len(path)

        # load nodes and edges at each depth level
        self._path = {}
        for level in range(0, self._depth):
            self._path[level] = {}
            for node_id, node_dict in path[level].items():

                # TODO: remove int() when data layer returns the right type!

                self._path[level][int(node_id)] = GraphNode(
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


class GraphInputError(Exception):

    """ GraphInputError is a subclass of Exception.

    Provide an exception to be raised when an input parameter supplied 
    to this graph API is invalid.

    Required:
    str     parameter   parameter which has bad data
    mixed   value       value of the bad parameter
    str     message     why is this data bad?

    """

    reason = None

    def __init__(self, parameter, value, message):
        """ Construct a GraphInputError extending Exception. """
        self.reason = "GraphInputError: [{0}] = [{1}] : {2}".format(
                parameter,
                value,
                message)


class GraphOutputError(Exception):

    """ GraphOutputError is a subclass of Exception.

    Provide an exception to be raised when output from the Data layer 
    supplied to this graph API is invalid.

    Required:
    iter    parameter   parameters which have bad data
    str     message     why is this data bad?

    """

    reason = None

    def __init__(self, parameters, message):
        """ Construct a GraphInputError extending Exception. """
        self.reason = "GraphOutputError: [{0}] : {1}".format(
                parameters,
                message)

