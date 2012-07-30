""" Module: components

App-specific reusable components that are building blocks.

"""

from view.elements.base import Span, Img, Div, Section
from view.elements.components import Thumbnail
from view.app.constants import DEFAULT_IMAGE

from constants import COMPONENT_CLASS


class Headline(Span):

    """ Headline is a title span. """


    def __init__(self, text):
        """ Construct a headline tag. """
        super(Headline, self).__init__()
        self.append_classes([COMPONENT_CLASS.HEADLINE])

        self.set_text(text)


class CoverPhoto(Img):

    """ CoverPhoto is the main image on a Page. """


    def __init__(self, src, title):
        """ Construct a cover photo. """
        super(CoverPhoto, self).__init__(src, title)
        self.append_classes([COMPONENT_CLASS.COVER_PHOTO])


class OpponentGroupsSection(Section):

    """ OpponentGroupsSection is a collection of OpponentGroups.

    Required:
    list first_group        a list of Opponents
    list second_group       a different list of Opponents

    """


    def __init__(self, first_group, second_group):
        """ Construct a section with OpponentGroups. """
        super(OpponentGroupsSection, self).__init__()
        self.append_class(COMPONENT_CLASS.OPPONENT_GROUP_SECTION)

        opponent_groups = [first_group, second_group]
        for group in opponent_groups:
            if len(group) == 1:
                self.append_child(SingleOpponentGroup(group[0]))
            elif len(group) in range(2, 5):
                self.append_child(MultiOpponentGroup(group))
            else:
                self.set_text("MAX 4 PLAYERS")


class OpponentGroup(Div):

    """ OpponentGroup is a section that contains one or more opponents. """


    def __init__(self, opponents):
        """ Construct an opponent section.

        Required:
        list    opponents   a list of Opponent objects.

        """
        super(OpponentGroup, self).__init__()
        self.append_class(COMPONENT_CLASS.OPPONENT_GROUP)

        for opponent in opponents:

            photo = Thumbnail(DEFAULT_IMAGE.THUMBNAIL, opponent.name)
            # TODO make model send None instead of ""
            if opponent.picture != "":
                photo = Thumbnail(opponent.picture, opponent.name)
            self.append_child(photo)


class SingleOpponentGroup(OpponentGroup):

    """ SingleOpponentGroup is a section that contains one opponent. """


    def __init__(self, opponent):
        """ Construct a single oppponent in the group

        Required:
        Opponent opponent   a single opponent for the OpponentGroup

        """
        super(SingleOpponentGroup, self).__init__([opponent])
        self.append_class(COMPONENT_CLASS.SINGLE_OPPONENT_GROUP)


class MultiOpponentGroup(OpponentGroup):

    """ MultiOpponentGroup is a section that contains two to four opponents.
    """

    def __init__(self, opponents):
        """ Construct a two to four opponent OpponentGroup.

        Required:
        list    opponents   a list of Opponents

        """
        super(MultiOpponentGroup, self).__init__(opponents)
        self.append_class(COMPONENT_CLASS.MULTI_OPPONENT_GROUP)
