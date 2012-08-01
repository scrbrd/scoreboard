""" Module: copy

Reusable copy for the element components. Currently, these are strings,
but later they should probably be templates.

"""


class _Copy(object):


    @property
    def app_name(self):
        return "Scoreboard"

    @property
    def challenge(self):
        return "Challenge"

    @property
    def feed_title(self):
        return "Feed"

    @property
    def defeated(self):
        return "defeated"

    @property
    def played(self):
        return "played"

    @property
    def player(self):
        return "Player"

    @property
    def tag_headline(self):
        return "Who played?"

    @property
    def tag_placeholder(self):
        return "Who Played?"

    @property
    def rankings_title(self):
        return "Standings"

    @property
    def score_placeholder(self):
        return "?"

    @property
    def win_streak_short(self):
        return "S"

    @property
    def win_percentage(self):
        return "%"

    @property
    def win(self):
        """ The copy for a win (noun). """
        return "Win"

    @property
    def loss(self):
        return "Loss"

    @property
    def won(self):
        return "Won"

    @property
    def lost(self):
        return "Lost"

    @property
    def win_short(self):
        return "W"

    @property
    def loss_short(self):
        return "L"

    @property
    def win_loss_short(self):
        return "W/L"

    @property
    def versus(self):
        return "Versus"

    @property
    def versus_short(self):
        return "VS"

    @property
    def with_(self):
        """ Note the trailing underscore; "with" is a python keyword. """
        return "With"


Copy = _Copy()
