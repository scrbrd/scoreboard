""" Module: Data Settings

Provide settings that allow for switching out and configuring databases.

"""
import os

from constants import SETTING, TYPE, PROTOCOL, NEO4J


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
        SETTING.HOST: os.environ.get(NEO4J.HOST),
        SETTING.PORT: int(os.environ.get(NEO4J.PORT)),
        SETTING.PROTOCOL: PROTOCOL.HTTP,
        SETTING.TYPE: TYPE.SECURE_NEO4J,
        SETTING.NAME: "heroku",
        SETTING.LOGIN: os.environ.get(NEO4J.LOGIN),
        SETTING.PASSWORD: os.environ.get(NEO4J.PASSWORD),
        }
databases[db1[SETTING.NAME]] = db1

active_db = "heroku"
