""" Module: create_game

Element components for Create Game dialog.

"""

from view.constants import SQ_DATA, PAGE_NAME
from view.app_copy import Copy

from view.elements.base import UL, Form, HiddenInput, CheckboxInput
from view.elements.components import HeadedList, HeadedListItem, SwitchInput

from constants import DIALOG_CLASS
from framework import PostButtonSection
from components import AutocompleteInput


class CreateGameForm(Form):

    """ Create Game form extending <form>. """


    def __init__(self, xsrf_token, data):
        """ Construct a Create Game form element tree.

        Required:
        str     xsrf_token  xsrf token to prevent forgery
        Model   data        populate data-* with model constants

        """
        super(CreateGameForm, self).__init__(PAGE_NAME.CREATE_GAME, xsrf_token)
        self.set_action("/create/game")
        self.append_class(DIALOG_CLASS.DIALOG_CONTENT)

        self.append_child(HiddenInput(PAGE_NAME.LEAGUE))

        # TODO: take out hard coded values
        # create game score form section with Player and Winner headings
        headings = ["Player", "W"]
        numberOfRows = 4
        rows = []
        for x in xrange(numberOfRows):
            rows.append(x)
        self.append_child(GameScoreHL(headings, rows))

        # add form submit and close buttons
        self.append_child(PostButtonSection())


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
                "game-score",
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
                "game-score",
                self._index,
                SQ_DATA.SCORE)
        winner_input = CheckboxInput(game_score_winner, winner_value)
        self.set_column(winner_input)
