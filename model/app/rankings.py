""" Module: rankings

Define a RankingsModel to provide to the RankingsHandler a context and a
summary and feed for that context.

"""

from model.api import person, league

import base


class RankingsModel(base.ReadModel):

    """ Generate league's rankings based on most wins.

    Required:
    Opponents   _opponents      Opponents sorted by Win Count
    str         _rank_field     Field that Opponents are sorted by

    """

    _opponents = None
    _rank_field = "win_count"


    def load(self):
        """ Load League, its Opponents, and sort by Win Count. """

        # TODO: we should be able to do all this in one or two queries. given
        # player id, traverse to a league. from there get games and opponents
        # for those games. the only tricky thing is just getting one league. it
        # shouldn't be tricky to avoid manually loading opponents.

        loaded_person = person.Person.load_leagues(self.session.person_id)

        # TODO: do better than simply getting someone's first league.
        loaded_league = loaded_person.get_leagues()[0]

        # Load league with games into generic context
        self._context = league.League.load_opponents(loaded_league.id)

        # league's opponents by Win Count
        self._opponents = self._context.get_opponents()
        self._opponents.sort(key=lambda x: x.win_count, reverse=True)

        # load opponents into rivals as well
        self._rivals = self._opponents


    @property
    def rankings(self):
        """ Return the ranked objects. """
        return self._opponents


    @property
    def rank_field(self):
        """ Return the field that the objects were ranked by. """
        return self._rank_field
