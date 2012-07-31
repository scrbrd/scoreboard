""" Module: components

Generic reusable components that are building blocks of
app-specific features.

"""
from view.app_copy import Copy

from constants import COMPONENT_CLASS

from base import Div, Span, OL, SubmitButton, Button, Header, LI, A, Img, Label
from base import CheckboxInput, RadioInput


class Thumbnail(Img):

    """ Thumbnail is an img element that identifies the associated object,
    extends <img>. """


    def __init__(self, src, name):
        """ Construct a thumbnail tag.

        Required:
        str src         the url of the thumbnail
        str name        the name associated with the image

        """
        super(Thumbnail, self).__init__(src, name)
        self.append_class(COMPONENT_CLASS.THUMBNAIL)


class NonRoutingAnchor(A):

    """ NonRoutingAnchor is an anchor that won't be handled by Router/AJAX.

    Required:
    url         url             Specifies the value for href
    str         text            Text to display.

    """


    def __init__(self, url, text):
        """ Construct an anchor that doesn't use internal routing. """
        super(NonRoutingAnchor, self).__init__(url, text)
        self.append_class(COMPONENT_CLASS.NON_ROUTING_ANCHOR)


class LoginAnchor(NonRoutingAnchor):

    """ Login Anchor that extends NonRoutingAnchor <a>. """

    def __init__(self, login_url, text=Copy.login):
        """ Construct a login anchor tag. """
        super(LoginAnchor, self).__init__(login_url, text)

        self.append_class(COMPONENT_CLASS.LOGIN_ANCHOR)


class FacebookLoginAnchor(LoginAnchor):

    """ Facebook Login Anchor that extends LoginAnchor. """


    def __init__(self, login_url, text=Copy.facebook_login):
        """ Construct a facebook login anchor tag. """
        super(FacebookLoginAnchor, self).__init__(login_url, text)

        self.append_class(COMPONENT_CLASS.FACEBOOK_LOGIN_ANCHOR)


class PostButton(SubmitButton):

    """ PostButton extending <button type="submit">. """


    def __init__(self):
        """ Construct a close button tag. """
        super(PostButton, self).__init__(Copy.post)


class CloseButton(Button):

    """ Close Button button that extends <button>. """


    def __init__(self):
        """ Construct a close button tag. """
        super(CloseButton, self).__init__(Copy.close)

        self.append_class(COMPONENT_CLASS.CLOSE_BUTTON)


class CreateButton(Button):

    """ CreateButton that extends <button>. """

    PLUS = "+"


    def __init__(self):
        """ Construct an add button tag. """
        super(CreateButton, self).__init__(self.PLUS)

        self.append_class(COMPONENT_CLASS.CREATE_BUTTON)


class MenuButton(Button):

    """ MenuButton that extends <button>, currently for invite friends. """

    MENU = "menu"


    def __init__(self):
        """ Construct a menu button tag. """
        super(MenuButton, self).__init__(self.MENU)

        self.append_class(COMPONENT_CLASS.MENU_BUTTON)


class MainHeaderDiv(Div):

    """ Main Header Div extends <div>.

    The div is for the background image and anything external. The
    inside h2 is for managing the font layout, specifically because
    some fonts aren't centered correctly.

    """


    def __init__(self, title):
        """ Construct Main Header tag. """
        super(MainHeaderDiv, self).__init__()
        self.append_class(COMPONENT_CLASS.MAIN_HEADER)

        # insert to separate text from background
        titleContainer = Div()
        titleContainer.set_text(title)

        self.append_child(titleContainer)


class MultiColumnLI(LI):

    """ An LI for multiple columns extends <li>. """


    def set_column(self, element):
        """ Add a single column to the <li>. """
        element.append_class(COMPONENT_CLASS.LIST_COLUMN)
        self.append_child(element)


class NumberedList(OL):

    """ A numbered list extends <ol>. """


    def __init__(self, items):
        """ Construct a numbered <ol>. """
        super(NumberedList, self).__init__(items)
        self.append_class(COMPONENT_CLASS.NUMBERED_LIST)


class HeadedList(Div):

    """ A list with headings that extends <div>. """


    def __init__(self, headings, items):
        """ Construct a list with headings. """
        super(HeadedList, self).__init__()
        self.append_class(COMPONENT_CLASS.HEADED_LIST)

        self.set_headings(headings)
        self.set_list(items)


    def set_headings(self, headings):
        """ Set the header element for this list. """
        self.append_child(ListHeader(headings))


    def set_list(self, items):
        """ Set the list element for this list. """
        raise NotImplementedError("Abstract Method: SUBCLASS MUST OVERRIDE!")


class ListHeader(Header):

    """ A header for a list that extends <header>. """


    def __init__(self, headings):
        """ Constuct a list header. """
        super(ListHeader, self).__init__()
        self.append_class(COMPONENT_CLASS.LIST_HEADER)
        self.append_class(COMPONENT_CLASS.HEADED_LIST_ITEM)

        for h in headings:
            col_head = Div()
            col_head.set_text(h)
            col_head.append_class(COMPONENT_CLASS.LIST_COLUMN)
            self.append_child(col_head)


class HeadedListItem(MultiColumnLI):

    """ A list item for a HeadedList that extends MultiColumnLI. """


    def __init__(self, item, index):
        """ Construct a list item for a HeadedList. """
        super(HeadedListItem, self).__init__(item, index)
        self.append_class(COMPONENT_CLASS.HEADED_LIST_ITEM)


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


class SwitchInput(Div):

    """ SwitchInput extending Div.

    <div class="switch">
        <span class="knob"></span>
        <input type="checkbox" />
    </div>

    """


    def __init__(
            self,
            name,
            value="",
            off_text="",
            on_text="",
            is_on=False):
        super(SwitchInput, self).__init__()
        self.append_class(COMPONENT_CLASS.SWITCH)

        span = Span()
        span.append_class(COMPONENT_CLASS.KNOB)
        span.set_text(off_text)
        span.set_tail(on_text)
        self.append_child(span)

        self.append_child(CheckboxInput(name, value, is_on))
