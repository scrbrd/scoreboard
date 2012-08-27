""" Module: components

App-specific reusable components that are building blocks.

"""

from view.view_util import date
from view.elements.base import Span, Img, Div, Button
from view.elements.components import Thumbnail

from constants import IMAGE
from copy import Copy


class Headline(Div):

    """ Headline is a title span. """

    HEADLINE_CLASS = "headline"


    def __init__(self, text):
        """ Construct a headline tag. """
        super(Headline, self).__init__()
        self.append_class(self.HEADLINE_CLASS)

        self.set_text(text)


class Subheadline(Div):

    """ Subheadline is a title span. """

    SUBHEADLINE_CLASS = "subheadline-class"


    def __init__(self, text):
        """ Construct a headline tag. """
        super(Subheadline, self).__init__()
        self.append_class(self.SUBHEADLINE_CLASS)

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
        # FIXME: model should send None instead of "" since "" is a valid
        # src, but model doesn't yet distinguish/translate empty db values.
        if src == "":
            src = None
        return IMAGE.DEFAULT_THUMBNAIL if src is None else src


class RemoveTagButton(Button):

    """ Remove Tag Button that extends <button>. """

    REMOVE_TAG_BUTTON_CLASS = "remove-tag-button"


    def __init__(self):
        """ Construct a remove tag button tag. """
        super(RemoveTagButton, self).__init__(Copy.remove_tag_button)

        self.append_class(self.REMOVE_TAG_BUTTON_CLASS)


class CoverPhoto(Img):

    """ CoverPhoto is the main image on a Page. """

    COVER_PHOTO_CLASS = "cover-photo"


    def __init__(self, src, title):
        """ Construct a cover photo. """
        super(CoverPhoto, self).__init__(src, title)
        self.append_class(self.COVER_PHOTO_CLASS)


class Icon(Img):

    """ Icon is a small image that is used as a symbol. """

    ICON_CLASS = "icon"


    def __init__(self, src, alt):
        """ Construct an Icon. """
        super(Icon, self).__init__(src, alt)
        self.append_class(self.ICON_CLASS)


class RelativeDateComponent(Div):

    """ RelativeDateComponent is a component that displays a date relative to
    the current date. (e.g., '4 days go') """

    RELATIVE_DATE_COMPONENT_CLASS = "relative-date-component"


    def __init__(self, ts, is_expanded=True):
        """Construct a RelativeDateComponent.

        Required:
        ts      ts      the time to display

        Optional:
        bool    is_expanded Expand the Relative Date Component

        """
        super(RelativeDateComponent, self).__init__()
        self.append_class(self.RELATIVE_DATE_COMPONENT_CLASS)

        relative_date = Span()
        if is_expanded:
            relative_date.set_text(
                    date.format_to_long_relative_datetime(ts))
        else:
            relative_date.set_text(date.format_to_short_relative_datetime(ts))

        self.append_child(relative_date)
