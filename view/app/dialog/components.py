""" Module: components

Element components that are reusable, non-positional, but only for dialogs.

"""

from view.app.copy import Copy
from view.elements.base import Div, TextInput, HiddenInput
from view.app.components import AppThumbnail, RemoveTagButton
from view.app.constants import IMAGE

from constants import DIALOG_CLASS


class AutocompleteInput(Div):

    """ AutocompleteInput extending Div.

    A set of Elements that capture both a TextInput and the other
    elements needed to handle autocomplete.

    """


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
        self.append_class(DIALOG_CLASS.AUTOCOMPLETE)

        # textinput doesn't actually contain data but does autocomplete.
        input = TextInput(name + "-" + DIALOG_CLASS.AUTOCOMPLETE_LABEL)
        input.set_placeholder(placeholder)
        input.append_class(DIALOG_CLASS.AUTOCOMPLETE_LABEL)
        self.append_child(input)

        # hiddeninput has actual data to submit.
        hidden = HiddenInput(name)
        hidden.append_class(DIALOG_CLASS.AUTOCOMPLETE_VALUE)
        self.append_child(hidden)


class TagAutocomplete(AutocompleteInput):

    """ TagAutocomplete extending AutocompleteInput.

    A set of Elements for autocomplete with an thumbnail and a clear
    button.

    """


    def __init__(self, name, placeholder=""):
        """ Construct a Autocomplete input for tagging.

        Required:
        str     name        name of the key to be submitted as part of the form

        Optional:
        str     placeholder placeholder to put inside TextInput

        """
        super(TagAutocomplete, self).__init__(name, placeholder)
        self.append_class(DIALOG_CLASS.AUTOCOMPLETE_TAG)

        thumbnail = AppThumbnail(None, Copy.app_name)
        thumbnail.append_class(DIALOG_CLASS.AUTOCOMPLETE_THUMBNAIL)
        self.insert_child(thumbnail)

        self.append_child(RemoveTagButton())


    def set_thumbnail(self):
        """ Set the thumbnail for this TagAutocomplete. """
        raise NotImplementedError("Abstract Method: SUBCLASS MUST OVERRIDE!")


class PlayerAutocomplete(TagAutocomplete):

    """ A PlayerAutocomplete extending TagAutocomplete. """


    def __init__(self, name):
        """ Construct an Autocomplete for tagging an Opponent in a Game.

        Required:
        str     name        name of the key to be submitted as part of the form

        """
        super(PlayerAutocomplete, self).__init__(
                name,
                Copy.opponent_tag_placeholder)
        self.append_class(DIALOG_CLASS.AUTOCOMPLETE_PLAYER)


    def set_thumbnail(self):
        """ Set the thumbnail for this TagAutocomplete. """
        return IMAGE.DEFAULT_OPPONENT_THUMBNAIL


class SportAutocomplete(TagAutocomplete):

    """ A SportAutocomplete extending TagAutocomplete. """


    def __init__(self, name):
        """ Construct an Autocomplete for tagging a Sport in a Game.

        Required:
        str     name        name of the key to be submitted as part of the form

        """
        super(SportAutocomplete, self).__init__(
                name,
                Copy.sport_tag_placeholder)
        self.append_class(DIALOG_CLASS.AUTOCOMPLETE_SPORT)


    def set_thumbnail(self):
        """ Set the thumbnail for this TagAutocomplete. """
        return IMAGE.DEFAULT_SPORT_THUMBNAIL
