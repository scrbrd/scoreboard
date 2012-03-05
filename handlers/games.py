from handlers.base import BaseHandler

import logging
logger = logging.getLogger('boilerplate.' + __name__)


class GamesHandler(BaseHandler):
    def get(self):
        self.render("games.html")
