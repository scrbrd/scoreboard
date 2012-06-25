""" Module: create

Handle all incoming requests for object creation.

"""

from model.app.catchers import CreateGameCatcher

from handlers.query import QueryHandler


class CreateGameHandler(QueryHandler):

    """ Render Create Game Dialog. """


    def process_asynchronous_request(self):
        """ Handle the asynchronous version of the create game dialog.

        Required:
        int     league      Game's league id
        list    game_score  Game's final score
                            [{"id": VALUE, "score": VALUE}]

        Return:
        bool is_success     if game creation was successful (None from fail)

        """

        # get game parameters from request
        parameters = self.get_request_parameters()

        # TODO: make request parameters a class or at least constants!
        league_id = parameters["league"]
        game_score = parameters["game-score"]

        # create game in model
        model = CreateGameCatcher(self.current_user)
        model.set_league_id(league_id)
        model.set_score(game_score)
        model.dispatch()

        self.write({"is_success": model.success})


    def process_synchronous_request(self):
        """ Override specifies this case effectively doesn't exist. """
        raise NotImplementedError("Unused Method: DO NOT CALL OR OVERRIDE!")


    def get_model(self):
        """ Define the controller's generic connection to the model. """
        raise NotImplementedError("Unused Method: DO NOT CALL OR OVERRIDE!")


    def get_context_header_url(self):
        """ Generate a URL for rendering a context header. """
        raise NotImplementedError("Unused Method: DO NOT CALL OR OVERRIDE!")


    def get_asynchronous_content_url(self):
        """ Generate a URL for handling asynchronous content requests. """
        raise NotImplementedError("Unused Method: DO NOT CALL OR OVERRIDE!")


    def get_synchronous_content_url(self):
        """ Generate a URL for handling synchronous content requests. """
        raise NotImplementedError("Unused Method: DO NOT CALL OR OVERRIDE!")
