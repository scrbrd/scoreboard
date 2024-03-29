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

from __future__ import division
from copy import deepcopy

from model.constants import NODE_PROPERTY, EDGE_PROPERTY
from model.constants import PROPERTY_KEY, PROPERTY_VALUE, THIRD_PARTY

from constants import API_CONSTANT, API_NODE_PROPERTY
from stat_computer import StatComputer


class SqObject(object):

    """ SqObject is a subclass of the __new__ python object.

    Provide access to the common attributes of all SqNode and SqEdge
    subclasses.

    Required:
    id      _id             SqObject id
    str     _type           SqObject type
    dict    _properties     SqObject properties from GraphObject
    int     _created_ts     Time that SqObject was created.
    int     _updated_ts     Time that SqObject was updated.

    """


    def __init__(self, graph_object):
        """ Construct a SqObject extending the __new__ python object. """
        self._id = graph_object.id()
        self._type = graph_object.type()

        # intentionally not exposed as a property or even as a method since
        # most of the helpers defined by subclasses are access wrappers.
        self._properties = graph_object.properties()

        # TODO: this is only needed because SqNode doesn't subclass from
        # GraphNode
        self._created_ts = graph_object.created_ts()
        self._updated_ts = graph_object.updated_ts()

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


    @property
    def created_ts(self):
        """ Return a created timestamp. """
        return self._created_ts


    @property
    def updated_ts(self):
        """ Return a updated timestamp. """
        return self._updated_ts



    def _get_property(self, key):
        """ Return SqObject property denoted by key. """
        raise NotImplementedError("Abstract Method: SUBCLASS MUST OVERRIDE!")


