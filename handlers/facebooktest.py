from handlers.base import BaseHandler

import logging
logger = logging.getLogger('boilerplate.' + __name__)


class FacebookTestHandler(BaseHandler):
    def get(self):
        self.render("facebooktest.html")
