""" Module: create_game

Element components for Create Game dialog.

"""
from view.constants import SQ_DATA, FORM_NAME
from view.app_copy import Copy
from view.html.elements import UL
from view.html.elements import Form, HiddenInput, CheckboxInput
from view.html.components import HeadedList, HeadedListItem

from constants import DIALOG_CLASS
from framework import SubmitButtonSection
from components import AutocompleteInput


class CreateGameForm(Form):

    """ Create Game form extending <form>. """


    def __init__(self, name, xsrf_token, action_url):
        """ Construct a Create Game form element tree.

        Required:
        str     name            the identifying name of the form
        str     xsrf_token      xsrf token to prevent forgery
        url     action_url      the url that the form submits to

        """
        super(CreateGameForm, self).__init__(name, xsrf_token, action_url)
        self.append_classes([DIALOG_CLASS.DIALOG_CONTENT])

        # FIXME take out hard coded values
        self.append_child(HiddenInput(FORM_NAME.LEAGUE, ""))
        self.append_child(HiddenInput(FORM_NAME.CREATOR, "700"))

        # create game score form section with Player and Winner headings
        headings = ["Player", "W"]
        numberOfRows = 4
        rows = []
        for x in xrange(numberOfRows):
            rows.append(x)
        self.append_child(GameScoreHL(headings, rows))

        # add form submit and close buttons
        self.append_child(SubmitButtonSection())


class GameScoreHL(HeadedList):

    """ Game Score List with header extending HeadedList. """


    def set_list(self, rows):
        """ Set the list element for this list. """
        self.append_child(GameScoreUL(rows))


class GameScoreUL(UL):

    """ Game Score List extending <ul>. """


    def set_list_item(self, item, index):
        """ Construct and add a list item as a child of this list. """
        self.append_child(GameScoreLI(item, index))


class GameScoreLI(HeadedListItem):

    """ Game Score list item extending HeadedListItem. """


    def set_content(self, item):
        """ Generate the content for this game score list item. """
        # list names format: NAME[INDEX][DATA_TYPE]
        # id
        game_score_id = "{0}[{1}][{2}]".format(
                FORM_NAME.GAME_SCORE,
                self._index,
                SQ_DATA.ID)
        id_input = AutocompleteInput(
                game_score_id,
                DIALOG_CLASS.AUTOCOMPLETE_PLAYERS,
                Copy.player_placeholder)
        self.set_column(id_input)

        # winner
        # translated to score to work with the backend
        winner_value = "1"
        game_score_winner = "{0}[{1}][{2}]".format(
                FORM_NAME.GAME_SCORE,
                self._index,
                SQ_DATA.SCORE)
        winner_input = CheckboxInput(game_score_winner, winner_value)
        self.set_column(winner_input)
