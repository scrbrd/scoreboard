""" Module: Data Constants

Provide constants for hardcoded values describing the database server.

"""

from util.decorators import constant


class _Database(object):

    """ _Database class to hold all Database constants. """


    @constant
    def DB(self):
        """ DB is a Database constant. """
        return "NEO4J"


    @constant
    def PROTOCOL(self):
        """ PROTOCOL is a Database constant. """
        return "http://"


    @constant
    def HOST(self):
        """ HOST is a Database constant. """
        return "localhost"


    @constant
    def PORT(self):
        """ PORT is a Database constant. """
        return ":7474"


    @constant
    def BASE_URL(self):
        """ BASE_URL is a Database constant. """
        return self.PROTOCOL + self.HOST + self.PORT


DATABASE = _Database()

