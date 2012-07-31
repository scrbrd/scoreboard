""" Module: create_game

Define a CreateGameModel to process an incoming request to create a game
and return whether or not the attempt was successful to the handler
responsible for returning the outgoing response.

"""

from model.api.game import Game
from model.api.metric import MetricFactory

from base import WriteModel


class CreateGameModel(WriteModel):

    """ Create a game and return it.

    Dispatch Game node creation. We might want to make a Model for
    each node type, or we might want to keep this more generic.

    Required:
    int     _league_id              the league of the new Game
    dict    _metrics_by_opponent    Metrics dicts keyed on Opponent id

    """

    _league_id = None
    _metrics_by_opponent = {}


    def dispatch(self):
        """ Create new Game in database and return it. """
        self._model = Game.create_game(
                self._league_id,
                self.session.person_id,
                self._metrics_by_opponent)


    def set_league_id(self, league_id):
        """ Set the League ID for the Game to be created. """
        self._league_id = league_id


    def set_metrics_by_opponent(self, metrics_by_opponent):
        """ Set the Metrics for each Opponent for the Game.

        Required:
        dict    metrics_by_opponent Metrics dicts keyed on Opponent  id

        """
        # convert the results into API_EDGE_TYPEs
        for opponent_id, metrics in metrics_by_opponent.items():
            metric_objects = MetricFactory.produce_metrics(metrics)
            self._metrics_by_opponent[opponent_id] = metric_objects


    @property
    def game(self):
        """ Return a newly created Game. """
        return self._model
