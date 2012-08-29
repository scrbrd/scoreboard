from handlers.home import HomeHandler
from handlers.login import LoginHandler
from handlers.league import LeagueHandler
from handlers.create import CreateGameHandler
from handlers.comment import CommentHandler

url_patterns = [
    (r"/", HomeHandler),
    (r"/login", LoginHandler),
    (r"/league", LeagueHandler),
    (r"/league/([0-9]+)", LeagueHandler),
    (r"/create/game", CreateGameHandler),
    (r"/comment", CommentHandler),
]
