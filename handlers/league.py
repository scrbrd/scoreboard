""" Module: league

Provide a simple LeagueHandler for processing incoming requests for and
serving outgoing responses to League Highlights.

"""

from model.app.base import LeagueModel

from handlers.query import QueryHandler


class LeagueHandler(QueryHandler):

    """ Handle a League request. """


    def get_model(self):
        """ Return a data model in response to a request for Games. """
        model = LeagueModel(self.current_user)
        model.load()
        return model


    def get_synchronous_content_url(self):
        """ Generate a URL for handling synchronous content requests. """
        # TODO: turn this hardcoded file path into a constant
        return "mobile/league.html"


    def get_asynchronous_content_url(self):
        """ Generate a URL for handling asynchronous content requests. """
        # TODO: turn this hardcoded file path into a constant
        return "mobile/components/league.html"


    def get_page_state_model_url(self):
        """ Generate a URL for rendering a page state model. """
        # TODO: turn this hardcoded file path into a constant
        return "mobile/components/league_model.html"
