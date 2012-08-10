""" Module: login

"""

import os
import hashlib
from time import time

import tornado.web
import tornado.auth

from model.app.auth import FacebookAuthModel

from constants import COOKIE_TYPE, COOKIE, ARGUMENT, SETTING
from constants import FACEBOOK_AUTH, FACEBOOK_AUTH_SCOPE, VERSION

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
        code = self.get_auth_code()

        extra_fields = [
                #FACEBOOK_AUTH_SCOPE.GENDER,
                FACEBOOK_AUTH_SCOPE.EMAIL,
                FACEBOOK_AUTH_SCOPE.USER_INTERESTS,
                FACEBOOK_AUTH_SCOPE.PUBLISH_ACTIONS,
                ]

        client_id = self.settings.get(SETTING.FACEBOOK_API_KEY)
        client_secret = self.settings.get(SETTING.FACEBOOK_SECRET)

        # if there is no "code" then do Facebook app authorization
        if not code:

            # create a unique state to prevent XSRF on auth/login
            state = self.generate_auth_state()
            self.create_auth_state(state)

            # TODO: is state supposed to be passed with extra_params?
            extra_params = {
                    FACEBOOK_AUTH.SCOPE: ",".join(extra_fields),
                    FACEBOOK_AUTH.STATE: state,
                    }

            # request authorization from Facebook and redirect as desired
            self.authorize_redirect(
                    self.redirect_uri(),
                    client_id,
                    client_secret,
                    extra_params)

        # Facebook has provided a "code," so get the "access token"
        else:

            request_auth_state = self.get_request_auth_state()
            cookie_auth_state = self.pop_auth_state()

            # if request and session state don't exist and match, this is CSRF
            if all([
                    request_auth_state is not None,
                    cookie_auth_state is not None,
                    request_auth_state == cookie_auth_state,
                    ]):

                # TODO: figure out how to distinguish between actual
                # authorization and fake authorization; meaning, Facebook will
                # make it seem like authorization just happened even if we
                # asked for it and it turns out we didn't need to. yuck.
                # anyway, fire off a MixPanelFirstAuthorization event.

                self.get_authenticated_user(
                        self.redirect_uri(),
                        client_id,
                        client_secret,
                        code,
                        self._on_auth)
                        #self._on_auth,
                        #set(extra_fields))

                return

            else:

                # TODO: log this appropriately too.
                self.write("CSRF!")
                self.finish()


    # TODO: make this Facebook-specific to make room for other _on_auth
    # definitions like our own, Twitter's, etc.
    def _on_auth(self, raw_user):
        """ Private method for wrapping up user authentication. """

        if not raw_user:
            raise tornado.web.HTTPError(500, "Facebook auth failed.")

        model = FacebookAuthModel(self.current_user, raw_user)
        model.set_ip(self.request.remote_ip)
        model.set_locale(self.locale.code)

        # TODO: default league should come from invitation to join
        model.set_default_league_id(
                self.settings.get(SETTING.DEFAULT_LEAGUE_ID))

        model.load_and_dispatch()

        # TODO: remove when we start firing off MixPanelSignUp python events!
        if model.is_new:
            self.create_mixpanel_signup()

        self.create_session(
                model.user,
                model.person,
                model.is_new,
                raw_user.get(FACEBOOK_AUTH_SCOPE.ACCESS_TOKEN))

        self.redirect(self.get_next_url())


    def redirect_uri(self):
        """ Generate a URI to redirect to after login/authorization. """
        # query argument "next" indicates the user's intended destination
        next_url = self.get_next_url()

        # TODO: build a URL class and use it here!

        # build URI to redirect to upon successful login/authorization
        return "{0}://{1}{2}?{3}={4}".format(
                self.request.protocol,  # http
                self.request.host,      # www.sqoreboard.com
                self.request.path,      # /login
                ARGUMENT.NEXT,
                tornado.escape.url_escape(next_url))


    def create_session(self, user, person, is_new=False, access_token=None):
        """ Return a dict to be set as a cookie. """
        session = {
                COOKIE.USER_ID: user.id,
                COOKIE.PERSON_ID: person.id,
                COOKIE.FACEBOOK_ID: user.fb_id,
                COOKIE.GENDER: person.gender,
                COOKIE.TIMEZONE: user.timezone,
                COOKIE.IP: user.last_ip,
                COOKIE.LOCALE: user.locale,
                COOKIE.VERSION: VERSION.CURRENT,
                # TODO: make this a timestamp instead?
                COOKIE.IS_NEW: is_new,
                }

        if access_token is not None:
            session[FACEBOOK_AUTH_SCOPE.ACCESS_TOKEN] = access_token

        return self.set_encoded_secure_cookie(COOKIE_TYPE.SESSION, session)


    def create_auth_state(self, state):
        """ Save a secure authorization status cookie. """
        # TODO: when adding other third party login solutions besides Facebook,
        # consider raising NotImplementedError and overriding in subclasses.
        self.set_encoded_secure_cookie(COOKIE_TYPE.AUTH_STATE, state)


    # TODO: remove when we start firing off the MixPanelSignUp event in python!
    def create_mixpanel_signup(self):
        """ Temporarily create a MixPanel Signup cookie. """
        self.set_encoded_cookie(COOKIE_TYPE.SIGN_UP, int(time()))


    def pop_auth_state(self):
        """ Return and clear a secure authorization status cookie. """
        # TODO: when adding other third party login solutions besides Facebook,
        # consider raising NotImplementedError and overriding in subclasses.
        return self.pop_decoded_secure_cookie(COOKIE_TYPE.AUTH_STATE)


    def generate_auth_state(self):
        """ Return a unique string to be set as the auth state cookie. """
        # TODO: do we need a more rigorous algorithm?
        return hashlib.md5(os.urandom(32)).hexdigest()


    def get_auth_code(self):
        """ Return the auth code for this request. """
        return self.get_code_argument()


    def get_request_auth_state(self):
        """ Return the auth state for this request. """
        return self.get_auth_state_argument()


    def get_next_url(self):
        """ Return the next url to forward to from this request. """
        return self.get_next_argument()


    def get_code_argument(self):
        """ Return the "code" request argument. """
        return self.get_argument(ARGUMENT.CODE, False)


    def get_auth_state_argument(self):
        """ Return the "state" request argument. """
        return self.get_argument(ARGUMENT.AUTH_STATE, None)


    def get_next_argument(self):
        """ Return the "next" request argument. """
        return self.get_argument(ARGUMENT.NEXT, self.get_login_url())
