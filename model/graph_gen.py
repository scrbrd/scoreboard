#!/usr/bin/env python
""" Script: Regenerate Sample Graph

...
"""
import random
from copy import copy

from model.api.constants import NODE_TYPE, EDGE_TYPE
from model.api.constants import NODE_PROPERTY, EDGE_PROPERTY

from model.api import editor, loader
from model.api.game import Game

# CONSTANTS
NUMBER_OF_GAMES = 30


# LEAGUE CREATION
# TODO: there should be a static League function for prototyping a League
proto = editor.prototype_node(
        NODE_TYPE.LEAGUE,
        {NODE_PROPERTY.NAME: "The Banana Stand"})
league = editor.create_node_and_edges(proto, [])

print("League ({0}) created successfully.".format(league.id))


# PLAYER CREATION
players = []
players.append({NODE_PROPERTY.FIRST_NAME: "Jon",        NODE_PROPERTY.LAST_NAME: "Warman"})
players.append({NODE_PROPERTY.FIRST_NAME: "Bobby",      NODE_PROPERTY.LAST_NAME: "Kellogg"})
players.append({NODE_PROPERTY.FIRST_NAME: "Evan",       NODE_PROPERTY.LAST_NAME: "Hammer"})
players.append({NODE_PROPERTY.FIRST_NAME: "Leigh",      NODE_PROPERTY.LAST_NAME: "Salem"})
players.append({NODE_PROPERTY.FIRST_NAME: "Tom",        NODE_PROPERTY.LAST_NAME: "Greenwood"})
players.append({NODE_PROPERTY.FIRST_NAME: "Tom",        NODE_PROPERTY.LAST_NAME: "Grant"})
players.append({NODE_PROPERTY.FIRST_NAME: "Zaphod",     NODE_PROPERTY.LAST_NAME: "Beeblebrox"})
players.append({NODE_PROPERTY.FIRST_NAME: "Blue",       NODE_PROPERTY.LAST_NAME: "Steel"})
players.append({NODE_PROPERTY.FIRST_NAME: "Jennifer",   NODE_PROPERTY.LAST_NAME: "Clone"})
players.append({NODE_PROPERTY.FIRST_NAME: "Melissa",    NODE_PROPERTY.LAST_NAME: "Merrill"})
players.append({NODE_PROPERTY.FIRST_NAME: "Rachael",    NODE_PROPERTY.LAST_NAME: "Rosen"})
players.append({NODE_PROPERTY.FIRST_NAME: "Eric",       NODE_PROPERTY.LAST_NAME: "Cartman"})
players.append({NODE_PROPERTY.FIRST_NAME: "Barack",     NODE_PROPERTY.LAST_NAME: "Obama"})
players.append({NODE_PROPERTY.FIRST_NAME: "Jeremy",     NODE_PROPERTY.LAST_NAME: "Lin"})
players.append({NODE_PROPERTY.FIRST_NAME: "Action",     NODE_PROPERTY.LAST_NAME: "Jackson"})

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
    # TODO: come up with constants for JSON and/or codify Score in an object
    Game.create_game(
            league.id, 
            creator, 
            [{"id" : opp1, "score" : score1}, {"id" : opp2, "score" : score2}])

print("{0} Games created successfully.".format(NUMBER_OF_GAMES))

