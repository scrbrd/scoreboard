from tornado.web import authenticated

from handlers.base import BaseHandler

import logging
logger = logging.getLogger('boilerplate.' + __name__)


class FacebookTestHandler(BaseHandler):
    
    def get(self):
        print("in get")
        # check for xsrf cookie
       
        if self.current_user is None:
            self.render("facebooktest.html")
        else: 
            self.write("you logged in")

