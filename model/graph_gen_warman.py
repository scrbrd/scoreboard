#!/usr/bin/env python
""" Script: Regenerate Sample Graph

...
"""
import random
from copy import copy

from model.constants import NODE_PROPERTY, EDGE_PROPERTY
from model.api.constants import API_NODE_TYPE, API_EDGE_TYPE
from model.api.constants import API_NODE_PROPERTY, API_EDGE_PROPERTY

from model.api import editor, loader
from model.api.game import Game

# CONSTANTS
NUMBER_OF_GAMES = 10


# LEAGUE CREATION
# TODO: there should be a static League function for prototyping a League
proto = editor.prototype_node(
        API_NODE_TYPE.LEAGUE,
        {API_NODE_PROPERTY.NAME: "Game of Thrones"})
league = editor.create_node_and_edges(proto, [])

print("League ({0}) created successfully.".format(league.id))


# PLAYER CREATION
players = []
players.append({
    API_NODE_PROPERTY.FIRST_NAME: "David",
    API_NODE_PROPERTY.LAST_NAME: "Wright"})
players.append({
    API_NODE_PROPERTY.FIRST_NAME: "Albert",
    API_NODE_PROPERTY.LAST_NAME: "Pujols"})
players.append({
    API_NODE_PROPERTY.FIRST_NAME: "Rafael",
    API_NODE_PROPERTY.LAST_NAME: "Nadal"})
players.append({
    API_NODE_PROPERTY.FIRST_NAME: "Cristiano",
    API_NODE_PROPERTY.LAST_NAME: "Ronaldo"})
players.append({
    API_NODE_PROPERTY.FIRST_NAME: "Michael",
    API_NODE_PROPERTY.LAST_NAME: "Phelps"})
players.append({
    API_NODE_PROPERTY.FIRST_NAME: "Jeremy",
    API_NODE_PROPERTY.LAST_NAME: "Lin"})
players.append({
    API_NODE_PROPERTY.FIRST_NAME: "Lance",
    API_NODE_PROPERTY.LAST_NAME: "Armstrong"})
players.append({
    API_NODE_PROPERTY.FIRST_NAME: "Alexander",
    API_NODE_PROPERTY.LAST_NAME: "Ovechkin"})

for p in players:
    protoplayer = editor.prototype_node(
            API_NODE_TYPE.PLAYER, 
            p)
    protoedge = editor.prototype_edge_and_complement(
            API_EDGE_TYPE.IN_LEAGUE, 
            {}, 
            league.id)
    r = editor.create_node_and_edges(protoplayer, protoedge)

print("{0} Players created successfully.".format(len(players)))


# GAME CREATION

# get updated league
league = loader.load_node(league.id)

# get all opponent ids
opp_ids = []
for e in league.get_edges().get(API_EDGE_TYPE.HAS_LEAGUE_MEMBER, {}).values():
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

