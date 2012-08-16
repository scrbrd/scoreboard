""" Module: page

Provide subclasses of Tornado's UIModule that render components as a single
html page. Typically called synchronously.


Basic Hierarchy:

    Page
    |
    ----AppPage
    |   |
    |   ----TabPage > LeaguePage
    |   |
    |   ----DialogPage > CreateGameDialog, InviteFriendsDialog
    |
    ----GenericPage
        |
        ----LandingPage
        |
        ----SignUpPage

Each class has a single requirement...override render.

"""

import tornado.web
from tornado import escape

from view.elements import xsrf
from view.elements.base import Element
from view.app.tab.framework import TabHeader, TabContentWrapper
from view.app.tab.league import LeagueContentSection
from view.app.dialog.framework import DialogContentWrapper
from view.app.dialog.create_game import CreateGameContentSection
from view.app.dialog.create_game import CreateGameDialogHeader
from view.app.page.landing import LandingPage


class UIAppPage(tornado.web.UIModule):


    def render(self, model=None, state=None):
        xsrf.set_xsrf_token(escape.xhtml_escape(self.handler.xsrf_token))

        self._set_current_person(model)

        main_header_tree = self._construct_main_header(model)
        content_section_tree = self._construct_content_section(model)
        content_wrapper_tree = self._construct_content_wrapper(
                content_section_tree)

        header_str = Element.to_string(main_header_tree)
        content_str = Element.to_string(content_wrapper_tree)

        return header_str + content_str


    def _set_current_person(self, model):
        raise NotImplementedError("MUST OVERRIDE")


    def _construct_main_header(self, model):
        raise NotImplementedError("MUST OVERRIDE")


    def _construct_content_wrapper(self, content_section):
        raise NotImplementedError("MUST OVERRIDE")


    def _construct_content_section(self, model):
        raise NotImplementedError("MUST OVERRIDE")


class UITabPage(UIAppPage):


    def _set_current_person(self, model):
        self._current_person = None
        for rival in model.rivals:
            if (rival.id == self.current_user.person_id):
                self._current_person = rival


    def _construct_main_header(self, model):
        return TabHeader(model.context)


    def _construct_content_wrapper(self, content_section):
        return TabContentWrapper(content_section)


class UILeaguePage(UITabPage):

    """ League Page UI Module. """

    def _construct_content_section(self, model):
        return LeagueContentSection(
                model.context,
                model.aggregations,
                model.objects,
                self._current_person)


class UIDialogPage(UIAppPage):

    def _set_current_person(self, model):
        pass

    def _construct_content_wrapper(self, content_section):
        return DialogContentWrapper(content_section)


class UICreateGameDialog(UIDialogPage):

    """ Create Game Dialog UI Module. """


    def _construct_main_header(self, model):
        return CreateGameDialogHeader()

    def _construct_content_section(self, model):
        return CreateGameContentSection(model)


class UILandingPage(tornado.web.UIModule):

    """ Splash Page UI Module.

    NOTE: Currently exists as a part of a separate hierarchy. It doesn't have
    access to the current person or the xsrf token.

    """


    def render(self, model=None, state=None):
        """ Render a Splash Page. """
        login_link = {
            "text": "Login",
            "href": "/login",
        }

        splash_tree = LandingPage(login_link)

        return Element.to_string(splash_tree)
