""" Data Request Catchers

All data requests are processed by request type and the appropriate
data is retrieved and returned.

"""

from model.api.game import Game
from model.api.league import League
from model.api.opponent import Opponent

def generate_games(league_id):
    """ Fetch and return all data necessary for a games list.

    Required:
    int league_id   id representing the League

    Return:
    {game_id: {opponent_id: (name, score)}}

    """
    
    # Load all needed data
    league = League.load_games(league_id) 
    league_games = league.get_games()
    Game.multiload_opponents(league_games)

    games_dict = {}

    # Process all data
    for g in league_games:
        opponents_return_dict = {}
        game_id = g.id
        # {opponent_id: score}
        scores_dict = g.outcome()
        # list of Opponents
        opponents = g.get_opponents()
        for o in opponents:
            opponents_return_dict[o.id] = (o.name(), scores_dict[id])
        games_dict[game_id] = opponents_return_dict

    return games_dict

def generate_rankings(league_id):
    """ Generate league rankings based on most wins.

    Required:
    id  league_id  League node id

    Return:
    dict of name/wins tuples keyed on opponent id.

    """

    league = League.load_opponents(league_id)

    rankings_dict = {}
    
    for opponent in league.get_opponents():
        rankings_dict[opponent.id()] = (opponent.name(), opponent.count_wins())
    
    return rankings_dict

def create_game(league_id, creator_id, opponent_score_pairs):
    """ Create a game and return it.

    Required:
    id league_id                league id that game belogs to
    id creator_id               player id of game's creator
    list opponent_score_pairs   tuples of opponent ids and score
    
    Return the created game.

    """
    new_game = Game.create_game(league_id, creator_id, opponent_score_pairs)
    return new_game

