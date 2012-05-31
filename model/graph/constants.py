""" Graph Constants

Provide a set of constants native to the Graph layer. Note that This
specifically excludes those provided by model.constants.

"""

from util.decorators import constant


class _GraphProperty(object):

    """ _GraphProperty class to hold all GraphObject Properties. """


    @constant
    def CREATED_TS(self):
        """ CREATED_TS is a Property of GraphObject. """
        return "created_ts"


    @constant
    def UPDATED_TS(self):
        """ UPDATED_TS is a Property of GraphObject. """
        return "updated_ts"


    @constant
    def DELETED_TS(self):
        """ DELETED_TS is a Property of GraphObject. """
        return "deleted_ts"


GRAPH_PROPERTY = _GraphProperty()

