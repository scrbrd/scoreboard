""" Module: rankings

...
"""
import logging

from handlers.base import BaseHandler

from model.app import catchers

# TODO figure out how logging works
logger = logging.getLogger('boilerplate.' + __name__)


class RankingsHandler(BaseHandler):
    
    """ Render Rankings Page. """
    
    def get(self):
        """ Overload BaseHandler's HTTP GET responder. """
        
        # FIXME - remove hardcoded league id
        league_id = 596

        # get ranking data from model
        rankings = catchers.RankingsCatcher(league_id) 

        # hand data over to view and render
        self.render("mobile/rankings.html", rankings=rankings)
        

