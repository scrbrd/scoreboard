""" Module: db

Provide access to a generic Sqoreboard database so that the graph
layer doesn't have to worry about implementation details.

"""
from model.constants import NODE_PROPERTY, EDGE_PROPERTY

from constants import PROTOCOL
from data_errors import DbInputError, DbReadError, DbWriteError
from data_errors import DbConnectionError


class SqDatabase(object):

    """ Provide access to a generic Sqoreboard database.

    Provide settings for configuring a database and also provide
    and interface for subclasses to implement. This database is
    abstract and should not be instantiated directly.

    Required:
    str     _host       the host of the database
    str     _port       the port of the database

    Optional:
    str     _protocol   the protocol of the database

    """

    _host = None
    _port = None
    _protocol = PROTOCOL.HTTP


    def __init__(self, host, port):
        """ Construct a new database object.

        Required:
        string host         host of the database
        string port         port of the database

        """
        self._host = host
        self._port = port


    def set_protocol(self, protocol):
        """ Set the URL protocol of the database. """
        self._protocol = protocol


    def base_url(self):
        """ Return the base url of the database. """
        return "{0}://{1}:{2}".format(
                self._protocol,
                self._host,
                self._port)


    def create_node(self, type, properties):
        """ Create a new node and return it.

        Checks for valid input and if valid, writes node to db.

        Required:
        string type         type of node
        dict properties     a dict of all the node's properties

        Returns the created Node.

        Raises:
        DbInputError        bad input
        DbWriteError        failed to write to database

        """
        required_properties = {
                NODE_PROPERTY.TYPE: type,
                }

        self._assert_input(properties, required_properties)

        try:
            new_node = self._query_create_node(
                    type,
                    properties)
            if new_node is None:
                raise DbWriteError(
                        "create_node",
                        "No new node returned from database.")
            return new_node
        except DbConnectionError as err:
            raise DbWriteError("create_node", err.read())


    def _query_create_node(self, type, properties):
        """ Create, store, and return a new node. """
        raise NotImplementedError("Subclass must implement.")


    def create_edge(self, from_node_id, to_node_id, type, properties):
        """ Create a new edge and return it.

        Checks for valid input and if valid, writes edge to db.

        Required:
        int from_node_id    id of start node
        int to_node_id      if of end node
        string type         type of edge
        dict properties     a dict of all the edge's properties

        Returns the created edge.

        Raises:
        DbInputError        bad input
        DbWriteError        failed to write to database

        """
        required_params = {
                EDGE_PROPERTY.FROM_NODE_ID: from_node_id,
                EDGE_PROPERTY.TO_NODE_ID: to_node_id,
                EDGE_PROPERTY.TYPE: type,
                }
        self._assert_input(properties, required_params)

        try:
            new_edge = self._query_create_edge(
                    from_node_id,
                    to_node_id,
                    type,
                    properties)
            if new_edge is None:
                raise DbWriteError(
                        "create_edge",
                        "No new edge returned from database.")
            return new_edge
        except DbConnectionError as err:
            raise DbWriteError("create_edge", err.read())


    def _query_create_edge(self, from_node_id, to_node_id, type, properties):
        """ Create, store, and return a new edge. """
        raise NotImplementedError("Subclass must implement.")


    def update_node(self, node_id, properties):
        """ Update existing node and return it.

        NOT IMPLEMENTED

        Required:
        int node_id         id of node to update
        dict properties     dictionary of new/updated properties

        Returns the node with updated properties.

        Raises:
        DbInputError    bad input
        DbWriteError    failed to write to database

        """
        raise NotImplementedError("TODO - Implement update_node.")

        if any(k in properties for k in (
                NODE_PROPERTY.TYPE,
                NODE_PROPERTY.ID)):
            raise DbInputError(
                    k,
                    properties,
                    k + " included in properties.")
        if node_id is None:
            raise DbInputError(
                    "node_id".
                    node_id,
                    "Required parameter not included.")

        try:
            updated_node = self._query_update_node(
                    node_id,
                    properties)
            if updated_node is None:
                raise DbWriteError(
                        "update_node",
                        "No updated node returned from database.")
            return updated_node
        except DbConnectionError as err:
            raise DbWriteError("update_node", err.read())


    def _query_update_node(self, node_id, properties):
        """ Update existing node and return it. """
        raise NotImplementedError("Subclass must implement.")


    def update_edge(self, edge_id, properties):
        """ Update existing edge and return it.

        Required:
        int edge_id     id of edge to update
        dict properties dictionary of new/updated properties

        Returns the edge with updated properties.

        Raises:
        DbInputError    bad input
        DbWriteError    failed to write to database

        """
        raise NotImplementedError("TODO - Implement update_edge.")

        if any(k in properties for k in (
            EDGE_PROPERTY.TYPE,
            EDGE_PROPERTY.FROM_NODE_ID,
            EDGE_PROPERTY.TO_NODE_ID,
            EDGE_PROPERTY.ID)):
            raise DbInputError(
                k,
                properties,
                k + " included in properties.")
        if edge_id is None:
            raise DbInputError(
                    "edge_id".
                    edge_id,
                    "Required parameter not included.")

        try:
            updated_edge = self._query_update_edge(
                    edge_id,
                    properties)
            if updated_edge is None:
                raise DbWriteError(
                        "update_edge",
                        "No updated edge returned from database.")
            return updated_edge
        except DbConnectionError as err:
            raise DbWriteError("update_edge", err.read())


    def _query_update_edge(self, edge_id, properties):
        """ Update and edge and return it. """
        raise NotImplementedError("Subclass must implement.")


    def delete_node(self, node_id, properties):
        raise NotImplementedError("TODO - Implement delete_node.")
        return None


    def delete_edge(self, edge_id, properties):
        raise NotImplementedError("TODO - Implement delete_edge.")
        return None


    def read_node_and_edges(self, node_id):
        """ Read a node and its edges.

        Required:
        int     node_id     id of requested Node

        Return:
        dict                node dict or None if no node exists

        Raises:
        DbReadError         read failure

        """
        try:
            return self._query_read_node_and_edges(node_id)

        except DbConnectionError as err:
            raise DbReadError("read_node_and_edges", err.read())


    def _query_read_node_and_edges(self, node_id):
        """ Read a node and its edges. """
        raise NotImplementedError("Subclasses must implement.")


    def read_nodes_by_index(self, key, value, node_return_filter=None):
        """ Return a dict of nodes with edges given a non-ID node property.

        Required:
        str     key                 indexed property for node lookup
        mixed   value               value (ideally unique) for node lookup

        Optional:
        list    node_return_filter  node types to filter for and return

        Return:
        dict                        nodes keyed on ID with edges (or None)

        Raises:
        DbReadError                 read failure

        """
        try:
            return self._query_read_nodes_by_index(
                    key,
                    value,
                    node_return_filter)

        except DbConnectionError as err:
            raise DbReadError("read_nodes_by_index", err.read())


    def _query_read_nodes_by_index(self, key, value, node_return_filter):
        """ Return a dict of nodes with edges given a non-ID node property. """
        raise NotImplementedError("Subclasses must implement.")


    def read_nodes_from_immediate_path(
            self,
            start_node_id,
            edge_pruner,
            node_return_filter):
        """ Read a pruned path from the database and return a filtered dict.

        Prune the path based on the edges list. Restrict the returned nodes
        to the filtered dictionary and the starting node.

        No duplicate edges in traversal. No duplicates in node lists.

        Required:
        id      start_node_id       ID of node to start traversing path from
        list    edge_pruner         edge types to include in traversal
        list    node_return_filter  node types to include in result set

        Return:
        dict            path defined as: {depth:{id:node}}

        Raises:
        DbInputError    if parameters are missing or incorrect
        DbReadError     db threw error

        """
        # TODO: instead of hardcoding, use constants or DbInputError
        # subclasses.
        # TODO: should node_return_filter and edge_pruner have default values?
        # TODO: THIS SHOULD BE DONE WITH ASSERT!

        if start_node_id is None:
            raise DbInputError(
                    start_node_id,
                    "start_node_id"
                    "Required parameter not included.")

        # empty list of edge types to prune for doesn't make sense
        if edge_pruner == []:
            raise DbInputError(
                    edge_pruner,
                    "edge_pruner"
                    "Required parameter not included.")

        # empty list of node types to return doesn't make sense
        if node_return_filter == []:
            raise DbInputError(
                    node_return_filter,
                    "node_return_filter",
                    "Required parameter not included.")

        try:
            return self._query_read_nodes_from_immediate_path(
                    start_node_id,
                    edge_pruner,
                    node_return_filter)

        except DbConnectionError as err:
            raise DbReadError("read_nodes_from_immediate_path", err.read())


    def _query_read_node_from_immediate_path(
            self,
            key,
            value,
            node_return_filter):
        """ Read and return a depth-1 set of nodes with their edges. """
        raise NotImplementedError("Subclasses must implement.")


    def read_edge(self, edge_id):
        raise NotImplementedError("NOT IMPLEMENTED...DO NOT CALL!")

    def read_node(self, edge_id):
        raise NotImplementedError("NOT IMPLEMENTED...DO NOT CALL!")


    def _assert_input(self, properties, required_properties):
        """ Validate the input properties.

        Check for both disallowed keys in properties and None values in both
        properties and required properties. Raise an error if the input doesn't
        validate.

        Required:
        dict properties         dict for all properties
        dict special_properties dict for required properties, which shouldn't
                                be in properties

        Raises:
        DbInputError    bad input

        """
        property_keys = set(properties.keys())
        required_property_keys = set(required_properties.keys())

        # ensure no required properties are in properties
        if not property_keys.isdisjoint(required_property_keys):
            bad_key = property_keys.union(required_property_keys).pop()
            raise DbInputError(
                    bad_key,
                    properties[bad_key],
                    "{0} included in properties.".format(bad_key))

        # ensure properties and required_properties are not None
        for key in property_keys:
            if properties[key] is None:
                raise DbInputError(
                        key,
                        None,
                        "Properties can not have value 'None'.")
        for key in required_property_keys:
            if required_properties[key] is None:
                raise DbInputError(
                        key,
                        None,
                        "Required parameter cannot have value 'None'.")

        # if this method doesn't error then the input is successfully asserted.
