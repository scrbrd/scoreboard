""" Module: components

Generic reusable components that are building blocks of
app-specific features.

"""
from copy import Copy

from base import Div, Span, OL, SubmitButton, Button, Header, LI, A, Img, Label
from base import CheckboxInput, RadioInput

# TODO: where should HEADED_LIST_ITEM be? it's used for ListHeader and
# HeadedListItem
HEADED_LIST_ITEM_CLASS = "headed-list-item"

# TODO: where should LIST_COLUMN_CLASS be? It's used for ListHeader and
# ListColumn
LIST_COLUMN_CLASS = "list-column"


class Thumbnail(Img):

    """ Thumbnail is an img element that identifies the associated object,
    extends <img>. """

    THUMBNAIL_CLASS = "thumbnail"


    def __init__(self, src, name=""):
        """ Construct a thumbnail tag.

        Required:
        str src         the url of the thumbnail
        str name        the name associated with the image

        """
        super(Thumbnail, self).__init__(src, name)
        self.append_class(self.THUMBNAIL_CLASS)


class NonRoutingAnchor(A):

    """ NonRoutingAnchor is an anchor that won't be handled by Router/AJAX.

    Required:
    url         url             Specifies the value for href
    str         text            Text to display.

    """

    NON_ROUTING_ANCHOR_CLASS = "non-routing-anchor"


    def __init__(self, url, text):
        """ Construct an anchor that doesn't use internal routing. """
        super(NonRoutingAnchor, self).__init__(url, text)
        self.append_class(self.NON_ROUTING_ANCHOR_CLASS)


class LoginAnchor(NonRoutingAnchor):

    """ Login Anchor that extends NonRoutingAnchor <a>. """

    LOGIN_ANCHOR_CLASS = "login-anchor"


    def __init__(self, login_url, text=Copy.login):
        """ Construct a login anchor tag. """
        super(LoginAnchor, self).__init__(login_url, text)

        self.append_class(self.LOGIN_ANCHOR_CLASS)


class FacebookLoginAnchor(LoginAnchor):

    """ Facebook Login Anchor that extends LoginAnchor. """

    FACEBOOK_LOGIN_ANCHOR_CLASS = "facebook-login-anchor"


    def __init__(self, login_url, text=Copy.login_with_facebook):
        """ Construct a facebook login anchor tag. """
        super(FacebookLoginAnchor, self).__init__(login_url, text)

        self.append_class(self.FACEBOOK_LOGIN_ANCHOR_CLASS)


class PostButton(SubmitButton):

    """ PostButton extending <button type="submit">. """


    def __init__(self):
        """ Construct a close button tag. """
        super(PostButton, self).__init__(Copy.post)


class CloseButton(Button):

    """ Close Button button that extends <button>. """

    CLOSE_BUTTON_CLASS = "close-button"


    def __init__(self):
        """ Construct a close button tag. """
        super(CloseButton, self).__init__(Copy.close)

        self.append_class(self.CLOSE_BUTTON_CLASS)


class CreateButton(Button):

    """ CreateButton that extends <button>. """

    CREATE_BUTTON_CLASS = "create-button"
    PLUS = "+"


    def __init__(self):
        """ Construct an add button tag. """
        super(CreateButton, self).__init__(self.PLUS)

        self.append_class(self.CREATE_BUTTON_CLASS)


class MenuButton(Button):

    """ MenuButton that extends <button>, currently for invite friends. """

    MENU_BUTTON_CLASS = "menu-button"
    MENU = "menu"


    def __init__(self):
        """ Construct a menu button tag. """
        super(MenuButton, self).__init__(self.MENU)

        self.append_class(self.MENU_BUTTON_CLASS)


class MainHeader(Header):

    """ Main Header extends <header>."""

    MAIN_HEADER_CLASS = "main-header"


    def __init__(self, title):
        """ Construct Main Header tag. """
        super(MainHeader, self).__init__()
        self.append_class(self.MAIN_HEADER_CLASS)

        # insert to separate text from background
        titleContainer = Div()
        titleContainer.set_text(title)

        self.append_child(titleContainer)


