""" Module: facebook

Components for interacting with facebook directly.

Note: FacebookLoginButton isn't here because it doesn't interact with Facebook
directly.

"""

from components import AppThumbnail


class FacebookThumbnail(AppThumbnail):

    """ FacebookThumbnail takes a facebook id and produces a thumbnail. """


    def __init__(self, fb_id, name):
        """ Construct a FacebookThumbnail. """
        super(FacebookThumbnail, self).__init__(
                FacebookThumbnail._prepare_src_from_fb_id(fb_id),
                name)


    @staticmethod
    def _prepare_src_from_fb_id(fb_id):
        """ Turn a facebook id into an image source. """
        return "http://graph.facebook.com/{}/picture".format(fb_id)
