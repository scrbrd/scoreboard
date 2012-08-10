""" Module: comment

Represent a Person's Comment on an SqObject by subclassing SqEdge.

"""

from constants import API_EDGE_TYPE, API_EDGE_PROPERTY
from sqobject import SqEdge
import editor


class Comment(SqEdge):

    """ An Comment on an object, which subclasses SqEdge.

    Variables:
    str _message        the body of the comment

    """

    # TODO: Comment is only being used for writing right now.


    @property
    def message(self):
        """ Return the message (comment body) of the comment. """
        return self._get_property(API_EDGE_PROPERTY.MESSAGE)


    @property
    def commenter_id(self):
        """ Return the id of the commenter. """
        # FIXME Make a comment class that has a generic system for accessing to
        # and from node ids for bidirectional edges.
        if self.type == API_EDGE_TYPE.COMMENTED_ON:
            return self.from_node_id
        else:
            return self.to_node_id


    @property
    def object_id(self):
        """ Return the id of the object being commented on. """
        return self.to_node_id


    """ Static loader wrappers. """


    @staticmethod
    def property_keys():
        """ Return a list of permitted property fields for Comment. """
        return [API_EDGE_PROPERTY.MESSAGE]


    @staticmethod
    def create_comment(object_id, commenter_id, message):
        """ Create a Comment and return it.

        Required:
        id      object_id       the object that the comment was posted to
        id      commenter_id    the Person who posted the comment
        str     message         the body of the Comment

        Return:
        Comment???

        """
        prototype_edges = editor.prototype_edge_and_complement(
                API_EDGE_TYPE.COMMENTED_ON,
                {API_EDGE_PROPERTY.MESSAGE: message},
                commenter_id,
                object_id)

        return editor.create_edges(prototype_edges)
