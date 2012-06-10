import logging

from handlers.base import BaseHandler

logger = logging.getLogger('boilerplate.' + __name__)


class LandingHandler(BaseHandler):

    """ Handle rendering the Landing page. """

    # NOT tornado.web.authenticated because anybody can see Splash.
    def get(self):
        """ Handle GET request for the Landing page. """
        self.process_request()


    def process_request(self):
        """ Render Landing page. """
        # TODO: turn this hardcoded file path into a constant
        self.render("mobile/landing.html")
