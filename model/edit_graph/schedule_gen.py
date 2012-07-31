#!/usr/bin/env python
""" Script: Generate Games for a League

Implicitly, this is a composite unit test for:
    def Game.create_game(...)

"""
import sys
import random

import gen_environment

from model.api.league import League
from model.api.game import Game


def generate_schedule(league):
    opponents = league.get_opponents()

    opponent_ids = [o.id for o in opponents]

    games = []
    number_of_games = gen_environment.NUMBER_OF_GAMES
    half_of_games = number_of_games / 2

    for n in range(0, half_of_games):
        games.append(generate_friendly_game(league.id, opponent_ids))

    for n in range(0, number_of_games - half_of_games):
        games.append(generate_competitive_game(league.id, opponent_ids))

    print("{0} Games created successfully.".format(len(games)))


def _prepare_game_creation(opponent_ids):
    # randomly select a game creator
    creator_id = random.choice(opponent_ids)
    random.shuffle(opponent_ids)

    return (creator_id, opponent_ids)


def _create_game(league_id, creator_id, results):
    # randomly select 2 opponents and set the score
    return Game.create_game(league_id, creator_id, results)


def _prepare_result(opponent_ids, type):
    results = {}
    for id in opponent_ids:
        results[id] = {"result": type}

    return results


def generate_friendly_game(league_id, opponent_ids):
    played = "played"
    number_of_players = random.randint(1, 5)

    (creator_id, opponent_ids) = _prepare_game_creation(opponent_ids)

    played_ids = [opponent_ids[n] for n in range(0, number_of_players)]
    results = _prepare_result(played_ids, played)

    return _create_game(league_id, creator_id, results)


def generate_competitive_game(league_id, opponent_ids):
    won = "won"
    lost = "lost"
    number_of_winners = random.randint(1, 4)
    number_of_losers = random.randint(1, 4)

    (creator_id, opponent_ids) = _prepare_game_creation(opponent_ids)

    won_ids = [opponent_ids[n] for n in range(0, number_of_winners)]
    lost_ids = [opponent_ids[n] for n in range(
            number_of_winners, number_of_winners + number_of_losers)]

    won_results = _prepare_result(won_ids, won)
    lost_results = _prepare_result(lost_ids, lost)
    results = dict(won_results.items() + lost_results.items())
    return _create_game(league_id, creator_id, results)


if __name__ == "__main__":
    league_id = int(sys.argv[1])
    print "Creating schedule for League {0}.".format(league_id)
    league = League.load_opponents(league_id)
    schedule = generate_schedule(league)
