#!/usr/bin/env python
""" Script: Regenerate Sample Graph

Implicitly, this is a composite unit test for:
    def Player.create_player(...)
    def League.create_league(...)
    def League.load_opponents(...)
    def Game.create_game(...)

"""

import league_gen
import schedule_gen

# LEAGUE, USERS, & PLAYERS CREATION
league = league_gen.initialize_league_with_players()

# GAME CREATION
schedule = schedule_gen.generate_schedule(league)
