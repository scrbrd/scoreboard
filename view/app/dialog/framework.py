""" Module: framework

Element components that are for the dialog framework. Their classes are to be
used for positioning (unlike the components which should not be used for
positioning.

"""

from view.elements.base import Div
from view.elements.components import MainHeaderDiv
from view.elements.components import CloseButton, SqSubmitButton

from constants import DIALOG_CLASS, DIALOG_ID


class DialogHeader(MainHeaderDiv):

    """ Dialog Header extending MainHeaderDiv <div>. """


    def __init__(self, dialog_name):
        """ Construct a dialog header element tree. """
        super(DialogHeader, self).__init__(dialog_name)

        self.set_id(DIALOG_ID.DIALOG_HEADER)

        close_button = CloseButton()
        # set close button to disabled to prevent accidental dialog closure.
        close_button.set_disabled()
        self.append_child(close_button)


class SubmitButtonSection(Div):

    """ Component that has a SqSubmitButton in a <div> (for centering). """


    def __init__(self):
        """ Construct a dialog component for a post button. """
        super(SubmitButtonSection, self).__init__()
        self.set_classes([DIALOG_CLASS.SUBMIT_BUTTON_WRAPPER])

        self.append_child(SqSubmitButton())
