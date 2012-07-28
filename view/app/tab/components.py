""" Module: components

Elements components that will be used in tabs but aren't part of the framework.

"""
from view.constants import SQ_DATA
from view.app_copy import Copy

from view.elements.base import Span
from view.elements.components import HeadedList, HeadedListItem, NumberedList

from constants import COMPONENT_CLASS


class RankingsList(HeadedList):

    """ Rankings List extending HeadedList.

    list    _headings   contain the column headings for Rankings.

    """

    _headings = [Copy.player, Copy.loss_short, Copy.win_short]


    def __init__(self, standings):
        """ Construct Rankings List using HeadedList. """
        super(RankingsList, self).__init__(self._headings, standings)

        self.append_classes([COMPONENT_CLASS.RANKINGS_LIST])


    def set_list(self, rows):
        """ Set the list element for this list. """
        self.append_child(RankingsOL(rows))


class RankingsOL(NumberedList):

    """ Rankings List exntends <ol>. """


    def set_list_item(self, item, index):
        """ Construct and add a list item as a child of this list. """
        self.append_child(RankingLI(item, index))


class RankingLI(HeadedListItem):

    """ Ranking list item extending <li>. """

    def __init__(self, item, index):
        """ Construct a standing list item element tree. """
        super(RankingLI, self).__init__(item, index)
        # TODO: add css and remove id.
        self.set_data(SQ_DATA.ID, item.id)
        self.set_data(SQ_DATA.OBJECT_TYPE, item.type)


    def set_content(self, item):
        """ Set content for Rankings LI. """
        opponent = Span()
        opponent.set_text(str(item.name))
        self.set_column(opponent)

        loss_count = Span()
        loss_count.set_text(str(item.loss_count))
        self.set_column(loss_count)

        win_count = Span()
        win_count.set_text(str(item.win_count))
        self.set_column(win_count)
