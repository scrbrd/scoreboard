#!/usr/bin/env python
""" Script: Run Temp Test for Model

...
"""

from model.app import catchers

def test1():
    gameslist = catchers.GamesCatcher(526)
    outcomes = gameslist.get_outcomes_by_game()
    games = gameslist.games
    league = gameslist.context_container

    print("League ({0}): {1}".format(league.id, league.name))

    for g in games:
        print("Game {0}:".format(g.id))
        
        outcome = outcomes[g.id]
        for result in outcome:
            score = result[0]
            opp = result[1]
            print("Score: {0}, Opp: {1}".format(score, opp.name))

def test2():
    from model.api import game, loader
    from model.api.constants import EDGE_TYPE

    g = loader.load_node(543)
    print "Game loaded: {0}".format(g.id)

    print g.get_edges()[EDGE_TYPE.WON_BY].values()[0].properties()

test1()
