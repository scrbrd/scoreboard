""" Module: components

Element components that are reusable, non-positional, but only for dialogs.

"""

from view.app.copy import Copy
from view.elements.base import Div, TextInput, HiddenInput
from view.app.components import AppThumbnail, RemoveTagButton
from view.app.constants import IMAGE


class AutocompleteInput(Div):

    """ AutocompleteInput extending Div.

    A set of Elements that capture both a TextInput and the other
    elements needed to handle autocomplete.

    """

    AUTOCOMPLETE_CLASS = "autocomplete"
    AUTOCOMPLETE_LABEL_CLASS = "autocomplete-label"
    AUTOCOMPLETE_VALUE_CLASS = "autocomplete-value"


    def __init__(
            self,
            name,
            placeholder=""):
        """ Construct a Autocomplete input set.

        Required:
        str     name                name of key to be submited as part of form

        Optional:
        str     autocomple_class    class representing which type of
                                    autocomplete
        str     placeholder         placeholder to put inside TextInput

        """
        super(AutocompleteInput, self).__init__()
        self.append_class(self.AUTOCOMPLETE_CLASS)

        # textinput doesn't actually contain data but does autocomplete.
        input_div = Div()  # for overflow auto and automatic width
        input = TextInput(name + "-" + self.AUTOCOMPLETE_LABEL_CLASS)
        input.set_placeholder(placeholder)
        input.append_class(self.AUTOCOMPLETE_LABEL_CLASS)
        input_div.append_child(input)
        self.append_child(input_div)

        # hiddeninput has actual data to submit.
        hidden = HiddenInput(name)
        hidden.append_class(self.AUTOCOMPLETE_VALUE_CLASS)
        self.append_child(hidden)


class TagAutocomplete(AutocompleteInput):

    """ TagAutocomplete extending AutocompleteInput.

    A set of Elements for autocomplete with an thumbnail and a clear
    button.

    """

    AUTOCOMPLETE_TAG_CLASS = "autocomplete-tag"
    AUTOCOMPLETE_THUMBNAIL_CLASS = "autocomplete-thumbnail"


    def __init__(self, name, placeholder=""):
        """ Construct a Autocomplete input for tagging.

        Required:
        str     name        name of the key to be submitted as part of the form

        Optional:
        str     placeholder placeholder to put inside TextInput

        """
        super(TagAutocomplete, self).__init__(name, placeholder)
        self.append_class(self.AUTOCOMPLETE_TAG_CLASS)

        thumbnail = AppThumbnail(None, Copy.app_name)
        thumbnail.append_class(self.AUTOCOMPLETE_THUMBNAIL_CLASS)
        self.insert_child(thumbnail)

        self.insert_child(RemoveTagButton())


    def set_thumbnail(self):
        """ Set the thumbnail for this TagAutocomplete. """
        raise NotImplementedError("Abstract Method: SUBCLASS MUST OVERRIDE!")


class PlayerAutocomplete(TagAutocomplete):

    """ A PlayerAutocomplete extending TagAutocomplete. """

    AUTOCOMPLETE_PLAYER_CLASS = "autocomplete-player"


    def __init__(self, name):
        """ Construct an Autocomplete for tagging an Opponent in a Game.

        Required:
        str     name        name of the key to be submitted as part of the form

        """
        super(PlayerAutocomplete, self).__init__(
                name,
                Copy.opponent_tag_placeholder)
        self.append_class(self.AUTOCOMPLETE_PLAYER_CLASS)


    def set_thumbnail(self):
        """ Set the thumbnail for this TagAutocomplete. """
        return IMAGE.DEFAULT_OPPONENT_THUMBNAIL


class SportAutocomplete(TagAutocomplete):

    """ A SportAutocomplete extending TagAutocomplete. """

    AUTOCOMPLETE_SPORT_CLASS = "autocomplete-sport"


    def __init__(self, name):
        """ Construct an Autocomplete for tagging a Sport in a Game.

        Required:
        str     name        name of the key to be submitted as part of the form

        """
        super(SportAutocomplete, self).__init__(
                name,
                Copy.sport_tag_placeholder)
        self.append_class(self.AUTOCOMPLETE_SPORT_CLASS)


    def set_thumbnail(self):
        """ Set the thumbnail for this TagAutocomplete. """
        return IMAGE.DEFAULT_SPORT_THUMBNAIL
