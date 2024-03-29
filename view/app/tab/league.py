""" Module: league

League tab components.

"""

from view.elements.base import Div
from view.app.components import Headline
from view.app.copy import Copy

from framework import TabContentSection, PropertiesDiv, SummaryDiv, FeedDiv
from components import RankingsList


class LeagueContentSection(TabContentSection):

    """ LeagueContentSection constructs a content section with league specific
    sections. """


    def construct_properties_content(self, context):
        """ Construct and add properties to this content section. """
        return LeaguePropertiesDiv(context)


    def construct_summary_content(self, aggregations):
        """ Construct and add summary content to this content section. """
        return LeagueSummaryDiv(aggregations)


    def construct_feed_content(self, objects):
        """ Construct and add feed content to this content section. """
        return LeagueFeedDiv(self._current_person, objects)



class LeaguePropertiesDiv(PropertiesDiv):

    """ LeaguePropertiesDiv extending PropertiesDiv. """
    # All functionality is in app.tab.framework.PropertiesDiv
    pass


class LeagueSummaryDiv(SummaryDiv):

    """ LeagueSummaryDiv extending SummaryDiv. """


    def set_content(self, aggregations):
        """ Construct and add content as a direct child. """
        # TODO: remove string and pull directly from aggregations
        div = Div()
        div.append_child(Headline(Copy.rankings_title))
        div.append_child(RankingsList(aggregations.get("standings")))

        self.append_child(div)


class LeagueFeedDiv(FeedDiv):

    """ LeagueFeedDiv extending FeedDiv. """

    # All functionality is in app.tab.framework.FeedDiv
    pass
