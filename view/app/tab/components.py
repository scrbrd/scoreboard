""" Module: components

Elements components that will be used in tabs but aren't part of the framework.

"""

from view.constants import SQ_DATA, PAGE_NAME
from view.elements.base import Span, Div, Section, UL, A, LI
from view.elements.base import Form, TextInput, HiddenInput, SubmitButton
from view.elements.components import HeadedList, HeadedListItem, NumberedList
from view.elements.components import MultiColumnLI
from view.app.copy import Copy
from view.app.components import AppThumbnail, RelativeDateComponent


class SportComponent(Span):

    """ SportComponent is a subheader for the Sport of a Game. """

    SPORT_COMPONENT_CLASS = "sport-component"


    def __init__(self, sport):
        """ Construct a SportComponent extending Span. """
        super(SportComponent, self).__init__()
        self.append_class(self.SPORT_COMPONENT_CLASS)
        self.set_text(sport)


class HeadlineSection(Section):

    """ HeadlineSection is the poster section of every story. """

    HEADLINE_SECTION_CLASS = "headline-section"


    def __init__(self, person_thumbnail, headline, date_component):
        """ Construct a headline section for a story. """
        super(HeadlineSection, self).__init__()
        self.append_class(self.HEADLINE_SECTION_CLASS)

        self.append_child(person_thumbnail)
        self.append_child(date_component)
        self.append_child(headline)


class CommentsSection(Section):

    """ Comments Section contains both the list of comments for a story and a
    form for inputting new comments. """

    COMMENTS_SECTION_CLASS = "comments-section"


    def __init__(self, current_person, object_with_comments):
        """ Construct a CommentsBox.

        Required:
        Person  current_person  the current User's associated Person
        sqobject object_with_comments  the object that was commented on

        """
        super(CommentsSection, self).__init__()
        self.append_class(self.COMMENTS_SECTION_CLASS)

        self.append_child(CommentsList(object_with_comments))
        self.append_child(CommentForm(current_person, object_with_comments.id))


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
        self.append_child(CommentLI(item, index))


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
            comment.commenter_picture_url = person.picture_url
            items.append(comment)

        return items



class CommentLI(MultiColumnLI):

    """ CommentLI is a single comment in the CommentsList. """


    def set_content(self, item):
        """ Set content for CommentLI. """
        comment = item  # item must be a comment

        thumbnail = AppThumbnail(
                comment.commenter_picture_url,
                comment.commenter_name)
        self.set_column(thumbnail)

        div = Div()

        name = A({"href": "#"}, comment.commenter_name)
        div.append_child(name)

        msg = Span()
        msg.set_text(comment.message)
        div.append_child(msg)

        created_ts = RelativeDateComponent(comment.created_ts)
        div.append_child(created_ts)

        self.set_column(div)


class CommentForm(Form):

    """ A Form for submitting a single comment to a Story. """

    COMMENT_FORM_CLASS = "comment-form"


    def __init__(self, current_person, story_id):
        """ Construct a CommentForm.

        Required:
        Person  current_person  the current User's associated Person
        id  story_id    id of the SqNode Story object

        """
        super(CommentForm, self).__init__(
                "{}{}".format(PAGE_NAME.LEAGUE, story_id))

        # TODO: make this draw from view.url constants
        self.set_action("/comment")
        self.append_class(self.COMMENT_FORM_CLASS)

        self.append_child(HiddenInput(SQ_DATA.GAME_ID, story_id))

        self.append_child(AppThumbnail(current_person.picture_url))

        # div allows overflow: auto to maximize that column
        comment_div = Div()
        comment_input = TextInput(SQ_DATA.MESSAGE)
        comment_input.set_placeholder(Copy.comment)
        comment_div.append_child(comment_input)

        self.append_child(comment_div)
        self.append_child(SubmitButton(Copy.comment))


class RankingsList(HeadedList):

    """ Rankings List extending HeadedList.

    list    _headings   contain the column headings for Rankings.

    """

    RANKINGS_LIST_CLASS = "rankings-list"

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

        self.append_class(self.RANKINGS_LIST_CLASS)


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


class OpponentsList(UL):

    """ OpponentsList is a list of players for anything. """

    OPPONENTS_LIST_CLASS = "opponents-list"


    def __init__(self, opponents):
        """ Construct an OpponentsList.

        Required:
        list    opponents   a list of opponents to display

        """
        super(OpponentsList, self).__init__(opponents)
        self.append_class(self.OPPONENTS_LIST_CLASS)

    def set_list_item(self, item, index):
        """ Construct and add a list item as a child of this list. """
        self.append_child(OpponentLI(item, index))


class OpponentLI(LI):

    """ OpponentLI is a single opponent with a thumbnail and name. """


    def set_content(self, item):
        """ Set content for OpponentLI. """
        opponent = item  # item must be an opponent

        thumbnail = AppThumbnail(opponent.picture_url, opponent.name)
        name = A({"href": "#"}, opponent.name)

        self.append_child(thumbnail)
        self.append_child(name)
