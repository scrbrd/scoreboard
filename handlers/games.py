""" Module: games

...
"""
import logging

from handlers.base import BaseHandler

from model.app import catchers

# TODO figure out how logging works
logger = logging.getLogger('boilerplate.' + __name__)


class GamesHandler(BaseHandler):
   
    """ Render Games List Page. """

    def get(self):
        """ Overload BaseHandler's HTTP GET responder. """

        # FIXME remove hardcoded league id
        league_id = 596
        
        # get games data from model
        games = catchers.GamesCatcher(league_id)
        
        # hand data over to view and render
        self.render("mobile/games.html", games=games)
