""" Module: rankings

...
"""
import logging
logger = logging.getLogger('boilerplate.' + __name__)

from handlers.base import BaseHandler

# TODO put this class in the catcher
class Player(object):
    id = None
    name = None
    wins = None
    def __init__(self, id, name, wins):
        self.id = id
        self.name = name
        self.wins = wins

#from model.app import catchers

class RankingsHandler(BaseHandler):
    
    """ Render Rankings Page. """
    
    def get(self):
        """ Overload BaseHandler's HTTP GET responder. """
        
        # TODO - remove hardcoded league id
        league_id = 24

        # get ranking data from model
        # TODO rankings_dict = catchers.generate_rankings(league_id) 
        rankings = []
        
        rankings.append(Player(19, "Evan Hammer", 5))
        rankings.append(Player(20, "Jon Warman", 2))
        rankings.append(Player(23, "Bobby Kellogg", 0))

        keywords_dict = {"players": rankings}
        self.render("rankings.html", **keywords_dict)
