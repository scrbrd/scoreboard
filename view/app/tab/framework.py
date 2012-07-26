""" Module: framework

Element components that are for the tab framework.

"""

from exceptions import NotImplementedError

from view.constants import SQ_DATA

from view.app_copy import Copy

from constants import TAB_CLASS, TAB_ID

from view.elements.base import H1, Nav, Footer, Section, UL, LI, A, Div
from view.elements.components import CreateButton, MenuButton, MainHeaderDiv


class AppHeader(H1):

    """ App header extending <h1>. """


    def __init__(self, app_name):
        """ Construct an app header element tree. """
        super(AppHeader, self).__init__()
        self.set_text(app_name)


class TabHeader(MainHeaderDiv):

    """ TabHeader extending MainHeaderDiv <div>. """


    def __init__(self, context):
        """ Construct a TabHeader element tree. """
        # TODO: remove context id bit, but put back the context.name
        super(TabHeader, self).__init__(Copy.app_name)

        self.set_id(TAB_ID.TAB_HEADER)
        # set context data
        self.set_data(SQ_DATA.ID, context.id)

        # TODO: Make the menu button go to invite friends
        null_link = {
            "text": "menu",
            "href": "",
        }
        self.append_child(MenuButton(null_link))

        # TODO this is a hardcoded string and not a constant because once we
        # have a Link class we will just be accessing its properties.
        create_link = {
            "text": "+",
            "href": "/create/game",
        }

        create_button = CreateButton(create_link)
        self.append_child(create_button)


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


# TODO: remove this class when removing [Rankings,Game]TabSection
class TabSection(Section):

    """ TabSection encapsulates generic tab attributes around <section>. """


    def __init__(self, page_name):
        """ Construct a tab section element tree.

        Required:
        string  page_name   the page name of this tab.

        """
        super(TabSection, self).__init__()
        self.set_id(TAB_ID.CONTENT)


# TODO: subclass this from an abstract app.page.framework.PageContentSection
# when it exists. DialogContentSection would be similar.
class TabContentSection(Section):

    """ TabContentSection encapsulates generic AppPage attributes. """


    def __init__(self):
        """ Construct a tab's content section element tree. """
        super(TabContentSection, self).__init__()
        # TODO: set this in an abstract superclass when one exists and probably
        # use PAGE_ID.CONTENT instead.
        self.set_id(TAB_ID.CONTENT)


    def set_properties_content(self, properties):
        """ Construct and add properties content to this content section. """
        self.append_child(PropertiesDiv(properties))


    def set_summary_content(self, summary):
        """ Construct and add summary content to this content section. """
        self.append_child(SummaryDiv(summary))


    def set_feed_content(self, feed):
        """ Construct and add feed content to this content section. """
        self.append_child(FeedDiv(feed))


class PropertiesDiv(Div):

    """ PropertiesDiv encapsulates a tab's properties attribute <div>. """


    def __init__(self, properties):
        """ Construct a tab's properties content element tree. """
        super(PropertiesDiv, self).__init__()
        self.set_id(TAB_ID.PROPERTIES)
        self.set_content(properties)


    def set_content(self, properties):
        """ Construct and add content as a direct child. """
        raise NotImplementedError("Abstract Method: SUBCLASS MUST OVERRIDE!")


class SummaryDiv(Div):

    """ SummaryDiv encapsulates a tab's summary attribute <div>. """


    def __init__(self, summary):
        """ Construct a tab's summary content element tree. """
        super(SummaryDiv, self).__init__()
        self.set_id(TAB_ID.SUMMARY)
        self.set_content(summary)


    def set_content(self, summary):
        """ Construct and add content as a direct child. """
        raise NotImplementedError("Abstract Method: SUBCLASS MUST OVERRIDE!")


class FeedDiv(Div):

    """ FeedDiv encapsulates a tab's feed attribute <div>. """


    def __init__(self, feed):
        """ Construct a tab's feed content element tree. """
        super(FeedDiv, self).__init__()
        self.set_id(TAB_ID.FEED)
        self.set_content(feed)


    def set_content(self, feed):
        """ Construct and add content as a direct child. """
        raise NotImplementedError("Abstract Method: SUBCLASS MUST OVERRIDE!")