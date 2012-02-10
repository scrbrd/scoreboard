import logging

from handlers.base import BaseHandler

logger = logging.getLogger('boilerplate.' + __name__)


class SplashHandler(BaseHandler):

    """ Handle rendering the Splash page. """


    def get(self):
        """ Handle GET request for the Splash page. """
        self.process_request()


    def process_request(self):
        """ Render Splash page. """
        # TODO: turn this hardcoded file path into a constant
        self.render("mobile/splash.html")

