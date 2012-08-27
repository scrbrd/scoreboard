""" Module: framework

Element components that are for the dialog framework. Their classes are to be
used for positioning (unlike the components which should not be used for
positioning.

"""

from view.elements.base import Div, Section
from view.elements.components import MainHeader
from view.elements.components import PostButton, CloseButton
from view.app.framework import ContentWrapper

from constants import DIALOG_ID


class DialogHeader(MainHeader):

    """ Dialog Header extending MainHeader<header>. """

    DIALOG_HEADER_CLASS = "dialog-header"


    def __init__(self, dialog_name):
        """ Construct a dialog header element tree. """
        super(DialogHeader, self).__init__(dialog_name)

        self.append_class(self.DIALOG_HEADER_CLASS)
        self.set_id(DIALOG_ID.DIALOG_HEADER)

        close_button = CloseButton()
        # set close button to disabled to prevent accidental dialog closure.
        close_button.set_disabled()
        self.append_child(close_button)


class DialogContentWrapper(ContentWrapper):

    """ DialogContentWrapper adds a wrapper for a dialog scroller. """


    def __init__(self, content_section):
        """ Construct a wrapper for a scroller.

        Required:
        Element     content_section     the content that the scroller wraps

        """
        super(DialogContentWrapper, self).__init__(
                DIALOG_ID.DIALOG_CONTENT_WRAPPER,
                DIALOG_ID.DIALOG_CONTENT_CONTAINER,
                content_section)


# TODO: subclass this from an abstract app.page.frameworkAppPageContentSection
# when it exists.
class DialogContentSection(Section):

    """ DialogContentSection encapsulates generic Dialog Page attributes. """


    def __init__(self):
        """ Construct a dialog's content section element tree. """
        super(DialogContentSection, self).__init__()


class PostButtonSection(Div):

    """ Component that has a PostButton in a <div> (for centering). """


    def __init__(self):
        """ Construct a dialog component for a post button. """
        super(PostButtonSection, self).__init__()
        self.append_child(PostButton())
