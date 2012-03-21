""" Data Request Catchers

All data requests are processed by request type and the appropriate
data is retrieved and returned as a Catcher.

"""

from copy import deepcopy
from exceptions import NotImplementedError

from model.api.game import Game
from model.api.league import League
from model.api.opponent import Opponent
from model.constants import GAMES, RANKINGS

class Catcher(object):
    
    """ Fetch and/or edit all data necessary for a model request. 

    Catchers wrap around returned data to provide controlled access
    outside of model.
    
    Required:
    League _context   container of objects (id, name fields required)
    
    """

    
    _context = None

    def __init__(self):
        """ Catcher is an abstract superclass. """
        raise NotImplementedError("Catcher must be extended by a subclass.")
    
    
    @property
    def context_container(self):
        """ Context/Container of fetched data. """
        return self._context


class GamesCatcher(Catcher):
    
    """ Fetch and return all data necessary for a games list.

    Required:
    list    _games              list of games
    dict    _outcome_by_game    {g_id: (score, Opponent)}
    """


    _games = []
    _outcomes_by_game = {}

    def __init__(self, league_id):
        """ Instantiate with League, Games, and Opponents. """
        # Load games data from API.
        self._context = League.load_games(league_id) 
        league = self._context

        # TODO: make it a depth-2 traversal. don't manually load opponents.
        
        # list of games that were loaded into league
        games = league.get_games()
        
        # iterating through this list is only temporary
        # because the multiload should have happened in the API
        game_ids = [g.id() for g in games]
        
        # load opponents for each game {g_id: Game}
        games_with_opponents = Game.multiload_opponents(game_ids)
        
        # store opponents loaded games
        self._games = games_with_opponents.values()
        
        # store score, Opponent tuples by game id for each game
        for game in self._games:
            outcome = game.outcome()
            for (score, opponent_id) in outcome:
                self._outcomes_by_game[id] = (
                        score, 
                        game.get_opponent(opponent_id))
                
            
    @property
    def games(self):
        """ Games that belong to the container. """
        return self._games


    def get_outcomes_by_game(self):
        """ Return dict by game_id of outcome highest to lowest. """
        return self._outcomes_by_game


class RankingsCatcher(Catcher):
        
    """ Generate league's rankings based on most wins.
    
    Required:
    Opponents   _opponents      Opponents sorted by Win Count
    str         _rank_field     Field that Opponents are sorted by
    
    """


    _opponents = None
    _rank_field = "win_count"

    def __init__(self, league_id):
        """ Instantiate Rankings with Leagues & Opponents. """        
        self._context = League.load_opponents(league_id)
        league = self._context 

        # leagues' opponents by Win Count
        self._opponents = league.get_opponents()
        self._opponents.sort(key = lambda x: x.win_count, reverse=True)


    @property
    def ranks(self):
        """ Return the ranked objects. """
        return self._opponents
    

    @property
    def rank_field(self):
        """ Return the field that the objects were ranked by. """
        return self._rank_field


def create_game(league_id, creator_id, opponent_score_pairs):
    """ Create a game and return it.

    Required:
    id league_id                league id that game belogs to
    id creator_id               player id of game's creator
    list opponent_score_pairs   tuples of opponent ids and score
    
    Return:
    Game                        instance of SqNode subclass Game

    """

    return Game.create_game(league_id, creator_id, opponent_score_pairs)

