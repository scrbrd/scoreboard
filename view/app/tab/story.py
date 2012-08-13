""" Module: story

All the story components. The Stories are currently only used in the
FeedSection of a Tab.

"""

from view.elements.base import Div
#from view.elements.base import Div, Button
from view.app.components import OpponentGroupsSection, RelativeDateComponent

from constants import COMPONENT_CLASS
from components import CamaraderieHeadline, RivalryHeadline, MainStorySection
from components import CommentsSection, SportComponent


# TODO: get this from handlers in production
APP_URL = "http://onscoreboard.com/"
STORY_SLUG = "story/"


class StoryFactory(object):

    """ StoryFactory churns out Story instances.

    This is basically just one giant switch statement to construct the
    correct Story based on the type of the Node/Edge Object supplied.

    When Node/Edge type alone is insufficient to determine which Story
    to construct, define and delegate this work to a secondary static
    implementation of construct_story in the Story subclass which
    corresponds to the Object's type. Usually, this will happen when an
    Object has a clear need for Story subclass variation. For example,
    GameStory has RivalryGameStory and CamaraderieGameStory subclasses.

    """


    @staticmethod
    def construct_story(current_person, story_object):
        """ Construct a Story from a Node or Edge Object. """

        story = None

        # TODO: find a way to ship node/edge types to the view.
        if story_object.type == "game":
            story = GameStory.construct_story(current_person, story_object)
        else:
            raise StoryError(story_object.type, "Story constructor not found.")

        if not story:
            raise StoryError(story_object.type, "Story output not valid.")

        return story


class StoryError(Exception):

    """ StoryError extending Exception.

    Provide an exception to be raised when input supplied to the
    StoryFactory is insufficient for locating a Story constructor or
    when the resulting Story is invalid.

    """


    def __init__(self, type, msg):
        """ Construct a StoryInputError. """
        self.reason = "Story Object Type=[{0}] : {1}".format(type, msg)


class Story(Div):

    """ Story is a single entry for the FeedDiv, extends <div>. """


    def __init__(self, current_person, story_object):
        """ Construct a Story.

        Required:
        Person  current_person  the current User's associated Person
        SqNode  story_object  Object to build story around

        """
        super(Story, self).__init__()

        self._photo_section = None
        self._main_section = MainStorySection()
        self.append_class(COMPONENT_CLASS.STORY)

        # FIXME: it is extremely confusing and misleading that this method
        # opaquely sets self._photo_section without saying so.
        self._construct_story_body(story_object)

        # add time icon
        self._main_section.append_child(
                RelativeDateComponent(story_object.created_ts))

        # add comments link to story
        # feedbackButton = Button()
        # feedbackButton.append_class("feedback-button")
        # self._main_section.append_child(feedbackButton)

        # add photo and main section to Story
        self.append_child(self._photo_section)
        self.append_child(self._main_section)

        # add feedback section to story
        self.append_child(CommentsSection(current_person, story_object))


    def _construct_story_body(self, story_object):
        """ Construct the body of the story.

        Required:
        SqNode  story_object  Object to build story around

        """
        raise NotImplementedError("Abstract Method: SUBCLASS MUST OVERRIDE!")


class GameStory(Story):

    """ Game Story is a single entry for a played game. """


    def __init__(self, current_person, game):
        """ Construct a GameStory.

        Required:
        Person  current_person  the current User's associated Person
        object  game    the Game that the story pulls data from

        """
        super(GameStory, self).__init__(current_person, game)
        self.append_class(COMPONENT_CLASS.GAME_STORY)


    @staticmethod
    def construct_story(current_person, game):
        """ Provide StoryFactory with GameStory subclass constructors. """
        story = None

        if game.is_rivalry:
            story = RivalryGameStory(current_person, game)
        else:
            story = CamaraderieGameStory(current_person, game)

        return story


class RivalryGameStory(GameStory):

    """ RivalryGameStory extending GameStory. """


    def _construct_story_body(self, game):
        """ Construct the body of the GameStory.

        Required:
        object  game    the Game that the story pulls data from

        """
        # FIXME: this all breaks the contract that the view doesnt get
        # access to non-property methods in model.api.Game.

        # display the Opponents, grouped by Result
        winners = game.get_opponents(game.winner_ids)
        losers = game.get_opponents(game.loser_ids)

        self._photo_section = OpponentGroupsSection(winners, losers)

        self._main_section.append_child(RivalryHeadline(game))

        self._main_section.append_child(SportComponent(game.sport))


class CamaraderieGameStory(GameStory):

    """ CamaraderieGameStory extending GameStory. """


    def _construct_story_body(self, game):
        """ Construct the body of the GameStory.

        Required:
        object  game    the Game that the story pulls data from

        """
        (main_players, other_players) = self._split_camaraderie_players(game)

        self._photo_section = OpponentGroupsSection(
                main_players,
                other_players)

        # Create the Headline with all players.
        self._main_section.append_child(CamaraderieHeadline(game))

        self._main_section.append_child(SportComponent(game.sport))


    @staticmethod
    def _split_camaraderie_players(game):
        """ Split player_ids into two groups for processing.

        Required:
        Game game           the game that the player_ids come from

        The first list of players is a single player that should be
        highlighted. If the game has a creator, this is him. Otherwise it's a
        random player.

        """
        # FIXME: this all breaks the contract that the view doesnt get
        # access to non-property methods in model.api.Game.

        # TODO: set the main player to be the user if possible.

        # Highlight creator, but if none, then set as a random player
        creator_id = game.creator_id
        main_player_id = game.camaraderie_ids[0]
        if creator_id in game.camaraderie_ids:
            main_player_id = creator_id
        other_player_ids = game.camaraderie_ids[:]
        other_player_ids.remove(main_player_id)

        # Create the photo section with two groups of players.
        main_players = [game.get_opponent(main_player_id)]
        other_players = game.get_opponents(other_player_ids)

        return (main_players, other_players)
