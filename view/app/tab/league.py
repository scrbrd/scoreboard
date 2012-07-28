""" Module: league

League tab components.

"""
from view.app_copy import Copy

from view.elements.base import Div
from view.elements.components import Headline

from framework import TabContentSection, PropertiesDiv, SummaryDiv, FeedDiv
from components import RankingsList


class LeagueContentSection(TabContentSection):

    """ LeagueContentSection constructs a content section with league specific
    sections. """


    def set_properties_content(self, context):
        """ Construct and add properties to this content section. """
        # TODO: Uncomment this line when LeagueProperties works.
        # self.append_child(LeaguePropertiesDiv(context))



    def set_summary_content(self, aggregations):
        """ Construct and add summary content to this content section. """
        self.append_child(LeagueSummaryDiv(aggregations))


    def set_feed_content(self, objects):
        """ Construct and add feed content to this content section. """
        # TODO: Uncomment this line when LeagueFeed works.
        # self.append_child(LeagueFeedDiv(objects))



class LeaguePropertiesDiv(PropertiesDiv):

    """ LeaguePropertiesDiv extending PropertiesDiv. """


    def set_content(self, context):
        """ Construct and add content as a direct child. """
        raise NotImplementedError("FILL ME IN!")


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


    def set_content(self, aggregations):
        """ Construct and add content as a direct child. """
        raise NotImplementedError("FILL ME IN!")
