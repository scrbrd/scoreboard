""" Module: rankings

...
"""
import logging
logger = logging.getLogger('boilerplate.' + __name__)

from model.constants import RANKINGS
from handlers.base import BaseHandler

# TODO use API classes
class Player(object):
    id = None
    name = None
    win_count = None
    def __init__(self, id, name, wins):
        self.id = id
        self.name = name
        self.win_count = wins

class League(object):
    id = None
    name = None
    def __init__(self, id, name):
        self.id = id
        self.name = name

#from model.app import catchers

class RankingsHandler(BaseHandler):
    
    """ Render Rankings Page. """
    
    def get(self):
        """ Overload BaseHandler's HTTP GET responder. """
        
        # TODO - remove hardcoded league id
        league_id = 24

        # get ranking data from model
        # TODO rankings_dict = catchers.generate_rankings(league_id) 
        rankings_dict = {}
        rankings_dict[RANKINGS.RANKED_IN] = League(24, "Basketball")
        rankings_dict[RANKINGS.SORT_FIELD] = "win_count"

        opponents = []
        opponents.append(Player(19, "Evan Hammer", 5))
        opponents.append(Player(20, "Jon Warman", 4))
        opponents.append(Player(23, "Bobby Kellogg", 3))
        opponents.append(Player(77, "Felix Grimm", 17))
        opponents.append(Player(76, "Asa Wildfire", 12))
        opponents.append(Player(75, "Captain Captain", 0))
        opponents.append(Player(74, "E. T.", 0))
        opponents.append(Player(72, "Jimmy Stewart", 6))
        opponents.append(Player(73, "Tom Greenwood", 10))
        opponents.append(Player(64, "Neil Armstrong", 45))
        opponents.append(Player(62, "Teddy Bearenstein", 16))
        opponents.append(Player(63, "Tommy O'Doyle", 5))

        opponents.sort(key = lambda x: x.win_count, reverse=True)
        rankings_dict[RANKINGS.RANKS] = opponents
        self.render("mobile/rankings.html", **rankings_dict)
        

