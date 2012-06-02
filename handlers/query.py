""" Module: query

...
"""
import logging

import tornado.web
from handlers.base import BaseHandler

# TODO figure out how logging works
logger = logging.getLogger('boilerplate.' + __name__)


class QueryHandler(BaseHandler):

    """ Encapsulates all generic query functionality.

    Any read or write request handler should subclass from this handler.

    """

    @tornado.web.authenticated
    def get(self):
        """ Overload BaseHandler's HTTP GET responder for reads. """
        self.process_request()


    @tornado.web.authenticated
    def post(self):
        """ Overload BaseHandler's HTTP GET responder for reads. """
        self.process_request()
