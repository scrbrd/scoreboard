""" Module: create

Handle all incoming requests for object creation.

"""

import logging
import urllib
import json

from handlers.base import BaseHandler

from model.app import catchers

# TODO figure out how logging works
logger = logging.getLogger('boilerplate.' + __name__)


class CreateGameHandler(BaseHandler):

    """ Render Create Game Dialog. """


    def post(self):
        """ Overload BaseHandler's HTTP GET responder. """
        
        # check for ajax request or not
        is_asynch = bool(self.get_argument("asynch", False))
       
        # only allow asynch request
        if is_asynch:
            self._post_asynch()
        else:
            pass

    
    def _post_asynch(self):
        """ Handle the asynchronous version of the create game dialog.
        
        Required:
        int     league      Game's league id
        int     creator     Game's creator id
        list    game_score  Game's final score
                            [{"id": VALUE, "score": VALUE}]
   
        Return:
        bool is_success     if game creation was successful (None from fail)
        """
            
        # get game parameters from request
        params_str  = self.get_argument("parameters", None)
        params_dict = json.loads(params_str)
        league_id = params_dict["league"]
        creator_id = params_dict["creator"]
        game_score = params_dict["game_score"]
        
        # create game in model
        creator = catchers.CreateCatcher();
        new_game = creator.create_game(
                league_id,
                creator_id,
                game_score);
       
        is_success = True
        if new_game is None:
            is_success = False

        self.write({"is_success": is_success})

