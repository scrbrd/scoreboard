""" Module: create_game

Element components for Create Game dialog.

"""

from view.constants import SQ_DATA, SQ_VALUE, PAGE_NAME
from view.app_copy import Copy

from view.elements.base import Div, Span, UL, Form, HiddenInput
from view.elements.components import SwitchInput, MultiColumnLI, Thumbnail
from view.elements.components import HeadedList, HeadedListItem

from view.app.components import Headline

from constants import DIALOG_CLASS
from framework import PostButtonSection
from components import AutocompleteInput


class CreateGameForm(Form):

    """ Create Game form extending <form>. """

    MAX_TAGS = 4


    def __init__(self, xsrf_token, data):
        """ Construct a Create Game form element tree.

        Required:
        str     xsrf_token  xsrf token to prevent forgery
        Model   data        model constants for data-* hidden inputs

        """
        super(CreateGameForm, self).__init__(PAGE_NAME.CREATE_GAME, xsrf_token)

        # TODO: make this draw from view.url constants
        self.set_action("/create/game")
        self.append_class(DIALOG_CLASS.DIALOG_CONTENT)

        # TODO: is there some mild abstraction needed here? or other info?
        # add some context to the form
        self.append_child(HiddenInput(SQ_DATA.LEAGUE_ID))

        # tag header
        self.append_child(OpponentTagsHeader())

        # group of won autocompletes
        winner_tags = [SQ_VALUE.WON for tag in range(self.MAX_TAGS / 2)]
        self.append_child(OpponentTagsUL(winner_tags))

        # group of lost autocompletes
        loser_tags = [SQ_VALUE.LOST for tag in range(self.MAX_TAGS / 2)]
        self.append_child(OpponentTagsUL(loser_tags))

        # group of player autocompletes
        player_tags = [SQ_VALUE.PLAYED for tag in range(self.MAX_TAGS)]
        self.append_child(OpponentTagsUL(player_tags))

        # TODO: add sport autocomplete input

        # add form submit and close buttons
        self.append_child(PostButtonSection())


class OpponentTagsHeader(Div):

    """ OpponentTagsHeader extending Div. """


    def __init__(self):
        """ Construct an OpponentTagsHeader with a Headline and Switch. """
        super(OpponentTagsHeader, self).__init__()

        # opponents headline
        self.append_child(OpponentTagsHeadline())

        # versus/with checkbox
        #TODO: set optional is_on based on some stored value in model/session
        self.append_child(GameTypeSwitch())


class OpponentTagsHeadline(Headline):

    """ OpponentTagsHeadline extending Headline. """


    def __init__(self):
        """ Construct an OpponentTagsHeadline. """
        super(OpponentTagsHeadline, self).__init__(Copy.tag_headline)
        self.append_class(DIALOG_CLASS.OPPONENT_TAGS_HEADLINE)


class OpponentTagsSubheader(Headline):

    """ OpponentTagsSubheader extending Headline. """


    def __init__(self, text=""):
        """ Construct an OpponentTagsHeadline. """
        super(OpponentTagsSubheader, self).__init__(text)
        self.append_class(DIALOG_CLASS.OPPONENT_TAGS_SUBHEADER)


class OpponentTagsHL(HeadedList):

    """ OpponentTagsSubheader extending Headline. """


    def __init__(self, headings, items):
        """ Construct an OpponentTagsHL. """
        super(OpponentTagsHL, self).__init__(headings, items)
        self.append_class(DIALOG_CLASS.OPPONENT_TAGS_SUBHEADER)


    def set_list(self, items):
        """ Set the List element for this HeadedList. """
        self.append_child(OpponentTagsUL(items))


class GameTypeSwitch(SwitchInput):

    """ GameTypeSwitch extending SwitchInput. """


    def __init__(self, is_on=False):
        """ Construct a GameTypeSwitch toggling versus/with. """
        super(GameTypeSwitch, self).__init__(
                SQ_DATA.GAME_TYPE,
                SQ_VALUE.RIVALRY,
                Copy.versus_short,
                Copy.with_,
                is_on)
        self.append_class(DIALOG_CLASS.GAME_TYPE_SWITCH)


class OpponentTagsUL(UL):

    """ OpponentTagsUL extending <ul>. """


    def __init__(self, items):
        """ Construct an OpponentTagsUL. """
        super(OpponentTagsUL, self).__init__(items)
        self.append_class(DIALOG_CLASS.OPPONENT_TAGS_LIST)


    def set_list_item(self, item, index):
        """ Override superclass only changing LI to OpponentTagLI. """
        self.append_child(OpponentTagLI(item, index))


class OpponentTagLI(MultiColumnLI):
#class OpponentTagLI(HeadedListItem):

    """ OpponentTagLI extending HeadedListItem. """


    def __init__(self, item, index):
        """ Construct an OpponentTagLI. """
        super(OpponentTagLI, self).__init__(item, index)
        self.append_class(DIALOG_CLASS.OPPONENT_TAG_LIST_ITEM)


    def set_content(self, item):
        """ Generate the content for this Opponent tag list item. """

        # TODO make this some default scoreboard icon
        protocol = "https://"
        host = "sphotos-b.xx.fbcdn.net/"
        path = "hphotos-prn1/526518_166559743468848_1182827715_n.jpg"
        url = protocol + host + path

        thumbnail_div = Div()
        thumbnail_div.append_child(Thumbnail(url, Copy.app_name))
        self.set_column(thumbnail_div)

        metrics_by_opponent = "{0}[{1}][{2}]".format(
                SQ_DATA.METRICS_BY_OPPONENT,
                self._index,
                item)
        input_span = Span()
        input_span.append_child(AutocompleteInput(
                metrics_by_opponent,
                DIALOG_CLASS.AUTOCOMPLETE_PLAYERS,
                Copy.tag_placeholder))
        self.set_column(input_span)

        # TODO: add x button
