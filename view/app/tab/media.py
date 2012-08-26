""" Module: media

All the media objects for Stories. These media objects should act and look
similar to each other. Some examples are Game, Picture...

"""
from view.elements.base import Section, Div, Span
from view.elements.components import FloatContainer
from view.app.copy import Copy

from constants import COMPONENT_CLASS
from components import SportComponent, OpponentsList


class BoxscoreMedia(Section):

    """ BoxscoreMedia is the Boxscore object for a Game. """


    def __init__(self, game):
        """ Construct a section with BoxscoreMedia.

        Required:
        Game game   the game to create the boxscore from

        """
        super(BoxscoreMedia, self).__init__()
        self.append_class(COMPONENT_CLASS.BOXSCORE_MEDIA)

        # to allow the outer object to fit the screen width and still
        # wrap the inner floats
        floatable = FloatContainer()

        # FIXME XXX: 2. Build layout for Opponent
        # Groups (this might need a rivalry versus a camaraderie version. 3.
        # Format OpponentGroup (maybe call it OpponentResultGroup)
        final = Span()
        final.set_text(Copy.final)
        floatable.append_child(final)
        floatable.append_child(SportComponent(game.sport))

        # FIXME: get_opponents breaks the contract that the view doesnt get
        # access to non-property methods in model.api.Game.

        # Generate Opponent groups.
        if game.is_rivalry:
            floatable.append_child(OpponentsResultGroup(
                    game.get_opponents(game.winner_ids),
                    Copy.won))
            floatable.append_child(OpponentsResultGroup(
                    game.get_opponents(game.loser_ids),
                    Copy.lost))
        else:
            floatable.append_child(OpponentsResultGroup(
                    game.get_opponents(game.camaraderie_ids),
                    Copy.played))

        self.append_child(floatable)


class OpponentsResultGroup(Div):

    """ OpponentsResultGroup is a section that contains one or more
    opponents. """


    def __init__(self, opponents, result_str):
        """ Construct an opponent section.

        Required:
        list    opponents   a list of Opponent objects.
        str     results_str a string for the result of the opponent group

        """
        super(OpponentsResultGroup, self).__init__()
        self.append_class(COMPONENT_CLASS.OPPONENTS_RESULT_GROUP)

        # each opponent with a thumbnail and name
        self.append_child(OpponentsList(opponents))

        # the result of the opponent group
        result_div = Div()
        result_div.set_text(result_str)
        self.append_child(result_div)
