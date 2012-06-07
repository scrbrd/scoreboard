""" Module: rankings

Rankings tab components.

"""
from view.constants import APP_CLASS, APP_DATA, APP_ID, DESIGN_CLASS
from view.constants import PAGE_NAME
from view.html.elements import OL, LI, Span
from view.html.tab.framework import TabSection


class RankingsTabSection(TabSection):

    """ Rankings tab section is the games list tab's content section. """

    def __init__(self, rankings):
        """ Construct a rankings tab content section element tree. """
        super(RankingsTabSection, self).__init__(PAGE_NAME.RANKINGS)
        self.append_child(RankingsOL(rankings))


class RankingsOL(OL):

    """ Rankings List extending <ol>. """


    def __init__(self, items):
        """ Construct a Rankings of type <ol>. """
        super(RankingsOL, self).__init__(items)
        self.set_classes([DESIGN_CLASS.COUNTER])


    def set_list_item(self, item, index):
        """ Construct and add a list item as a child of this list. """
        self.append_child(RankingLI(item, index))


class RankingLI(LI):

    """ Ranking list item extending <li>. """


    def __init__(self, item, index):
        """ Construct a ranking list item element tree. """
        super(RankingLI, self).__init__(item, index)

        # TODO: add css and remove id.

        self.set_data(APP_DATA.ID, item.id)
        self.set_data(APP_DATA.OBJECT_TYPE, item.type)
        self.create_content(item)


    def create_content(self, item):
        """ Generate the content for this ranking list item. """
        span = Span()
        span.set_text("{0} {1}".format(item.name, item.win_count))
        self.append_child(span)
