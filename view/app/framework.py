""" Module: framework

NOTE: This module should eventually be app_framework.

This framework module holds all the framework elements that dialog and tab
subclass from.

"""

from view.elements.base import Div


class ContentWrapper(Div):

    """ ContentWrapper creates the elements that iScroll needs to make the
    content scrollable. """

    OUTER_CONTAINER_CLASS = "outer-content-container"
    INNER_CONTAINER_CLASS = "inner-content-container"


    def __init__(self, unique_str, content_element):
        """ Construct a content container, which is needed by iScroll for nice
        scrolling.

        Both the outer and inner container are required and they both must have
        unique ids for iScroll to work.

        Required:
        str     unique_str          the unique identifier of this content
        Element content_element     the element that should be scrollable

        """
        super(ContentWrapper, self).__init__()
        outer_container_id = "{}-{}".format(
                unique_str,
                self.OUTER_CONTAINER_CLASS)
        inner_container_id = "{}-{}".format(
                unique_str,
                self.INNER_CONTAINER_CLASS)

        self.set_id(outer_container_id)
        self.append_class(self.OUTER_CONTAINER_CLASS)

        inner_container = Div()
        inner_container.set_id(inner_container_id)
        inner_container.append_class(self.INNER_CONTAINER_CLASS)

        inner_container.append_child(content_element)
        self.append_child(inner_container)
