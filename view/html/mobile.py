""" Module: mobile

Provide mobile views.

"""
import json

from view.app_copy import Copy

from constants import HTML_DATA, HTML_ID, HTML_CLASS, HTML_NAME
from elements import Element, Div, Span, OL, UL, LI, Nav, A, H1, H2, Header
from elements import Form, TextInput, HiddenInput, CheckboxInput, SubmitButton, Button


class AppHeader(H1):

    """ App header extending <h1>. """


    def __init__(self, app_name):
        """ Construct an app header element tree. """
        super(AppHeader, self).__init__()
        self.set_text(app_name)


class ContextHeader(H2):

    """ Context header extending <h2>. """


    def __init__(self, context, rivals):
        """ Construct a context header element tree. """
        super(ContextHeader, self).__init__()

        # set context data
        self.set_id(HTML_ID.CONTEXT)
        self.set_data(HTML_DATA.ID, context.id)
        self.set_data(HTML_DATA.OBJECT_TYPE, context.type)
        self.set_text(context.name)

        # set rivals data
        view_rivals = []
        for r in rivals:
            view_rivals.append({HTML_DATA.ID: r.id, HTML_DATA.NAME: r.name})
        self.set_data(HTML_DATA.RIVALS, json.dumps(view_rivals))

class DialogHeader(Header):
    
    """ Dialog Header extending <header> and including <h2>. """


    def __init__(self, dialog_name):
        """ Construct a dialog header element tree. """
        super(DialogHeader, self).__init__()

        # h2 elem to insert into header
        h2 = H2()
        h2.set_text(dialog_name)
        self.append_child(h2)
        
    
class NavHeader(Nav):

    """ Nav header extending <nav>. """


    def __init__(self, items, special_item=None, special_item_index=0):
        """ Construct a nav header element tree. """
        super(NavHeader, self).__init__(
                items,
                special_item,
                special_item_index)

        # TODO: is there css we want applied to this class?
        #self.append_classes([])


    def set_list(self, items):
        """ Construct and add the NavUL list for this NavHeader. """
        self.append_child(NavUL(items))


class NavUL(UL):

    """ Nav header extending <nav>. """


    def __init__(self, items):
        """ Construct a nav header element tree. """
        super(NavUL, self).__init__(items)

        # TODO: add a special link parameter to account for plus button?

        # TODO: is there css we want applied even to this base class?
        #self.append_classes([])


    def set_list_item(self, item, index):
        """ Construct and add a link list item as this NavUL's child. """
        return self.append_child(NavHeaderLI(item, index))


class NavHeaderLI(LI):

    """ Nav header list item extending <li>.

        <li><span><a href="/foo">bar</a></span></li>

    """


    def __init__(self, item, index):
        """ Construct a nav header list item element tree. """
        super(NavHeaderLI, self).__init__(item, index)

        span = Span()
        # TODO: is there css we want applied even to this base class?
        #span.append_classes([])
        self.append_child(span)

        a = A(item)
        # TODO: this is a hardcoded string and not a constant because once we
        # have a Link class [and an Item interface or some such thing for it
        # to implement] we will just be accessing properties there. this makes
        # it more obvious what to change.
        a.append_class(item["class"])
        span.append_child(a)


class GamesOL(OL):

    """ Games List extending <ol>. """


    def set_list_item(self, item, index):
        """ Construct and add a list item as a child of this list. """
        return self.append_child(GameLI(item, index))


class RankingsOL(OL):

    """ Rankings List extending <ol>. """


    def set_list_item(self, item, index):
        """ Construct and add a list item as a child of this list. """
        return self.append_child(RankingLI(item, index))


class GameLI(LI):

    """ Game list item extending <li>. """


    def __init__(self, item, index):
        """ Construct a game list item element tree. """
        super(GameLI, self).__init__(item, index)

        # TODO: add css
        self.set_data(HTML_DATA.ID, item.id)
        self.set_data(HTML_DATA.OBJECT_TYPE, item.type)
        self.create_content(item)


    def create_content(self, item):
        """ Generate the content for this game list item. """
        # FIXME: this all breaks the contract that the view doesnt get
        # access to non-property methods in model.api.Game.

        # get results' Opponents' names, results' scores
        for result in item.outcome():
            # TODO: these are hardcoded to make the fact that they need to be
            # changed more obvious once we have result/outcome classes.
            id = result["id"]
            opponent = item.get_opponent(id)
            span = Span()
            span.set_data(HTML_DATA.ID, id)
            span.set_data(HTML_DATA.OBJECT_TYPE, opponent.type)
            span.set_text("{0} {1}".format(opponent.name, result["score"]))
            self.append_child(span)
        # game_text = ", ".join(results)


class RankingLI(LI):

    """ Ranking list item extending <li>. """


    def __init__(self, item, index):
        """ Construct a ranking list item element tree. """
        super(RankingLI, self).__init__(item, index)

        # TODO: add css and remove id.

        self.set_data(HTML_DATA.ID, item.id)
        self.set_data(HTML_DATA.OBJECT_TYPE, item.type)
        self.create_content(item)


    def create_content(self, item):
        """ Generate the content for this ranking list item. """
        span = Span()
        span.set_text("{0} {1}".format(item.name, item.win_count))
        self.append_child(span)


class CreateGameForm(Form):

    """ Create Game form extending <form>. """

    
    def __init__(self, name, xsrf_token, action_url):
        """ Construct a Create Game form element tree. 
        
        Required:
        str     name            the identifying name of the form
        str     xsrf_token      xsrf token to prevent forgery
        url     action_url      the url that the form submits to

        """
        super(CreateGameForm, self).__init__(name, xsrf_token, action_url)

        # FIXME take out hard coded values
        self.append_child(HiddenInput(HTML_NAME.LEAGUE, ""))
        self.append_child(HiddenInput(HTML_NAME.CREATOR, "700"))

        # need a single item so that OpponentScoreLI is created
        self.append_child(GameScoreUL(["", "", "", ""]))

        # add form submit and close buttons
        submit_button = SubmitButton()
        submit_button.set_text(Copy.submit)
        self.append_child(submit_button)
        close_button = Button()
        close_button.append_class(HTML_CLASS.CLOSE)
        close_button.set_text(Copy.close)
        self.append_child(close_button)


class GameScoreUL(UL):

    """ Game Score List extending <ul>. """


    def set_list_item(self, item, index):
        """ Construct and add a list item as a child of this list. """
        return self.append_child(GameScoreLI(item, index))


class GameScoreLI(LI):

    """ Game Score list item extending <li>. """


    def __init__(self, item, index):
        """ Construct a player score list item element tree. """
        super(GameScoreLI, self).__init__(item, index)

        self.create_content(item)


    def create_content(self, item):
        """ Generate the content for this game score list item. """
        # list names format: NAME[INDEX][DATA_TYPE]
        # id
        game_score_id = "{0}[{1}][{2}]".format(
                HTML_NAME.GAME_SCORE, 
                self._index,
                HTML_DATA.ID)
        id_input = TextInput(game_score_id)
        id_input.set_placeholder(Copy.player_placeholder)
        id_input.set_classes([HTML_CLASS.PLAYER_SELECT])
        self.append_child(id_input)

        # score
        game_score_score = "{0}[{1}][{2}]".format(
                HTML_NAME.GAME_SCORE, 
                self._index,
                HTML_DATA.SCORE)
        score_input = TextInput(game_score_score)
        score_input.set_placeholder(Copy.score_placeholder)
        self.append_child(score_input)


