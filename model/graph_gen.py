#!/usr/bin/env python
""" Script: Regenerate Sample Graph

Implicitly, this is a composite unit test for:
    def Player.create_player(...)
    def League.create_league(...)
    def League.load_opponents(...)
    def Game.create_game(...)

"""

import random

from model.constants import PROPERTY_VALUE

from model.api.user import User
from model.api.league import League 
from model.api.game import Game

# CONSTANTS

NUMBER_OF_GAMES = 30

# XXX: add a new League name to the end of this list when generating a new
# graph so that test Leagues are uniquely named and more easily identifiable.
LEAGUE_NAMES = [
        "The Banana Stand",
        "Game of Thrones",
        "The Joy of Serving Others",
        ]


# USER/PLAYER CREATION

empty = PROPERTY_VALUE.EMPTY

users_and_players = [
        User.create_user_and_player(empty, empty, empty, "David",   "Wright"),
        User.create_user_and_player(empty, empty, empty, "Albert",  "Pujols"),
        User.create_user_and_player(empty, empty, empty, "Rafael",  "Nadal"),
        User.create_user_and_player(empty, empty, empty, "Lionel",  "Messi"),
        User.create_user_and_player(empty, empty, empty, "Michael", "Phelps"),
        User.create_user_and_player(empty, empty, empty, "Jeremy",  "Lin"),
        User.create_user_and_player(empty, empty, empty, "Bodie",   "Miller"),
        User.create_user_and_player(empty, empty, empty, "Magic",   "Johnson"),
        User.create_user_and_player(empty, empty, empty, "Charles", "Barkley"),
        User.create_user_and_player(empty, empty, empty, "Buster",  "Posey"),
        User.create_user_and_player(empty, empty, empty, "Rory",    "McIlroy"),
        User.create_user_and_player(empty, empty, empty, "Flozell", "Adams"),
        User.create_user_and_player(empty, empty, empty, "Tim",     "Tebow"),
        User.create_user_and_player(empty, empty, empty, "Wayne",   "Gretzky"),
        ]

user_ids = []
player_ids = []
for user, player in users_and_players:
    if user is not None:
        user_ids.append(user.id)
    if player is not None:
        player_ids.append(player.id)

print("{0} Users created successfully.".format(len(user_ids)))
print("{0} Players created successfully.".format(len(player_ids)))


# LEAGUE CREATION

league = League.create_league(
        LEAGUE_NAMES.pop(),
        random.choice(player_ids),
        player_ids)

if league is not None:
    print("League ({0}) created successfully.".format(league.id))


# GAME CREATION

# reload league just to make sure it works
league = League.load_opponents(league.id)
opponents = league.get_opponents()

opponent_ids = []
for opponent in opponents:
    opponent_ids.append(opponent.id)

games = []
for n in range(0, NUMBER_OF_GAMES):

    # randomly select a game creator
    creator_id = random.choice(opponent_ids)

    # TODO: swap "score" and "id" for JSON constants or member properties in a
    # Score/Outcome class.

    random.shuffle(opponent_ids)

    # randomly select 2 opponents and set the score
    outcome = [
            {"id" : opponent_ids[0], "score" : random.randint(0, 10)},
            {"id" : opponent_ids[1], "score" : random.randint(0, 10)},
            ]

    game = Game.create_game(league.id, creator_id, outcome)

    if game is not None:
        games.append(game)

print("{0} Games created successfully.".format(len(games)))

