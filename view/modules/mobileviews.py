""" Module: mobileviews

Provide generic mobile views.
"""

import xml.etree.cElementTree as ET
from exceptions import NotImplementedError

import tornado.web

class ElementView(tornado.web.UIModule):

    """ Abstract Element. """

    def render(self):
        """ Raise NotImplementedError. """
        raise NotImplementedError("No generic HTML element.")


    def html(self):
        """ Raise NotImplementedError. """
        raise NotImplementedError("No generic HTML element.")


class ListView(ElementView):

    """ Abstract Wrapper around a List Element. """


    def _html_generate_list_items(self, handler, list_elem, list_items):
        """ Generate all the html list items for a list. """
        for li in list_items:
            list_elem.append(self._html_generate_list_item(self, li))
        return list_elem


    def _html_generate_list_item(self, handler, list_item):
        """ Generate the html for an individual list_item. """
        return ListItemView(handler).html(list_item)


class OrderedListView(ListView):

    """ Wrapper around an Ordered List Element. <ol> """
    
    def render(self):
        """ Render the <ol> element. """
        return ET.tostring(self.html(), encoding="utf-8")

    def html(self, list_items):
        """ Generate and return Element for <ol>. """
        list_elem = ET.Element("ol")
        
        # add any needed ol attributes here
        # TODO Move JQM Processing to separate processor
        list_elem.set("data-role", "listview")
        list_elem.set("data-theme", "sq-content")
        
        list_elem = self._html_generate_list_items(self, list_elem, list_items)        
        
        return list_elem
        

class GamesListView(OrderedListView):

    """ Games List View that extends Ordered List. """

    def render(self, games_list):
        """ Override render to generate Games List. """
        games_list = self.html(games_list.games)

        return ET.tostring(games_list, encoding="utf-8")


    def _html_generate_list_item(self, handler, game):
        """ Generate the html for a Game list item. """
        return GameListItemView(handler).html(game)


class RankingsListView(OrderedListView):

    """ Rankings View that extends Ordered List. """

    def render(self, rankings):
        """ Override render to generate Rankings List. """
        rankings_list = self.html(rankings.ranks)

        # TODO use / manipulate rank field
        rank_field = rankings.rank_field

        return ET.tostring(rankings_list, encoding="utf-8")


    def html(self, ranks):
        """ Generate and return ET.Element for a Rankings List <ol>. """
        rankings_list = super(RankingsListView, self).html(ranks)
        return rankings_list


    def _html_generate_list_item(self, handler, rank):
        """ Generate the html for a Rank list item. """
        return RankListItemView(handler).html(rank)


class ListItemView(ElementView):

    """ Wrapper around a List Element. <li> """

    def render(self):
        """ Render the <li> element. """
        return ET.tostring(self.html(), encoding="utf-8")


    def html(self):
        """ Generate and return Element for <li>. """
        list_item_elem = ET.Element("li")

        return list_item_elem


class GameListItemView(ListItemView):

    """ Game List Item View that extends List Item. """

    def render(self, game):
        """ Override render to generate Game List Items. """
        return ET.tostring(self.html(game), encoding="utf-8")


    def html(self, game):
        """ Generate html for a Game List Item using id,
        outcome, results' scores, and results' Opponents' names. """
        game_elem = super(GameListItemView, self).html()

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
        game_elem.text = "{0}: {1}".format(
                game.id,
                results_val)

        return game_elem


class RankListItemView(ListItemView):

    """ Rank List Item View that extends List Item. """

    def render(self, rank):
        """ Override render to generate Rank List Items. """
        return ET.tostring(self.html(rank), encoding="utf-8")


    def html(self, rank):
        """ Generate html for a Rank List Item using id, name, 
        and win_count. """
        rank_elem = super(RankListItemView, self).html()
        
        # add id, name, and win_count to list item
        # TODO organize this code in the framework, hide id
        rank_elem.text = "{0}: {1} {2}".format(
                rank.id, 
                rank.name,
                rank.win_count)
        
        return rank_elem


class Header2View(ElementView):

    """ Wrapper around a List Element. <li> """

    def render(self, header_text):
        """ Render the <h2> element. """
        return ET.tostring(self.html(header_text), encoding="utf-8")


    def html(self, header_text):
        """ Generate and return Element for <h2>. """
        header_elem = ET.Element("h2")

        # FIXME move this to generic Element
        # FIXME add attributes dictionary
        header_elem.text = header_text
        
        return header_elem


class ContentHeaderView(Header2View):

    """ Content Header View that extends Header2. """

    def render(self, content_header_text):
        """ Render the content header's <h2> element. """
        return ET.tostring(self.html(content_header_text), encoding="utf-8")


    def html(self, content_header):
        """ Generate adn return Element for content header. """
        content_header_elem = super(ContentHeaderView, self).html(
                content_header.name)
        
        content_header_elem.set("id", "content-header")

        return content_header_elem

