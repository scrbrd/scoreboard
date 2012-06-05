""" Module: mobile

Provide mobile views.

"""
import json

from view.app_copy import Copy

from view.constants import APP_DATA, FORM_NAME, APP_ID, APP_CLASS
from view.constants import DESIGN_ID, DESIGN_CLASS
from elements import Div, Span, OL, UL, LI, Nav, A, H1, H2, Header, Footer
from elements import Section, BR, Form, TextInput, HiddenInput, CheckboxInput
from elements import SubmitButton, Button, Table, TR, TD


class AppHeader(H1):

    """ App header extending <h1>. """


    def __init__(self, app_name):
        """ Construct an app header element tree. """
        super(AppHeader, self).__init__()
        self.set_text(app_name)


class ContextHeader(Div):

    """ Context header extending <div>. """


    def __init__(self, context, rivals):
        """ Construct a context header element tree.

        The div is for the background image and anything external. The
        inside h2 is for managing the font layout, specifically because
        some fonts aren't centered correctly.

        """
        super(ContextHeader, self).__init__()

        # set context data
        self.set_id(APP_ID.CONTEXT)
        self.set_data(APP_DATA.ID, context.id)
        self.set_data(APP_DATA.OBJECT_TYPE, context.type)
        self.set_classes([
            DESIGN_CLASS.MAIN_HEADER,
            DESIGN_CLASS.HEADER_SECTION,
        ])

        #add inner h2 and span around context
        h2 = H2()
        span = Span()
        span.set_text(context.name)
        h2.append_child(span)
        self.append_child(h2)

        # set rivals data
        view_rivals = []
        for r in rivals:
            view_rivals.append({APP_DATA.ID: r.id, APP_DATA.NAME: r.name})
        self.set_data(APP_DATA.RIVALS, json.dumps(view_rivals))


class DialogHeader(Header):

    """ Dialog Header extending <header> and including <h2>. """


    def __init__(self, dialog_name):
        """ Construct a dialog header element tree. """
        super(DialogHeader, self).__init__()

        # div elem to insert into header
        div = Div()
        div.set_classes([
            DESIGN_CLASS.HEADER_SECTION,
            DESIGN_CLASS.MAIN_HEADER,
        ])

        # insert h2 and span to separate text from background
        h2 = H2()
        span = Span()
        span.set_text(dialog_name)

        h2.append_child(span)
        div.append_child(h2)

        self.append_child(div)

        # close button is in dialog header
        close_button = Button()
        close_button.append_class(APP_CLASS.CLOSE)
        close_button.set_text(Copy.close)
        self.append_child(close_button)


class NavHeader(Nav):

    """ Nav header extending <nav>. """


    def __init__(self, items, special_item=None, special_item_index=0):
        """ Construct a nav header element tree. """
        super(NavHeader, self).__init__(
                items,
                special_item,
                special_item_index)

        self.append_classes([
            DESIGN_CLASS.SECOND_HEADER,
            DESIGN_CLASS.HEADER_SECTION,
        ])


    def set_list(self, items):
        """ Construct and add the NavUL list for this NavHeader. """
        self.append_child(NavUL(items))


class NavUL(UL):

    """ Nav header extending <nav>. """


    def __init__(self, items):
        """ Construct a nav header element tree. """
        super(NavUL, self).__init__(items)

        # TODO: is there css we want applied even to this base class?
        #self.append_classes([])


    def set_list_item(self, item, index):
        """ Construct and add a link list item as this NavUL's child. """
        self.append_child(NavHeaderLI(item, index))


class NavHeaderLI(LI):

    """ Nav header list item extending <li>.

        <li><span><a href="/foo">bar</a></span></li>

    """


    def __init__(self, item, index):
        """ Construct a nav header list item element tree. """
        super(NavHeaderLI, self).__init__(item, index)

        span = Span()
        self.append_child(span)

        a = A(item)
        # TODO: this is a hardcoded string and not a constant because once we
        # have a Link class [and an Item interface or some such thing for it
        # to implement] we will just be accessing properties there. this makes
        # it more obvious what to change.
        a.append_class(item["class"])
        span.append_child(a)


class AppFooter(Footer):

    """ App footer contains a fixed add button in a <footer>. """

    def __init__(self):
        """ Construct the apps' footer element tree. """
        super(AppFooter, self).__init__()

        add_link = {
            "text": "+",
            "href": "/create/game",
        }

        anchor = A(add_link)
        anchor.set_id(APP_ID.ADD_BUTTON)
        anchor.set_classes([APP_CLASS.DIALOG_LINK])
        self.append_child(anchor)


class PageSection(Section):

    """ Page section encapsulates the generic page wrappers around i
    <section>. """

    def __init__(self, page_name):
        """ Construct a page section element tree.

        Required:
        string  page_name   the page name of this page.

        """
        super(PageSection, self).__init__()
        self.set_id(APP_ID.CONTENT)
        self.set_data(APP_DATA.PAGE_NAME, page_name)


