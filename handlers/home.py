import logging

from handlers.splash import SplashHandler
from handlers.rankings import RankingsHandler

logger = logging.getLogger('boilerplate.' + __name__)


class HomeHandler(SplashHandler, RankingsHandler):

    """ Determine if the user needs to see the Splash page or the Home page.
    
    Check for a logged in user and then route appropriately.

    """

    # NOT @tornado.web.authenticated so that it can handle unknown users
    # differently.
    def get(self):
        """ Handle GET request for the Home page. """
        
        # if the user is logged in then send him home.
        if self.current_user is not None:
            RankingsHandler.process_request(self)

        # TODO could check with facebook to see if the user's still logged in

        # if the user is not logged in then show him the Splash Page.
        else:
            SplashHandler.process_request(self)


