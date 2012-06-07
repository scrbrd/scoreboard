""" Module: create_game

Element components for Create Game dialog.

"""
from view.constants import APP_DATA, FORM_NAME, APP_ID, APP_CLASS
from view.app_copy import Copy
from view.html.elements import Div, UL, LI, Header
from view.html.elements import BR, Form, TextInput, HiddenInput, CheckboxInput

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
        self.append_classes([APP_CLASS.DIALOG_CONTENT])

        # FIXME take out hard coded values
        self.append_child(HiddenInput(FORM_NAME.LEAGUE, ""))
        self.append_child(HiddenInput(FORM_NAME.CREATOR, "700"))

        # create game score form section with Player and Winner headings
        headings = ["Player", "W"]
        self.append_child(GameScoreDiv(headings))

        # add form submit and close buttons
        self.append_child(SubmitButtonSection())


class GameScoreDiv(Div):

    """ Game Score List with header extending <div>. """

    def __init__(self, headings):
        """ Construct a GameScore header and list container <div>. """
        super(GameScoreDiv, self).__init__()

        # create Header object
        game_score_header = GameScoreHeader(headings)
        self.append_child(game_score_header)

        # create List
        numberOfRows = 4
        rows = []
        for x in xrange(numberOfRows):
            rows.append(x)
        self.append_child(GameScoreUL(rows))

        self.set_classes([APP_CLASS.LIST_WITH_HEADERS])


class GameScoreHeader(Header):

    """ Game Score column headings extending <header>. """

    def __init__(self, headings):
        """ Construct a GameScore header element <header>. """
        super(GameScoreHeader, self).__init__()

        col_head_0 = Div()
        col_head_0.set_text(headings[0])
        col_head_0.set_classes([APP_CLASS.COLUMN_0])

        col_head_1 = Div()
        col_head_1.set_text(headings[1])
        col_head_1.set_classes([APP_CLASS.COLUMN_1])

        self.append_child(col_head_0)
        self.append_child(col_head_1)

        self.set_classes([APP_CLASS.HEADED_LIST_ITEM])


class GameScoreUL(UL):

    """ Game Score List extending <ul>. """


    def set_list_item(self, item, index):
        """ Construct and add a list item as a child of this list. """
        self.append_child(GameScoreLI(item, index))


class GameScoreLI(LI):

    """ Game Score list item extending <li>. """


    def __init__(self, item, index):
        """ Construct a player score list item element tree. """
        super(GameScoreLI, self).__init__(item, index)
        self.create_content(item)


    def create_content(self, item):
        """ Generate the content for this game score list item. """
        # list names format: NAME[INDEX][DATA_TYPE]
        # id
        game_score_id = "{0}[{1}][{2}]".format(
                FORM_NAME.GAME_SCORE,
                self._index,
                APP_DATA.ID)
        id_input = AutocompleteInput(
                game_score_id,
                APP_CLASS.PLAYER_SELECT,
                Copy.player_placeholder)
        id_input.append_classes([APP_CLASS.COLUMN_0])
        self.append_child(id_input)

        # winner
        # translated to score to work with the backend
        winner_value = "1"
        game_score_winner = "{0}[{1}][{2}]".format(
                FORM_NAME.GAME_SCORE,
                self._index,
                APP_DATA.SCORE)
        winner_input = CheckboxInput(game_score_winner, winner_value)
        winner_input.set_classes([APP_CLASS.COLUMN_1])
        self.append_child(winner_input)

        self.set_classes([APP_CLASS.HEADED_LIST_ITEM])
