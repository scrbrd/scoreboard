""" Module: landing

"""

from handlers.base import BaseHandler


class LandingHandler(BaseHandler):

    """ Handle rendering the Landing page. """

    # explicitly NOT tornado.web.authenticated because anybody can see this.
    def get(self):
        """ Handle GET request for the Landing page. """
        self.process_request()


    def process_request(self):
        """ Render Landing page. """
        # TODO: turn this hardcoded file path into a constant
        self.render("mobile/landing.html")
