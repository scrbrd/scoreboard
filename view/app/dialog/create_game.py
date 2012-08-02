""" Module: create_game

Element components for Create Game dialog.

"""

from view.constants import SQ_DATA, SQ_VALUE, PAGE_NAME
from view.elements.base import Div, Span, UL, Form, HiddenInput
from view.elements.components import SwitchInput, MultiColumnLI
from view.app.copy import Copy
from view.app.components import Headline, Subheadline

from constants import DIALOG_CLASS
from framework import PostButtonSection, DialogContentSection
from components import TagAutocomplete


class CreateGameContentSection(DialogContentSection):

    """ The main content of the CreateGameDialog. """


    def __init__(self, xsrf_token, model):
        """ Construct a content section for CreateGame Dialog. """
        super(CreateGameContentSection, self).__init__()

        # TODO: add this iScroll container / wrapper to AppContentSection
        self.set_id("dialog-content-wrapper")
        div = Div()
        div.set_id("dialog-content-container")

        div.append_child(CreateGameForm(xsrf_token, model))
        self.append_child(div)


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
        self.set_id(DIALOG_CLASS.DIALOG_CONTENT)

        # TODO: is there some mild abstraction needed here? or other info?
        # add some context to the form
        self.append_child(HiddenInput(SQ_DATA.LEAGUE_ID))

        # tag header
        self.append_child(OpponentTagsHeader())

        # the three tag groups: won,lost, played
        self.append_child(OpponentTagsGroup(
                SQ_VALUE.RIVALRY,
                SQ_VALUE.WON,
                self.MAX_TAGS,
                Copy.won))
        self.append_child(OpponentTagsGroup(
                SQ_VALUE.RIVALRY,
                SQ_VALUE.LOST,
                self.MAX_TAGS,
                Copy.lost))
        self.append_child(OpponentTagsGroup(
                SQ_VALUE.CAMARADERIE,
                SQ_VALUE.PLAYED,
                self.MAX_TAGS))

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


class GameTypeSwitch(SwitchInput):

    """ GameTypeSwitch extending SwitchInput. """


    def __init__(self, is_on=True):
        """ Construct a GameTypeSwitch toggling versus/with. """
        super(GameTypeSwitch, self).__init__(
                SQ_DATA.GAME_TYPE,
                SQ_VALUE.RIVALRY)
        self.append_class(DIALOG_CLASS.GAME_TYPE_SWITCH)
        self.set_on(is_on)


class OpponentTagsGroup(Div):

    """ OpponentTagsGroup extending <div>, for grouping tags together with a
    Subheader. """


    def __init__(self, game_type, result_type, number_of_tags, title=None):
        """ Construct a OpponentTagsGroup.

        Required:
        str     game_type           the type of game (rivalry / camaraderie
        str     result_type         the type of result (won / lost / played)
        int     number_of_tags      the number of tags

        Optional:
        str     title               the title of the group.

        """
        super(OpponentTagsGroup, self).__init__()
        self.append_class(DIALOG_CLASS.OPPONENT_TAGS_GROUP)
        self.append_class(game_type)
        # subheader for the group.
        if title is not None:
            self.append_child(OpponentTagsSubheader(title))

        # group of autocompletes
        tags = [result_type for n in range(number_of_tags)]
        self.append_child(OpponentTagsUL(tags))



class OpponentTagsSubheader(Subheadline):

    """ OpponentTagsSubheader extending Headline. """


    def __init__(self, text=""):
        """ Construct an OpponentTagsHeadline. """
        super(OpponentTagsSubheader, self).__init__(text)
        self.append_class(DIALOG_CLASS.OPPONENT_TAGS_SUBHEADER)


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

    """ OpponentTagLI extending MultiColumnLI. """


    def __init__(self, item, index):
        """ Construct an OpponentTagLI. """
        super(OpponentTagLI, self).__init__(item, index)
        self.append_class(DIALOG_CLASS.OPPONENT_TAG_LIST_ITEM)


    def set_content(self, item):
        """ Generate the content for this Opponent tag list item. """


        metrics_by_opponent = "{0}[{1}][{2}]".format(
                SQ_DATA.METRICS_BY_OPPONENT,
                self._index,
                item)
        input_span = Span()
        input_span.append_child(TagAutocomplete(
                metrics_by_opponent,
                Copy.tag_placeholder))
        self.set_column(input_span)

        # TODO: add x button
