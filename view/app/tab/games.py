""" Module: games

Games tab components.

"""

from view.constants import SQ_DATA, PAGE_NAME

from view.elements.base import OL, LI, Span, BR

from framework import TabSection


class GamesTabSection(TabSection):

    """ Games tab section is the games list tab's content section. """


    def __init__(self, games):
        """ Construct a games list tab content section element tree. """
        super(GamesTabSection, self).__init__(PAGE_NAME.GAMES)
        self.append_child(GamesList(games))


class GamesList(OL):

    """ Games List extending <ol>. """


    def set_list_item(self, item, index):
        """ Construct and add a list item as a child of this list. """
        self.append_child(GameLI(item, index))


class GameLI(LI):

    """ Game list item extending <li>. """


    def __init__(self, item, index):
        """ Construct a game list item element tree. """
        super(GameLI, self).__init__(item, index)
        # TODO: add css
        self.set_data(SQ_DATA.ID, item.id)
        self.set_data(SQ_DATA.OBJECT_TYPE, item.type)


    def set_content(self, item):
        """ Generate the content for this game list item. """

        # get results' Opponents' names, results' scores
        for result, opponent_ids in item.opponent_ids_by_result.items():
            for id in opponent_ids:
                # FIXME: this all breaks the contract that the view doesnt get
                # access to non-property methods in model.api.Game.
                opponent = item.get_opponent(id)

                span = Span()
                span.set_data(SQ_DATA.ID, id)
                span.set_data(SQ_DATA.OBJECT_TYPE, opponent.type)
                span.set_text("{0}: {1}".format(opponent.name, result))
                self.append_child(span)

                # add break between results
                br = BR()
                self.append_child(br)
