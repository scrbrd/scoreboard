""" Module: test

...
"""
from handlers.base import BaseHandler

# FIXME delete this module
class TestHandler(BaseHandler):
   
    def get(self, type_ext):
        if type_ext == "2":
            
            self.render("test2.html")
        else:
            self.render("test.html")
