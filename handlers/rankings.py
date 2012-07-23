""" Module: rankings

...

"""

from model.app.rankings import RankingsModel

from handlers.query import QueryHandler


class RankingsHandler(QueryHandler):

    """ Handle a Rankings request. """


    def get_model(self):
        """ Return a data model in response to a request for Rankings. """
        model = RankingsModel(self.current_user)
        model.load()
        return model


    def get_synchronous_content_url(self):
        """ Generate a URL for handling synchronous content requests. """
        # TODO: turn this hardcoded file path into a constant
        return "mobile/rankings.html"


    def get_asynchronous_content_url(self):
        """ Generate a URL for handling asynchronous content requests. """
        # TODO: turn this hardcoded file path into a constant
        return "mobile/components/rankings.html"


    def get_page_state_model_url(self):
        """ Generate a URL for rendering a page state model. """
        # TODO: turn this hardcoded file path into a constant
        return "mobile/components/rankings_model.html"
