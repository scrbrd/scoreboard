""" Package: api

The api package contains our application objects. To help with circular imports
we have an SqFactory singleton object that creates all the nodes (e.g., Game,
League, User, Player.) In this __init__ file we create a dictionary that the
factory can use to instantiate any api node.

"""
import league
import player
import game
import user
import sqfactory
from constants import API_NODE_TYPE

# Create Node Constructor dictionary.
node_mapping = {}
node_mapping[API_NODE_TYPE.LEAGUE] = league.League
node_mapping[API_NODE_TYPE.PLAYER] = player.Player
node_mapping[API_NODE_TYPE.GAME] = game.Game
node_mapping[API_NODE_TYPE.USER] = user.User

# Construct the SqFactory singleton and pass it this dictionary.
sqfactory.SqFactory(node_mapping)
