""" Module: rankings

...
"""
import logging
logger = logging.getLogger('boilerplate.' + __name__)

from model.app import catchers
from handlers.base import BaseHandler

class RankingsHandler(BaseHandler):
    
    """ Render Rankings Page. """
    
    def get(self):
        """ Overload BaseHandler's HTTP GET responder. """
        
        # FIXME - remove hardcoded league id
        league_id = 596

        # get ranking data from model
        rankings = catchers.RankingsCatcher(league_id) 

        # hand data over to view
        self.render("mobile/rankings.html", rankings=rankings)
        

