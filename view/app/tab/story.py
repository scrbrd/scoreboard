""" Module: story

All the story components. The Stories are currently only used in the
FeedSection of a Tab.

"""


from view.constants import SQ_DATA
from view.elements.base import Div, Span

from constants import COMPONENT_CLASS


class Story(Div):

    """ Story is a single entry for the FeedDiv, extends <div>. """


    def __init__(self):
        """ Construct a Story. """
        super(Story, self).__init__()
        self.append_class(COMPONENT_CLASS.STORY)


class GameStory(Story):

    """ Game Story is a single entry for a played game. """


    def __init__(self, game):
        """ Construct a GameStory.

        Required:
        object  game    the Game that the story pulls data from

        """
        super(GameStory, self).__init__()
        self.append_class(COMPONENT_CLASS.GAME_STORY)

        # get results' Opponents' names, results' scores
        for result, opponent_ids in game.opponent_ids_by_result.items():
            for id in opponent_ids:
                # FIXME: this all breaks the contract that the view doesnt get
                # access to non-property methods in model.api.Game.
                opponent = game.get_opponent(id)

                span = Span()
                span.set_data(SQ_DATA.ID, id)
                span.set_data(SQ_DATA.OBJECT_TYPE, opponent.type)
                span.set_text("{0}: {1}".format(opponent.name, result))
                self.append_child(span)
