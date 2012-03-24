#!/usr/bin/env python
""" Script: Regenerate Sample Graph

...
"""
import random
from copy import copy

from model.api.constants import NODE_TYPE, EDGE_TYPE
from model.api import editor, loader
from model.api.game import Game

# CONSTANTS
NUMBER_OF_GAMES = 30


# LEAGUE CREATION
proto = editor.prototype_node(NODE_TYPE.LEAGUE, {"name": "The Banana Stand"})
league = editor.create_node_and_edges(proto, [])

print("League ({0}) created successfully.".format(league.id))


# PLAYER CREATION
players = []
players.append({"first_name": "Jon", "last_name": "Warman"})
players.append({"first_name": "Bobby", "last_name": "Kellogg"})
players.append({"first_name": "Evan", "last_name": "Hammer"})
players.append({"first_name": "Bryan", "last_name": "Smokey"})
players.append({"first_name": "Tom", "last_name": "Greenwood"})
players.append({"first_name": "Tom", "last_name": "Grant"})
players.append({"first_name": "Zaphod", "last_name": "Beeblebrox"})
players.append({"first_name": "Blue", "last_name": "Steel"})
players.append({"first_name": "Jennifer", "last_name": "Clone"})
players.append({"first_name": "Melissa", "last_name": "Merrill"})
players.append({"first_name": "Rachael", "last_name": "Rosen"})
players.append({"first_name": "Alia", "last_name": "Atreides"})
players.append({"first_name": "Asa", "last_name": "Wildfire"})
players.append({"first_name": "Jeremy", "last_name": "Lin"})
players.append({"first_name": "Corduroy", "last_name": "Jackson"})

for p in players:
    protoplayer = editor.prototype_node(
            NODE_TYPE.PLAYER, 
            p)
    protoedge = editor.prototype_edge_and_complement(
            EDGE_TYPE.IN_LEAGUE, 
            {}, 
            league.id)
    r = editor.create_node_and_edges(protoplayer, protoedge)

print("{0} Players created successfully.".format(len(players)))


# GAME CREATION

# get updated league
league = loader.load_node(league.id)

# get all opponent ids
opp_ids = []
for e in league.get_edges().get(EDGE_TYPE.HAS_LEAGUE_MEMBER, {}).values():
    opp_ids.append(e.to_node_id)

for n in range(0, NUMBER_OF_GAMES):
    
    temp_opps = copy(opp_ids)
    
    # get 2 random opponents and a random creator
    opp1 = random.choice(temp_opps)
    temp_opps.remove(opp1)
    opp2 = random.choice(temp_opps)
    creator = random.choice(opp_ids)

    # give them a score (0-20)
    score1 = random.randint(0, 10)
    score2 = random.randint(0, 10)

    # create game
    Game.create_game(
            league.id, 
            creator, 
            [(opp1, score1), (opp2, score2)])

print("{0} Games created successfully.".format(NUMBER_OF_GAMES))

