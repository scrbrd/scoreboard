""" Module: league

League tab components.

"""

from exceptions import NotImplementedError

#from view.constants import SQ_DATA, PAGE_NAME

#from view.elements.base import Div, Span

from framework import PropertiesDiv, SummaryDiv, FeedDiv


class LeaguePropertiesDiv(PropertiesDiv):

    """ LeaguePropertiesDiv extending PropertiesDiv. """


    def set_content(self, properties):
        """ Construct and add content as a direct child. """
        raise NotImplementedError("FILL ME IN!")


class LeagueSummaryDiv(SummaryDiv):

    """ LeagueSummaryDiv extending SummaryDiv. """


    def set_content(self, summary):
        """ Construct and add content as a direct child. """
        raise NotImplementedError("FILL ME IN!")


class LeagueFeedDiv(FeedDiv):

    """ LeagueFeedDiv extending FeedDiv. """


    def set_content(self, feed):
        """ Construct and add content as a direct child. """
        raise NotImplementedError("FILL ME IN!")
