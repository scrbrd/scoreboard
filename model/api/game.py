""" Module: game

TODO: fill this in with required methods to implement since required
members aren't strictly members [they are pulled from properties].

"""
from util.dev import print_timing
from constants import API_NODE_TYPE, API_EDGE_TYPE, API_NODE_PROPERTY
from constants import API_CONSTANT
from sports import SPORT

from sqobject import SqNode
import loader
import editor



class Game(SqNode):

    """ Game is a subclass of SqEdge for representing games.

    Provide access to the attributes of a Game, including fields,
    relationships, and nearby nodes.

    A Game cannot exist without CREATED_BY and SCHEDULED_IN outgoing
    SqEdges and either a WON_BY and one or more LOST_BY outgoing
    SqEdges, two or more TIED_BY outgoing SqEdges, or one PLAYED_BY
    outgoing SqEdge. In all cases, the incoming SqEdge complements
    are also required.

    Variables:
    dict    _opponents      store loaded Opponents by id
    dict    _commenters     store loaded Commenters by id
    Person  creator         store loaded Person

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
                API_EDGE_TYPE.PLAYED_BY,
                API_EDGE_TYPE.HAS_COMMENT_FROM,
                ]


    @property
    def comments(self):
        """ Return a list of comments on the Game, sorted with most recent
        comment last. """
        comments = self.get_edges() \
            .get(API_EDGE_TYPE.HAS_COMMENT_FROM, {}) \
            .values()
        comments.sort(key=lambda x: x.created_ts)
        return comments


    @property
    def creator_id(self):
        """  Return the Player who created the game. """
        return self.get_edges() \
            .get(API_EDGE_TYPE.CREATED_BY, {}) \
            .values()[0] \
            .to_node_id


    @property
    def sport_id(self):
        """ Return the Sport ID for this Game. """
        return self._get_property(API_NODE_PROPERTY.SPORT_ID)


    @property
    def sport(self):
        """ Return the Sport for this Game. """
        return SPORT.ALL.get(self.sport_id)


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


    @property
    def winner_ids(self):
        """ Return a list of competitive Opponent IDs who won. """
        return self.opponent_ids_by_result.get(API_EDGE_TYPE.WON_BY, [])


    @property
    def loser_ids(self):
        """ Return a list of competitive Opponent IDs who lost. """
        return self.opponent_ids_by_result.get(API_EDGE_TYPE.LOST_BY, [])


    @property
    def tier_ids(self):
        """ Return a list of competitive Opponent IDs who tied. """
        return self.opponent_ids_by_result.get(API_EDGE_TYPE.TIED_BY, [])


    @property
    def rivalry_ids(self):
        """ Return a list of all competitive Opponent IDs for this Game. """
        rivalry_ids = []
        rivalry_ids.extend(self.winner_ids)
        rivalry_ids.extend(self.loser_ids)
        rivalry_ids.extend(self.tier_ids)
        return rivalry_ids


    @property
    def camaraderie_ids(self):
        """ Return a list of friendly Opponent IDs who played. """
        return self.opponent_ids_by_result.get(API_EDGE_TYPE.PLAYED_BY, [])


    # TODO: maybe we should use competitive instead of rivalry
    @property
    def is_rivalry(self):
        """ Return whether this Game is competitive. """
        return bool(self.rivalry_ids)


    # TODO: maybe we should use friendly instead of camaraderie
    @property
    def is_camaraderie(self):
        """ Return whether this Game is friendly. """
        return bool(self.camaraderie_ids)


    def get_creator(self):
        """ Return the Person that created this Game. """
        SqNode.assert_loaded(self._creator)
        return self._creator


    def set_creator(self, creator):
        """ Set a Game's loaded Creator. """
        self._creator = creator


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


    def get_commenter(self, commenter_id):
        """ Return a Person that's commented by their id. """
        SqNode.assert_loaded(self._commenters)
        return self._commenters.get(commenter_id, None)


    def get_commenters(self, commenter_ids=None):
        """ Return a dict of Commenters. """
        SqNode.assert_loaded(self._commenters)
        if commenter_ids is None:
            return self._commenters
        else:
            return {id: self.get_commenter(id) for id in commenter_ids}


    def set_opponents(self, opponents):
        """ Set a Game's loaded Opponents from a dict. """
        self._opponents = opponents


    def set_commenters(self, commenters):
        """ Set a Game's loaded Commenters from a dict. """
        self._commenters = commenters


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
    def load_important_persons(game_id):
        """ Load the Game's Opponents, Commenters, Creator and attributes into
        a Game.

        Required:
        int game_id     the id of the Game

        Return:
        Game            Game SqNode

        """
        # TODO: commenters should really be loaded in SqNode. This is a mess
        # because load_neighbors returns a single list of neighbors and then we
        # break that list up by type.

        edge_types = []
        edge_types.extend(API_CONSTANT.RESULT_EDGE_TYPES)
        edge_types.append(API_EDGE_TYPE.HAS_COMMENT_FROM)
        edge_types.append(API_EDGE_TYPE.CREATED_BY)

        node_types = []
        node_types.extend(API_CONSTANT.OPPONENT_NODE_TYPES)
        # should include "PERSON_NODE_TYPES"

        (game, important_persons) = loader.load_neighbors(
                game_id,
                edge_types,
                node_types)

        # sort the folks into separate lists of opponents and commenters
        opponent_ids = set(game.results_by_opponent_id.keys())
        comments = game.get_edges().get(
                API_EDGE_TYPE.HAS_COMMENT_FROM,
                {})
        commenter_ids = set(
                [comment.to_node_id for comment in comments.values()])

        opponents = {}
        commenters = {}
        creator = None
        for person in important_persons.values():
            id = person.id
            if id in opponent_ids:
                opponents[id] = person
            if id in commenter_ids:
                commenters[id] = person
            if id == game.creator_id:
                creator = person
        game.set_opponents(opponents)
        game.set_commenters(commenters)
        game.set_creator(creator)

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
    @print_timing
    def multiload_important_persons(game_ids):
        """ Load multiple Games' Opponents, Commenters, Creator and attributes.

        Required:
        list game_ids   the ids of the Games

        Return:
        dict            Game SqNodes keyed on id

        """

        games = {}

        for id in game_ids:
            games[id] = Game.load_important_persons(id)

        return games


    @staticmethod
    def create_game(league_id, creator_id, metrics_by_opponent, sport_id):
        """ Create a Game and return it.

        Required:
        id      league_id           League id that Game belogs to
        id      creator_id          Player id of Game's creator
        dict    metrics_by_opponent Metrics keyed on Opponent id
        id      sport_id            Sport id for this Game

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
        prototype_node = editor.prototype_node(
                API_NODE_TYPE.GAME,
                {API_NODE_PROPERTY.SPORT_ID: sport_id})

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
