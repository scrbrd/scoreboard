""" Module: game

TODO: fill this in with required methods to implement since required
members aren't strictly members [they are pulled from properties].

"""
from util.dev import print_timing
from constants import API_NODE_TYPE, API_EDGE_TYPE
from constants import API_CONSTANT

from sqobject import SqNode
import loader
import editor



class Game(SqNode):

    """ Game is a subclass of SqObject for representing games.

    Provide access to the attributes of a Game, including fields,
    relationships, and nearby nodes.

    A Game cannot exist without CREATED_BY and SCHEDULED_IN outgoing
    SqEdges and either a WON_BY and one or more LOST_BY outgoing
    SqEdges, two or more TIED_BY outgoing SqEdges, or one PLAYED_BY
    outgoing SqEdge. In all cases, the incoming SqEdge complements
    are also required.

    Variables:
    dict    _opponents     store loaded Opponents by id

    """


    @property
    def name(self):
        """ Games do not have names. Raise an error. """
        raise NotImplementedError("Game does not implement name property.")


    def outgoing_edge_types(self):
        """ Return a list of allowed outgoing SqEdge types. """
        return [
                API_EDGE_TYPE.SCHEDULED_IN,
                API_EDGE_TYPE.CREATED_BY,
                API_EDGE_TYPE.WON_BY,
                API_EDGE_TYPE.LOST_BY,
                API_EDGE_TYPE.TIED_BY,
                API_EDGE_TYPE.PLAYED_BY
                ]


    @property
    def creator_id(self):
        """  Return the Player who created the game. """
        return self.get_edges()[API_EDGE_TYPE.CREATED_BY].iterkeys().next()


    @property
    def results_by_opponent_id(self):
        """ Return a dictionary of results keyed by opponent id. """
        results = {}

        # Loop through each RESULT_EDGE_TYPE and get the result/opponent_id
        for edge_type in API_CONSTANT.RESULT_EDGE_TYPES:
            for edge in self.get_edges().get(edge_type, {}).values():
                opponent_id = edge.to_node_id
                results[opponent_id] = edge_type

        return results


    @property
    def opponent_ids_by_result(self):
        """ Return a dictionary of opponents keyed by result. Each result
        will have a list of opponents. """
        opponents = {}

        # Loop through each RESULT_EDGE_TYPE and get the result/opponent_id
        for edge_type in API_CONSTANT.RESULT_EDGE_TYPES:
            edges = self.get_edges().get(edge_type)
            if edges is not None:
                opponents[edge_type] = []
                for edge in edges.values():
                    opponent_id = edge.to_node_id
                    opponents[edge_type].append(opponent_id)

        return opponents


    def get_opponent(self, opp_id):
        """ Return an Opponent by its id. """
        SqNode.assert_loaded(self._opponents)
        return self._opponents.get(opp_id, None)


    def get_opponents(self, opponent_ids=None):
        """ Return a list of Opponents. """
        SqNode.assert_loaded(self._opponents)
        if opponent_ids is None:
            return self._opponents.values()
        else:
            return [self.get_opponent(id) for id in opponent_ids]


    def set_opponents(self, opponents):
        """ Set a Game's loaded Opponents from a dict. """
        self._opponents = opponents


    """ Static loader wrappers. """


    @staticmethod
    def property_keys():
        """ Return a list of permitted property fields for Game. """
        return []


    @staticmethod
    def load_opponents(game_id):
        """ Load the Game's Opponents and attributes into a Game.

        Required:
        int game_id     the id of the Game

        Return:
        Game            Game SqNode

        """

        (game, opponents) = loader.load_neighbors(
                game_id,
                API_CONSTANT.RESULT_EDGE_TYPES,
                API_CONSTANT.OPPONENT_NODE_TYPES)

        game.set_opponents(opponents)

        return game


    @staticmethod
    @print_timing
    def multiload_opponents(game_ids):
        """ Load multiple Games' Opponents and attributes into a dict.

        Required:
        list game_ids   the ids of the Games

        Return:
        dict            Game SqNodes keyed on id

        """

        games = {}

        for id in game_ids:
            games[id] = Game.load_opponents(id)

        return games


    @staticmethod
    def create_game(league_id, creator_id, metrics_by_opponent):
        """ Create a Game and return it.

        Required:
        id      league_id           League id that Game belogs to
        id      creator_id          Player id of Game's creator
        dict    metrics_by_opponent Metrics keyed on Opponent id

        Return:
        Game                        newly created Game

        """

        # TODO: when games have properties, fill these in!
        #
        #raw_properties = {}
        #
        #properties = SqNode.prepare_node_properties(
        #        Game.property_keys(),
        #        raw_properties)

        # prepare a node prototype for this game
        prototype_node = editor.prototype_node(API_NODE_TYPE.GAME, {})

        # prepare edge prototypes for schedule edges
        prototype_edges = editor.prototype_edge_and_complement(
                API_EDGE_TYPE.HAS_SCHEDULED,
                {},
                league_id)

        # prepare edge prototypes for creator edges
        prototype_edges.extend(editor.prototype_edge_and_complement(
                API_EDGE_TYPE.CREATED,
                {},
                creator_id))

        # prepare edge prototypes for result edges
        for opponent_id, metrics in metrics_by_opponent.items():
            for metric in metrics:
                # TODO: handle other metrics besides ResultMetric
                prototype_edges.extend(editor.prototype_edge_and_complement(
                        metric.result,
                        {},
                        opponent_id))

        return editor.create_node_and_edges(prototype_node, prototype_edges)
