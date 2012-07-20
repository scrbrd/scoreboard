""" Module: Data Constants

Provide constants for hardcoded values describing the database server.

"""
from util.decorators import constant


class _Setting(object):

    """ _Setting class to hold all Database settings constants. """


    @constant
    def DELIMITER(self):
        """ DELIMITER is a Database settings constant. """
        return "_"


    @constant
    def HOST(self):
        """ HOST is a Database settings constant. """
        return "HOST"


    @constant
    def LOGIN(self):
        """ LOGIN is a Database settings constant. """
        return "LOGIN"


    @constant
    def NAME(self):
        """ NAME is a Database settings constant. """
        return "NAME"


    @constant
    def PASSWORD(self):
        """ PASSWORD is a Database settings constant. """
        return "PASSWORD"


    @constant
    def PORT(self):
        """ PORT is a Database settings constant. """
        return "PORT"


    @constant
    def PROTOCOL(self):
        """ PROTOCOL is a Database settings constant. """
        return "PROTOCOL"


    @constant
    def TYPE(self):
        """ TYPE is a Database settings constant. """
        return "TYPE"


SETTING = _Setting()


class _Type(object):

    """ _Type class to hold all of our many database types. """


    @constant
    def NEO4J(self):
        """ NEO4J is a type of datbase that we use. """
        return "NEO4J"


    @constant
    def SECURE_NEO4J(self):
        """ SECURE_NEO4J is a type of datbase that we use. """
        return "SECURE_NEO4J"


TYPE = _Type()


class _Protocol(object):

    """ _Protocol class to hold the different types of protocols. """


    @constant
    def HTTP(self):
        """ HTTP is a type of protocol. """
        return "http"


    @constant
    def HTTPS(self):
        """ HTTPS is a type of protocol. """
        return "https"


PROTOCOL = _Protocol()


class _Neo4j(object):

    """ _Neo4j class to hold Neo4j Constants. """


    @constant
    def HOST(self):
        """ HOST is a Heroku Neo4j setting. """
        return TYPE.NEO4J + SETTING.DELIMITER + SETTING.HOST


    @constant
    def PORT(self):
        """ PORT is a Heroku Neo4j setting. """
        return TYPE.NEO4J + SETTING.DELIMITER + SETTING.PORT


    @constant
    def LOGIN(self):
        """ LOGIN is a Heroku Neo4j setting. """
        return TYPE.NEO4J + SETTING.DELIMITER + SETTING.LOGIN


    @constant
    def PASSWORD(self):
        """ PASSWORDis a Heroku Neo4j setting. """
        return TYPE.NEO4J + SETTING.DELIMITER + SETTING.PASSWORD


NEO4J = _Neo4j()
