""" Module: games

Define a GamesModel to provide to the GamesHandler a context and a
summary and feed for that context.

"""

from model.api.person import Person
from model.api.game import Game
from model.api.league import League

from base import ReadModel


class GamesModel(ReadModel):

    """ Fetch and return all data necessary for a games list.

    Required:
    list    _games              list of games

    """

    _games = None


    def load(self):
        """ Load League, its Games, and its Games' Opponents. """

        # TODO: we should be able to do all this in one or two queries. given
        # player id, traverse to a league. from there get games and opponents
        # for those games. the only tricky thing is just getting one league. it
        # shouldn't be tricky to avoid manually loading opponents.

        person = Person.load_leagues(self.session.person_id)

        # TODO: do better than simply getting someone's first league.
        league = person.get_leagues()[0]

        # Load league with games into generic context
        self._context = League.load_games(league.id)

        # list of games that were loaded into league
        games = self._context.get_games()

        # iterating through this list is only temporary
        # because the multiload should have happened in the API
        game_ids = [g.id for g in games]

        # load opponents for each game {g_id: Game}
        games_with_opponents = Game.multiload_opponents(game_ids)

        # store opponents loaded games
        # NOTE: These Games are different objects than the ones in the
        # League though they represent the same data objects.
        self._games = games_with_opponents.values()
        # sort games in reverse order (so it's new first)
        self._games.reverse()

        # send all opponents to rivals
        unique_opponents = {}
        for g in games_with_opponents.values():
            for o in g.get_opponents():
                unique_opponents[o.id] = o
        self._rivals = unique_opponents.values()


    @property
    def games(self):
        """ Games that belong to the container. """
        return self._games


    def get_outcomes_by_game(self):
        """ Return dict by game_id of outcome highest to lowest.

        Each outcome is a list of (score, Opponent) tuples ordered
        by score from highest to lowest.

        # TODO remove this method if accessing outcomes directly in Game

        """

        # store score, Opponent tuples by game id for each game
        outcomes_by_game = {}

        for game in self._games:
            # get outcome for each game
            outcome = game.outcome()

            # replace opp_id with actual Opponent object from Game
            outcome_with_opponents = []
            for result in outcome:
                new_result = GenericModel()
                new_result.score = result[0]
                opponent_id = result[1]
                new_result.opponent = game.get_opponent(opponent_id)
                outcome_with_opponents.append(new_result)

            # save updated outcome for each game
            outcomes_by_game[game.id] = outcome_with_opponents

        return outcomes_by_game


# FIXME remove this class
class GenericModel(object):

    """ Generic object for returning data that a Model constructs.

    Common models should be added to the API.

    """

    pass
