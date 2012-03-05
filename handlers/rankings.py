""" Module: rankings

...
"""
import logging
logger = logging.getLogger('boilerplate.' + __name__)

from handlers.base import BaseHandler

from model.app import catchers

class RankingsHandler(BaseHandler):
    
    """ Render Rankings Page. """
    
    def get(self):
        """ Overload BaseHandler's HTTP GET responder. """
        
        # TODO - remove hardcoded league id
        league_id = 24

        # get ranking data from model
        rankings_dict = catchers.generate_rankings(league_id) 
        self.render("ranking.html", **rankings_dict)
