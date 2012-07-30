""" Module: app_copy

Reusable copy for the view. Currently strings but will be templates.

"""


class _Copy(object):

    """ _Copy class holds all the application's copy. """


    @property
    def app_name(self):
        """ The copy for the app name. """
        return "Scoreboard"


    @property
    def post(self):
        """ The copy for the post button. """
        return "Post"


    @property
    def close(self):
        """ The copy for the close button. """
        return "Close"


    @property
    def okay(self):
        """ The copy for the okay button. """
        return "Okay"


    @property
    def challenge(self):
        """ The copy for the challenge button. """
        return "Challenge"


    @property
    def login(self):
        """ The copy for the login button. """
        return "Login"


    @property
    def facebook_login(self):
        """ The copy for the Facebook login button. """
        return "Login with Facebook"


    @property
    def create_game_dialog_header(self):
        """ The copy for the creat game dialog's header. """
        return "Add Game"


    @property
    def defeated(self):
        """ The verb for one team beating another team. """
        return "defeated"


    @property
    def loss(self):
        """ The copy for a loss. """
        return "Loss"


    @property
    def loss_short(self):
        """ The copy for a shortened loss. """
        return "L"


    @property
    def played(self):
        """ The verb for one team playing. """
        return "played"

    @property
    def player(self):
        """ The copy for the player title. """
        return "Player"


    @property
    def player_placeholder(self):
        """ The copy for a player placeholer. """
        return "Who played?"


    @property
    def rankings_title(self):
        """ The copy for the rankings title. """
        return "Standings"


    @property
    def score_placeholder(self):
        """ The copy for a score placeholder. """
        return "?"


    @property
    def win(self):
        """ The copy for a win. """
        return "Win"


    @property
    def win_short(self):
        """ The copy for a shortened win. """
        return "W"


    @property
    def won(self):
        """ The copy for the Create Game dialog winners subheader. """
        return "Won"


    @property
    def lost(self):
        """ The copy for the Create Game dialog losers subheader. """
        return "Lost"


    @property
    def played_with(self):
        """ The copy for the Create Game dialog players subheader. """
        return "With"


Copy = _Copy()
