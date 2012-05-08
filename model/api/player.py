""" Module: Player

TODO: fill this in with required methods to implement since required
members aren't strictly members [they are pulled from properties].

"""

from constants import API_EDGE_TYPE
from person import Person
from opponent import Opponent


class Player(Person, Opponent):

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
                API_EDGE_TYPE.HAS_PRIMARY
                ]


    def count_wins(self):
        """ Return the number of Games this Player has won. """
        # it's possible for a player not to have any wins, in which case there 
        # won't be an entry in the edges dict, so default to the empty dict
        return len(self.get_edges().get(API_EDGE_TYPE.WON, {}))


    @property
    def win_count(self):
        """ Alias for count_wins() intended for use as a property. """
        return self.count_wins()


    # TODO FIXME XXX: convert this to create_player

    #@staticmethod
    #def create_player(league_id, creator_id, game_score):
    #    """ Create a Game and return it.
    #
    #    Required:
    #    id      league_id       league id that game belogs to
    #    id      creator_id      player id of game's creator
    #    list    game_score      final score of a game
    #                            [{"id": VALUE, "score": VALUE}]
    #
    #    Return the created game.
    #
    #    """
    #
    #    # prepare a node prototype for this game
    #    prototype_node = editor.prototype_node(API_NODE_TYPE.GAME, {})
    #
    #    prototype_edges = []
    #
    #    # prepare edge prototypes for schedule edges
    #    prototype_edges.extend(editor.prototype_edge_and_complement(
    #            API_EDGE_TYPE.SCHEDULED_IN,
    #            {},
    #            league_id))
    #
    #    # prepare edge prototypes for creator edges
    #    prototype_edges.extend(editor.prototype_edge_and_complement(
    #            API_EDGE_TYPE.CREATED_BY,
    #            {},
    #            creator_id))
    #
    #    # get outcome from gamescore
    #    outcome = Game.calculate_outcome(game_score)
    #
    #    # prepare edge prototypes for result edges
    #    for type, result in outcome.items():
    #        for opponent_score in result:
    #            prototype_edges.extend(editor.prototype_edge_and_complement(
    #                type,
    #                {API_EDGE_PROPERTY.SCORE: opponent_score["score"]},
    #                opponent_score["id"]))
    #
    #    return editor.create_node_and_edges(prototype_node, prototype_edges)

