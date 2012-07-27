""" Module: rankings

Rankings tab components.

"""

from view.constants import SQ_DATA, PAGE_NAME

from view.elements.base import LI, Span
from view.elements.components import NumberedList

from framework import TabSection


class RankingsTabSection(TabSection):

    """ Rankings tab section is the rankings list tab's content section. """

    def __init__(self, rankings):
        """ Construct a rankings tab content section element tree. """
        super(RankingsTabSection, self).__init__(PAGE_NAME.RANKINGS)
        self.append_child(RankingsList(rankings))


class RankingsList(NumberedList):

    """ Rankings List extending NumberedList. """


    def set_list_item(self, item, index):
        """ Construct and add a list item as a child of this list. """
        self.append_child(RankingLI(item, index))


class RankingLI(LI):

    """ Ranking list item extending <li>. """

    def __init__(self, item, index):
        """ Construct a ranking list item element tree. """
        super(RankingLI, self).__init__(item, index)
        # TODO: add css and remove id.
        self.set_data(SQ_DATA.ID, item.id)
        self.set_data(SQ_DATA.OBJECT_TYPE, item.type)


    def set_content(self, item):
        """ Set content for Rankings LI. """
        span = Span()
        span.set_text("{0} - W:{1}  L:{2}".format(
                item.name,
                item.win_count,
                item.loss_count))
        self.append_child(span)
