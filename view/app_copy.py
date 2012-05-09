""" Module: app_copy

Reusable copy for the view. Currently strings but will be templates.

"""

class _Copy(object):

    """ _Copy class holds all the application's copy. """


    @property
    def submit(self):
        """ The copy for the submit button. """
        return "Submit!"


    @property
    def close(self):
        """ The copy for the close button. """
        return "Close it"


    @property
    def create_game_dialog_header(self):
        """ The copy for the creat game dialog's header. """
        return "Add Game"


    @property
    def player_placeholder(self):
        """ The copy for a player placeholer. """
        return "Who played?"

    
    @property
    def score_placeholder(self):
        """ The copy for a score placeholder. """
        return "And the score?"

Copy = _Copy()