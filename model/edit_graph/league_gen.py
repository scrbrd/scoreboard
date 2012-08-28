#!/usr/bin/env python
""" Script: Generate Sample League with Players

Implicitly, this is a composite unit test for:
    def Player.create_player(...)
    def League.create_league(...)
    def League.load_opponents(...)

"""

# IMPORTS
import random

import gen_environment

from model.constants import PROPERTY_VALUE

from model.api.user import User
from model.api.league import League


def generate_players(player_templates_list):
    user_player_tuples = []
    for p in player_templates_list:

        email = PROPERTY_VALUE.EMPTY
        password_hash = PROPERTY_VALUE.EMPTY
        referrer_url = PROPERTY_VALUE.EMPTY
        first_name = p['first_name']
        last_name = p['last_name']

        user_player_tuples.append(
                User.create_user_and_player(
                        email,
                        password_hash,
                        referrer_url,
                        first_name,
                        last_name))
    users = [user for user, player in user_player_tuples]
    players = [player for user, player in user_player_tuples]

    print("{0} Users created successfully.".format(len(users)))
    print("{0} Players created successfully.".format(len(players)))

    return (users, players)


def generate_league(league_name, players):
    player_ids = [p.id for p in players]
    if not player_ids:
        player_ids.append(95)
    league = League.create_league(
            league_name,
            random.choice(player_ids),
            player_ids)

    loaded_league = League.load_opponents(league.id)
    if loaded_league is not None:
        print("League ({0}) created successfully.".format(loaded_league.id))

    return loaded_league


def initialize_league_with_players():
    player_templates = gen_environment.player_templates
    (users, players) = generate_players(player_templates)


    # LEAGUE CREATION
    league_name = gen_environment.LEAGUE_NAME
    league = generate_league(league_name, players)

    return league

if __name__ == "__main__":
    initialize_league_with_players()
