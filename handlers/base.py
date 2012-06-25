""" Module: base

Provide our base class for all Handlers in the Controller. In reality,
this subclasses tornado.web.RequestHandler to get all of Tornado's
Controller functionality.

Think of this as the one-stop shop for all the basic cookie, request
argument, user, etc. functionality that any handler in our ecosystem
would want access to.

Also included:

Simple class hierarchy for the controller's cookie functionality so that
handlers don't have to repeat work and can take advantage of a good API.

"""

#import base64
#import hashlib
#import hmac

from exceptions import NotImplementedError

import tornado.web
#import logging


#logger = logging.getLogger('boilerplate.' + __name__)


class BaseHandler(tornado.web.RequestHandler):

    """ Collect common handler methods.

    All handlers should be subclasses.

    """

    _cookies = {}


    def get_current_user(self):
        """ Return current user from cookie or return None.

        Only override when authentication is required by a subclass.

        """
        return None


    def process_request(self):
        raise NotImplementedError("Abstract Method: SUBCLASS MUST OVERRIDE!")


    def process_asynchronous_request(self, model):
        raise NotImplementedError("Abstract Method: SUBCLASS MUST OVERRIDE!")


    def process_synchronous_request(self, model):
        raise NotImplementedError("Abstract Method: SUBCLASS MUST OVERRIDE!")


    def set_encrypted_cookie(self, type, cookie):
        """ Return a secure cookie decrypted. """
        self.set_secure_cookie(type, tornado.escape.json_encode(cookie))
        self._cookies[type] = cookie


    def get_decrypted_cookie(self, type):
        """ Return a secure cookie decrypted. """
        if self._cookies.get(type) is None:
            secure_cookie = self.get_secure_cookie(type)
            if secure_cookie:
                self._cookies[type] = tornado.escape.json_decode(secure_cookie)

        return self._cookies.get(type)


    def pop_decrypted_cookie(self, type):
        """ Return and clear a secure cookie. """
        cookie = self.get_decrypted_cookie(type)
        self.clear_cookie(type)
        self._cookies[type] = None
        return cookie


    #def get_json_argument(self, name, default=None):
    #    """ Find and return the argument with key 'name' from JSON request
    #    data.
    #    Similar to Tornado's get_argument() method.
    #
    #    """
    #    if default is None:
    #        default = self._ARG_DEFAULT
    #    if not self.request.arguments:
    #        raise tornado.web.HTTPError(405, "Don't use GET for JSON")
    #    if name not in self.request.arguments:
    #        if default is self._ARG_DEFAULT:
    #            msg = "Missing argument '%s'" % name
    #            logger.debug(msg)
    #            raise tornado.web.HTTPError(400, msg)
    #        logger.debug("Returning default argument %s, as we couldn't find "
    #                "'%s' in %s" % (default, name, self.request.arguments))
    #        return default
    #    arg = self.request.arguments[name]
    #    logger.debug("Found '%s': %s in JSON arguments" % (name, arg))
    #    return arg


    # TODO: remove this method if it isn't needed for authentication
    #@staticmethod
    #def base64_url_decode(inp):
    #    padding_factor = (4 - len(inp) % 4) % 4
    #    inp += "=" * padding_factor
    #    return base64.b64decode(unicode(inp).translate(
    #            dict(zip(map(ord, u'-_'), u'+/'))))
    #
    #
    # TODO: remove this method if it isn't needed for authentication
    #@staticmethod
    #def parse_signed_request(signed_request, secret):
    #    l = signed_request.split('.', 2)
    #    encoded_sig = l[0]
    #    payload = l[1]
    #
    #    sig = BaseHandler.base64_url_decode(encoded_sig)
    #    data = json.loads(BaseHandler.base64_url_decode(payload))
    #
    #    if data.get('algorithm').upper() != 'HMAC-SHA256':
    #        # log.error('Unknown algorithm')
    #        return None
    #    else:
    #        expected_sig = hmac.new(
    #                secret,
    #                msg=payload,
    #                digestmod=hashlib.sha256).digest()
    #
    #    if sig != expected_sig:
    #        return None
    #    else:
    #        # log.debug('valid signed request received..')
    #        return data
