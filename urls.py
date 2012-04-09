from handlers.splash import SplashHandler
from handlers.games import GamesHandler
from handlers.rankings import RankingsHandler
from handlers.dialog import CreateGameDialogHandler

# FIXME delete this handler
from handlers.test import TestHandler

url_patterns = [
    (r"/", SplashHandler),
    (r"/games", GamesHandler),
    (r"/rankings", RankingsHandler),
    (r"/dialog-create-game", CreateGameDialogHandler),
    (r"/test(.*)", TestHandler),
]
