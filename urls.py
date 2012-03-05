from handlers import SplashHandler, GamesHandler, RankingsHandler

url_patterns = [
    (r"/", SplashHandler),
    (r"/games", GamesHandler),
    (r"/rankings", RankingsHandler),
]
