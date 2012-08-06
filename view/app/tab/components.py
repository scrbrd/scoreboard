""" Module: components

Elements components that will be used in tabs but aren't part of the framework.

"""
from view.constants import SQ_DATA
from view.elements.base import Span, Div, Section, UL, A
from view.elements.components import HeadedList, HeadedListItem, NumberedList
from view.elements.components import MultiColumnLI
from view.app.copy import Copy
from view.app.components import Headline, AppThumbnail, RelativeDateComponent
from view.app.facebook import FacebookThumbnail

from constants import COMPONENT_CLASS


class ResultHeadline(Headline):

    """ResultHeadline is a headline for the result of a game. """


    def __init__(self, winners, losers):
        """ Construct a headline for the played game type. """
        super(ResultHeadline, self).__init__("")

        winners_text = ", ".join([winner.name for winner in winners])
        losers_text = ", ".join([loser.name for loser in losers])
        headline = "{0} {1} {2}".format(
                winners_text,
                Copy.defeated,
                losers_text)
        self.set_text(headline)


class PlayedHeadline(Headline):

    """PlayedHeadline is a headline for a game without a result. """


    def __init__(self, players):
        """ Construct a headline for the played game type. """
        super(PlayedHeadline, self).__init__("")

        players_text = ", ".join([p.name for p in players])
        headline = "{0} {1}".format(players_text, Copy.played)
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


    def __init__(self, comments):
        """ Construct a CommentsBox.

        Required:
        list    comments    A list of comments, sorted by created_ts

        """
        super(CommentsSection, self).__init__()
        self.append_class(COMPONENT_CLASS.COMMENTS_SECTION)

        self.append_child(CommentsList(comments))
        # self.append_child(CommentsForm())


class CommentsList(UL):

    """ Comments List is a list of comments for a story. """


    def _init__(self, comments):
        """ Construct a CommentsList.

        Required:
        list    comments    A list of comments, sorted by created_ts

        """
        super(CommentsList, self).__init__(comments)

    def set_list_item(self, item, index):
        """ Construct and add a list item as a child of this list. """
        self.append_child(CommentsLI(item, index))


class CommentsLI(MultiColumnLI):

    """ CommentsLI is a single comment in the CommentsList. """


    def set_content(self, item):
        """ Set content for Rankings LI. """
        comment = item

        thumbnail = FacebookThumbnail(
                comment.commenter_fb_id,
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
