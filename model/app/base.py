""" Module: base

All data requests are processed by request type and the appropriate
data is retrieved and returned as a Model.

"""

import tornado.web

from exceptions import NotImplementedError

from model.constants import NODE_PROPERTY, PROPERTY_VALUE, THIRD_PARTY

from model.api.user import User
from model.api.person import Person
from model.api.game import Game
from model.api.league import League


class BaseModel(object):

    """ Fetch and/or edit all data necessary for a model request.

    BaseModels wrap around returned data to provide controlled access
    outside of model.

    """

    _session = None


    def __init__(self, session):
        """ BaseModel is an abstract superclass. """
        self._session = session


    @property
    def session(self):
        """ Return a Session with some User/Person session data. """
        return self._session


    def load(self):
        """ Return a model. """
        raise NotImplementedError("Abstract Class: SUBCLASS MUST OVERRIDE!")


    def dispatch(self):
        """ Propagate a write to a model. """
        raise NotImplementedError("Abstract Class: SUBCLASS MUST OVERRIDE!")


class ReadModel(BaseModel):

    """ Read and return all data for a model request.

    Required:
    League  _context    container of objects (id, name fields required)
    dict    _summary    aggregated stats describing context
    list    _feed       discrete units describing context
    list    _rivals     list of Opponents (id, name)

    """

    _context = None
    _summary = None
    _feed = None
    _rivals = None


    def dispatch(self):
        """ Propagate a write to a model. """
        raise NotImplementedError("Unused Method: DO NOT CALL OR OVERRIDE!")


    @property
    def context(self):
        """ Context/Container of fetched data. """
        return self._context


    @property
    def summary(self):
        """ Return a dict of aggregated data describing context. """
        return self._summary


    @property
    def feed(self):
        """ Return a list of discrete units of data describing context. """
        return self._feed


    @property
    def rivals(self):
        """ List of Opponents with name and id. """
        return self._rivals


class WriteModel(BaseModel):

    """ Write data to a model and return success.

    Required:
    bool    success     was this dispatched write successful?

    """

    _model = None


    def load(self):
        """ Return a model. """
        raise NotImplementedError("Unused Method: DO NOT CALL OR OVERRIDE!")


    @property
    def success(self):
        """ Return whether this Model successfully dispatched a write. """
        return bool(self._model)


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


class RankingsModel(ReadModel):

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

        person = Person.load_leagues(self.session.person_id)

        # TODO: do better than simply getting someone's first league.
        league = person.get_leagues()[0]

        # Load league with games into generic context
        self._context = League.load_opponents(league.id)

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


