import logging
import os
import hashlib

import tornado.web
import tornado.auth

from handlers.base import BaseHandler

logger = logging.getLogger('boilerplate.' + __name__)


# TODO allow other types of login
class LoginHandler(BaseHandler, tornado.auth.FacebookGraphMixin):

    """ Handle User login. Currently handles FAcebook Graph Login only. """

    # NOT tornado.web.authenticated because this creates the user info.
    @tornado.web.asynchronous
    def get(self):
        """ Handles GET requests for logging in. """
        self.process_request()


    def process_request(self):
        """ Process login request. Inherited from BaseHandler. """

        # TODO: make redirect_uri a function and "/login" a constant
        # redirect uri pulls "next" which current_user creates to maintain url
        redirect_uri = "{0}://{1}{2}?next={3}".format(
                self.request.protocol,
                self.request.host,
                "/login",
                tornado.escape.url_escape(self.get_argument("next", "/")))

        # TODO: make a constant so we don't have to hardcode this.
        # if there is no "code" then do facebook app authorization
        if not self.get_argument("code", False):

            # TODO: make a constant so we don't have to hardcode this.
            # create a unique state to prevent XSRF
            state = self.create_unique_state()
            self.set_secure_cookie("state", state)

            # TODO: make a constant so we don't have to hardcode any of this.
            # request authorization from facebook
            params = {"scope": "email,user_interests", "state": state}
            self.authorize_redirect(
                    redirect_uri=redirect_uri,
                    client_id=self.settings["facebook_api_key"],
                    extra_params=params)

        # facebook has provided a "code" so get the "access token"
        # check the state cookie to make sure there is not CSRF
        else:
            # TODO: make a constant so we don't have to hardcode any of this.
            request_state = self.get_argument("state", None)
            session_state = self.get_secure_cookie("state")
            if all([
                    request_state is not None,
                    session_state is not None,
                    request_state == session_state]):
                self.get_authenticated_user(
                        redirect_uri=redirect_uri,
                        client_id=self.settings["facebook_api_key"],
                        client_secret=self.settings["facebook_secret"],
                        code=self.get_argument("code"),
                        callback=self._on_auth)
                return
            else:
                self.write("you have a CSRF")
                self.finish()


    def _on_auth(self, user):
        """ Private method for wrapping up user authentication. """

        if not user:
            raise tornado.web.HTTPError(500, "Facebook auth failed")
        # TODO - save useful user info in db
        self.set_secure_cookie("user", tornado.escape.json_encode(user))
        print("the state is: {0}: ".format(self.get_secure_cookie("state")))
        self.redirect(self.get_argument("next", "/"))


    # TODO make a more rigorous algorithm
    @staticmethod
    def create_unique_state():
        """ Create a unique string that can be used as a state. """
        return hashlib.md5(os.urandom(32)).hexdigest()
