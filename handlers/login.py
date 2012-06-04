import os
import hashlib

import tornado.web
import tornado.auth

from model.app.catchers import FacebookAuthCatcher

from constants import ARGUMENT_TYPE, COOKIE_TYPE, COOKIE_KEY

from handlers.base import BaseHandler


# TODO: allow other types of login by subclassing for Facebook, Twitter, etc.
class LoginHandler(BaseHandler, tornado.auth.FacebookGraphMixin):

    """ Handle User login. Currently handles Facebook Graph Login only. """

    # NOT tornado.web.authenticated because this creates the user info.
    @tornado.web.asynchronous
    def get(self):
        """ Handles GET requests for login. """
        self.process_request()


    def process_request(self):
        """ Process login request. Inherited from BaseHandler. """

        code = self.get_argument(ARGUMENT_TYPE.CODE, False)

        # TODO: make constants so we don't have to hardcode any of this.
        # TODO: does this belong in the LoginCatcher?
        extra_fields = [
                #"gender",
                "email",
                "user_interests",
                ]

        # if there is no "code" then do Facebook app authorization
        if not code:

            # create a unique state to prevent XSRF
            state = self.create_unique_state()
            self.set_secure_cookie(COOKIE_TYPE.STATE, state)
            scope = ",".join(extra_fields)

            # request authorization from Facebook and redirect as desired
            self.authorize_redirect(
                    redirect_uri=self.redirect_uri(),
                    client_id=self.settings["facebook_api_key"],
                    extra_params={"scope": scope, "state": state})

        # Facebook has provided a "code," so get the "access token"
        else:

            request_state = self.get_argument(ARGUMENT_TYPE.STATE, None)
            session_state = self.get_secure_cookie(COOKIE_TYPE.STATE)

            # if request and session state don't exist and match, this is CSRF
            if all([
                    request_state is not None,
                    session_state is not None,
                    request_state == session_state]):

                # TODO: make a constant so we don't have to hardcode any of this.

                self.get_authenticated_user(
                        redirect_uri=self.redirect_uri(),
                        client_id=self.settings["facebook_api_key"],
                        client_secret=self.settings["facebook_secret"],
                        code=code,
                        callback=self._on_auth)
                        #callback=self._on_auth,
                        #extra_fields=set(extra_fields))

                return

            else:

                self.write("CSRF!")
                self.finish()


    # TODO: make this Facebook-specific to make room for other _on_auth
    # definitions like our own, Twitter's, etc.
    def _on_auth(self, raw_user):
        """ Private method for wrapping up user authentication. """

        if not raw_user:
            raise tornado.web.HTTPError(500, "Facebook auth failed.")

        # TODO: implement join-league and remove league_id argument!

        auth = FacebookAuthCatcher(
                raw_user,
                self.request.remote_ip,
                self.settings['league_id'])
        cookie = self.secure_cookie(auth.user(), auth.player(), auth.league())
        self.set_secure_cookie(COOKIE_TYPE.USER, cookie)

        self.redirect(
                self.get_argument(ARGUMENT_TYPE.NEXT, self.get_login_url()))


    def redirect_uri(self):
        """ Generate a URI to redirect to after login/authorization. """
        # query argument "next" indicates the user's intended destination
        path = self.get_argument(ARGUMENT_TYPE.NEXT, self.get_login_url())

        # build URI to redirect to upon successful login/authorization
        return "{0}://{1}{2}?{3}={4}".format(
                self.request.protocol,  # http
                self.request.host,      # www.sqoreboard.com
                self.request.path,      # /login
                ARGUMENT_TYPE.NEXT,
                tornado.escape.url_escape(path))


    def secure_cookie(self, user, player, league):
        """ Return a json-encoded dictionary to be set as a cookie. """
        league_id = league.id if league is not None else None

        return tornado.escape.json_encode({
                COOKIE_KEY.USER_ID   : user.id,
                COOKIE_KEY.TIMEZONE  : user.timezone,
                COOKIE_KEY.PLAYER_ID : player.id,
                COOKIE_KEY.GENDER    : player.gender,
                COOKIE_KEY.LEAGUE_ID : league_id,
                })


    @staticmethod
    def create_unique_state():
        """ Create a unique string that can be used as a state. """
        # TODO: make a more rigorous algorithm
        return hashlib.md5(os.urandom(32)).hexdigest()
