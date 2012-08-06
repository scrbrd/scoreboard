""" Module: sports

Sports!

"""

from util.decorators import sport


class _SportID(object):

    @sport
    def BASKETBALL(self):
        return "basketball"

    @sport
    def SOCCER(self):
        return "soccer"

    @sport
    def HOCKEY(self):
        return "hockey"

    @sport
    def FOOTBALL(self):
        return "football"

    @sport
    def BASEBALL(self):
        return "baseball"

    @sport
    def SOFTBALL(self):
        return "softball"

    @sport
    def WIFFLEBALL(self):
        return "wiffleball"

    @sport
    def PING_PONG(self):
        return "ping_pong"

    @sport
    def BOWLING(self):
        return "bowling"

    @sport
    def GOLF(self):
        return "golf"

    @sport
    def MINI_GOLF(self):
        return "mini_golf"

    @sport
    def ULTIMATE_FRISBEE(self):
        return "ultimate_frisbee"

    @sport
    def BOARD_GAMES(self):
        return "board_games"

    @sport
    def CHESS(self):
        return "chess"

    @sport
    def SURFING(self):
        return "surfing"

    @sport
    def BOXING(self):
        return "boxing"

    @sport
    def BOCCE(self):
        return "bocce"

    @sport
    def SKEEBALL(self):
        return "skeeball"

    @sport
    def FOOSBALL(self):
        return "foosball"

    @sport
    def AIR_HOCKEY(self):
        return "air_hockey"

    @sport
    def SHUFFLEBOARD(self):
        return "shuffleboard"

    @sport
    def BEER_PONG(self):
        return "beer_pong"

    @sport
    def POOL(self):
        return "pool"

    @sport
    def DARTS(self):
        return "darts"

    @sport
    def TENNIS(self):
        return "tennis"

    @sport
    def VOLLEYBALL(self):
        return "volleyball"

    @sport
    def RUNNING(self):
        return "running"

    @sport
    def CYCLING(self):
        return "cycling"

    @sport
    def SWIMMING(self):
        return "swimming"

    @sport
    def HANDBALL(self):
        return "handball"


SPORT_ID = _SportID()


class _Sport(object):

    @sport
    def BASKETBALL(self):
        return "Basketball"

    @sport
    def SOCCER(self):
        return "Soccer"

    @sport
    def HOCKEY(self):
        return "Hockey"

    @sport
    def FOOTBALL(self):
        return "Football"

    @sport
    def BASEBALL(self):
        return "Baseball"

    @sport
    def SOFTBALL(self):
        return "Softball"

    @sport
    def WIFFLEBALL(self):
        return "Wiffleball"

    @sport
    def PING_PONG(self):
        return "Ping Pong"

    @sport
    def BOWLING(self):
        return "Bowling"

    @sport
    def GOLF(self):
        return "Golf"

    @sport
    def MINI_GOLF(self):
        return "Mini Golf"

    @sport
    def ULTIMATE_FRISBEE(self):
        return "Ultimate Frisbee"

    @sport
    def BOARD_GAMES(self):
        return "Board Games"

    @sport
    def CHESS(self):
        return "Chess"

    @sport
    def SURFING(self):
        return "Surfing"

    @sport
    def BOXING(self):
        return "Boxing"

    @sport
    def BOCCE(self):
        return "Bocce"

    @sport
    def SKEEBALL(self):
        return "Skeeball"

    @sport
    def FOOSBALL(self):
        return "Foosball"

    @sport
    def AIR_HOCKEY(self):
        return "Air Hockey"

    @sport
    def SHUFFLEBOARD(self):
        return "Shuffleboard"

    @sport
    def BEER_PONG(self):
        return "Beer Pong"

    @sport
    def POOL(self):
        return "Pool"

    @sport
    def DARTS(self):
        return "Darts"

    @sport
    def TENNIS(self):
        return "Tennis"

    @sport
    def VOLLEYBALL(self):
        return "Volleyball"

    @sport
    def RUNNING(self):
        return "Running"

    @sport
    def CYCLING(self):
        return "Cycling"

    @sport
    def SWIMMING(self):
        return "Swimming"

    @sport
    def HANDBALL(self):
        return "Handball"

    @sport
    def ALL(self):
        return {
                SPORT_ID.BASKETBALL: self.BASKETBALL,
                SPORT_ID.SOCCER: self.SOCCER,
                SPORT_ID.HOCKEY: self.HOCKEY,
                SPORT_ID.FOOTBALL: self.FOOTBALL,
                SPORT_ID.BASEBALL: self.BASEBALL,
                SPORT_ID.SOFTBALL: self.SOFTBALL,
                SPORT_ID.WIFFLEBALL: self.WIFFLEBALL,
                SPORT_ID.PING_PONG: self.PING_PONG,
                SPORT_ID.BOWLING: self.BOWLING,
                SPORT_ID.GOLF: self.GOLF,
                SPORT_ID.MINI_GOLF: self.MINI_GOLF,
                SPORT_ID.ULTIMATE_FRISBEE: self.ULTIMATE_FRISBEE,
                SPORT_ID.BOARD_GAMES: self.BOARD_GAMES,
                SPORT_ID.CHESS: self.CHESS,
                SPORT_ID.SURFING: self.SURFING,
                SPORT_ID.BOXING: self.BOXING,
                SPORT_ID.BOCCE: self.BOCCE,
                SPORT_ID.SKEEBALL: self.SKEEBALL,
                SPORT_ID.FOOSBALL: self.FOOSBALL,
                SPORT_ID.AIR_HOCKEY: self.AIR_HOCKEY,
                SPORT_ID.SHUFFLEBOARD: self.SHUFFLEBOARD,
                SPORT_ID.BEER_PONG: self.BEER_PONG,
                SPORT_ID.POOL: self.POOL,
                SPORT_ID.DARTS: self.DARTS,
                SPORT_ID.TENNIS: self.TENNIS,
                SPORT_ID.VOLLEYBALL: self.VOLLEYBALL,
                SPORT_ID.RUNNING: self.RUNNING,
                SPORT_ID.CYCLING: self.CYCLING,
                SPORT_ID.SWIMMING: self.SWIMMING,
                SPORT_ID.HANDBALL: self.HANDBALL,
                }

SPORT = _Sport()
