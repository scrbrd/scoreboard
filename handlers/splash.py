from handlers.base import BaseHandler

import logging
logger = logging.getLogger('boilerplate.' + __name__)


class SplashHandler(BaseHandler):
    def get(self):
        # TODO: turn this hardcoded file path into a constant
        self.render("mobile/splash.html")