class SqNode(SqObject, StatComputer):

    """ SqNode is a subclass of SqObject, and implements the StatComputer
    interface.

    Provide access to the common attributes of a League, Team, Player,
    User, and Game, including fields and edges connecting to other
    nodes.

    SqNode's only requirement is at least one set of SqEdges.

    StatComputer allows all subclasses to compute stats based on particular
    metrics.

    Optional:
    dict    _edges       this SqNode's outgoing SqEdges keyed on id

    """


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


    def get_edges_by_type(self, edge_type):
        """ Return a dict of SqEdges of a given type for a SqNode. """
        return self.get_edges()[edge_type]


    def get_edge_ids_by_type(self, edge_type):
        """ Return a list of SqEdge IDs of a given type for a SqNode. """
        return self.get_edges_by_type(edge_type).keys()


    def get_to_node_ids_by_type(self, edge_type):
        """ Return a list of to-SqNode IDs by SqEdge type for a SqNode. """
        edges = self.get_edges_by_type(edge_type)
        return [edge.to_node_id for id, edge in edges.items()]


    def set_edges(self, edges):
        """ Set a member variable with a dict of outgoing SqEdges. """
        self._edges = edges


    def _get_property(
            self,
            key,
            third_party=THIRD_PARTY.FACEBOOK,
            use_third_party=False):
        """ Return a GraphObject property as a member.

        If we have data stored for this property key, use it. Otherwise,
        fall back on the supplied third party. Or, when specified, use
        the third party and ignore our data altogether.

        Required:
        str     key             SqNode property key

        Optional:
        str     third_party     third party to use or default to
        bool    use_third_party use third party property, not SqNode

        """

        # FIXME: create a mapping from SqNode property to third party property
        # so that we don't rely on keys always being the same. also, maybe
        # create a hierarchy when other third parties enter the mix.

        property = None
        sq_property = self._properties.get(key, None)

        tp_key = SqNode.third_party_property_key(third_party, key)

        tp_property = self._properties.get(tp_key, None)

        if use_third_party:
            property = tp_property
        else:
            # if the property is not empty then use it.
            if sq_property != PROPERTY_VALUE.EMPTY:
                property = sq_property
            # else (so the property is empty) use a third party property
            elif tp_property is not None:
                property = tp_property
            # but if the third party property is None then use the empty
            # sq_property.
            else:
                property = sq_property

        if property is None:
            raise SqObjectPropertyError(
                    key,
                    "SqObject property doesn't exist.")

        return property


    def _compute_count(self, edge_types):
        """ Return a count of a metric.

        Required:
        list    edge_types  a list of edge_types to be counted.

        """
        # it's possible for a player not to have any of that edge type, in
        # which case there won't be an entry in the edges dict, so default to
        # the empty dict
        count = 0
        for edge_type in edge_types:
            count += len(self.get_edges().get(edge_type, {}))
        return count


    def _compute_percentage(
            self,
            antecedent_edge_types,
            consequent_edge_types):
        """ Return a percentage of a ratio of a set of edge types to another
        set of edge types.

        Required:
        list antecedent_edge_types      a list of edge types for the top of the
                                        fraction.
        list consequent_edge_types      a list of edge types for the bottom of
                                        the fraction.

        """
        antecedent_count = self._compute_count(antecedent_edge_types)
        consequent_count = self._compute_count(consequent_edge_types)

        # from __future__ import division in imports (converts to float
        # automatically and gets us ready for Python 3.*)
        if consequent_count == 0:
            # prevents ZeroDivisionError
            return 0
        else:
            return antecedent_count / consequent_count


    def _compute_current_streak(self, streak_conditions, all_edge_types):
        """ Return the count of consecutive fulfilled conditions
        when all the edges are sorted by created_ts, looking back from now.

        Required:
        list    streak_conditions   a list of edge types that count for streak
        list    all_edge_types      a list of all edge types

        """
        edges = []
        for edge_type in all_edge_types:
            edges.extend(self.get_edges().get(edge_type, {}).values())
        edges.sort(key=lambda x: x.created_ts, reverse=True)

        streak = 0
        for e in edges:
            if e.type in streak_conditions:
                streak += 1
            else:
                break
        return streak


    @staticmethod
    def assert_loaded(loaded_data):
        """ If data is not loaded, raise an error. """
        if loaded_data is None:
            raise SqObjectNotLoadedError("SqObject member not loaded")


    @staticmethod
    def locked_property_keys():
        """ Return a list of uneditable SqNode properties. """
        return [
                NODE_PROPERTY.ID,
                NODE_PROPERTY.TYPE,
                NODE_PROPERTY.EDGES,
                ]


    @staticmethod
    def prepare_node_properties(type_keys, raw_properties, third_parties=None):
        """ Return a dict with node properties prepared for storage.

        This is intended to make use of sibling static methods
        SqNode.prepare_default_properties() and
        SqNode.prepare_third_party_properties() when called by SqNode
        subclasses at node creation and update time.

        Largely, this is a convenience method which centralizes logic
        around preparing the properties of a new or existing node for
        storage. For a given SqNode type, We expunge invalid keys and
        values, store a default value for any unspecified properties,
        and merge in valid keys and values provided by third parties.

        Required:
        list    type_keys       property keys for a specific SqNode type
        dict    raw_properties  SqNode property values keyed on type

        Optional:
        dict    third_parties   3rd party property dicts keyed on party

        Return:
        dict                    SqNode properties valid for storage

        """

        # TODO: make this available and functional for create/update.

        # initialize the dict to return
        properties = SqNode.prepare_default_properties(type_keys)

        valid_properties = SqNode.validate_properties(
                type_keys,
                raw_properties)

        properties.update(valid_properties)

        if third_parties is not None:
            tp_properties = SqNode.prepare_third_party_properties(
                    type_keys,
                    third_parties)

            properties.update(tp_properties)

        return properties


    @staticmethod
    def prepare_default_properties(type_keys):
        """ Return a dict initialized with default node properties.

        This is intended to be called from related static method
        SqNode.prepare_node_properties(), which is called by SqNode
        subclasses at node creation time.

        Largely, this is a convenience method which centralizes usage of
        PROPERTY_VALUE.EMPTY. However, if we decide to initialize
        different types of data to different values, this is the right
        place to do it.

        Further, this is helpful if we swap out one database for another
        and find different restrictions on storage (None, null, boolean,
        etc.).

        Required:
        list    type_keys   property keys for a specific type of SqNode

        Return:
        dict                default SqNode properties keyed on type_keys

        """

        properties = {}

        # TODO: upgrade to python2.7, make this a dict comprehension
        #d = dict((k,v) for (k,v) in blah blah blah)
        #d = {k : v for k in blah blah blah}

        # initialize properties to empty
        for key in type_keys:
            properties[key] = PROPERTY_VALUE.EMPTY

        return properties


    @staticmethod
    def prepare_third_party_properties(type_keys, third_parties):
        """ Return a dict with flat, valid third party properties.

        This is intended to be called by static method
        SqNode.prepare_node_properties(), which is invoked at SqNode
        create/update time, but it can also function on its own.

        Largely, this is a convenience method which centralizes usage of
        PROPERTY_KEY.DELIMITER and prevents duplication of unnecessarily
        complicated logic around flattening data from third parties into
        our storage mechanism.

        Required:
        list    type_keys       property keys for a specific SqNode type
        dict    third_parties   3rd party property dicts keyed on party

        Return:
        dict                    SqNode properties valid for storage

        """
        properties = {}

        # iterate over third party property dicts
        for tp, tp_properties in third_parties.items():

            # is this a valid third party?
            if tp not in THIRD_PARTY.ALL:
                # TODO: raise exception on failure
                continue

            # expunge invalid key/value pairs from this third party
            valid_properties = SqNode.validate_properties(
                    type_keys,
                    tp_properties,
                    True)


            # FIXME: we are blindly trusting that property keys we share with
            # third parties like Facebook are exactly equivalent strings we use
            # for database storage...this is very bad.

            # flatten this third party's data into a storable dict
            for tp_key, tp_value in valid_properties.items():

                # TODO: if this becomes a trend, bake type into third party
                # constants definitions to cast from strings more generically.
                if tp_key == NODE_PROPERTY.ID:
                    tp_value = int(tp_value)

                key = SqNode.third_party_property_key(tp, tp_key)
                properties[key] = tp_value

        return properties


    @staticmethod
    def validate_properties(type_keys, properties, id_is_valid=False):
        """ Return a dict with invalid properties expunged.

        Required:
        list    type_keys   property keys for a specific SqNode type
        dict    properties  property values for a specific SqNode type

        Optional:
        bool    id_is_valid ignore id key when excluding locked keys?

        Return:
        dict                valid SqNode property key/value pairs

        """

        # these properties may not be edited directly by the API layer
        locked_keys = SqNode.locked_property_keys()

        # it is valid to store third party IDs linking our accounts to theirs,
        # but it is not valid to attempt to overwrite our internally-created
        # IDs, so we allow callers to explicitly specify that we ignore ID when
        # excluding locked properties.
        if id_is_valid:
            type_keys.append(NODE_PROPERTY.ID)
            locked_keys.remove(NODE_PROPERTY.ID)

        valid_properties = {}

        # expunge disallowed keys and values
        for key, value in properties.items():

            # is this a valid key for this type?
            if key not in type_keys:
                # TODO: raise an error, or silently remove the property?
                pass

            # is this an immutable SqNode key?
            elif key in locked_keys:
                # TODO: raise an error, or silently remove the property?
                pass

            # is this a valid property value?
            elif value is None:
                # TODO: raise an error, or silently convert to EMPTY?
                pass

            # success!
            else:
                if key == API_NODE_PROPERTY.PICTURE:
                    facebook_bug_value = value.get("data")
                    if facebook_bug_value is None:
                        valid_properties[key] = value
                    else:
                        valid_properties[key] = facebook_bug_value.get("url")
                else:
                    valid_properties[key] = value

        return valid_properties


    @staticmethod
    def third_party_property_key(third_party, property_key):
        """ Return a property key for third party data storage.

        Create a key like "fb_first_name" by joining third party ("fb"),
        delimiter ("_"), and property key ("first_name").

        Required:
        str     third_party     who is the third party? ex: "fb" or "tw"
        str     property_key    what is the property? ex: "first_name"

        Return:
        str                     valid property key for our database

        """

        # TODO: raise an error when third party or property key is invalid

        return "{0}{1}{2}".format(
                third_party,
                PROPERTY_KEY.DELIMITER,
                property_key)


