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

import tornado.web

from html.elements import Element
from html.mobile import AppHeader, ContextHeader
from html.mobile import NavHeader, GamesOL, RankingsOL


class UIAppHeader(tornado.web.UIModule):

    """ App Header UI Module. """

    def render(self, model=None):
        """ Render a App Header. """
        # TODO: if we ever use this, there should be an App object that
        # contains things like the name, icon, etc.
        return Element.to_string(AppHeader("SQOREBOARD").element())


class UIContextHeader(tornado.web.UIModule):

    """ Context Header UI Module. """

    def render(self, model=None):
        """ Render a Context Header. """

        element_tree = None

        # TODO: do more rigorous error checking on this type of model

        try:
            context = model.context
            element_tree = ContextHeader(context).element()

        except AttributeError as e:
            #logger.debug(e.reason)
            element_tree = None

        return Element.to_string(element_tree)


class UINavHeader(tornado.web.UIModule):

    """ Nav Header UI Module. """

    def render(self, model=None):
        """ Render a Nav Header. """

        # TODO: stop hardcoding all parameters to NavHeader...build a URL
        # class and use href constants and use a constant for index

        nav_links = [
                {
                    "text" : "Rankings",
                    "href" : "/rankings",
                    "class" : "link"
                    },
                {
                    "text" : "Games",
                    "href" : "/games",
                    "class" : "link"
                    }
                ]

        create_link = {
                    "text" : "+",
                    "href" : "/create/game",
                    "class" : "dialog-link route-bypass"
                    }

        create_link_index = 1

        element_tree = NavHeader(
                nav_links,
                create_link,
                create_link_index).element()

        return Element.to_string(element_tree)


class UIGamesList(tornado.web.UIModule):

    """ Games List UI Module. """

    def render(self, model=None):
        """ Render a Games List. """

        element_tree = None

        # TODO: do more rigorous error checking on this type of model

        try:
            games = model.games
            element_tree = GamesOL(games).element()

        except AttributeError as e:
            #logger.debug(e.reason)
            element_tree = None

        return Element.to_string(element_tree)


class UIRankingsList(tornado.web.UIModule):

    """ Rankings List UI Module. """

    def render(self, model=None):
        """ Render a Rankings List. """

        element_tree = None

        # TODO: do more rigorous error checking on this type of model

        try:
            rankings = model.rankings
            element_tree = RankingsOL(rankings).element()

        except AttributeError as e:
            #logger.debug(e.reason)
            element_tree = None

        return Element.to_string(element_tree)

