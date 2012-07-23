""" Module: league

Define a LeagueModel to provide to the LeagueHandler a League context and
aggregated standings and/or activity and a feed for that League context.

"""

from model.api.person import Person
from model.api.game import Game
from model.api.league import League

from base import ReadModel


class LeagueModel(ReadModel):

    """ Load and prepare data for the View to render a League. """


    def __init__(self, session):
        """ Construct a ReadModel. """
        super(ReadModel, self).__init__(session)

        self._summary = {
                "standings": None,
                "activity": None,
                }


    def load(self):
        """ Populate context, summary, stories, and opponents. """

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
        league.set_opponents(League.load_opponents(league.id))
        league.set_games(League.load_games(league.id))

        # load league with opponents and games into generic context
        self._context = league

        # league's opponents by Win Count
        self._summary["standings"] = self._context.get_opponents().sort(
                key=lambda x: x.win_count,
                reverse=True)

        # TODO: iterating through this list is only temporary becaue the
        # multiload should have happened in the api.
        game_ids = [game.id for game in self._context.get_games()]

        # load opponents for each game {g_id: Game}
        games_with_opponents = Game.multiload_opponents(game_ids)

        # store opponents loaded games in reverse order (so it's new first)
        # NOTE: These Games are different objects than the ones in the
        # League though they represent the same data objects.
        self._feed = games_with_opponents.values().reverse()

        # load opponents into rivals as well
        self._rivals = self._context.get_opponents()


    @property
    def standings_summary(self):
        """ Return a list of League standings demonstrating rivalry. """
        return self._summary.get("standings")


    @property
    def activity_summary(self):
        """ Return a dict of League stats demonstrating camaraderie. """
        return self._summary.get("activity")
