""" Module: story

All the story components. The Stories are currently only used in the
FeedSection of a Tab.

"""

from view.elements.base import Div
from view.app.components import OpponentGroupsSection, RelativeDateComponent

from constants import COMPONENT_CLASS
from components import PlayedHeadline, ResultHeadline, MainStorySection


class Story(Div):

    """ Story is a single entry for the FeedDiv, extends <div>. """


    def __init__(self):
        """ Construct a Story. """
        super(Story, self).__init__()
        self.append_class(COMPONENT_CLASS.STORY)


class GameStory(Story):

    """ Game Story is a single entry for a played game. """

    WON = 'won_by'
    LOST = 'lost_by'
    PLAYED = 'played_by'

    def __init__(self, game):
        """ Construct a GameStory.

        Required:
        object  game    the Game that the story pulls data from

        """
        super(GameStory, self).__init__()
        self.append_class(COMPONENT_CLASS.GAME_STORY)

        main_section = MainStorySection()

        # FIXME: this all breaks the contract that the view doesnt get
        # access to non-property methods in model.api.Game.

        # display the Opponents, grouped by Result
        opponent_ids_by_result = game.opponent_ids_by_result
        winner_ids = opponent_ids_by_result.get(self.WON)
        loser_ids = opponent_ids_by_result.get(self.LOST)
        player_ids = opponent_ids_by_result.get(self.PLAYED)

        if player_ids is not None:
            # Friendly Game

            (main_players, other_players) = self._split_camaraderie_players(
                    game,
                    player_ids)
            self.append_child(
                    OpponentGroupsSection(main_players, other_players))

            # Create the Headline with all players.
            all_players = game.get_opponents(player_ids)
            main_section.append_child(PlayedHeadline(all_players))

        else:
            # Competitive Game
            winners = game.get_opponents(winner_ids)
            losers = game.get_opponents(loser_ids)

            self.append_child(OpponentGroupsSection(winners, losers))
            main_section.append_child(ResultHeadline(winners, losers))

        # add time icon
        main_section.append_child(RelativeDateComponent(game.created_ts))
        self.append_child(main_section)

    @staticmethod
    def _split_camaraderie_players(game, player_ids):
        """ Split player_ids into two groups for processing.

        Required:
        Game game           the game that the player_ids come from
        list player_ids     a list of player_ids (ints)

        The first list of players is a single player that should be
        highlighted. If the game has a creator, this is him. Otherwise it's a
        random player.

        """
        # TODO: set the main player to be the user if possible.

        # Highlight creator, but if none, then set as a random player
        creator_id = game.creator_id
        main_player_id = player_ids[0]
        if creator_id in player_ids:
            main_player_id = creator_id
        other_player_ids = player_ids[:]
        other_player_ids.remove(main_player_id)

        # Create the photo section with two groups of players.
        main_players = [game.get_opponent(main_player_id)]
        other_players = game.get_opponents(other_player_ids)

        return (main_players, other_players)
