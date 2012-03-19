""" Data Request Catchers

All data requests are processed by request type and the appropriate
data is retrieved and returned.

"""

from model.api.game import Game
from model.api.league import League
from model.api.opponent import Opponent
from model.constants import GAMES, RANKINGS

def generate_games(league_id):
    """ Fetch and return all data necessary for a games list.

    Required:
    int league_id   id representing the League

    Return:
    GAMES.PLAYED_IN     League which games were/are played in
    GAMES.GAMES         List of Games (with populated 'opponents')

    """

    # Load games data from API.
    
    league = League.load_games(league_id) 

    # TODO: make it a depth-2 traversal. don't manually load opponents.
    games = league.get_games()
    game_ids = games.keys()
    
    opponents_by_game = Game.multiload_opponents(game_ids)

    # add opponents to each game and add that game to the return list.
    games_list = []
    for g_id in game_ids:
        games[g_id].set_opponents(opponents_by_game[g_id])
        games_list.append(games[g_id])

    # Prepare games data for handler.
    games_dict = {}
    games_dict[GAMES.PLAYED_IN] = league
    games_dict[GAMES.GAMES] = games

# TODO figure out if the operations below are needed.
#    for g_id, game in league.get_games():
#        opponents_dict = {}
#
#        # {opponent_id: score}
#        scores_dict = game.outcome()
#
#        # list of Opponents
#        opponents = game.get_opponents()
#
#        for o_id, opponent in opponents:
#            opponents_dict[o_id] = (o.name(), scores_dict[o_id])
#
#        games_dict[g_id] = opponents_return_dict

    return games_dict


def generate_rankings(league_id):
    """ Generate league rankings based on most wins.

    Required:
    id  league_id   League node id

    Return dict:
    RANKED_IN   League that rankings occur in
    RANKS       Opponents sorted by Win Count
    SORT_FIELD  Field that Opponents are sorted by

    """

    league = League.load_opponents(league_id)

    rankings_dict = {}
    rankings_dict[RANKINGS.RANKED_IN] = league
    rankings_dict[RANKINGS.SORT_FIELD] = "win_count"

    # leagues' opponents by Win Count
    opponents_dict = league.get_opponents()
    opponents = [o for o in opponents_dict.values()]
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

