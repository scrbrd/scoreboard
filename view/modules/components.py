""" Module: components

Provide required subclasses of Tornado's UIModule for delagating the
rendering of markup from Tornado's PSP templates to our implementation
of HTML, which subclasses python's xml.etree.cElementTree.

Effectively, this will serve as a mapping between the opaque model the
controller has passed along and the specific data the view needs
extracted in order to render markup.

Each class has a single requirement...override the following:
    def render(self, model=None):

"""

# TODO: should this be in a util?
import xml.etree.cElementTree as ET

import tornado.web

from view.app_copy import Copy
from view.constants import PAGE_TYPE, PAGE_NAME, APP_CLASS, SQ_DATA

from view.elements.base import Element

from view.app.tab.framework import AppHeader, AppFooter, NavHeader
from view.app.tab.framework import TabHeader, TabContentSection
from view.app.tab.model import ContextModel, PageModel, SessionModel
from view.app.tab.games import GamesTabSection
from view.app.tab.rankings import RankingsTabSection

from view.app.dialog.framework import DialogHeader
from view.app.dialog.create_game import CreateGameForm

from view.app.page.landing import LandingPage


class UIAppHeader(tornado.web.UIModule):

    """ App Header UI Module. """

    def render(self, model=None, state=None):
        """ Render a App Header. """
        # TODO: if we ever use this, there should be an App object that
        # contains things like the name, icon, etc.
        element_tree = AppHeader(Copy.app_name).element()

        return Element.to_string(element_tree)


class UIAppFooter(tornado.web.UIModule):

    """ App Footer UI Module. """

    def render(self, model=None, state=None):
        """ Render an App Footer. """
        element_tree = AppFooter().element()

        return Element.to_string(element_tree)


class UITabHeader(tornado.web.UIModule):

    """ TabHeader UI Module. """

    def render(self, model=None, state=None):
        """ Render a TabHeader. """
        context = model.context

        element_tree = TabHeader(context).element()

        return Element.to_string(element_tree)


class UIContextModel(tornado.web.UIModule):

    """ Context Model UI Module. """

    def render(self, model=None, state=None):
        """ Render a Context Model. """
        context = model.context
        element_tree = ContextModel(context).element()

        return Element.to_string(element_tree)


class UISessionModel(tornado.web.UIModule):

    """ Session Model UI Module. """

    def render(self, model=None, state=None):
        """ Render a Session Model. """
        element_tree = SessionModel(model).element()

        return Element.to_string(element_tree)


class UINavHeader(tornado.web.UIModule):

    """ Nav Header UI Module. """

    def render(self, model=None, state=None):
        """ Render a Nav Header. """

        # TODO: stop hardcoding all parameters to NavHeader...build a URL
        # class and use href constants and use a constant for index

        nav_items = []
        special_item = None
        special_index = -1

        rankings_item = {
            "page_name": PAGE_NAME.RANKINGS,
            "text": "Rankings",
            "href": "/rankings",
            "class": PAGE_NAME.RANKINGS,
        }
        games_item = {
            "page_name": PAGE_NAME.GAMES,
            "text": "Games",
            "href": "/games",
            "class": PAGE_NAME.GAMES,
        }

        if rankings_item["page_name"] == state:
            nav_items.append(games_item)
            special_item = rankings_item
            special_index = 0
        elif games_item["page_name"] == state:
            nav_items.append(rankings_item)
            special_item = games_item
            special_index = 1
        else:
            print("ERROR in render UINavHeader")

        sp_classes = special_item["class"] + " " + APP_CLASS.ACTIVE_NAV
        special_item["class"] = sp_classes

        for item in nav_items:
            classes = item["class"] + " " + APP_CLASS.INACTIVE_NAV
            item["class"] = classes

        element_tree = NavHeader(
                nav_items,
                special_item,
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


class UIPageModel(tornado.web.UIModule):

    """ Generic Content Model View. """

    def render(self, model=None, state=None):
        """ Render a Content Model View. """
        element_tree = PageModel(state).element()

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


class UIGamesModel(UITabModel):

    """ Games Content Model View. """

    def render(self, model=None, state=None):
        """ Render a Games Content Model View. """
        return super(UIGamesModel, self).render(None, PAGE_NAME.GAMES)


class UIRankingsModel(UITabModel):

    """ Rankings Content Model View. """

    def render(self, model=None, state=None):
        """ Render a Rankings Content Model View. """
        return super(UIRankingsModel, self).render(None, PAGE_NAME.RANKINGS)


class UILeagueModel(UITabModel):

    """ League Content Model View. """

    def render(self, model=None, state=None):
        """ Render a League Content Model View. """
        return super(UILeagueModel, self).render(None, PAGE_NAME.LEAGUE)


class UIGamesList(tornado.web.UIModule):

    """ Games List UI Module. """

    def render(self, model=None, state=None):
        """ Render a Games List. """
        element_tree = GamesTabSection(model.games).element()
        return Element.to_string(element_tree)


class UIRankingsList(tornado.web.UIModule):

    """ Rankings List UI Module. """

    def render(self, model=None, state=None):
        """ Render a Rankings List. """
        element_tree = RankingsTabSection(model.rankings).element()
        return Element.to_string(element_tree)


class UILeaguePage(tornado.web.UIModule):

    """ League Page UI Module. """

    def render(self, model=None, state=None):
        """ Render a League. """
        league_page = TabContentSection()

        # TODO: hook up model to the way we use it here.
        league_page.set_properties_content(model.league.context)
        league_page.set_summary_content(model.league.aggregations)
        league_page.set_feed_content(model.league.objects)

        return Element.to_string(league_page.element())


class UICreateGameDialog(tornado.web.UIModule):

    """ Create Game Dialog UI Module. """


    def render(self, model=None, state=None):
        """ Render a Create Game Dialog Screen. """
        # block xsrf for forms. required for Tornado posts.
        # get the input element and pass the token only.
        xsrf_tag = self.handler.xsrf_form_html()
        xsrf_token = ET.fromstring(xsrf_tag).attrib.get("value")

        header_tree = DialogHeader(Copy.create_game_dialog_header).element()
        form_tree = CreateGameForm(
                "create-game",
                xsrf_token,
                "/create/game"
                ).element()

        return Element.to_string(header_tree) + Element.to_string(form_tree)


class UILandingPage(tornado.web.UIModule):

    """ Splash Page UI Module. """

    def render(self, model=None, state=None):
        """ Render a Splash Page. """
        login_link = {
            "text": "Login",
            "href": "/login",
        }

        splash_tree = LandingPage(login_link).element()

        return Element.to_string(splash_tree)
