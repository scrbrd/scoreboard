""" Module: Data Settings

Provide settings that allow for switching out and configuring databases.

"""
from constants import SETTING, TYPE, PROTOCOL

databases = {}

db0 = {
        SETTING.HOST: "localhost",
        SETTING.PORT: "7474",
        SETTING.PROTOCOL: PROTOCOL.HTTP,
        SETTING.TYPE: TYPE.NEO4J,
        SETTING.NAME: "local",
        }
databases[db0[SETTING.NAME]] = db0

db1 = {
        SETTING.HOST: "f7e1861b3.hosted.neo4j.org",
        SETTING.PORT: "7134",
        SETTING.PROTOCOL: PROTOCOL.HTTP,
        SETTING.TYPE: TYPE.SECURE_NEO4J,
        SETTING.NAME: "heroku",
        SETTING.USERNAME: "1dd76643b",
        SETTING.PASSWORD: "919115168",
        }
databases[db1[SETTING.NAME]] = db1

active_db = "local"
