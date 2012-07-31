""" Module: sqcopy

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
    def feed_title(self):
        """ The title of the Feed Section. """
        return "Feed"


    @property
    def defeated(self):
        """ The verb for one team beating another team. """
        return "defeated"


    @property
    def played(self):
        """ The verb for one team playing. """
        return "played"

    @property
    def player(self):
        """ The copy for the player title. """
        return "Player"


    @property
    def tag_headline(self):
        """ The copy for a tag headline. """
        return "Who played?"


    @property
    def tag_placeholder(self):
        """ The copy for a tag placeholer. """
        return "Start typing a player's name"


    @property
    def rankings_title(self):
        """ The copy for the rankings title. """
        return "Standings"


    @property
    def score_placeholder(self):
        """ The copy for a score placeholder. """
        return "?"


    @property
    def win_streak_short(self):
        """ The copy for a shortened win streak. """
        return "S"


    @property
    def win_percentage(self):
        """ The copy for a win percentage. """
        return "%"


    @property
    def win(self):
        """ The copy for a win (noun). """
        return "Win"


    @property
    def loss(self):
        """ The copy for a loss. """
        return "Loss"


    @property
    def won(self):
        """ The copy for the Create Game dialog winners subheader. """
        return "Won"


    @property
    def lost(self):
        """ The copy for the Create Game dialog losers subheader. """
        return "Lost"


    @property
    def win_short(self):
        """ The copy for a shortened win. """
        return "W"


    @property
    def loss_short(self):
        """ The copy for a shortened loss. """
        return "L"


    @property
    def win_loss_short(self):
        """ The copy for a shortened win/loss header or subheader. """
        return "W/L"


    @property
    def versus(self):
        """ The copy for a versus header or subheader. """
        return "Versus"


    @property
    def versus_short(self):
        """ The copy for a shortened versus header or subheader. """
        return "VS"


    @property
    def with_(self):
        """ The copy for a shortened non-versus header or subheader.

        Note the trailing underscore; "with" is a python keyword.

        """
        return "With"


Copy = _Copy()
