""" Data Request Catchers

All data requests are processed by request type and the appropriate
data is retrieved and returned as a Catcher.

"""

from copy import deepcopy
from exceptions import NotImplementedError

from model.constants import NODE_PROPERTY, PROPERTY_VALUE, THIRD_PARTY

from model.api.constants import API_NODE_PROPERTY

from model.api.user import User
from model.api.person import Person
from model.api.player import Player
from model.api.game import Game
from model.api.league import League
from model.api.opponent import Opponent


class Catcher(object):

    """ Fetch and/or edit all data necessary for a model request.

    Catchers wrap around returned data to provide controlled access
    outside of model.

    """


    def __init__(self):
        """ Catcher is an abstract superclass. """
        raise NotImplementedError("Catcher must be extended by a subclass.")


class ReadCatcher(Catcher):
    
    """ Read and return all data for a model request.

    Required:
    League  _context    container of objects (id, name fields required)
    list    _rivals     list of Opponents (id, name)

    """

    _context = None
    _rivals = None


    def _load_catcher(self):
        """ Load all necessary data. """
        raise NotImplementedError("Catcher must be extended by a subclass.")


    def _load_rivals(self, league_id, opponents=None):
        """ Load rival list for context.

        Required:
        int     league_id   league that rivals are part of

        Optional:
        list    opponents   List of opponents. if it is excluded then
                            load from league_id.

        """
        if opponents is None:
            league = League.load_opponents(league_id)
            self._rivals = league.get_opponents()
        else:
            self._rivals = opponents


    @property
    def context(self):
        """ Context/Container of fetched data. """
        return self._context


    @property
    def rivals(self):
        """ List of Opponents with name and id. """
        return self._rivals


class GamesCatcher(ReadCatcher):

    """ Fetch and return all data necessary for a games list.

    Required:
    list    _games              list of games

    """

    _games = []


    def __init__(self, league_id):
        """ Instantiate with League, Games, and Opponents. """
        self._load_catcher(league_id)


    def _load_catcher(self, league_id):
        """ Load League, its Games, and its Games' Opponenets. """

        # Load league with games into generic context
        self._context = League.load_games(league_id)
        league = self._context

        # TODO: make it a depth-2 traversal. don't manually load opponents.

        # list of games that were loaded into league
        games = league.get_games()

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
        self._load_rivals(league_id, unique_opponents.values())


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


class RankingsCatcher(ReadCatcher):

    """ Generate league's rankings based on most wins.

    Required:
    Opponents   _opponents      Opponents sorted by Win Count
    str         _rank_field     Field that Opponents are sorted by

    """

    _opponents = None
    _rank_field = "win_count"

    def __init__(self, league_id):
        """ Instantiate Rankings with Leagues & Opponents. """
        self._load_catcher(league_id)


    def _load_catcher(self, league_id):
        """ Load League, its Opponents, and sort by Win Count. """

        self._context = League.load_opponents(league_id)
        league = self._context

        # leagues' opponents by Win Count
        self._opponents = league.get_opponents()
        self._opponents.sort(key=lambda x: x.win_count, reverse=True)

        # load opponents into rivals as well
        self._load_rivals(league_id, self._opponents)


    @property
    def rankings(self):
        """ Return the ranked objects. """
        return self._opponents


    @property
    def rank_field(self):
        """ Return the field that the objects were ranked by. """
        return self._rank_field


class CreateCatcher(Catcher):

    """ Create a game and return it.

    Catcher for handling all Node Creation. We might want to
    make a catcher for each creation type. We might also want
    to make this more generic.

    """


    def __init__(self):
        """ Instantiate new CreateCatcher. """
        pass


    def create_game(self, league_id, creator_id, game_score):
        """ Create new Game in database and return it.

        Required:
        id      league_id       league id that game belogs to
        id      creator_id      player id of game's creator
        list    game_score      final score of a game
                                [{"id": id1, "score": score1},
                                 {"id": id2, "score": score2},
                                 ...
                                 {"id": idN, "score": scoreN}]

        Return:
        Game                    instance of SqNode subclass Game

        """
        return Game.create_game(league_id, creator_id, game_score)


class AuthCatcher(Catcher):

    """ Authenticate a User. Prompt for authorization if needed.

    Create, fetch, and/or prepare all necessary data for storing a
    cookie that can be used for authentication and analytics tracking on
    future requests. On first login, Create and store a new User.

    """


    def __init__(self, raw_user, ip):
        """ Constructor for a AuthCatcher. """
        pass


    def get_user_by_id(self, id):
        """ Return a User given an id. """
        return User.load_by_id(id)


    def get_user_by_email(self, email):
        """ Return a User given an email. """
        return User.load_by_email(email)


class FacebookAuthCatcher(AuthCatcher):

    """ Authenticate a Facebook User. Prompt for authorization if needed.
    
    Lookup and/or create/update a User on login with Facebook.

    On Facebook login, we attempt to fetch a User and potentially create
    or update our database with the user information supplied.

    """

    _user = None
    _player = None
    _league = None
    _ip = None


    def __init__(self, raw_user, ip, default_league_id):
        """ Constructor for a FacebookAuthCatcher. """

        self._ip = ip

        # TODO: there's probably a more efficient way to do this.
        # TODO: should this all be broken out into a couple methods?
        # TODO: devise a naming scheme that generally works for Catchers.

        fb_id = raw_user.get(NODE_PROPERTY.ID)

        if fb_id is None:
            raise tornado.web.HTTPError(500, "No Facebook User ID.")

        existing_user = User.load_by_external_id(fb_id, THIRD_PARTY.FACEBOOK)

        if existing_user is None:

            (user, player) = User.create_user_and_player(
                    PROPERTY_VALUE.EMPTY,
                    PROPERTY_VALUE.EMPTY,
                    None,
                    PROPERTY_VALUE.EMPTY,
                    PROPERTY_VALUE.EMPTY,
                    {THIRD_PARTY.FACEBOOK : raw_user},
                    None,
                    self._ip)
                    #self._ip,
                    #VERSION.CURRENT,
                    #from_node_id,
                    #API_EDGE_TYPE.HAS_LEAGUE_MEMBER)

            # TODO: uncomment and figure out where from_node_id comes from in
            # order to automatically add the new Player to a League.

            league = None

        else:

            # TODO: implement update and use it here!

            user = existing_user
            #(user, player) = User.update_user_and_player(
            #        raw_user,
            #        existing_user)

            # TODO: implement joining leagues and query joined leagues here!

            player = Person.load_leagues(user.get_default_person_id())
            #league = player.get_leagues()[0]

        # TODO: implement joining leagues. stop using the default global league

        self._user = user
        self._player = player
        self._league = League.load_opponents(default_league_id)


    def user(self):
        """ Return a User. """
        return self._user


    def player(self):
        """ Return a Player. """
        return self._player


    def league(self):
        """ Return a League. """
        return self._league


# FIXME remove this class
class GenericModel(object):

    """ Generic object for returning data that a catcher constructs.

    Common models should be added to the API.

    """

    pass
