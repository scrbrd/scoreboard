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
NUMBER_OF_GAMES = 30


# LEAGUE CREATION
# TODO: there should be a static League function for prototyping a League
proto = editor.prototype_node(
        API_NODE_TYPE.LEAGUE,
        {API_NODE_PROPERTY.NAME: "The Banana Stand"})
league = editor.create_node_and_edges(proto, [])

print("League ({0}) created successfully.".format(league.id))


# PLAYER CREATION
players = []
players.append({
    API_NODE_PROPERTY.FIRST_NAME: "Jon",
    API_NODE_PROPERTY.LAST_NAME: "Warman"})
players.append({
    API_NODE_PROPERTY.FIRST_NAME: "Bobby",
    API_NODE_PROPERTY.LAST_NAME: "Kellogg"})
players.append({
    API_NODE_PROPERTY.FIRST_NAME: "Evan",
    API_NODE_PROPERTY.LAST_NAME: "Hammer"})
players.append({
    API_NODE_PROPERTY.FIRST_NAME: "Leigh",
    API_NODE_PROPERTY.LAST_NAME: "Salem"})
players.append({
    API_NODE_PROPERTY.FIRST_NAME: "Tom",
    API_NODE_PROPERTY.LAST_NAME: "Greenwood"})
players.append({
    API_NODE_PROPERTY.FIRST_NAME: "Tom",
    API_NODE_PROPERTY.LAST_NAME: "Grant"})
players.append({
    API_NODE_PROPERTY.FIRST_NAME: "Zaphod",
    API_NODE_PROPERTY.LAST_NAME: "Beeblebrox"})
players.append({
    API_NODE_PROPERTY.FIRST_NAME: "Blue",
    API_NODE_PROPERTY.LAST_NAME: "Steel"})
players.append({
    API_NODE_PROPERTY.FIRST_NAME: "Jennifer",
    API_NODE_PROPERTY.LAST_NAME: "Clone"})
players.append({
    API_NODE_PROPERTY.FIRST_NAME: "Melissa",
    API_NODE_PROPERTY.LAST_NAME: "Merrill"})
players.append({
    API_NODE_PROPERTY.FIRST_NAME: "Rachael",
    API_NODE_PROPERTY.LAST_NAME: "Rosen"})
players.append({
    API_NODE_PROPERTY.FIRST_NAME: "Eric",
    API_NODE_PROPERTY.LAST_NAME: "Cartman"})
players.append({
    API_NODE_PROPERTY.FIRST_NAME: "Barack",
    API_NODE_PROPERTY.LAST_NAME: "Obama"})
players.append({
    API_NODE_PROPERTY.FIRST_NAME: "Jeremy",
    API_NODE_PROPERTY.LAST_NAME: "Lin"})
players.append({
    API_NODE_PROPERTY.FIRST_NAME: "Action",
    API_NODE_PROPERTY.LAST_NAME: "Jackson"})

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

