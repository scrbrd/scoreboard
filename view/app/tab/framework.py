""" Module: framework

Element components that are for the tab framework.

"""

from view.constants import SQ_DATA
from view.elements.base import Section, Div
from view.elements.components import CreateButton, MenuButton, MainHeader
from view.app.components import CoverPhoto, Headline
from view.app.copy import Copy
from view.app.framework import ContentWrapper

from constants import TAB_CLASS, TAB_ID
from story import StoryFactory


class TabHeader(MainHeader):

    """ TabHeader extending MainHeader <header>. """


    def __init__(self, context):
        """ Construct a TabHeader element tree. """
        # TODO: remove context id bit, but put back the context.name
        super(TabHeader, self).__init__(Copy.app_name)

        self.append_class(TAB_CLASS.TAB_HEADER)
        self.set_id(TAB_ID.TAB_HEADER)

        # set context data
        self.set_data(SQ_DATA.ID, context.id)

        self.append_child(MenuButton())
        self.append_child(CreateButton())


class TabContentWrapper(ContentWrapper):

    """ TabContentWrapper allows a scroller object to wrap the tab's
    content. """


    def __init__(self, content_section):
        """ Construct a wrapper for a scroller object to manipulate.

        Required:
        Element     content_section     the content that the scroller wrap.

        """
        super(TabContentWrapper, self).__init__(
                TAB_ID.TAB_CONTENT_WRAPPER,
                TAB_ID.TAB_CONTENT_CONTAINER,
                content_section)


# TODO: subclass this from an abstract app.page.framework.AppPageContentSection
# when it exists. DialogContentSection would be similar.
class TabContentSection(Section):

    """ TabContentSection encapsulates generic AppPage attributes.

    Person      _current_person     the current User's Person

    """


    def __init__(self, context, aggregations, objects, current_person):
        """ Construct a tab's content section element tree. """
        super(TabContentSection, self).__init__()
        self._current_person = current_person

        # TODO: set this in an abstract superclass when one exists and probably
        # use PAGE_ID.CONTENT instead.
        self.set_id(TAB_ID.CONTENT)

        self.append_child(self.construct_properties_content(context))
        self.append_child(self.construct_summary_content(aggregations))
        self.append_child(self.construct_feed_content(objects))


    def construct_properties_content(self, context):
        """ Construct and add properties to this content section. """
        return PropertiesDiv(context)


    def construct_summary_content(self, aggregations):
        """ Construct and add summary content to this content section. """
        return SummaryDiv(aggregations)


    def construct_feed_content(self, objects):
        """ Construct and add feed content to this content section. """
        return FeedDiv(self._current_person, objects)


class PropertiesDiv(Div):

    """ PropertiesDiv encapsulates a tab's properties attribute <div>. """


    def __init__(self, context):
        """ Construct a tab's properties content element tree. """
        super(PropertiesDiv, self).__init__()
        self.set_id(TAB_ID.PROPERTIES)
        self.set_content(context)


    def set_content(self, context):
        """ Construct and add content as a direct child. """
        # Currently a static image
        src = "/static/images/covers/baseballPhoto.jpg"
        self.append_child(CoverPhoto(src, context.name))


class SummaryDiv(Div):

    """ SummaryDiv encapsulates a tab's summary attribute <div>. """


    def __init__(self, aggregations):
        """ Construct a tab's summary content element tree. """
        super(SummaryDiv, self).__init__()
        self.set_id(TAB_ID.SUMMARY)
        self.set_content(aggregations)

        # add a summary item class to the children
        for child in self.children():
            child.append_class(TAB_CLASS.SUMMARY_ITEM)


    def set_content(self, aggregations):
        """ Construct and add content as a direct child. """
        raise NotImplementedError("Abstract Method: SUBCLASS MUST OVERRIDE!")


class FeedDiv(Div):

    """ FeedDiv encapsulates a tab's feed attribute <div>. """


    def __init__(self, current_person, objects):
        """ Construct a tab's feed content element tree. """
        super(FeedDiv, self).__init__()
        self.set_id(TAB_ID.FEED)

        self.append_child(Headline(Copy.feed_title))

        if len(objects) > 0:
            self.set_content(current_person, objects)


    def set_content(self, current_person, objects):
        """ Construct and add content as a direct child. """
        for object in objects:
            self.append_child(
                    StoryFactory.construct_story(current_person, object))
