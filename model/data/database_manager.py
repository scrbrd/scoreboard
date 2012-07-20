""" Module: database_manager

Manage databases and provide access to them. Return active databases
to the graph layer.

"""
from neo4j.db import Neo4jDatabase, SecureNeo4jDatabase

from constants import TYPE, SETTING
import settings

# load the databases from the settings file
_databases = {}
for db_key, db_value in settings.databases.items():
    db = None
    if db_value[SETTING.TYPE] == TYPE.NEO4J:
        db = Neo4jDatabase(
                db_value[SETTING.HOST],
                db_value[SETTING.PORT])
    elif db_value[SETTING.TYPE] == TYPE.SECURE_NEO4J:
        db = SecureNeo4jDatabase(
                db_value[SETTING.HOST],
                db_value[SETTING.PORT],
                db_value[SETTING.LOGIN],
                db_value[SETTING.PASSWORD])
    else:
        # TODO: add an InvalidDatabaseTypeError here
        print("add an InvalidDatabaseError here")

    _databases[db_key] = db

_active_db = settings.active_db


def database():
    """ Return the an active Database object. """
    return _databases[_active_db]
