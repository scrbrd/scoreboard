""" Module: rankings

...
"""
import logging
logger = logging.getLogger('boilerplate.' + __name__)

from model.const import RANKINGS
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
        opponents.append(Player(20, "Jon Warman", 12))
        opponents.append(Player(23, "Bobby Kellogg", 0))

        rankings_dict[RANKINGS.RANKS] = opponents
        self.render("mobile/rankings.html", **rankings_dict)
        

