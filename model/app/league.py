""" Module: league

Define a LeagueModel to provide to the LeagueHandler a League context and
aggregated standings and/or activity and a list of obejcts for that League
context.

"""

from model.api.person import Person
from model.api.game import Game
from model.api.league import League

from base import ReadModel


class LeagueModel(ReadModel):

    """ Load and prepare data for the View to render a League.

    Required:
    Opponents   _opponents      Opponents sorted by Win Count
    str         _rank_field     Field that Opponents are sorted by

    """


    def __init__(self, session):
        """ Construct a ReadModel. """
        super(ReadModel, self).__init__(session)

        self._aggregations = {
                "standings": None,
                "activity": None,
                }


    def load(self):
        """ Populate context, aggregations, objects, and opponents. """

        # TODO: we should be able to do all this in one or two queries. given
        # player id, traverse to a league. from there get games and opponents
        # for those games. the only tricky thing is just getting one league. it
        # shouldn't be tricky to avoid manually loading opponents.

        person = Person.load_leagues(self.session.person_id)

        # TODO: do better than simply getting someone's first league.
        league = person.get_leagues()[0]

        # TODO: we don't need to load Games from League when they can be loaded
        # from Opponents [or the vice-versa] all at the same time. we should
        # never be calling set_opponents() and set_games() outside the api.

        # RANKINGS LOAD
        opponents_list = League.load_opponents(league.id).get_opponents()
        league.set_opponents({o.id: o for o in opponents_list})

        # GAMES LOAD
        games_list = League.load_games(league.id).get_games()
        league.set_games({g.id: g for g in games_list})

        # TODO: iterating through this list is only temporary becaue the
        # multiload should have happened in the api.
        game_ids = [game.id for game in league.get_games()]

        # load opponents for each game {g_id: Game}
        games_with_opponents = Game.multiload_opponents(game_ids)

        # load league with opponents and games into generic context
        self._context = league

        # league's opponents by Win Count
        # store the list because the league has a dict, and sort returns None
        opponents = self._context.get_opponents()
        opponents.sort(
                key=lambda x: x.win_count,
                reverse=True)
        self._aggregations["standings"] = opponents

        self._aggregations["activity"] = None

        # store opponents loaded games in reverse order (so it's new first)
        games = games_with_opponents.values()
        # reverse returns None as it's in-place
        games.reverse()
        self._objects = games

        # load opponents into rivals as well
        self._rivals = self._context.get_opponents()


    @property
    def standings_aggregation(self):
        """ Return a list of League standings demonstrating rivalry. """
        return self._aggregations.get("standings")


    @property
    def activity_aggregation(self):
        """ Return a dict of League stats demonstrating camaraderie. """
        return self._aggregations.get("activity")
