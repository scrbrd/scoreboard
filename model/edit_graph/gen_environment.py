""" Script: Generation Environment """

# SET UP ENVIRONMENT
import os

os.environ["NEO4J_HOST"] = "f7e1861b3.hosted.neo4j.org"
os.environ["NEO4J_PORT"] = "7134"
os.environ["NEO4J_LOGIN"] = "1dd76643b"
os.environ["NEO4J_PASSWORD"] = "919115168"


# CONSTANTS
NUMBER_OF_GAMES = 10
NUMBER_OF_PLAYER_SETS = 1
LEAGUE_NAME = "Lake Owego"


# USER/PLAYER CREATION
first_name_field = "first_name"
last_name_field = "last_name"
player_templates = []
for n in range(0, NUMBER_OF_PLAYER_SETS):
    new_players = [
            {first_name_field: "David", last_name_field: "Wright"},
            {first_name_field: "Rafael", last_name_field: "Nadal"},
            {first_name_field: "Michael", last_name_field: "Phelps"},
            {first_name_field: "Jeremy", last_name_field: "Lin"},
            {first_name_field: "Magic", last_name_field: "Johnson"},
            {first_name_field: "Charles", last_name_field: "Barkley"},
            {first_name_field: "Buster", last_name_field: "Posey"},
            {first_name_field: "Doc", last_name_field: "Brown"},
            {first_name_field: "Flozell", last_name_field: "Adams"},
            {first_name_field: "Wayne", last_name_field: "Gretzky"},
            ]
    player_templates.extend(new_players)


#
