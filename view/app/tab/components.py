""" Module: components

Elements components that will be used in tabs but aren't part of the framework.

"""
from view.constants import SQ_DATA
from view.elements.base import Span, Div, Section, UL, A
from view.elements.components import HeadedList, HeadedListItem, NumberedList
from view.elements.components import MultiColumnLI
from view.app.copy import Copy
from view.app.components import Headline, AppThumbnail, RelativeDateComponent

from constants import COMPONENT_CLASS


class GameStoryHeadline(Headline):

    """ GameStoryHeadline extending Headline. """


    def __init__(self, game):
        """ Construct a Headline for a GameStory. """
        super(GameStoryHeadline, self).__init__("")

        self._game = game

        # defined by subclasses
        self.set_opponents_text()

        self.append_child(SportComponent(game.sport))


    def join_opponent_names(self, opponents):
        """ Return a string list of Opponent names. """
        return ", ".join([opponent.name for opponent in opponents])


    def set_opponents_text(self):
        """ Set the Opponents Headline text for a GameStory. """
        raise NotImplementedError("Abstract Method: SUBCLASS MUST OVERRIDE!")


class SportComponent(Div):

    """ SportComponent is a subheader for the Sport of a Game. """


    def __init__(self, sport):
        """ Construct a SportComponent extending Div. """
        super(SportComponent, self).__init__()
        self.append_class(COMPONENT_CLASS.SPORT_STORY_COMPONENT)
        self.set_text(sport)


class RivalryHeadline(GameStoryHeadline):

    """ RivalryHeadline is a headline for the result of a game. """


    def __init__(self, game):
        """ Construct a headline for the played game type. """
        super(RivalryHeadline, self).__init__(game)


    def set_opponents_text(self):
        """ Set the Opponents Headline text for a GameStory. """
        # FIXME: this all breaks the contract that the view doesnt get
        # access to non-property methods in model.api.Game.
        winners = self._game.get_opponents(self._game.winner_ids)
        losers = self._game.get_opponents(self._game.loser_ids)
        headline = "{0} {1} {2}".format(
                self.join_opponent_names(winners),
                Copy.defeated,
                self.join_opponent_names(losers))
        self.set_text(headline)


class CamaraderieHeadline(GameStoryHeadline):

    """ CamaraderieHeadline is a headline for a game without a result. """


    def __init__(self, game):
        """ Construct a headline for the played game type. """
        super(CamaraderieHeadline, self).__init__(game)


    def set_opponents_text(self):
        """ Set the Opponents Headline text for a GameStory. """
        # FIXME: this all breaks the contract that the view doesnt get
        # access to non-property methods in model.api.Game.
        comrades = self._game.get_opponents(self._game.camaraderie_ids)
        headline = "{0} {1}".format(
                self.join_opponent_names(comrades),
                Copy.played)
        self.set_text(headline)


class MainStorySection(Section):

    """ MainStorySection is the main section of every story. """


    def __init__(self):
        """ Construct a main section for a story. """
        super(MainStorySection, self).__init__()
        self.append_class(COMPONENT_CLASS.MAIN_STORY_SECTION)


class CommentsSection(Section):

    """ Comments Section contains both the list of comments for a story and a
    form for inputting new comments. """


    def __init__(self, object_with_comments):
        """ Construct a CommentsBox.

        Required:
        sqobject object_with_comments  the object that was commented on

        """
        super(CommentsSection, self).__init__()
        self.append_class(COMPONENT_CLASS.COMMENTS_SECTION)

        self.append_child(CommentsList(object_with_comments))
        # self.append_child(CommentsForm())


