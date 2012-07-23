""" Module: create_game

Define a CreateGameModel to process an incoming request to create a game
and return whether or not the attempt was successful to the handler
responsible for returning the outgoing response.

"""

from model.api.game import Game

from base import WriteModel


class CreateGameModel(WriteModel):

    """ Create a game and return it.

    Dispatch Game node creation. We might want to make a Model for
    each node type, or we might want to keep this more generic.

    """

    _league_id = None
    _score = None


    def dispatch(self):
        """ Create new Game in database and return it. """
        self._model = Game.create_game(
                self._league_id,
                self.session.person_id,
                self._score)


    def set_league_id(self, league_id):
        """ Set the League ID for the Game to be created. """
        self._league_id = league_id


    def set_score(self, score):
        """ Set the Score for the Game to be created.

        Required:
        list    game_score      final score of a game
                                [{"id": id1, "score": score1},
                                 {"id": id2, "score": score2},
                                 ...
                                 {"id": idN, "score": scoreN}]

        """
        self._score = score


    @property
    def game(self):
        """ Return a newly created Game. """
        return self._model
