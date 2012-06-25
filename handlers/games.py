""" Module: games

...
"""

import logging

from handlers.query import QueryHandler

from model.app import catchers

# TODO figure out how logging works
logger = logging.getLogger('boilerplate.' + __name__)


class GamesHandler(QueryHandler):

    """ Render Games List Page. """

    def process_request(self):
        """ Handle processing of Games request. Inherited from BaseHandler.
        """

        # check for ajax request or not
        is_asynch = self.get_argument("asynch", False)

        # FIXME remove hardcoded league id
        league_id = self.settings['league_id']

        # get games data from model
        games_model = catchers.GamesCatcher(league_id)

        # hand data over to view and render
        if is_asynch:
            self._get_asynch(games_model)
        else:
            self._get_synch(games_model)


    def _get_asynch(self, model):
        """ Handle the asynchronous version of the games request.

        Render both the context_header and the games components.

        """

        # TODO: turn this hardcoded file path into a constant
        context = self.render_string(
                "mobile/components/context.html",
                model=model)
        context_model = self.render_string(
                "mobile/components/context_model.html",
                model=model)
        viewer_context_model = self.render_string(
                "mobile/components/viewer_context_model.html",
                model=model)
        content = self.render_string(
                "mobile/components/games.html",
                model=model)
        page_state_model = self.render_string(
                "mobile/components/games_model.html",
                model=model)

        self.write({
            "context": context,
            "context_model": context_model,
            "viewer_context_model": viewer_context_model,
            "content": content,
            "page_state_model": page_state_model,
        })


    def _get_synch(self, model):
        """ Handle the synchronous version of the games request.

        Render the full games page.

        """

        # TODO: turn this hardcoded file path into a constant
        self.render("mobile/games.html", model=model)