class GamesOL(OL):

    """ Games List extending <ol>. """


    def set_list_item(self, item, index):
        """ Construct and add a list item as a child of this list. """
        self.append_child(GameLI(item, index))


class RankingsOL(OL):

    """ Rankings List extending <ol>. """


    def __init__(self, items):
        """ Construct a Rankings of type <ol>. """
        super(RankingsOL, self).__init__(items)
        self.set_classes([DESIGN_CLASS.COUNTER])


    def set_list_item(self, item, index):
        """ Construct and add a list item as a child of this list. """
        self.append_child(RankingLI(item, index))


class GameLI(LI):

    """ Game list item extending <li>. """


    def __init__(self, item, index):
        """ Construct a game list item element tree. """
        super(GameLI, self).__init__(item, index)

        # TODO: add css
        self.set_data(APP_DATA.ID, item.id)
        self.set_data(APP_DATA.OBJECT_TYPE, item.type)
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
            span.set_data(APP_DATA.ID, id)
            span.set_data(APP_DATA.OBJECT_TYPE, opponent.type)
            span.set_text("{0} {1}".format(opponent.name, result["score"]))
            self.append_child(span)

            # add break between results
            br = BR()
            self.append_child(br)

        # game_text = ", ".join(results)


class RankingLI(LI):

    """ Ranking list item extending <li>. """


    def __init__(self, item, index):
        """ Construct a ranking list item element tree. """
        super(RankingLI, self).__init__(item, index)

        # TODO: add css and remove id.

        self.set_data(APP_DATA.ID, item.id)
        self.set_data(APP_DATA.OBJECT_TYPE, item.type)
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
        self.append_child(HiddenInput(FORM_NAME.LEAGUE, ""))
        self.append_child(HiddenInput(FORM_NAME.CREATOR, "700"))

        # need a single item so that OpponentScoreLI is created
        headings = ["Player", "W"]
        self.append_child(GameScoreDiv(headings))

        # need break to make buttons clear
        self.append_child(BR())

        # add form submit and close buttons
        button_wrapper = Div()
        button_wrapper.set_classes([APP_CLASS.BUTTON_WRAPPER])

        submit_button = SubmitButton()
        submit_button.set_text(Copy.submit)
        button_wrapper.append_child(submit_button)

        self.append_child(button_wrapper)
        self.append_classes([APP_CLASS.DIALOG_CONTENT])


class GameScoreDiv(Div):

    """ Game Score List with header extending <div>. """

    def __init__(self, headings):
        """ Construct a GameScore header and list container <div>. """
        super(GameScoreDiv, self).__init__()

        # create Header object
        game_score_header = GameScoreHeader(headings)
        self.append_child(game_score_header)

        # create List
        numberOfRows = 4
        rows = []
        for x in xrange(numberOfRows):
            rows.append(x)
        self.append_child(GameScoreUL(rows))

        self.set_classes([APP_CLASS.LIST_WITH_HEADERS])


class GameScoreHeader(Header):

    """ Game Score column headings extending <header>. """

    def __init__(self, headings):
        """ Construct a GameScore header element <header>. """
        super(GameScoreHeader, self).__init__()

        col_head_0 = Div()
        col_head_0.set_text(headings[0])
        col_head_0.set_classes([APP_CLASS.COLUMN_0])

        col_head_1 = Div()
        col_head_1.set_text(headings[1])
        col_head_1.set_classes([APP_CLASS.COLUMN_1])

        self.append_child(col_head_0)
        self.append_child(col_head_1)

        self.set_classes([APP_CLASS.HEADED_LIST_ITEM])
    
class GameScoreUL(UL):

    """ Game Score List extending <ul>. """


    def set_list_item(self, item, index):
        """ Construct and add a list item as a child of this list. """
        self.append_child(GameScoreLI(item, index))


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
                FORM_NAME.GAME_SCORE,
                self._index,
                APP_DATA.ID)
        id_input = TextInput(game_score_id)
        id_input.set_placeholder(Copy.player_placeholder)
        id_input.set_classes([APP_CLASS.PLAYER_SELECT, APP_CLASS.COLUMN_0])
        # add autofocus to first element
        if item == 0:
            id_input.set_autofocus()
        self.append_child(id_input)

        # winner
        # translated to score to work with the backend
        winner_value = "1"
        game_score_winner = "{0}[{1}][{2}]".format(
                FORM_NAME.GAME_SCORE,
                self._index,
                APP_DATA.SCORE)
        winner_input = CheckboxInput(game_score_winner, winner_value)
        winner_input.set_classes([APP_CLASS.COLUMN_1])
        self.append_child(winner_input)

        self.set_classes([APP_CLASS.HEADED_LIST_ITEM])
