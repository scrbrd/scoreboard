""" Module: mobileview

Provide generic mobile views.

"""

import xml.etree.cElementTree as ET

from elementview import DivView, SpanView, NavView
from elementview import OLView, ULView, LIView
from elementview import H1View, H2View


class AppHeaderView(H1View):

    """ App header extending <h1> in the H1View. """
    pass


class ContextHeaderView(H2View):

    """ Context header extending <h2> in the H2View. """

    def html(self, text):
        """ Generate and return the content header block element. """
        elem = super(ContextHeaderView, self).html(text)
        # FIXME: do this with type+id to guarantee uniqueness
        elem.set("id", "context_header-{0}".format(text))
        return elem


class NavHeaderView(NavView):

    """ Nav Header View extending NavView. """

    def render(self):
        """ Render the nav header as a <nav> and nested <ul>. """
        nav_items = {
                "Rankings" : "#/rankings",
                "Games" : "#/games"
                }
        return super(NavHeaderView, self).render(nav_items)


class GamesListView(OLView):

    """ Games List View that extends Ordered List. """

    def _html_generate_list_item(self, game):
        """ Generate the html for a Game list item. """
        return GameListItemView(self).html(game)


class RankingsListView(OLView):

    """ Rankings View that extends Ordered List. """

    def _html_generate_list_item(self, rank):
        """ Generate the html for a Rank list item. """
        return RankListItemView(self).html(rank)


class GameListItemView(LIView):

    """ Game List Item View that extends List Item. """

    def html(self, game):
        """ Generate html for a Game List Item using id,
        outcome, results' scores, and results' Opponents' names. """

        # get results' Opponents' names, results' scores
        # TODO organize this code using our framework, hide id
        results_val = ""
        for result in game.outcome():
            score = result[0]
            opp_id = result[1]
            name = game.get_opponent(opp_id).name
            results_val = "{0}{1} {2}, ".format(
                    results_val,
                    name,
                    score)
        results_val = results_val[:-2]
        
        results_val = ", ".join(
                "{name} {score}".format(
                        score=score, 
                        name=game.get_opponent(opp_id).name)
                for (score, opp_id) in game.outcome())
      
        # FIXME which results_val does Warman like better?

        # add game id and outcome info to element
        text = "{0}: {1}".format(
                game.id,
                results_val)

        return super(GameListItemView, self).html(SpanView(self).html(text))


class RankListItemView(LIView):

    """ Rank List Item View that extends List Item. """

    def html(self, rank):
        """ Generate html for a Rank List Item using id, name, 
        and win_count. """

        # add id, name, and win_count to list item
        # TODO organize this code in the framework, hide id
        text = "{0}: {1} {2}".format(
                rank.id, 
                rank.name,
                rank.win_count)

        return super(RankListItemView, self).html(SpanView(self).html(text))

