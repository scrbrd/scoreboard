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
    
    Any tab or read request handler should subclass from this handler.

    """

    @tornado.web.authenticated
    def get(self):
        """ Overload BaseHandler's HTTP GET responder. """
        self.process_request()


