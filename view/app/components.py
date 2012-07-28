""" Module: components

App-specific reusable components that are building blocks.

"""
from view.elements.base import Span, Img

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
