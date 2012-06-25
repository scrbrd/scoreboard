""" Module: Person

SqNode
  |
  +-- Person

TODO: fill this in with required methods to implement since required
members aren't strictly members [they are pulled from properties].

"""

from exceptions import NotImplementedError

from model.constants import NODE_PROPERTY, THIRD_PARTY

from constants import API_NODE_TYPE, API_NODE_PROPERTY, API_EDGE_TYPE
from sqobject import SqNode
import loader
import editor


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

    _leagues = None


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
        model.constants.GENDER.MALE
        model.constants.GENDER.FEMALE

        """

        # TODO: should this be an enum?

        return self._get_property(API_NODE_PROPERTY.GENDER)


    @property
    def picture(self):
        """ Return a url for this Person's profile picture. """
        return self._get_property(API_NODE_PROPERTY.PICTURE)


    def get_leagues(self):
        """ Return a list of Leagues. """
        SqNode.assert_loaded(self._leagues)
        return self._leagues.values()


    def set_leagues(self, leagues):
        """ Set a Person's loaded Leagues with a dict. """
        self._leagues = leagues


    @staticmethod
    def load_leagues(person_id):
        """ Return a Person with Leagues data loaded. """
        (person, leagues) = loader.load_neighbors(
                person_id,
                [API_EDGE_TYPE.IN_LEAGUE],
                [API_NODE_TYPE.LEAGUE])

        person.set_leagues(leagues)

        return person


    @staticmethod
    def join_league(person_id, league_id, tagger_id=None):
        """ Add a Person to a League.

        Required:
        id  person_id   ID of Person to add to League
        id  league_id   ID of League the Person is joining

        Optional:
        id  tagger_id   ID of Person who tagged/added/invited the joiner

        Return:
        bool            success

        """
        # TODO: for now, tagger_id is unused. fix this when we implement
        # tagging and/or invites. also, figure out whether we will need to
        # track the tagging/inviting User in addition to Person. for now, the
        # only call to this method is from create_player(), but there we don't
        # actually have access to the tagging/inviting Player. fix that too.
        return editor.create_edges(editor.prototype_edge_and_complement(
                API_EDGE_TYPE.IN_LEAGUE,
                {},
                person_id,
                league_id))


    # The below are duplicated in User for now.


    @property
    def fb_id(self):
        """ Return this Person's Facebook ID. """

        # TODO: for now, we guarantee this is set. later, there may be other
        # third parties and some established hierarchy for checking or we may
        # have implemented our own login system.

        # signal _get_property() to bypass NODE_PROPERTY.ID since that field is
        # guaranteed to always be set and we explicitly want the Facebook ID.
        return self._get_property(NODE_PROPERTY.ID, THIRD_PARTY.FACEBOOK, True)


    @property
    def fb_username(self):
        """ Return this User's Facebook username. """
        return self._get_property(API_NODE_PROPERTY.USERNAME)


    @property
    def email(self):
        """ Return this User's email address. """
        return self._get_property(API_NODE_PROPERTY.EMAIL)
