""" Module: framework

Element components that are for the dialog framework. Their classes are to be
used for positioning (unlike the components which should not be used for
positioning.

"""

from view.elements.base import Header, Div
from view.elements.components import MainHeaderDiv
from view.elements.components import DefaultCloseButton, DefaultSubmitButton

from constants import DIALOG_CLASS


class DialogHeader(Header):

    """ Dialog Header extending <header> and including <h2>. """


    def __init__(self, dialog_name):
        """ Construct a dialog header element tree. """
        super(DialogHeader, self).__init__()

        self.append_child(MainHeaderDiv(dialog_name))
        self.append_child(DefaultCloseButton())


class SubmitButtonSection(Div):

    """ Component that has a submit button in a <div> (for centering). """


    def __init__(self):
        """ Construct a dialog component for a submit button. """
        super(SubmitButtonSection, self).__init__()
        self.set_classes([DIALOG_CLASS.SUBMIT_BUTTON_WRAPPER])

        self.append_child(DefaultSubmitButton())
