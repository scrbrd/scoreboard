""" Module: query

...

"""

import json
from exceptions import NotImplementedError

import tornado.web

from constants import COOKIE_TYPE, COOKIE, ARGUMENT
from base import BaseHandler
from session import Session


class QueryHandler(BaseHandler):

    """ Encapsulates all generic query functionality.

    Any read or write request handler should subclass from this handler.

    """


    def get_current_user(self):
        """ Return current user from cookie or return None. """
        session = None

        # TODO: deal with the user deauthorizing the app

        session_cookie = self.get_session_cookie()

        if session_cookie:
            session = Session(
                    session_cookie.get(COOKIE.USER_ID),
                    session_cookie.get(COOKIE.PERSON_ID))

            session.set_is_new(session_cookie.get(COOKIE.IS_NEW))
            session.set_access_token(session_cookie.get(COOKIE.ACCESS_TOKEN))
            session.set_fb_id(session_cookie.get(COOKIE.FACEBOOK_ID))
            session.set_gender(session_cookie.get(COOKIE.GENDER))
            session.set_timezone(session_cookie.get(COOKIE.TIMEZONE))
            session.set_ip(session_cookie.get(COOKIE.IP))
            session.set_locale(session_cookie.get(COOKIE.LOCALE))
            session.set_version(session_cookie.get(COOKIE.VERSION))

        return session


    @tornado.web.authenticated
    def get(self):
        """ Overload BaseHandler's HTTP GET responder for reads. """
        self.process_request()


    @tornado.web.authenticated
    def post(self):
        """ Overload BaseHandler's HTTP GET responder for reads. """
        self.process_request()


    def process_request(self):
        """ Generic request processing for query handler subclasses. """
        if self.is_asynchronous_request():
            self.process_asynchronous_request()
        else:
            self.process_synchronous_request()


    def process_asynchronous_request(self):
        """ Handle an asynchronous query request. """
        model = self.get_model()

        content = self.render_string(
                self.get_asynchronous_content_url(),
                model=model)

        context = self.render_string(
                self.get_context_url(),
                model=model)

        context_model = self.render_string(
                self.get_context_model_url(),
                model=model)

        session_model = self.render_string(
                self.get_session_model_url(),
                model=model)

        page_state_model = self.render_string(
                self.get_page_state_model_url(),
                model=model)

        # TODO: make these constants!
        self.write({
            "content": content,
            "context": context,
            "context_model": context_model,
            "session_model": session_model,
            "page_state_model": page_state_model,
            })


    def process_synchronous_request(self):
        """ Handle a synchronous query request. """
        self.render(self.get_synchronous_content_url(), model=self.get_model())


    def get_model(self):
        """ Define the controller's generic connection to the model. """
        raise NotImplementedError("Abstract Method: SUBCLASS MUST OVERRIDE!")


    def get_synchronous_content_url(self):
        """ Generate a URL for handling synchronous content requests. """
        raise NotImplementedError("Abstract Method: SUBCLASS MUST OVERRIDE!")


    def get_asynchronous_content_url(self):
        """ Generate a URL for rendering content markup asynchronously. """
        raise NotImplementedError("Abstract Method: SUBCLASS MUST OVERRIDE!")


    def get_context_url(self):
        """ Generate a URL for rendering a context header markup. """
        # TODO: turn this hardcoded file path into a constant
        return "mobile/components/context.html"


    def get_context_model_url(self):
        """ Generate a URL for rendering a context model. """
        # TODO: turn this hardcoded file path into a constant
        return "mobile/components/context_model.html"


    def get_session_model_url(self):
        """ Generate a URL for rendering a session model. """
        # TODO: turn this hardcoded file path into a constant
        return "mobile/components/session_model.html"


    def get_page_state_model_url(self):
        """ Generate a URL for rendering a page state model. """
        raise NotImplementedError("Abstract Method: SUBCLASS MUST OVERRIDE!")


    def get_session_cookie(self):
        """ Return a secure cookie modeling a session for a request. """
        return self.get_decoded_secure_cookie(COOKIE_TYPE.SESSION)


    def get_asynchronous_argument(self):
        """ Return the asynchronous request argument. """
        return self.get_argument(ARGUMENT.ASYNCHRONOUS, False)


    def get_parameters_argument(self):
        """ Return the parameters request argument. """
        return self.get_argument(ARGUMENT.PARAMETERS, None)


    def is_asynchronous_request(self):
        """ Return whether this is an asynchronous request. """
        return bool(self.get_asynchronous_argument())


    def get_request_parameters(self):
        """ Return the request parameters argument. """
        return json.loads(self.get_parameters_argument())
