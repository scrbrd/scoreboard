""" Module: framework

Element components that are for the tab framework.

"""
import json

from view.constants import SQ_DATA 
from view.html.elements import H1, Nav, Footer, Section
from view.html.elements import UL, LI
from view.html.elements import A
from view.html.components import AddButton, MainHeaderDiv

from constants import TAB_CLASS, TAB_ID


class AppHeader(H1):

    """ App header extending <h1>. """


    def __init__(self, app_name):
        """ Construct an app header element tree. """
        super(AppHeader, self).__init__()
        self.set_text(app_name)


class ContextHeader(MainHeaderDiv):

    """ Context header extending MainHeaderDiv <div>. """


    def __init__(self, context, rivals):
        """ Construct a context header element tree. """
        super(ContextHeader, self).__init__(context.name)

        # set context data
        self.set_id(TAB_ID.CONTEXT)
        self.set_data(SQ_DATA.ID, context.id)
        self.set_data(SQ_DATA.OBJECT_TYPE, context.type)

        # set rivals data
        view_rivals = []
        for r in rivals:
            view_rivals.append({SQ_DATA.ID: r.id, SQ_DATA.NAME: r.name})
        self.set_data(SQ_DATA.RIVALS, json.dumps(view_rivals))


class NavHeader(Nav):

    """ Nav header extending <nav>. """


    def __init__(self, items, special_item=None, special_item_index=0):
        """ Construct a nav header element tree. """
        super(NavHeader, self).__init__(
                items,
                special_item,
                special_item_index)

        self.append_classes([TAB_CLASS.SECOND_HEADER])


    def set_list(self, items):
        """ Construct and add the NavUL list for this NavHeader. """
        self.append_child(NavUL(items))


class NavUL(UL):

    """ Nav header extending <nav>. """


    def __init__(self, items):
        """ Construct a nav header element tree. """
        super(NavUL, self).__init__(items)

        # TODO: is there css we want applied even to this base class?
        #self.append_classes([])


    def set_list_item(self, item, index):
        """ Construct and add a link list item as this NavUL's child. """
        self.append_child(NavHeaderLI(item, index))


class NavHeaderLI(LI):

    """ Nav header list item extending <li>.

        <li><a href="/foo">bar</a></li>

    """


    def set_content(self, item):
        """ Set content for the NavHeaderLI. """
        a = A(item)
        # TODO: this is a hardcoded string and not a constant because once we
        # have a Link class [and an Item interface or some such thing for it
        # to implement] we will just be accessing properties there. this makes
        # it more obvious what to change.
        a.append_class(item["class"])
        self.append_child(a)


class AppFooter(Footer):

    """ App footer contains a fixed add button in a <footer>. """

    def __init__(self):
        """ Construct the apps' footer element tree. """
        super(AppFooter, self).__init__()

        # TODO this is a hardcoded string and not a constant because once we
        # have a Link class we will just be accessing its properties.
        add_link = {
            "text": "+",
            "href": "/create/game",
        }

        add_button = AddButton(add_link)
        self.append_child(add_button)


class TabSection(Section):

    """ Tab section encapsulates the generic tab attributes around i
    <section>. """

    def __init__(self, page_name):
        """ Construct a tab section element tree.

        Required:
        string  page_name   the page name of this tab.

        """
        super(TabSection, self).__init__()
        self.set_id(TAB_ID.CONTENT)
        self.set_data(SQ_DATA.PAGE_NAME, page_name)
