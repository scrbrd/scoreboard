""" Module: mobile

Provide mobile views.

"""

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


    def __init__(self, context):
        """ Construct a context header element tree. """
        super(ContextHeader, self).__init__()
        self.set_text("{0} : {1}".format(context.id, context.name))


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


    def set_list_item(self, item):
        """ Construct and add a link list item as this NavUL's child. """
        return self.append_child(NavHeaderLI(item))


class NavHeaderLI(LI):

    """ Nav header list item extending <li>.

        <li><span><a href="/foo">bar</a></span></li>

    """


    def __init__(self, item):
        """ Construct a nav header list item element tree. """
        super(NavHeaderLI, self).__init__(item)

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


    def set_list_item(self, item):
        """ Construct and add a list item as a child of this list. """
        return self.append_child(GameLI(item))


class RankingsOL(OL):

    """ Rankings List extending <ol>. """


    def set_list_item(self, item):
        """ Construct and add a list item as a child of this list. """
        return self.append_child(RankingLI(item))


class GameLI(LI):

    """ Game list item extending <li>. """


    def __init__(self, item):
        """ Construct a game list item element tree. """
        super(GameLI, self).__init__(item)

        # TODO: this is the same as RankingLI...should there be a superclass
        # adding a <span> element to all <li> elements?

        # TODO: add css

        span = Span()
        span.set_text(self.create_text(item))
        #span.append_classes([])
        self.append_child(span)
        #self.append_classes([])


    def create_text(self, item):
        """ Generate the text for this game list item. """
        # FIXME: this all breaks the contract that the view doesnt get
        # access to non-property methods in model.api.Game.

        # get results' Opponents' names, results' scores
        results = []
        for result in item.outcome():
            # TODO: these are hardcoded to make the fact that they need to be
            # changed more obvious once we have result/outcome classes.
            results.append("{0} {1}".format(
                item.get_opponent(result["id"]).name,
                result["score"]))

        game_text = ", ".join(results)
        return "{0}: {1}".format(item.id, game_text)


class RankingLI(LI):

    """ Ranking list item extending <li>. """


    def __init__(self, item):
        """ Construct a ranking list item element tree. """
        super(RankingLI, self).__init__(item)

        # TODO: this is the same as RankingLI...should there be a superclass
        # adding a <span> element to all <li> elements?

        # TODO: add css and remove id.

        span = Span()
        span.set_text(self.create_text(item))
        #span.append_classes([])
        self.append_child(span)
        #self.append_classes([])


    def create_text(self, item):
        """ Generate the text for this game list item. """
        return "{0}: {1} {2}".format(item.id, item.name, item.win_count)


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

        # TODO make league and creator hidden fields
        # FIXME take out hard coded values
        self.append_child(HiddenInput("league", "693"))
        self.append_child(HiddenInput("creator", "700"))

        # add the game score list
        example_item = {
                "rank": 0,
                "id": "700",
                "score": "5",
                }
        self.append_child(GameScoreUL([example_item]))

        # add form submit and close buttons
        submit_button = SubmitButton()
        submit_button.set_text("Submit")
        self.append_child(submit_button)
        close_button = Button()
        close_button.append_class("close")
        close_button.set_text("Close")
        self.append_child(close_button)


class GameScoreUL(UL):

    """ Game Score List extending <ul>. """


    def set_list_item(self, item):
        """ Construct and add a list item as a child of this list. """
        return self.append_child(OpponentScoreLI(item))


class OpponentScoreLI(LI):

    """ Opponent's Score list item extending <li>. """


    def __init__(self, item):
        """ Construct a player score list item element tree. """
        super(OpponentScoreLI, self).__init__(item)

        id_name = "game_score[{0}][id]".format(item["rank"])
        id_input = TextInput(id_name, item["id"])
        score_name = "game_score[{0}][score]".format(item["rank"])
        score_input = TextInput(score_name, item["score"])

        self.append_child(id_input)
        self.append_child(score_input)


