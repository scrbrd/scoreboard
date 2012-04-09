""" Module: dialog

Handle all incoming requests for dialogs.

"""
import logging

from handlers.base import BaseHandler

# TODO figure out how logging works
logger = logging.getLogger('boilerplate.' + __name__)


class CreateGameDialogHandler(BaseHandler):

    """ Render Create Game Dialog. """
    # FIXME make this whole set of handlers AJAX oriented


    def get(self):
        """ Overload BaseHandler's HTTP GET responder. """

        # no data/model.... just call view
        self.render("mobile/create_game.html")
