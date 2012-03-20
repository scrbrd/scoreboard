""" Data Request Catchers

All data requests are processed by request type and the appropriate
data is retrieved and returned.

"""

from copy import deepcopy

from model.api.game import Game
from model.api.league import League
from model.api.opponent import Opponent
from model.constants import GAMES, RANKINGS

def generate_games(league_id):
    """ Fetch and return all data necessary for a games list.

    Required:
    int league_id   id representing the League

    Return:
    dict            League and Games played in that League      

    {
        GAMES.PLAYED_IN: League which games were/are played in
        GAMES.GAMES: List of Games (with populated 'opponents')
    }

    """

    # Load games data from API.

    league = League.load_games(league_id) 

    # TODO: make it a depth-2 traversal. don't manually load opponents.
    
    # list of games that were loaded into league
    games = league.get_games()
   
    # iterating through this list is only temporary
    # because the multiload should have happened in the API
    game_ids = [g.id() for g in games]

    # load opponents for each game {g_id: Game}
    opponents_by_game = Game.multiload_opponents(game_ids)

    # manually add opponents to each game in the league object.
    games_list = []
    for g in games:
        opponents = opponents_by_game[g.id()].get_opponents()
        g.set_opponents(opponents_by_game[g.id()])

    # Prepare games data for handler.
    games_dict = {}
    games_dict[GAMES.PLAYED_IN] = league
    games_dict[GAMES.GAMES] = games

    return games_dict


def generate_rankings(league_id):
    """ Generate league rankings based on most wins.

    Required:
    id  league_id   League node id

    Return:
    dict            League, Sorted Opponents in League, and Sort Field
    
    {
        RANKED_IN   League that rankings occur in
        RANKS       Opponents sorted by Win Count
        SORT_FIELD  Field that Opponents are sorted by
    }

    """

    league = League.load_opponents(league_id)

    rankings_dict = {}
    rankings_dict[RANKINGS.RANKED_IN] = league
    rankings_dict[RANKINGS.SORT_FIELD] = "win_count"

    # leagues' opponents by Win Count
    opponents = deepcopy(league.get_opponents())
    opponents.sort(key = lambda x: x.win_count, reverse=True)
    rankings_dict[RANKINGS.RANKS] = opponents

    return rankings_dict


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

