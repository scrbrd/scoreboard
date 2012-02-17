"""
Catchers

...
"""

from model.api import League
from model.api import Opponent 


def generate_rankings(league_id):
    """ Generate league rankings based on most wins.

    Required:
    id  league_id  League node id

    Return:
    dict of name/wins tuples keyed on opponent id.

    """

    league = League.load_opponents(league_id)

    rankings = {}
    for opponent in league.get_opponents():
        rankings[opponent.id()] = (opponent.name(), opponent.count_wins())
    return rankings

