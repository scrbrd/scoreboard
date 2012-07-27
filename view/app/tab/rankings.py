""" Module: rankings

Rankings tab components.

"""
from view.constants import PAGE_NAME

from framework import TabSection
from components import RankingsList


class RankingsTabSection(TabSection):

    """ Rankings tab section is the rankings list tab's content section. """

    def __init__(self, rankings):
        """ Construct a rankings tab content section element tree. """
        super(RankingsTabSection, self).__init__(PAGE_NAME.RANKINGS)
        self.append_child(RankingsList(rankings))
