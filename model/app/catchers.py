"""
Catchers

...
"""

from model.api import League
from model.api import Opponent 


def generate_rankings(league_id):
    """
    
    """
    rankings = {}

    league = League.load_opponents(league_id)

    for opponent in league.get_opponents():
        rankings[opponent.id()] = opponent.count_wins()
    return rankings

