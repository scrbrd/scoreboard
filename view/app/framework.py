""" Module: framework

NOTE: This module should eventually be app_framework.

This framework module holds all the framework elements that dialog and tab
subclass from.

"""

from view.elements.base import Div


class ContentWrapper(Div):

    """ ContentWrapper creates the elements that iScroll needs to make the
    content scrollable. """


    def __init__(self, outer_wrapper_id, inner_wrapper_id, content_element):
        """ Construct a content wrapper.

        Required:
        str     outer_wrapper_id    the outermost shell of the wrapper
        str     inner_wrapper_id    the shell directly around the content
        Element content_element     the element that should be scrollable

        """
        super(ContentWrapper, self).__init__()

        self.set_id(outer_wrapper_id)

        content_container = Div()
        content_container.set_id(inner_wrapper_id)

        content_container.append_child(content_element)

        self.append_child(content_container)