class MultiColumnLI(LI):

    """ An LI for multiple columns extends <li>. """


    def set_column(self, element):
        """ Add a single column to the <li>. """
        element.append_class(LIST_COLUMN_CLASS)
        self.append_child(element)


class NumberedList(OL):

    """ A numbered list extends <ol>. """

    NUMBERED_LIST_CLASS = "numbered-list"


    def __init__(self, items):
        """ Construct a numbered <ol>. """
        super(NumberedList, self).__init__(items)
        self.append_class(self.NUMBERED_LIST_CLASS)


class HeadedList(Div):

    """ A list with headings that extends <div>. """

    HEADED_LIST_CLASS = "headed-list"


    def __init__(self, headings, items):
        """ Construct a list with headings. """
        super(HeadedList, self).__init__()
        self.append_class(self.HEADED_LIST_CLASS)

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

    LIST_HEADER_CLASS = "list-header"


    def __init__(self, headings):
        """ Constuct a list header. """
        super(ListHeader, self).__init__()
        self.append_class(self.LIST_HEADER_CLASS)
        self.append_class(HEADED_LIST_ITEM_CLASS)

        for h in headings:
            col_head = Div()
            col_head.set_text(h)
            col_head.append_class(LIST_COLUMN_CLASS)
            self.append_child(col_head)


class HeadedListItem(MultiColumnLI):

    """ A list item for a HeadedList that extends MultiColumnLI. """


    def __init__(self, item, index):
        """ Construct a list item for a HeadedList. """
        super(HeadedListItem, self).__init__(item, index)
        self.append_class(HEADED_LIST_ITEM_CLASS)


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

    SWITCH_CONTROL_CLASS = "switch-control"
    SWITCH_ON_CLASS = "switch-on"
    SWITCH_KNOB_CLASS = "switch-knob"
    SWITCH_CHECKBOX_CLASS = "switch-checkbox"


    def __init__(
            self,
            name,
            on_value="",
            off_text="",
            on_text="",
            is_on=False):
        super(SwitchInput, self).__init__()
        self.append_class(self.SWITCH_CONTROL_CLASS)

        # this is important for making sure the various components of the
        # switch are in sync with one another.
        if is_on:
            self.append_class(self.SWITCH_ON_CLASS)

        span = Span()
        span.append_class(self.SWITCH_KNOB_CLASS)
        # TODO: set on/off text in content for css class switch-knob, add style
        # and positioning to the class, and override display of |/0.
        #span.set_text(off_text)
        #span.set_tail(on_text)
        self.append_child(span)

        checkbox = CheckboxInput(name, on_value, is_on)
        checkbox.append_class(self.SWITCH_CHECKBOX_CLASS)
        self.append_child(checkbox)


    def _knob(self):
        """ Private helper returns SwitchInput's knob Span child.

        Note: if more children are appended before knob Span, update
        this method to reflect its child rank in the Div.

        """
        return self.first_child()


    def _switch(self):
        """ Private helper returns SwitchInput's CheckboxInput child.

        Note: if more children are appended after CheckboxInput, update
        this method to reflect its child rank in the Div.

        """
        return self.last_child()


    def set_on(self, is_on):
        """ Set the SwitchInput to on/off.

        Provide a wrapper for subclasses who don't have a reference to
        this Element's child CheckboxInput.

        """
        self._switch().set_checked(is_on)


class FloatContainer(Div):

    """ FloatContainer is used as an inner div to fix rendering quirks.

    The quirk is that the height of the outer element won't extend to include
    the inner floating elements. By creating this floatable div, which will
    also float, and thus extend the box, we give it the properties that the
    outer div would like to display (e.g. background color). The benefit is
    that the outer shell can still be positioned based on its own container,
    which won't happen correctly if it floats too.

    """

    FLOAT_CONTAINER_CLASS = "float-container"


    def __init__(self):
        """ Construct a <div> that floats. """
        super(FloatContainer, self).__init__()
        self.append_class(self.FLOAT_CONTAINER_CLASS)
