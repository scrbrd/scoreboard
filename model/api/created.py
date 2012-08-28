""" Module: created

A Created edge between Person and Game. Subclasses SqEdge.

"""
from constants import API_EDGE_TYPE, API_EDGE_PROPERTY
from sqobject import SqEdge
import editor


class Created(SqEdge):

    """ A Created (and created by) object that subclases SqEdge.

    Variables:
    str _message        the message that the creator attached to the Edge

    """

    @property
    def message(self):
        """ Return the message of the created edge. """
        message = self._get_property(API_EDGE_PROPERTY.MESSAGE)
        if message is None:
            message = "Nope"
        return message


    @property
    def creator_id(self):
        """ Return the id of the creator. """
        # FIXME Make edge class that has a generic system for accessing to
        # and from node ids for bidirectional edges.
        if self.type == API_EDGE_TYPE.CREATED:
            return self.from_node_id
        else:
            return self.to_node_id


    @property
    def object_id(self):
        """ Return the id of the created object. """
        # FIXME Make a edge class that has a generic system for accessing to
        # and from node ids for bidirectional edges.
        if self.type == API_EDGE_TYPE.CREATED:
            return self.to_node_id
        else:
            return self.from_node_id


    """ Static loader wrappers. """


    @staticmethod
    def property_keys():
        """ Return a list of permitted property fields for Created Edge. """
        return [API_EDGE_PROPERTY.MESSAGE]


    @staticmethod
    def create_created(creator_id, object_id, message):
        """ Create a Created Edge and return it.

        Required:
        id      creator_id  the creator of that object
        id      object_id   the object that was created
        str     message     the message the creator attached

        Return:
        Created???

        """
        prototype_edges = editor.prototype_edge_and_complement(
                API_EDGE_TYPE.CREATED,
                {API_EDGE_PROPERTY.MESSAGE: message},
                creator_id,
                object_id)

        return editor.create_edges(prototype_edges)
