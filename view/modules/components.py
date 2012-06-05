""" Module: components

Provide required subclasses of Tornado's UIModule for delagating the
rendering of markup from Tornado's PSP templates to our implementation
of HTML, which subclasses python's xml.etree.cElementTree.

Effectively, this will serve as a mapping between the opaque model the
controller has passed along and the specific data the view needs
extracted in order to render markup.

Provides the following:
    class UIAppHeader
    class UIContextHeader
    class UINavHeader
    class UIGamesList
    class UIRankingsList

Each class has a single requirement...override the following:
    def render(self, model=None):

"""
# TODO: should this be in a util?
import xml.etree.cElementTree as ET
import tornado.web

from view.app_copy import Copy
from view.constants import PAGE_NAME, DESIGN_CLASS, APP_CLASS
from html.elements import Element
from html.mobile import AppHeader, ContextHeader, AppFooter
from html.mobile import NavHeader, GamesOL, RankingsOL
from html.mobile import DialogHeader, CreateGameForm
from html.mobile import PageSection


class UIAppHeader(tornado.web.UIModule):

    """ App Header UI Module. """

    def render(self, model=None, state=None):
        """ Render a App Header. """
        # TODO: if we ever use this, there should be an App object that
        # contains things like the name, icon, etc.
        element_tree = None

        try:
            element_tree = AppHeader("SQOREBOARD").element()

        except AttributeError as e:
            raise e
            element_tree = None

        return Element.to_string(element_tree)


class UIAppFooter(tornado.web.UIModule):

    """ App Footer UI Module. """

    def render(self, model=None, state=None):
        """ Render an App Footer. """
        element_tree = None

        try:
            element_tree = AppFooter().element()

        except AttributeError as e:
            raise e
            element_tree = None

        return Element.to_string(element_tree)


class UIContextHeader(tornado.web.UIModule):

    """ Context Header UI Module. """

    def render(self, model=None, state=None):
        """ Render a Context Header. """

        element_tree = None

        # TODO: do more rigorous error checking on this type of model

        try:
            context = model.context
            rivals = model.rivals
            element_tree = ContextHeader(context, rivals).element()

        except AttributeError as e:
            #logger.debug(e.reason)
            element_tree = None

        return Element.to_string(element_tree)


class UINavHeader(tornado.web.UIModule):

    """ Nav Header UI Module. """

    def render(self, model=None, state=None):
        """ Render a Nav Header. """

        # TODO: stop hardcoding all parameters to NavHeader...build a URL
        # class and use href constants and use a constant for index

        nav_links = []
        special_link = None
        special_index = -1

        rankings_link = {
            "page_name": PAGE_NAME.RANKINGS,
            "text": "Rankings",
            "href": "/rankings",
            "class": PAGE_NAME.RANKINGS,
        }
        games_link = {
            "page_name": PAGE_NAME.GAMES,
            "text": "Games",
            "href": "/games",
            "class": PAGE_NAME.GAMES,
        }

        if rankings_link["page_name"] == state:
            nav_links.append(games_link)
            special_link = rankings_link
            special_index = 0
        elif games_link["page_name"] == state:
            nav_links.append(rankings_link)
            special_link = games_link
            special_index = 1
        else:
            print("ERROR in render UINavHeader")

        sp_classes = special_link["class"] + " " + DESIGN_CLASS.ACTIVE_NAV
        special_link["class"] = sp_classes

        for link in nav_links:
            classes = link["class"] + " " + APP_CLASS.INACTIVE_NAV
            link["class"] = classes

        element_tree = NavHeader(
                nav_links,
                special_link,
                special_index).element()

        return Element.to_string(element_tree)


class UIGamesNav(UINavHeader):

    """ Nav Header UI Module with Games active. """

    def render(self, model=None, state=None):
        """ Render a Nav Header with Games active. """
        return super(UIGamesNav, self).render(model, PAGE_NAME.GAMES)


class UIRankingsNav(UINavHeader):

    """ Nav Header UI Module with Rankings active. """

    def render(self, model=None, state=None):
        """ Render a Nav Header with Rankings active. """
        return super(UIRankingsNav, self).render(model, PAGE_NAME.RANKINGS)


class UIGamesList(tornado.web.UIModule):

    """ Games List UI Module. """

    def render(self, model=None, state=None):
        """ Render a Games List. """

        element_tree = None

        # TODO: do more rigorous error checking on this type of model

        try:
            games = model.games

            section = PageSection(PAGE_NAME.GAMES)
            section.append_child(GamesOL(games))
            element_tree = section.element()

        except AttributeError as e:
            #logger.debug(e.reason)
            element_tree = None

        return Element.to_string(element_tree)


class UIRankingsList(tornado.web.UIModule):

    """ Rankings List UI Module. """

    def render(self, model=None, state=None):
        """ Render a Rankings List. """

        element_tree = None

        # TODO: do more rigorous error checking on this type of model

        try:
            rankings = model.rankings

            section = PageSection(PAGE_NAME.RANKINGS)
            section.append_child(RankingsOL(rankings))
            element_tree = section.element()

        except AttributeError as e:
            #logger.debug(e.reason)
            element_tree = None

        return Element.to_string(element_tree)


class UICreateGameDialog(tornado.web.UIModule):

    """ Create Game Dialog UI Module. """

    def render(self, model=None, state=None):
        """ Render a Create Game Dialog Screen. """

        header_tree = None
        form_tree = None

        # block xsrf for forms. required for Tornado posts.
        # get the input element and pass the token only.
        xsrf_tag = self.handler.xsrf_form_html()
        xsrf_token = ET.fromstring(xsrf_tag).attrib.get("value")

        try:
            header_elem = DialogHeader(Copy.create_game_dialog_header)
            header_tree = header_elem.element()

            form_tree = CreateGameForm(
                    "create-game",
                    xsrf_token,
                    "/create/game"
                    ).element()

        except AttributeError as e:
            #logger.debug(e.reason)
            raise e
            header_tree = None
            form_tree = None

        header_str = Element.to_string(header_tree)
        form_str = Element.to_string(form_tree)
        dialog_str = header_str + form_str
        return dialog_str
