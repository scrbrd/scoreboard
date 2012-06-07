""" Module: components

Generic reusable components that are building blocks of
app-specific features.

"""
from view.constants import APP_CLASS
from view.app_copy import Copy
from view.html.elements import Div, SubmitButton, Button, H2
from view.html.elements import Span, A


class AddButton(A):

    """ Add Button anchor that extends <a>. """

    def __init__(self, link):
        """ Construct an add button anchor tag. """
        super(AddButton, self).__init__(link)

        self.set_text("+")
        self.set_classes([APP_CLASS.ADD_BUTTON, APP_CLASS.JS_LINK])


class DefaultCloseButton(Button):

    """ Default Close Button button that extends <button>. """

    def __init__(self):
        """ Construct a close button tag. """
        super(DefaultCloseButton, self).__init__()

        self.append_class(APP_CLASS.CLOSE_BUTTON)
        self.set_text(Copy.close)


class DefaultSubmitButton(SubmitButton):

    """ Submit Button button that extends <button type="submit">. """

    def __init__(self):
        """ Construct a submit button tag. """
        super(DefaultSubmitButton, self).__init__()

        self.append_class(APP_CLASS.SUBMIT_BUTTON)
        self.set_text(Copy.submit)


class MainHeaderDiv(Div):

    """ Main Header Div extends <div>.

    The div is for the background image and anything external. The
    inside h2 is for managing the font layout, specifically because
    some fonts aren't centered correctly.

    """

    def __init__(self, title):
        """ Construct Main Header tag. """
        super(MainHeaderDiv, self).__init__()
        self.set_classes([APP_CLASS.MAIN_HEADER])

        # insert h2 and span to separate text from background
        span = Span()
        span.set_text(title)

        h2 = H2()
        h2.append_child(span)
        self.append_child(h2)
