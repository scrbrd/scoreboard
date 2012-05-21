""" Module: dialog

Handle all incoming requests for dialog creation.

"""


import logging

from handlers.query import QueryHandler


class CreateGameDialogHandler(QueryHandler):

    """ Render Create Game Dialog. """
    
    def process_request(self):
        """ Handle processing Dialog Request. """

        # TODO: turn this hardcoded file path into a constant
        self.render("mobile/components/create_game.html")
