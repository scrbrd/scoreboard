""" Module: create_game

Element components for Create Game dialog.

"""

from view.constants import SQ_DATA, SQ_VALUE, PAGE_NAME
from view.elements.base import Div, UL, Form, HiddenInput, LI, TextInput
from view.elements.components import SwitchInput
from view.app.copy import Copy
from view.app.components import Subheadline

from framework import DialogHeader, DialogContentSection, PostButtonSection
from components import PlayerAutocomplete, SportAutocomplete


class CreateGameDialogHeader(DialogHeader):

    """ The main header for the Create Game Dialog. """


    def __init__(self):
        """ Construct a header. """
        super(CreateGameDialogHeader, self).__init__(
                Copy.create_game_dialog_header)


class CreateGameContentSection(DialogContentSection):

    """ The main content of the CreateGameDialog. """


    def __init__(self, model):
        """ Construct a content section for CreateGame Dialog. """
        super(CreateGameContentSection, self).__init__()

        self.append_child(CreateGameForm(model))


class CreateGameForm(Form):

    """ Create Game form extending <form>. """

    HEADLINE_INPUT_CLASS = "headline-input"
    MAX_TAGS = 2
    HEADLINE_LENGTH = 21


    def __init__(self, data):
        """ Construct a Create Game form element tree.

        Required:
        Model   data        model constants for data-* hidden inputs

        """
        super(CreateGameForm, self).__init__(PAGE_NAME.CREATE_GAME)

        # TODO: make this draw from view.url constants
        self.set_action("/create/game")

        # TODO: is there some mild abstraction needed here? or other info?
        # add some context to the form
        self.append_child(HiddenInput(SQ_DATA.LEAGUE_ID))

        # tag header
        headline_input = TextInput(SQ_DATA.MESSAGE)
        headline_input.set_maxlength(self.HEADLINE_LENGTH)
        headline_input.set_placeholder(Copy.headline)
        headline_input.append_class(self.HEADLINE_INPUT_CLASS)
        self.append_child(headline_input)

        # versus/with checkbox
        # TODO: optionally set is_on based on some stored model/session value.
        self.append_child(GameTypeSubheader())

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

        # add a blank subheadline for the dotted-line separator
        self.append_child(Subheadline(""))

        # add a sport tag autocomplete
        self.append_child(SportTagSubheader())

        # add form submit and close buttons
        self.append_child(PostButtonSection())


class GameTypeSubheader(Subheadline):

    """ GameTypeSubheader extending Subheadline. """

    GAME_TYPE_SUBHEADER_CLASS = "game-type-subheader"


    def __init__(self):
        """ Construct a GameTypeSwitch toggling versus/with. """
        super(GameTypeSubheader, self).__init__(Copy.versus)
        self.append_class(self.GAME_TYPE_SUBHEADER_CLASS)

        self.append_child(GameTypeSwitch())


class GameTypeSwitch(SwitchInput):

    """ GameTypeSwitch extending SwitchInput. """

    GAME_TYPE_SWITCH_CLASS = "game-type-switch"


    def __init__(self):
        """ Construct a GameTypeSwitch toggling versus/with. """
        super(GameTypeSwitch, self).__init__(
                SQ_DATA.GAME_TYPE,
                SQ_VALUE.RIVALRY)
        self.append_class(self.GAME_TYPE_SWITCH_CLASS)

        # would be necessary if we associate a Label with the switch
        #self.set_id(SQ_DATA.GAME_TYPE)


class OpponentTagsGroup(Div):

    """ OpponentTagsGroup extending <div>, for grouping tags together with a
    Subheader. """

    OPPONENT_TAGS_GROUP_CLASS = "opponent-tags-group"


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
        self.append_class(self.OPPONENT_TAGS_GROUP_CLASS)
        self.append_class(game_type)
        # subheader for the group.
        if title is not None:
            self.append_child(OpponentTagsSubheader(title))

        # group of autocompletes
        tags = [result_type for n in range(number_of_tags)]
        self.append_child(OpponentTagsUL(tags))


class OpponentTagsSubheader(Subheadline):

    """ OpponentTagsSubheader extending Headline. """

    OPPONENT_TAGS_SUBHEADER_CLASS = "opponent-tags-subheader"


    def __init__(self, text=""):
        """ Construct an OpponentTagsHeadline. """
        super(OpponentTagsSubheader, self).__init__(text)
        self.append_class(self.OPPONENT_TAGS_SUBHEADER_CLASS)


class OpponentTagsUL(UL):

    """ OpponentTagsUL extending <ul>. """

    OPPONENT_TAGS_LIST_CLASS = "opponent-tags-list"


    def __init__(self, items):
        """ Construct an OpponentTagsUL. """
        super(OpponentTagsUL, self).__init__(items)
        self.append_class(self.OPPONENT_TAGS_LIST_CLASS)


    def set_list_item(self, item, index):
        """ Override superclass only changing LI to OpponentTagLI. """
        self.append_child(OpponentTagLI(item, index))


class OpponentTagLI(LI):

    """ OpponentTagLI extending LI. """

    OPPONENT_TAG_LIST_ITEM_CLASS = "opponent-tag-list-item"


    def __init__(self, item, index):
        """ Construct an OpponentTagLI. """
        super(OpponentTagLI, self).__init__(item, index)
        self.append_class(self.OPPONENT_TAG_LIST_ITEM_CLASS)


    def set_content(self, item):
        """ Generate the content for this Opponent tag list item. """


        metrics_by_opponent = "{0}[{1}][{2}]".format(
                SQ_DATA.METRICS_BY_OPPONENT,
                self._index,
                item)
        self.append_child(PlayerAutocomplete(metrics_by_opponent))


class SportTagSubheader(Subheadline):

    """ SportTagSubheader extending Subheadline. """

    SPORT_TAG_SUBHEADER_CLASS = "sport-tag-subheader"


    def __init__(self):
        """ Construct a SportTagSubheader. """
        super(SportTagSubheader, self).__init__("")
        self.append_class(self.SPORT_TAG_SUBHEADER_CLASS)
        self.append_child(SportAutocomplete(SQ_DATA.SPORT_ID))
