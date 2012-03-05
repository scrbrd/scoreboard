from handlers.splash import SplashHandler
from handlers.games import GamesHandler
from handlers.rankings import RankingsHandler

url_patterns = [
    (r"/", SplashHandler),
    (r"/games", GamesHandler),
    (r"/rankings", RankingsHandler),
]
