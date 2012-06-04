import json
import base64
import hashlib
import hmac
from exceptions import NotImplementedError

import tornado.web
import logging

from constants import COOKIE_TYPE


logger = logging.getLogger('boilerplate.' + __name__)


class BaseHandler(tornado.web.RequestHandler):

    """ A class to collect common handler methods - all other handlers should
    subclass this one.

    """

    def load_json(self):
        """ Load JSON from the request body and store them in
        self.request.arguments, like Tornado does by default for POSTed form
        parameters.

        If JSON cannot be decoded, raises an HTTPError with status 400.

        """
        try:
            self.request.arguments = json.loads(self.request.body)
        except ValueError:
            msg = "Could not decode JSON: %s" % self.request.body
            logger.debug(msg)
            raise tornado.web.HTTPError(400, msg)


    def get_json_argument(self, name, default=None):
        """ Find and return the argument with key 'name' from JSON request
        data.
        Similar to Tornado's get_argument() method.

        """
        if default is None:
            default = self._ARG_DEFAULT
        if not self.request.arguments:
            self.load_json()
        if name not in self.request.arguments:
            if default is self._ARG_DEFAULT:
                msg = "Missing argument '%s'" % name
                logger.debug(msg)
                raise tornado.web.HTTPError(400, msg)
            logger.debug("Returning default argument %s, as we couldn't find "
                    "'%s' in %s" % (default, name, self.request.arguments))
            return default
        arg = self.request.arguments[name]
        logger.debug("Found '%s': %s in JSON arguments" % (name, arg))
        return arg


    def get_current_user(self):
        """ Return current user from cookie or return None. """
        user = None

        cookie = self.get_secure_cookie(COOKIE_TYPE.USER)

        # no authenticated User/Player exists
        if cookie is None:

            # TODO: could see if Facebook has de-authorized the user.

            #cookie = self.get_cookie("fbsr_" + self.settings["facebook_api_key"], "")
            #if not cookie:
            #    print('no cookie found')
            #    return None
            #print('cookie found')
            #app_secret = self.settings["facebook_secret"]
            #response = BaseHandler.parse_signed_request(cookie, app_secret)
            #print ("WE HAVE SUCCESS! {0}: ".format(response)
            pass

        # an authenticated User/Player exists
        else:
            user = tornado.escape.json_decode(cookie)

        # TODO: this is not a User SqNode. it is also not a User ID. instead,
        # it is a dictionary containing user, player, and league IDs.
        return user


    def process_request(self):
        """ Handle the bulk of the request work. """
        raise NotImplementedError("Abstract Method: SUBCLASS MUST OVERRIDE!")


    # TODO remove this method if it ends up not being needed for authentication
    @staticmethod
    def base64_url_decode(inp):
        padding_factor = (4 - len(inp) % 4) % 4
        inp += "=" * padding_factor
        return base64.b64decode(unicode(inp).translate(
                dict(zip(map(ord, u'-_'), u'+/'))))

    # TODO remove this method if it ends up not being needed for authentication
    @staticmethod
    def parse_signed_request(signed_request, secret):
        l = signed_request.split('.', 2)
        encoded_sig = l[0]
        payload = l[1]

        sig = BaseHandler.base64_url_decode(encoded_sig)
        data = json.loads(BaseHandler.base64_url_decode(payload))

        if data.get('algorithm').upper() != 'HMAC-SHA256':
            # log.error('Unknown algorithm')
            return None
        else:
            expected_sig = hmac.new(
                    secret,
                    msg=payload,
                    digestmod=hashlib.sha256).digest()

        if sig != expected_sig:
            return None
        else:
            # log.debug('valid signed request received..')
            return data
