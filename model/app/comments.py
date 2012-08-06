""" Module: comments

Define a CommentsModel to fetch facebook comments and organize them for the
CommentsHandler.

Using facebook-sdk (https://github.com/pythonforfacebook/facebook-sdk)

"""

from util.dev import print_timing

import datetime
import time
import facebook

from base import ReadModel


# TODO: put these in a constants file
FB_COMMENTS = "comments"
FB_ID = "id"
FB_DATA = "data"
FB_CREATED_TIME = "created_time"
FB_MESSAGE = "message"
FB_COMMENTER = "from"
FB_COMMENTER_FB_ID = "id"
FB_COMMENTER_NAME = "name"

APP_URL = "http://onscoreboard.com/"
STORY_SLUG = "story/"


class CommentsModel(ReadModel):

    """ Fetch comments (from facebook).

    Required:
    list    _game_ids       list of game ids.
    dict    _comments       key: game_id, value: list of comments

    See:
    http://graph.facebook.com/comments?id=http://onscoreboard.com/story/12

    """


    def __init__(self, session, game_ids):
        """ Construct a CommentsModel from a list of game ids.

        Required:
        list    game_ids    list of game ids

        """
        super(CommentsModel, self).__init__(session)

        self._game_ids = game_ids
        self._comments = {}


    @print_timing
    def load(self):
        """ Load comments for games. """

        # TODO: investigate performance to make sure that these facebook
        # requests are fast.

        graph = facebook.GraphAPI(self.session.get_access_token())

        # make this a batch request
        for id in self._game_ids:
            post_url = "{}{}{}".format(APP_URL, STORY_SLUG, id)
            comments = graph.request(FB_COMMENTS, {FB_ID: post_url})

            self._comments[id] = [Comment(c) for c in comments[FB_DATA]]


    @property
    def comments(self):
        """ Return the comments from facebook as a dict, keyed on game id. """
        return self._comments


class Comment(object):

    """ An individual comment.

    Required:
    ts  _created_ts     the ts of the comment
    str _message        the body of the comment
    id  _from_fb_id     the facebook id of the commenter
    str _from_name      the name of the commenter

    TODO: Move this to the API layer.

    """


    def __init__(self, comments_dict):
        """ Construct a comment.

        Required:
        dict comments_dict  the dict that facebook returns with a single
                            comment.

        """
        self._created_ts = Comment._get_ts_from_fb_time(
                comments_dict[FB_CREATED_TIME])
        self._message = comments_dict[FB_MESSAGE]
        self._from_fb_id = comments_dict[FB_COMMENTER][FB_COMMENTER_FB_ID]
        self._from_name = comments_dict[FB_COMMENTER][FB_COMMENTER_NAME]


    @property
    def created_ts(self):
        """ Return the timestamp of the comment. """
        return self._created_ts


    @property
    def message(self):
        """ Return the message (comment body) of the comment. """
        return self._message


    @property
    def commenter_fb_id(self):
        """ Return the facebook id of the commenter. """
        return self._from_fb_id


    @property
    def commenter_name(self):
        """ Return the name of the commenter. """
        return self._from_name

    @staticmethod
    def _get_ts_from_fb_time(fb_time):
        """ Convert the facebook time to a normal timestamp. """
        format = "%Y-%m-%dT%H:%M:%S+0000"
        dt = datetime.datetime.strptime(fb_time, format)
        return int(time.mktime(dt.timetuple()))
