#!/usr/bin/env python
""" Script: Regenerate Sample Graph

Implicitly, this is a composite unit test for:
    def Player.create_player(...)
    def League.create_league(...)
    def League.load_opponents(...)
    def Game.create_game(...)

"""
# SET UP ENVIRONMENT
import os

os.environ["NEO4J_HOST"] = "f7e1861b3.hosted.neo4j.org"
os.environ["NEO4J_PORT"] = "7134"
os.environ["NEO4J_LOGIN"] = "1dd76643b"
os.environ["NEO4J_PASSWORD"] = "919115168"


# OTHER IMPORTS
import random

from model.constants import PROPERTY_VALUE

from model.api.user import User
from model.api.league import League
from model.api.game import Game

# CONSTANTS

NUMBER_OF_GAMES = 10
NUMBER_OF_PLAYER_SETS = 1

# XXX: add a new League name to the end of this list when generating a new
# graph so that test Leagues are uniquely named and more easily identifiable.
#LEAGUE_NAME = "The Banana Stand"
#LEAGUE_NAME = "Game of Thrones"
#LEAGUE_NAME = "The Joy of Serving Others"
LEAGUE_NAME = "SPORTS!"

timer_start = os.times()[4]

# USER/PLAYER CREATION

empty = PROPERTY_VALUE.EMPTY

users_and_players = []
for n in range(0, NUMBER_OF_PLAYER_SETS):
    new_players = [
            User.create_user_and_player(empty, empty, empty, "David", "Wright"),
            User.create_user_and_player(empty, empty, empty, "Rafael", "Nadal"),
            User.create_user_and_player(empty, empty, empty, "Michael", "Phelps"),
            User.create_user_and_player(empty, empty, empty, "Jeremy", "Lin"),
            User.create_user_and_player(empty, empty, empty, "Magic", "Johnson"),
            User.create_user_and_player(empty, empty, empty, "Charles", "Barkley"),
            User.create_user_and_player(empty, empty, empty, "Buster", "Posey"),
            User.create_user_and_player(empty, empty, empty, "Doc", "Brown"),
            User.create_user_and_player(empty, empty, empty, "Flozell", "Adams"),
            User.create_user_and_player(empty, empty, empty, "Wayne", "Gretzky"),
            ]
    users_and_players.extend(new_players)

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
        LEAGUE_NAME,
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

results_type = ["competitive", "friendly"]

games = []
for n in range(0, NUMBER_OF_GAMES):

    # randomly select a game creator
    creator_id = random.choice(opponent_ids)

    random.shuffle(opponent_ids)

    # figure out results
    random.shuffle(results_type)
    first = "won"
    second = "lost"
    if results_type[0] == "friendly":
        first = "played"
        second = "played"

    # randomly select 2 opponents and set the score
    results = {
            opponent_ids[0]: {"result": first},
            opponent_ids[1]: {"result": second}
            }

    game = Game.create_game(league.id, creator_id, results)

    if game is not None:
        games.append(game)

print("{0} Games created successfully.".format(len(games)))

timer_end = os.times()[4]

print("THE OVERALL TIME is: {0}s".format(timer_end - timer_start))
