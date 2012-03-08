""" Module: mobileviews

Provide generic mobile views.
"""

import tornado.web

class ListView(tornado.web.UIModule):

    """ View of mobile list. """

    def render(self, header, listed_entries, sort_field):
        return self.render_string(
                "mobile/list.html", 
                header=header, 
                listed_entries=listed_entries,
                sort_field=sort_field)
        #return "<div>happyness is a warm gunn.</div>"


