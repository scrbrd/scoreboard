from handlers.home import HomeHandler
from handlers.login import LoginHandler
from handlers.games import GamesHandler
from handlers.rankings import RankingsHandler
from handlers.create import CreateGameHandler

url_patterns = [
    (r"/", HomeHandler),
    (r"/login", LoginHandler),
    (r"/games", GamesHandler),
    (r"/rankings", RankingsHandler),
    (r"/create/game", CreateGameHandler),
]
