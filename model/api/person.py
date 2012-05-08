""" Module: Person

SqNode
  |
  +-- Person

TODO: fill this in with required methods to implement since required
members aren't strictly members [they are pulled from properties].

"""

from exceptions import NotImplementedError

from model.constants import NODE_PROPERTY

from constants import API_NODE_TYPE, API_NODE_PROPERTY, API_CONSTANT
from sqobject import SqNode


class Person(SqNode):

    """ Person is an abstract subclass of SqNode.

    Provide access to the attributes of a Person, including fields and 
    edges connecting to other nodes.

    Required:
    int     fb_id           Facebook user ID
    str     name            full name
    str     first_name      first name
    str     middle_name     middle name
    str     last_name       last name
    url     link            profile url
    url     picture         profile picture url

    """


    def outgoing_edge_types(self):
        """ Return a list of allowed outgoing SqEdge types. """
        raise NotImplementedError("Abstract Method: SUBCLASS MUST OVERRIDE!")


    @property
    def name(self):
        """ Return this Person's full name. """

        # TODO: this wouldn't have to be defined here or in League if it were
        # instead defined in SqNode, but this seems less confusing for now.

        return "{0} {1}".format(self.first_name, self.last_name)
        #return self._get_property(API_NODE_PROPERTY.NAME)


    @property
    def first_name(self):
        """ Return this Person's first name. """
        return self._get_property(API_NODE_PROPERTY.FIRST_NAME)


    @property
    def middle_name(self):
        """ Return this Person's middle name. """
        return self._get_property(API_NODE_PROPERTY.MIDDLE_NAME)


    @property
    def last_name(self):
        """ Return this Person's last name. """
        return self._get_property(API_NODE_PROPERTY.LAST_NAME)


    @property
    def short_name(self):
        """ Return this Person's first name and last initial. """
        return "{0} {1}".format(
                self.first_name,
                self.last_name[0])


    @property
    def link(self):
        """ Return a url for this Person's profile or website. """
        return self._get_property(API_NODE_PROPERTY.LINK)


    @property
    def gender(self):
        """ Return this Person's gender string.

        Enumeratued Type:
        "e_male"
        "e_female"

        """

        # TODO: should this be an enum?

        return self._get_property(API_NODE_PROPERTY.GENDER)


    @property
    def picture(self):
        """ Return a url for this Person's profile picture. """
        return self._get_property(API_NODE_PROPERTY.PICTURE)


    """ The below are duplicated in User for now. """


    @property
    def fb_id(self):
        """ Return this Person's Facebook ID. """

        # for now, this is guaranteed to be set. later, there may be other
        # third parties and some established hierarchy for checking or we may
        # have implemented our own login system.
        return self._properties.get(
                API_CONSTANT.FACEBOOK_NODE_PROPERTIES[NODE_PROPERTY.ID],
                None)


    @property
    def fb_username(self):
        """ Return this User's Facebook username. """
        return self._get_property(API_NODE_PROPERTY.USERNAME)


    @property
    def email(self):
        """ Return this User's email address. """
        return self._get_property(API_NODE_PROPERTY.EMAIL)


    """ The above are duplicated in User for now. """