class AuthModel(BaseModel):

    """ Authenticate a User. Prompt for authorization if needed.

    Create, fetch, and/or prepare all necessary data for storing a
    cookie that can be used for authentication and analytics tracking on
    future requests. On first login, Create and store a new User.

    This is set up so that there should be a subclass for each third
    party login implementation we support. These Subclasses need only
    override the credentials-related methods described herein. Further,
    to implement our own login, we need only implement those same
    credentials-related methods here.

    """

    MAX_ATTEMPTS = 5

    _user = None
    _person = None
    _existing_user = None
    _raw_user = None
    _ip = None
    _locale = None
    _is_new = False

    # TODO: remove this when removing default league!
    _default_league_id = None


    def set_raw_user(self, raw_user):
        """ Set the raw User credentials for the Session to be created. """
        self._raw_user = raw_user


    def set_ip(self, ip):
        """ Set the IP address for the Session to be created. """
        self._ip = ip


    def set_locale(self, locale):
        """ Set the browser locale for the Session to be created. """
        self._locale = locale


    # TODO: remove this when no longer needed!
    def set_default_league_id(self, default_league_id):
        """ Set the default League ID to join for new Users. """
        self._default_league_id = default_league_id


    def load_and_dispatch(self):
        """ Load a User from credentials and dispatch creates/updates. """
        self.load()
        self.dispatch()


    def load(self):
        """ Load an existing User from supplied login credentials. """
        # retry lookup from credentials a couple times to avoid duplicates.
        # this is an absolute and utter hackjob!
        for attempt in range(self.MAX_ATTEMPTS):
            self._existing_user = self._load_credentials(self._raw_user)
            if self._existing_user:
                break


    def dispatch(self):
        """ Dispatch a create/update based on whether a User exists. """

        # this User/Person exists; update our data with raw data.
        if self._existing_user:
            (self._user, self._person) = self._update_credentials(
                    self._raw_user,
                    self._existing_user)

        # this User/Person is new; create new ones!
        else:
            (self._user, self._person) = self._create_credentials(
                    self._raw_user,
                    self._default_league_id)

            # set a flag to alert subscribers that a new user was created!
            self._is_new = all([self._user, self._person])


    def _load_credentials(self, raw_user):
        """ Try to return an existing user for a set of credentials. """
        raise NotImplementedError("Not Yet Implemented: SUBCLASS, OVERRIDE!")


    def _update_credentials(self, old_user, raw_user):
        """ Update an existing User with new raw user credentials. """
        raise NotImplementedError("Not Yet Implemented: SUBCLASS, OVERRIDE!")


    # TODO: drop league_id from this signature when leagues are better!
    def _create_credentials(self, raw_user, league_id=None):
        """ Create a new User and Player from raw user credentials. """
        raise NotImplementedError("Not Yet Implemented: SUBCLASS, OVERRIDE!")


    @property
    def user(self):
        """ Return the User for this request. """
        return self._user


    @property
    def person(self):
        """ Return the Person for this request. """
        return self._person


    @property
    def is_new(self):
        """ Return whether this User/Person is newly created. """
        return self._is_new


class FacebookAuthModel(AuthModel):

    """ Authenticate a Facebook User. Prompt for authorization if needed.

    Lookup and/or create/update a User on login with Facebook.

    On Facebook login, we attempt to fetch a User and potentially create
    or update our database with the user information supplied.

    """


    def _load_credentials(self, raw_user):
        """ Return an existing user for a set of credentials. """
        fb_id = raw_user.get(NODE_PROPERTY.ID)

        if fb_id is None:
            raise tornado.web.HTTPError(500, "No Facebook User ID.")

        return User.load_by_external_id(fb_id, THIRD_PARTY.FACEBOOK)


    def _update_credentials(self, raw_user, user):
        """ Update an existing User with new raw user credentials. """
        # TODO: implement update and use it here!
        #return User.update_user_and_player(user, raw_user)
        return (user, Person.load_leagues(user.get_default_person_id()))


    # TODO: drop league_id from this signature when leagues are better!
    def _create_credentials(self, raw_user, league_id=None, inviter_id=None):
        """ Create a new User and Player from raw user credentials. """

        # TODO: there are a lot of open questions here:
        # 1/ maybe fix this parameter list...it's ridiculous!
        # 2/ what about when we want to create a Person who isn't a Player?
        # 3/ when other credentialing options exist, it might not be good to
        #    assume exclusively.
        # 4/ is it more sensible to keep these methods separate if it turns out
        #    we can't easily generalize across other Person subclasses?

        (user, player) = User.create_user_and_player(
                PROPERTY_VALUE.EMPTY,
                PROPERTY_VALUE.EMPTY,
                None,
                PROPERTY_VALUE.EMPTY,
                PROPERTY_VALUE.EMPTY,
                {THIRD_PARTY.FACEBOOK: raw_user},
                inviter_id,
                self._ip,
                self._locale)

        # TODO: uncomment TAGGED SqEdge type and pass optional third argument.
        if league_id is not None:
            Person.join_league(player.id, league_id)

        return (user, player)


    def set_facebook_user(self, fb_user):
        """ Set the Facebook User for the Session to be created. """
        self.set_raw_user(fb_user)


# FIXME remove this class
class GenericModel(object):

    """ Generic object for returning data that a Model constructs.

    Common models should be added to the API.

    """

    pass