class CommentsList(UL):

    """ Comments List is a list of comments for a story. """


    def __init__(self, object_with_comments):
        """ Construct a CommentsList.

        Required:
        SqObject object_with_comments  the object that was commented on

        """
        super(CommentsList, self).__init__(
                self._construct_items(object_with_comments))


    def set_list_item(self, item, index):
        """ Construct and add a list item as a child of this list. """
        self.append_child(CommentsLI(item, index))


    # remove this function when the items can be more properly constructed
    def _construct_items(self, object_with_comments):
        """ Return a list of comment_items.

        Required:
        SqObject object_with_comments  the object that was commented on

        """
        items = []
        comments = object_with_comments.comments
        for comment in comments:
            person = object_with_comments.get_commenter(comment.commenter_id)
            # FIXME: this is the worst code in our application
            # because it breaks the contract that view shouldn't be calling
            # methods on model object (see line above this comment) and also
            # the view shouldn't have to merge two items into one item. clearly
            # the comment should have more information in it.
            comment.commenter_name = person.name
            comment.commenter_picture = person.picture
            items.append(comment)

        return items



class CommentsLI(MultiColumnLI):

    """ CommentsLI is a single comment in the CommentsList. """


    def set_content(self, item):
        """ Set content for Rankings LI. """
        comment = item

        thumbnail = AppThumbnail(
                comment.commenter_picture,
                comment.commenter_name)
        self.set_column(thumbnail)

        div = Div()

        name = A({"href": "#"}, comment.commenter_name)
        div.append_child(name)

        msg = Span()
        msg.set_text(comment.message)
        div.append_child(msg)

        created_ts = RelativeDateComponent(comment.created_ts, False)
        div.append_child(created_ts)

        self.set_column(div)


class RankingsList(HeadedList):

    """ Rankings List extending HeadedList.

    list    _headings   contain the column headings for Rankings.

    """

    _headings = [
            " ",
            Copy.player,
            Copy.win_streak_short,
            Copy.win_percentage,
            Copy.loss_short,
            Copy.win_short
            ]


    def __init__(self, standings):
        """ Construct Rankings List using HeadedList. """
        super(RankingsList, self).__init__(self._headings, standings)

        self.append_class(COMPONENT_CLASS.RANKINGS_LIST)


    def set_list(self, rows):
        """ Set the list element for this list. """
        self.append_child(RankingsOL(rows))


class RankingsOL(NumberedList):

    """ Rankings List exntends <ol>. """


    def set_list_item(self, item, index):
        """ Construct and add a list item as a child of this list. """
        self.append_child(RankingLI(item, index))


class RankingLI(HeadedListItem):

    """ Ranking list item extending <li>. """

    def __init__(self, item, index):
        """ Construct a standing list item element tree. """
        super(RankingLI, self).__init__(item, index)
        # TODO: add css and remove id.
        self.set_data(SQ_DATA.ID, item.id)
        self.set_data(SQ_DATA.OBJECT_TYPE, item.type)


    def set_content(self, item):
        """ Set content for Rankings LI. """
        # TODO make this some default scoreboard icon

        div = Div()
        # FIXME: model should send None instead of "" since "" is a valid
        # src, but model doesn't yet distinguish/translate empty db values.
        src = item.picture_url if item.picture_url else None
        div.append_child(AppThumbnail(src, item.name))
        self.set_column(div)

        opponent = A({"href": "#"}, item.name)
        self.set_column(opponent)

        current_result_streak = Span()
        streak_text = item.current_result_streak
        if streak_text > 0:
            streak_text = "{}{}".format(
                    Copy.win_short,
                    streak_text)
        elif streak_text < 0:
            streak_text = "{}{}".format(
                    Copy.loss_short,
                    -streak_text)
        else:
            streak_text = "--"
        current_result_streak.set_text(streak_text)
        self.set_column(current_result_streak)

        percentage_span = Span()
        win_percentage = item.win_percentage
        win_percentage_text = " .{:.0f}".format(win_percentage * 1000)
        if win_percentage == 1.0:
            win_percentage_text = "1.000"
        elif win_percentage == 0.0:
            win_percentage_text = " .000"
        percentage_span.set_text(win_percentage_text)
        self.set_column(percentage_span)

        loss_count = Span()
        loss_count.set_text(item.loss_count)
        self.set_column(loss_count)

        win_count = Span()
        win_count.set_text(item.win_count)
        self.set_column(win_count)
