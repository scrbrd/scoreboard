""" Module: components

Generic reusable components that are building blocks of
app-specific features.

"""

from view.constants import APP_CLASS
from view.app_copy import Copy

from constants import COMPONENT_CLASS

from base import Div, OL, SubmitButton, Button, Header, LI, A
from base import RadioInput, Label


class CreateButton(A):

    """ CreateButton anchor that extends <a>. """


    def __init__(self, link):
        """ Construct an add button anchor tag. """
        super(CreateButton, self).__init__(link)

        self.set_text("+")
        self.append_classes([COMPONENT_CLASS.CREATE_BUTTON, APP_CLASS.JS_LINK])


class MenuButton(A):

    """ MenuButton anchor that extends <a> currently for invite friends. """


    def __init__(self, link):
        """ Construct a menu button anchor tag. """
        super(MenuButton, self).__init__(link)

        self.set_text("menu")
        self.append_classes([COMPONENT_CLASS.MENU_BUTTON, APP_CLASS.JS_LINK])


class LoginButton(A):

    """ Login Button anchor that extends <a>. """


    def __init__(self, login_link):
        """ Construct a login button anchor tag. """
        super(LoginButton, self).__init__(login_link)

        self.set_text(Copy.login)
        self.append_classes([COMPONENT_CLASS.LOGIN_BUTTON])


class FacebookLoginButton(LoginButton):

    """ Facebook Login Button anchor that extends LoginButton. """


    def __init__(self, login_link):
        """ Construct a facebook login button anchor tag. """
        super(FacebookLoginButton, self).__init__(login_link)

        self.set_text(Copy.facebook_login)
        self.append_classes([
            COMPONENT_CLASS.FACEBOOK_LOGIN_BUTTON,
            APP_CLASS.EXTERNAL_LINK,
        ])


class DefaultCloseButton(Button):

    """ Default Close Button button that extends <button>. """


    def __init__(self):
        """ Construct a close button tag. """
        super(DefaultCloseButton, self).__init__()

        self.append_classes([COMPONENT_CLASS.CLOSE_BUTTON])
        self.set_text(Copy.close)


class DefaultSubmitButton(SubmitButton):

    """ Submit Button button that extends <button type="submit">. """


    def __init__(self):
        """ Construct a submit button tag. """
        super(DefaultSubmitButton, self).__init__()

        self.append_classes([COMPONENT_CLASS.SUBMIT_BUTTON])
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
        self.append_classes([COMPONENT_CLASS.MAIN_HEADER])

        # insert to separate text from background
        titleContainer = Div()
        titleContainer.set_text(title)

        self.append_child(titleContainer)


class MultiColumnLI(LI):

    """ An LI for multiple columns extends <li>. """


    def set_column(self, element):
        """ Add a single column to the <li>. """
        element.append_classes([COMPONENT_CLASS.LIST_COLUMN])
        self.append_child(element)


class NumberedList(OL):

    """ A numbered list extends <ol>. """


    def __init__(self, items):
        """ Construct a numbered <ol>. """
        super(NumberedList, self).__init__(items)
        self.append_classes([COMPONENT_CLASS.NUMBERED_LIST])


class HeadedList(Div):

    """ A list with headings that extends <div>. """


    def __init__(self, headings, items):
        """ Construct a list with headings. """
        super(HeadedList, self).__init__()
        self.append_classes([COMPONENT_CLASS.HEADED_LIST])

        self.set_headings(headings)
        self.set_list(items)


    def set_headings(self, headings):
        """ Set the header element for this list. """
        self.append_child(ListHeader(headings))


    def set_list(self, items):
        """ Set the list element for this list. """
        raise NotImplementedError()


class ListHeader(Header):

    """ A header for a list that extends <header>. """


    def __init__(self, headings):
        """ Constuct a list header. """
        super(ListHeader, self).__init__()
        self.append_classes([
            COMPONENT_CLASS.LIST_HEADER,
            COMPONENT_CLASS.HEADED_LIST_ITEM,
        ])

        for h in headings:
            col_head = Div()
            col_head.set_text(h)
            col_head.append_classes([COMPONENT_CLASS.LIST_COLUMN])
            self.append_child(col_head)


class HeadedListItem(MultiColumnLI):

    """ A list item for a HeadedList that extends MultiColumnLI. """


    def __init__(self, item, index):
        """ Construct a list item for a HeadedList. """
        super(HeadedListItem, self).__init__(item, index)
        self.append_classes([COMPONENT_CLASS.HEADED_LIST_ITEM])


class LabeledRadioInput(Div):

    """ RadioInput with an associated Label. """


    def __init__(self, text, name, value, id, checked=False):
        """ Construct a RadioInput with an associated Label. """
        super(LabeledRadioInput, self).__init__()
        self.append_child(RadioInput(name, value, id, checked))
        self.append_child(Label(text, id))


class RadioInputGroup(Div):

    """ Set of related Radio input elements.

    Note that this is not a standard HTML tag. We are pioneers.

    Required:
    str     name                    name of a RadioInput
    dict    options                 text/id tuples keyed on value

    Optional:
    bool    default_checked_value   which value is checked by default?

    """


    def __init__(self, name, options, default_checked_value=None):
        """ Construct a Div with a set of <input type="radio"> buttons. """
        super(RadioInputGroup, self).__init__()

        # if no options or default unspecified or non-existent, use first
        if options and default_checked_value not in options:
            default_checked_value = options.keys()[0]

        for value, (text, id) in options.items():
            self.append_child(LabeledRadioInput(
                    text,
                    name,
                    value,
                    (id if id else value),
                    (value == default_checked_value)))
