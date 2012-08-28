""" Module: create

Handle all incoming requests for object creation.

"""

from model.app.create_game import CreateGameModel

from handlers.query import QueryHandler

from constants import PARAMETER


class CreateGameHandler(QueryHandler):

    """ Render Create Game Dialog. """


    def process_asynchronous_request(self):
        """ Handle the asynchronous version of the create game dialog.

        Required:
        int     league                  Game's League id
        dict    metrics_by_opponent     Metrics dicts keyed on Opponent id

        Return:
        bool                            "is_success" from model.success

        """

        # get game parameters from request
        parameters = self.get_request_parameters()
        league_id = parameters.get(PARAMETER.LEAGUE_ID)
        message = parameters.get(PARAMETER.MESSAGE)
        metrics_by_opponent = parameters.get(PARAMETER.METRICS_BY_OPPONENT)
        sport_id = parameters.get(PARAMETER.SPORT_ID)

        # create game in model
        model = CreateGameModel(
                self.current_user,
                metrics_by_opponent,
                sport_id)
        model.set_league_id(league_id)
        model.set_message(message)
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
