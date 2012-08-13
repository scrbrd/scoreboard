""" Script: Generation Environment """

# SET UP ENVIRONMENT
import os

os.environ["NEO4J_HOST"] = "f7e1861b3.hosted.neo4j.org"
os.environ["NEO4J_PORT"] = "7134"
os.environ["NEO4J_LOGIN"] = "1dd76643b"
os.environ["NEO4J_PASSWORD"] = "919115168"


# CONSTANTS
NUMBER_OF_GAMES = 4
NUMBER_OF_PLAYER_SETS = 1
LEAGUE_NAME = "Lake Owego"


# USER/PLAYER CREATION
first_name_field = "first_name"
last_name_field = "last_name"
player_templates = []
for n in range(0, NUMBER_OF_PLAYER_SETS):
    new_players = [
            {first_name_field: "Dan", last_name_field: "Sinnreich"},
            {first_name_field: "Tom", last_name_field: "Greenwoord"},
            {first_name_field: "Roophy", last_name_field: "Roy"},
            {first_name_field: "Jason", last_name_field: "White"},
            ]
    player_templates.extend(new_players)


#
