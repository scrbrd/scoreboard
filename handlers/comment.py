""" Module: comment

Provide a CRUD CommentHandler for processing incoming comment requests.
Currently only setup to handle CREATE / POST requests.

"""

from model.app.comments import CreateCommentModel

from handlers.query import QueryHandler

from constants import PARAMETER


class CommentHandler(QueryHandler):

    """ Handle all single comment requests. """


    def process_asynchronous_request(self):
        """ Handle the asynchronous requests. """

        print("here!!!!!")
        # get comment parameters from request
        parameters = self.get_request_parameters()
        game_id = parameters[PARAMETER.GAME_ID]
        message = parameters[PARAMETER.MESSAGE]

        print(game_id)
        print(message)
        # create comment in model
        model = CreateCommentModel(
                self.current_user,
                game_id,
                message)
        model.dispatch()

        self.write({"is_success": model.success})


    def process_synchronous_request(self):
        """ Override specifies this case effectively doesn't exist. """
        raise NotImplementedError("Unused Method: DO NOT CALL OR OVERRIDE!")


    def get_model(self):
        """ Define the controller's generic connection to the model. """
        raise NotImplementedError("Unused Method: DO NOT CALL OR OVERRIDE!")


    def get_dialog_header_url(self):
        """ Generate a URL for rendering a context header. """
        raise NotImplementedError("Unused Method: DO NOT CALL OR OVERRIDE!")


    def get_asynchronous_content_url(self):
        """ Generate a URL for handling asynchronous content requests. """
        raise NotImplementedError("Unused Method: DO NOT CALL OR OVERRIDE!")


    def get_synchronous_content_url(self):
        """ Generate a URL for handling synchronous content requests. """
        raise NotImplementedError("Unused Method: DO NOT CALL OR OVERRIDE!")
