""" Module: Player

TODO: fill this in with required methods to implement since required
members aren't strictly members [they are pulled from properties].

"""

from constants import API_NODE_TYPE, API_EDGE_TYPE, API_NODE_PROPERTY

import person
import opponent
import editor


class Player(person.Person, opponent.Opponent):

    """ Player is a subclass of SqNode.

    Provide access to the attributes of a Player, including fields and
    edges connecting to other nodes.

    Required:

    """


    def outgoing_edge_types(self):
        """ Return a list of allowed outgoing SqEdge types. """
        # TODO: other eventual Person subclasses will be able to log in as well
        # and will need API_EDGE_TYPE.HAS_PRIMARY to refer to a User. this
        # method in the super class should define a list to be extend()ed here.
        return [
                API_EDGE_TYPE.IN_LEAGUE,
                API_EDGE_TYPE.CREATED,
                API_EDGE_TYPE.WON,
                API_EDGE_TYPE.LOST,
                API_EDGE_TYPE.TIED,
                API_EDGE_TYPE.PLAYED,
                API_EDGE_TYPE.SPAWNED_BY,
                API_EDGE_TYPE.OWNED_BY,
                API_EDGE_TYPE.HAS_PRIMARY,
                #API_EDGE_TYPE.TAGGED,
                #API_EDGE_TYPE.TAGGED_BY,
                ]


    def _count_losses(self):
        """ Return the number of Games this Player has lost. """
        # it's possible for a player not to have any losses, in which case
        # there won't be an entry in the edges dict, so default to the empty
        # dict.
        return len(self.get_edges().get(API_EDGE_TYPE.LOST, {}))


    @property
    def loss_count(self):
        """ Alias for count_losses() intended for use as a property. """
        return self._count_losses()


    def _count_wins(self):
        """ Return the number of Games this Player has won. """
        # it's possible for a player not to have any wins, in which case there
        # won't be an entry in the edges dict, so default to the empty dict
        return len(self.get_edges().get(API_EDGE_TYPE.WON, {}))


    @property
    def win_count(self):
        """ Alias for count_wins() intended for use as a property. """
        return self._count_wins()


    @staticmethod
    def property_keys():
        """ Return a list of permitted property fields for Player. """
        return [
                API_NODE_PROPERTY.FIRST_NAME,
                API_NODE_PROPERTY.MIDDLE_NAME,
                API_NODE_PROPERTY.LAST_NAME,
                API_NODE_PROPERTY.LINK,
                API_NODE_PROPERTY.GENDER,
                API_NODE_PROPERTY.PICTURE,
                ]


    @staticmethod
    def create_player(
            first_name,
            last_name,
            spawner_id,
            owner_id=None,
            third_parties={}):
        """ Create a Player and return it.

        Required:
        str     first_name          created Player's first name
        str     last_name           created Player's last name
        id      spawner_id          id of User creating this Player

        Optional:
        id      owner_id            id of User controlling this Player
        dict    third_parties       key/val dicts keyed on 3rd party

        Return:
        Player                      is a Person, acts as an Opponent

        Example:
        Optional parameter third_parties should be defined as follows:

        {
            "fb" : {<CONVERT FROM JSON TO DICT AND LEAVE DATA AS IS>},
            "tw" : {<CONVERT FROM JSON TO DICT AND LEAVE DATA AS IS>},
        }

        This will be flattened, validated, and culled by SqNode.

        """

        player_keys = Player.property_keys()

        # TODO: everything below should happen generically in Person._create()
        #return Person.create(
        #        raw_properties,
        #        Player.property_keys(),
        #        spawner_id,
        #        owner_id,
        #        third_parties)

        # FIXME: for now, we co-locate third party username/email with both
        # the associated User and Person...it's kinda bad.
        player_keys.extend([
                API_NODE_PROPERTY.USERNAME,
                API_NODE_PROPERTY.EMAIL,
                ])

        raw_properties = {
                API_NODE_PROPERTY.FIRST_NAME: first_name,
                API_NODE_PROPERTY.LAST_NAME: last_name,
                }

        properties = Player.prepare_node_properties(
                player_keys,
                raw_properties,
                third_parties)

        # TODO: add a static method call to generically check required fields
        # against statically defined lists in each class.

        # prepare a node prototype for this game
        prototype_node = editor.prototype_node(
                API_NODE_TYPE.PLAYER,
                properties)

        # prepare edge prototypes for spawner edges
        prototype_edges = editor.prototype_edge_and_complement(
                API_EDGE_TYPE.SPAWNED,
                {},
                spawner_id)

        if owner_id is None:
            owner_id = spawner_id

        # prepare edge prototypes for owner edges
        prototype_edges.extend(editor.prototype_edge_and_complement(
                API_EDGE_TYPE.OWNS,
                {},
                owner_id))

        prototype_edges.append(editor.prototype_edge(
                API_EDGE_TYPE.HAS_PRIMARY,
                {},
                None,
                owner_id))

        prototype_edges.append(editor.prototype_edge(
                API_EDGE_TYPE.DEFAULTS_TO,
                {},
                owner_id,
                None))

        return editor.create_node_and_edges(prototype_node, prototype_edges)
