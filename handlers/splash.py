from handlers.base import BaseHandler

import logging
logger = logging.getLogger('boilerplate.' + __name__)


class SplashHandler(BaseHandler):
    def get(self):
        self.render("splash.html")
