""" Module: Data Constants

Provide constants for hardcoded values describing the database server.

"""
from util.decorators import constant


class _Setting(object):

    """ _Setting class to hold all Database settings constants. """


    @constant
    def HOST(self):
        """ HOST is a Database settings constant. """
        return "host"


    @constant
    def NAME(self):
        """ NAME is a Database settings constant. """
        return "name"


    @constant
    def PASSWORD(self):
        """ PASSWORD is a Database settings constant. """
        return "password"


    @constant
    def PORT(self):
        """ PORT is a Database settings constant. """
        return "port"


    @constant
    def PROTOCOL(self):
        """ PROTOCOL is a Database settings constant. """
        return "protocol"


    @constant
    def TYPE(self):
        """ TYPE is a Database settings constant. """
        return "type"


    @constant
    def USERNAME(self):
        """ USERNAME is a Database settings constant. """
        return "username"


SETTING = _Setting()


class _Type(object):

    """ _Type class to hold all of our many database types. """


    @constant
    def NEO4J(self):
        """ NEO4J is a type of datbase that we use. """
        return "neo4j"


    @constant
    def SECURE_NEO4J(self):
        """ SECURE_NEO4J is a type of datbase that we use. """
        return "secure_neo4j"


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
