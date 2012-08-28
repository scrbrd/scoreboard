""" Module: league

Provide a simple LeagueHandler for processing incoming requests for and
serving outgoing responses to League Highlights.

"""

from util.dev import print_timing
from model.app.league import LeagueModel

from query import QueryHandler


class LeagueHandler(QueryHandler):

    """ Handle a League request. """

    @print_timing
    def get_model(self):
        """ Return a data model in response to a request for Games. """
        model = LeagueModel(self.current_user)
        model.set_league_id(self._id)
        model.load()
        return model


    @print_timing
    def get_synchronous_content_url(self):
        """ Generate a URL for handling synchronous content requests. """
        # TODO: turn this hardcoded file path into a constant
        return "mobile/league.html"


    @print_timing
    def get_asynchronous_content_url(self):
        """ Generate a URL for handling asynchronous content requests. """
        # TODO: turn this hardcoded file path into a constant
        return "mobile/components/league.html"


    @print_timing
    def get_page_state_model_url(self):
        """ Generate a URL for rendering a page state model. """
        # TODO: turn this hardcoded file path into a constant
        return "mobile/components/league_model.html"