class SqEdge(SqObject):

    """ SqEdge is a subclass of SqObject.

    Provide access to the common attributes of Win, Loss, Tie, Member,
    and other edges modeling relationships between SqNodes.

    Required:
    id      _from_node_id   SqNode id for which this SqEdge is outgoing
    id      _to_node_id     SqNode id for which this SqEdge is incoming
    dict    _properties     all edge properties (temporary)

    """


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


    def _get_property(self, key):
        """ Return SqEdge property denoted by key. """
        return self._properties.get(key, None)


    @staticmethod
    def locked_property_keys():
        """ Return a list of uneditable SqEdge properties. """
        return [
                EDGE_PROPERTY.ID,
                EDGE_PROPERTY.TYPE,
                EDGE_PROPERTY.FROM_NODE_ID,
                EDGE_PROPERTY.TO_NODE_ID,
                EDGE_PROPERTY.CREATED_TS,
                EDGE_PROPERTY.UPDATED_TS,
                EDGE_PROPERTY.DELETED_TS,
                ]


class SqObjectPropertyError(Exception):

    """ SqObjectPropertyError is a subclass of Exception.

    Provide an exception to be raised when an attempt is made to access
    a SqObject property which does not exist. Usually this means that
    we failed to retrieve the property from our own database and from
    third party APIs like Facebook as well.

    Required:
    str     reason      the reason for the error

    """


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

    Required:
    str     reason      the reason for the error

    """


    def __init__(self, reason):
        self.reason = reason
