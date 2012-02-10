""" Module: rankings

...
"""

import logging

from handlers.query import QueryHandler

from model.app import catchers

# TODO figure out how logging works
logger = logging.getLogger('boilerplate.' + __name__)


class RankingsHandler(QueryHandler):
    
    """ Render Rankings Page. """

    def process_request(self):
        """ Handle processing of Rankings request. Inherited from BaseHandler.
        """
        
        # check for ajax request or not
        is_asynch = bool(self.get_argument("asynch", False))

        # FIXME remove hardcoded league id
        league_id = self.settings['league_id']

        # get ranking data from model
        rankings_model = catchers.RankingsCatcher(league_id) 

        # hand data over to view and render
        if is_asynch:
            self._get_asynch(rankings_model)
        else:
            self._get_synch(rankings_model)


    def _get_asynch(self, model):
        """ Handle the asynchronous version of the rankings request.
        
        Render both the context_header and the rankings components.

        """

        context_header = self.render_string(
                "mobile/components/context_header.html",
                model=model)
        content = self.render_string(
                "mobile/components/rankings.html",
                model=model)

        self.write({
            "context_header": context_header,
            "content": content})


    def _get_synch(self, model):
        """ Handle the synchronous version of the rankings request. 
        
        Render the full rankings page.

        """

        # TODO: turn this hardcoded file path into a constant
        self.render("mobile/rankings.html", model=model)

