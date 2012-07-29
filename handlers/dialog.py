""" Module: dialog

Handle all incoming requests for dialog creation.

"""

from model.app.dialog import DialogModel

from handlers.query import QueryHandler


class CreateGameDialogHandler(QueryHandler):

    """ Handle rendering the empty Create Game Dialog. """


    def get_model(self):
        """ Override avoids raising an error, but no model is needed. """
        model = DialogModel(self.current_user)
        model.load()
        return model


    def process_asynchronous_request(self):
        """ Override forces the dialog to render synchronously. """
        self.process_synchronous_request()


    def get_asynchronous_content_url(self):
        """ Generate a URL for handling asynchronous content requests. """
        raise NotImplementedError("Unused Method: DO NOT CALL OR OVERRIDE!")


    def get_synchronous_content_url(self):
        """ Generate a URL for handling synchronous content requests. """
        # TODO: turn this hardcoded file path into a constant
        return "mobile/components/create_game.html"
