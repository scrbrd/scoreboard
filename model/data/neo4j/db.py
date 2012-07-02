""" Module: db

Implement Sqoreboard's database api so that we can interact with a
neo4j database. It handles requests and also parses the neo4j
responses into something useful.

All the functions raise DbConnectionError if they can't connect
to the db or if the db returns an error, including a bad id error.

"""
import urllib2
import json


from util.decorators import print_timing
from model.constants import NODE_PROPERTY, EDGE_PROPERTY
from model.data.db import SqDatabase
from model.data.data_errors import DbConnectionError

from constants import NEO4J, NEO4J_INDEX, GREMLIN
import response_parser


class Neo4jDatabase(SqDatabase):

    """ Implement a SqDatabase to connect with neo4j. """


    def _query_create_node(self, type, properties):
        """ Create, store, and return a new Neo4j node using Gremlin.

        Keys: node_id, type, properties, edges

        Required:
        str     type        type of neo4j node to create
        dict    properties  properties to set in new neo4j node

        Returns:
        dict                properly formatted node

        """

        # add type to properties dictionary before generating script
        properties[NODE_PROPERTY.TYPE] = type

        # write a gremlin query and specify substitution fields
        # TODO: does grabbing the empty edges list take time here?
        script = "g.addVertex({0}).transform{{[it, it.outE()]}}".format(
                NODE_PROPERTY.PROPERTIES)

        # specify substitution values for the gremlin query
        parameters = {NODE_PROPERTY.PROPERTIES: properties}

        # send a request to the database
        response = self._gremlin(script, parameters)

        # format the response as a proper node
        if response is None:
            # TODO: raise DbWriteError
            return None
        else:
            return response_parser.format_node(response[0])

    def _query_create_edge(
            self,
            from_node_id,
            to_node_id,
            type,
            properties):
        """ Create, store, and return a new Neo4j edge using Gremlin.

        Required:
        id      from_node_id    id of outgoing node
        id      to_node_id      id of incoming node
        str     type            type of neo4j edge to create
        dict    properties      properties to set in new neo4j edge

        Return:
        dict                    properly formatted edge
        Keys: edge_id, from_node_id, to_node_id, type, properties

        """

        # write a gremlin query and specify substitution fields
        script = "g.addEdge(g.v({0}), g.v({1}), {2}, {3})".format(
                EDGE_PROPERTY.FROM_NODE_ID,
                EDGE_PROPERTY.TO_NODE_ID,
                EDGE_PROPERTY.TYPE,
                EDGE_PROPERTY.PROPERTIES)

        # specify substitution values for the gremlin query
        params = {
                EDGE_PROPERTY.FROM_NODE_ID: from_node_id,
                EDGE_PROPERTY.TO_NODE_ID: to_node_id,
                EDGE_PROPERTY.TYPE: type,
                EDGE_PROPERTY.PROPERTIES: properties,
                }

        # send a request to the database
        response = self._gremlin(script, params)

        # format the response as a proper edge
        if response is None:
            # TODO: raise RbWriteError
            return None
        else:
            return response_parser.format_edge(response)


    def _query_read_node_and_edges(self, node_id):
        """ Read and return a Neo4j node and its edges using Gremlin.

        Keys: node_id, type, properties, edges

        Required:
        id      node_id     id of node to query

        Return:
        dict                properly formatted node

        """

        # write a gremlin query and specify substitution fields
        # [ [ { v }, [ { Pipe }, { Pipe }, { Pipe } ] ] ]
        script = "g.v({0}).transform{{[it, it.outE()]}}".format(
                NODE_PROPERTY.ID)

        # specify substitution values for the gremlin query
        params = {NODE_PROPERTY.ID: node_id}

        # send a request to the database
        response = self._gremlin(script, params)

        # format response as a proper node
        if response is None:
            return None
        else:
            return response_parser.format_node(response[0])


    def _query_read_nodes_by_index(
            self,
            key,
            value,
            node_return_filter):
        """ Return a dict of nodes with edges given a non-ID node property.

        Required:
        str     key                 indexed node property to look up
        mixed   value               value (ideally unique) to look up
        list    node_return_filter  node types to filter for

        Return:
        dict                        properly formatted node
        Keys: node_id, type, properties, edges

        """

        # write a gremlin query
        filter = ""
        if node_return_filter:
            filter = ".filter{{it.{0}.matches({1})}}".format(
                    NODE_PROPERTY.TYPE,
                    "\"{0}\"".format("|".join(node_return_filter)))
        # specify substitution fields
        # [ { v }, [ { Pipe }, { Pipe } ] ]
        script = """
        g.idx(\"{0}\").get({1}, {2})._(){3}.transform{{[it, it.outE()]}}
        """.format(
                NEO4J_INDEX.NODES,
                key,
                value,
                filter)

        # specify substitution values for the gremlin query
        params = {
                key: key,
                value: value,
                NODE_PROPERTY.TYPE: NODE_PROPERTY.TYPE,
                }

        # send a request to the database
        response = self._gremlin(script, params)

        # format the response as a proper node
        if response is None:
            return None
        else:
            return response_parser.format_nodes(response)



    def _query_read_nodes_from_immediate_path(
            self,
            start_node_id,
            edge_pruner,
            node_return_filter):
        """ Read and return a depth-1 set of Neo4j nodes using Gremlin.

        Use edge_pruner and node_return_filter to impose path constraints.

        Required:
        id      start_node_id       id of requested neo4j node
        list    edge_pruner         edges to traverse (None=all)
        list    node_return_filter  nodes to return (None=all)

        Return:
        dict                        formatted nodes keyed on depth and id
        {depth: {node_id: node}}

        """

        # None is standard for specifying no filter (or, filter for all
        # types). an empty list would be the correct way to ask for no
        # return types, but we consider that to be an obvious error, which
        # is raised a layer above by the generic model.db, which has no
        # knowledge of or interest in how we format these filters here.

        if edge_pruner is None:
            edge_pruner = []

        if node_return_filter is None:
            node_return_filter = []

        # TODO: there's got to be a better way to do all of this string
        # formatting

        # format the pruners and filter
        edge_pruner = ",".join(["\"{0}\"".format(f) for f in edge_pruner])

        return_filter = ""
        if node_return_filter:
            return_filter = ".filter{{it.{0}.matches({1})}}".format(
                    NODE_PROPERTY.TYPE,
                    "\"{0}\"".format("|".join(node_return_filter)))

        # all unique nodes depth 1 from start node with restrictions
        start = "s=g.v({0}).transform{{[it, it.outE()]}}; ".format(
                NODE_PROPERTY.ID)
        path = """
                n=g.v({0}).out({1}).dedup(){2}.transform{{[it, it.outE()]}};
                """.format(
                        NODE_PROPERTY.ID,
                        edge_pruner,
                        return_filter)
        concat = "[s,n]"

        # write a gremlin query and specify substitution fields
        script = start + path + concat

        # specify substitution values for the gremlin query
        params = {NODE_PROPERTY.ID: start_node_id}

        # send a request to the database
        response = self._gremlin(script, params)

        # format response as a proper path
        if response is None:
            return None
        else:
            return response_parser.format_path(response)


    @print_timing
    def _gremlin(self, script, params):
        """ POST a Gremlin JSON request to a URL and handle the response.

        Script and parameters describe the JSON request. The
        Gremlin path describes the database to send it to.

        Required:
        str     script      gremlin script query
        dict    params      paramters to substitute in script

        Return:
        json                unformatted HTTP response.

        Raises:
        DbConnectionError   bad db connection

        """
        request = urllib2.Request(
                self.base_url() + GREMLIN.PATH,
                json.dumps({NEO4J.SCRIPT: script, NEO4J.PARAMS: params}))
        request.add_header(GREMLIN.REQUEST_HEADER_TYPE, GREMLIN.REQUEST_HEADER)

        serialized_response = None
        try:
            serialized_response = self._connect(request)
        except (urllib2.HTTPError) as err:
            # object not found
            if self._isNeo4jNullPointerError(err):
                print("Neo4j Null Pointer error caught. Returning None.")
                print("CURRENTLY THE INDEX ISN'T WORKING...PROLLY.")
                print script
                return None
            # some other type of HTTPError
            else:
                raise DbConnectionError("HTTPError: {0}".format(err.read()))
        except (urllib2.URLError) as err:
            # a URLError without an HTTP response code
            raise DbConnectionError("URLError: {0}".format(err.reason))

        response = None
        # input failed
        if GREMLIN.BASE_ERROR + GREMLIN.INPUT_ERROR in serialized_response:
            # TODO: make this a more explicit DbConnectionError
            raise DbConnectionError(serialized_response)
        # success!
        else:
            response = json.loads(serialized_response)

        return response


    def _connect(self, request):
        """ Connect to the database by opening the request.

        Required:
        urllib2.Request     request     The URL Request.

        Return:
        str                 serialized_response     response data

        """
        serialized_response = urllib2.urlopen(request).read()

        return serialized_response


    def _isNeo4jNullPointerError(self, error):
        """ Check if the error is a Neo4j Null Pointer Error. """
        error_dict = json.loads(error.read())
        error_msg = error_dict[GREMLIN.ERROR_MESSAGE]
        if GREMLIN.BASE_ERROR + GREMLIN.NULL_ERROR in error_msg:
            return True
        else:
            return False


class SecureNeo4jDatabase(Neo4jDatabase):

    """ Implement a secure version of Neo4jDatabase. """

    _username = None
    _password = None


    def __init__(self, host, port, username, password):
        """ Construct a SecureNeo4jDatabase. """
        super(SecureNeo4jDatabase, self).__init__(host, port)
        self._username = username
        self._password = password


    def _connect(self, request):
        """ Connect to the secured database by opening the request.

        Required:
        urllib2.Request     request     The URL Request.

        Return:
        str                 serialized_response     response data

        """
        # create a password manager
        password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

        # Add the username and password.
        # If we knew the realm, we could use it instead of None.
        password_mgr.add_password(
                None,
                self.base_url(),
                self._username,
                self._password)

        handler = urllib2.HTTPBasicAuthHandler(password_mgr)

        # create "opener" (OpenerDirector instance)
        opener = urllib2.build_opener(handler)

        # Install the opener.
        # Now all calls to urllib2.urlopen use our opener.
        urllib2.install_opener(opener)

        serialized_response = urllib2.urlopen(request).read()

        return serialized_response
