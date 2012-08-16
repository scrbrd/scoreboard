""" Module: components

Provide required subclasses of Tornado's UIModule for delagating the
rendering of markup from Tornado's PSP templates to our implementation
of HTML, which subclasses python's xml.etree.cElementTree.

Each class has a single requirement...override render.

"""

import tornado.web

from view.constants import PAGE_TYPE, PAGE_NAME, SQ_DATA

from view.elements.base import Element
from view.app.tab.framework import TabHeader
from view.app.tab.model import ContextModel, PageModel, SessionModel


class UITabHeader(tornado.web.UIModule):

    """ TabHeader UI Module. """

    def render(self, model=None, state=None):
        """ Render a TabHeader. """
        context = model.context

        element_tree = TabHeader(context)

        return Element.to_string(element_tree)


class UIContextModel(tornado.web.UIModule):

    """ Context Model UI Module. """

    def render(self, model=None, state=None):
        """ Render a Context Model. """
        context = model.context
        element_tree = ContextModel(context)

        return Element.to_string(element_tree)


class UISessionModel(tornado.web.UIModule):

    """ Session Model UI Module. """

    def render(self, model=None, state=None):
        """ Render a Session Model. """
        element_tree = SessionModel(model)

        return Element.to_string(element_tree)


class UIPageModel(tornado.web.UIModule):

    """ Generic Content Model View. """

    def render(self, model=None, state=None):
        """ Render a Content Model View. """
        element_tree = PageModel(state)

        return Element.to_string(element_tree)


class UITabModel(UIPageModel):

    """ Generic Content Model View. """

    def render(self, model=None, state=None):
        """ Render a Content Model View. """
        return super(UITabModel, self).render(
                None,
                {
                    SQ_DATA.PAGE_NAME: state,
                    SQ_DATA.PAGE_TYPE: PAGE_TYPE.TAB,
                })


class UILeagueModel(UITabModel):

    """ League Content Model View. """

    def render(self, model=None, state=None):
        """ Render a League Content Model View. """
        return super(UILeagueModel, self).render(None, PAGE_NAME.LEAGUE)
