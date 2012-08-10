""" Module: comments

Define a CommentsModel to fetch facebook comments and organize them for the
CommentsHandler. Define a CreateCommentModel to process incoming create comment
requests.

Using facebook-sdk (https://github.com/pythonforfacebook/facebook-sdk)

"""

from util.dev import print_timing

from model.api.comment import Comment

from base import ReadModel, WriteModel


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
        # TODO: Reading comments without a larger context is not supported.
        pass


    @property
    def comments(self):
        """ Return the comments from facebook as a dict, keyed on game id. """
        return self._comments


class CreateCommentModel(WriteModel):

    """ Handle create comment requests by sending the comment to facebook.

    Required:
    id  _object_id       id of the object that is the object of the comment
    str _message         the comment body

    Return:
    SqObject    _object     the new comment

    """


    def __init__(self, session, object_id, message):
        """ Construct a model for creating a comment.

        Required:
        dict    session                 all the User/Person session data
        id  object_id       id of the object that is the object of the comment
        str message         the comment body

        """
        super(CreateCommentModel, self).__init__(session)

        self._object_id = object_id
        self._message = message


    def dispatch(self):
        """ Create new Comment on facebook and return it. """
        self._object = Comment.create_comment(
            self._object_id,
            self.session.person_id,
            self._message)


    @property
    def comment(self):
        """ Return a newly created Comment. """
        return self._object
