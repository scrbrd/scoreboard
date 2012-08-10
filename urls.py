from handlers.home import HomeHandler
from handlers.login import LoginHandler
from handlers.league import LeagueHandler
from handlers.games import GamesHandler
from handlers.rankings import RankingsHandler
from handlers.create import CreateGameHandler
from handlers.comment import CommentHandler
from handlers.dialog import CreateGameDialogHandler

url_patterns = [
    (r"/", HomeHandler),
    (r"/login", LoginHandler),
    (r"/league", LeagueHandler),
    (r"/games", GamesHandler),
    (r"/rankings", RankingsHandler),
    (r"/create/game", CreateGameHandler),
    (r"/comment", CommentHandler),
    (r"/dialog/creategame", CreateGameDialogHandler),
]
