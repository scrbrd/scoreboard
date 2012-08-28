""" Module: story

All the story components. The Stories are currently only used in the
FeedSection of a Tab.

"""

from view.elements.base import Div
from view.app.components import RelativeDateComponent, Headline, AppThumbnail

from components import HeadlineSection
from components import CommentsSection
from media import BoxscoreMedia


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

    STORY_CLASS = "story"


    def __init__(self, current_person, story_object):
        """ Construct a Story.

        Required:
        Person  current_person  the current User's associated Person
        SqNode  story_object  Object to build story around

        """
        super(Story, self).__init__()

        self.append_class(self.STORY_CLASS)

        # add creator photo
        creator = story_object.get_creator()
        creator_thumbnail = AppThumbnail(
                creator.picture_url,
                creator.name)

        # add story headline
        story_headline = self._construct_story_headline(story_object)
        headline_section = HeadlineSection(
                creator_thumbnail,
                story_headline,
                RelativeDateComponent(story_object.created_ts, False))

        # add headline and media section to story
        self.append_child(headline_section)
        self.append_child(self._construct_media_section(story_object))


        # add comments link to story
        # feedbackButton = Button()
        # feedbackButton.append_class("feedback-button")
        # self._main_section.append_child(feedbackButton)

        # add feedback section to story
        self.append_child(CommentsSection(current_person, story_object))


    def _construct_story_headline(self, story_object):
        """ Construct the headline for the story.

        Required:
        SqNode  story_object  Object to build story around

        """
        raise NotImplementedError("Abstract Method: SUBCLASS MUST OVERRIDE!")


    def _construct_media_section(self, story_object):
        """ Construct the media object for the the story.

        Required:
        SqNode  story_object  Object to build story around

        """
        raise NotImplementedError("Abstract Method: SUBCLASS MUST OVERRIDE!")


class GameStory(Story):

    """ Game Story is a single entry for a played game. """

    GAME_STORY_CLASS = "game-story"


    def __init__(self, current_person, game):
        """ Construct a GameStory.

        Required:
        Person  current_person  the current User's associated Person
        object  game    the Game that the story pulls data from

        """
        super(GameStory, self).__init__(current_person, game)
        self.append_class(self.GAME_STORY_CLASS)


    def _construct_media_section(self, story_object):
        """ Construct the media object for the the Game Story.

        Required:
        SqNode  story_object  Game to build story around

        """
        return BoxscoreMedia(story_object)


    def _construct_story_headline(self, story_object):
        """ Construct the GameStory's Headline.

        Required:
        SqNode  story_object  Game to build story around

        Return Headline

        """
        game = story_object  # game methods required
        return Headline(game.creators_message)


    @staticmethod
    def construct_story(current_person, game):
        """ Provide StoryFactory with GameStory subclass constructors. """
        return GameStory(current_person, game)
