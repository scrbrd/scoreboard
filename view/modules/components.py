""" Module: components

Provide required subclasses of Tornado's UIModule for delagating the
rendering of markup from Tornado's PSP templates to our implementation
of HTML, which subclasses python's xml.etree.cElementTree.

Effectively, this will serve as a mapping between the opaque model the
controller has passed along and the specific data the view needs
extracted in order to render markup.

Each class has a single requirement...override render.

"""

import tornado.web
from tornado import escape

from view.constants import PAGE_TYPE, PAGE_NAME, SQ_DATA

from view.elements import xsrf
from view.elements.base import Element

from view.app.tab.framework import TabHeader
from view.app.tab.model import ContextModel, PageModel, SessionModel
from view.app.tab.league import LeagueContentSection

from view.app.dialog.framework import DialogHeader
from view.app.dialog.create_game import CreateGameContentSection

from view.app.page.landing import LandingPage

from copy import Copy


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


class UILeaguePage(tornado.web.UIModule):

    """ League Page UI Module. """

    def render(self, model=None, state=None):
        """ Render a League. """
        xsrf.set_xsrf_token(escape.xhtml_escape(self.handler.xsrf_token))
        current_person = None
        for rival in model.rivals:
            if (rival.id == self.current_user.person_id):
                current_person = rival

        league_page = LeagueContentSection(
                model.context,
                model.aggregations,
                model.objects,
                current_person)

        return Element.to_string(league_page)


class UICreateGameDialog(tornado.web.UIModule):

    """ Create Game Dialog UI Module. """


    def render(self, model=None, state=None):
        """ Render a Create Game Dialog Screen. """
        xsrf.set_xsrf_token(escape.xhtml_escape(self.handler.xsrf_token))

        header_tree = DialogHeader(Copy.create_game_dialog_header)
        content_tree = CreateGameContentSection(model)

        return Element.to_string(header_tree) + Element.to_string(content_tree)


class UILandingPage(tornado.web.UIModule):

    """ Splash Page UI Module. """

    def render(self, model=None, state=None):
        """ Render a Splash Page. """
        login_link = {
            "text": "Login",
            "href": "/login",
        }

        splash_tree = LandingPage(login_link)

        return Element.to_string(splash_tree)
