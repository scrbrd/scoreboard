""" Module: components

App-specific reusable components that are building blocks.

"""

from view.view_util import date
from view.elements.base import Span, Img, Div, Section, Button
from view.elements.components import Thumbnail

from constants import COMPONENT_CLASS, IMAGE
from copy import Copy


class Headline(Div):

    """ Headline is a title span. """


    def __init__(self, text):
        """ Construct a headline tag. """
        super(Headline, self).__init__()
        self.append_class(COMPONENT_CLASS.HEADLINE)

        self.set_text(text)


class Subheadline(Div):

    """ Subheadline is a title span. """


    def __init__(self, text):
        """ Construct a headline tag. """
        super(Subheadline, self).__init__()
        self.append_class(COMPONENT_CLASS.SUBHEADLINE)

        self.set_text(text)


class AppThumbnail(Thumbnail):

    """ AppThumbnail extending Thumbnail.

    This is the canonical way to display a Thumbnail for a Node. It may
    even be more appropriate to call it NodeThumbnail. We may later
    subclass this to be more specific about the style and implementation
    for Opponents and for Leagues and Games.

    """


    def __init__(self, src=IMAGE.DEFAULT_THUMBNAIL, name=""):
        """ Construct an AppThumbnail. """
        super(AppThumbnail, self).__init__(self._prepare_src(src), name)


    def _prepare_src(self, src):
        """ Distinguish None from "" when choosing the default thumbnail. """
        return IMAGE.DEFAULT_THUMBNAIL if src is None else src


class RemoveTagButton(Button):

    """ Remove Tag Button that extends <button>. """


    def __init__(self):
        """ Construct a remove tag button tag. """
        super(RemoveTagButton, self).__init__(Copy.remove_tag_button)

        self.append_class(COMPONENT_CLASS.REMOVE_TAG_BUTTON)


class CoverPhoto(Img):

    """ CoverPhoto is the main image on a Page. """


    def __init__(self, src, title):
        """ Construct a cover photo. """
        super(CoverPhoto, self).__init__(src, title)
        self.append_class(COMPONENT_CLASS.COVER_PHOTO)


class Icon(Img):

    """ Icon is a small image that is used as a symbol. """


    def __init__(self, src, alt):
        """ Construct an Icon. """
        super(Icon, self).__init__(src, alt)
        self.append_class(COMPONENT_CLASS.ICON)


class RelativeDateComponent(Div):

    """ RelativeDateComponent is a component that displays a date relative to
    the current date. (e.g., '4 days go') """


    def __init__(self, datetime, with_icon=True):
        """Construct a RelativeDateComponent.

        Required:
        ts      datetime    the time to display

        Optional:
        bool    with_icon   if true, display icon

        """
        super(RelativeDateComponent, self).__init__()
        self.append_class(COMPONENT_CLASS.RELATIVE_DATE_COMPONENT)

        if with_icon:
            self.append_child(Icon(IMAGE.TIME_ICON, "time"))

        relative_date = Span()
        relative_date.set_text(date.get_simple_datetime_ago(datetime))
        self.append_child(relative_date)


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
            if len(group) == 0:
                pass
            elif len(group) == 1:
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
            # FIXME: model should send None instead of "" since "" is a valid
            # src, but model doesn't yet distinguish/translate empty db values.
            # big_picture_url is from Person, not Opponent
            src = None
            if opponent.big_picture_url:
                src = opponent.big_picture_url
            self.append_child(AppThumbnail(src, opponent.name))


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
