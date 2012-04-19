from handlers.splash import SplashHandler
from handlers.games import GamesHandler
from handlers.rankings import RankingsHandler
from handlers.create import CreateGameHandler

url_patterns = [
    (r"/", SplashHandler),
    (r"/games", GamesHandler),
    (r"/rankings", RankingsHandler),
    (r"/create/game", CreateGameHandler),
]
