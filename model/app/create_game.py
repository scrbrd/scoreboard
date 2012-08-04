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
    dict    _session                the User/Person data keyed by property
    dict    _metrics_by_opponent    metrics dicts keyed on opponent id

    Optional:
    int     _league_id              the league of the new Game

    """


    def __init__(self, session, metrics_by_opponent):
        """ BaseModel is an abstract superclass.

        Required:
        dict    session                 all the User/Person session data
        dict    metrics_by_opponent     metrics dict keyed on opponent id

        """
        super(CreateGameModel, self).__init__(session)

        self._metrics_by_opponent = {}
        self._league_id = None

        # convert the results into API_EDGE_TYPEs
        for opponent_id, metrics in metrics_by_opponent.items():
            metric_objects = MetricFactory.produce_metrics(metrics)
            self._metrics_by_opponent[opponent_id] = metric_objects


    def dispatch(self):
        """ Create new Game in database and return it. """
        self._object = Game.create_game(
                self._league_id,
                self._session.person_id,
                self._metrics_by_opponent)


    def set_league_id(self, league_id):
        """ Set the League ID for the Game to be created. """
        self._league_id = league_id


    @property
    def game(self):
        """ Return a newly created Game. """
        return self._object
