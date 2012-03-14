""" Module: mobileviews

Provide generic mobile views.
"""

import tornado.web

class ListView(tornado.web.UIModule):

    """ View of mobile list. """

    def render(self, header_entry, listed_entries, sort_field):
        """ Override render to use components to build list view. """
        header_component = self.render_string(
                "mobile/components/content_header.html",
                header=header_entry.name)
        content_component = self.render_string(
                "mobile/components/content_list.html", 
                listed_entries=listed_entries,
                sort_field=sort_field,
                fields=["name", "win_count"],
                numbered=True)

        page_content = header_component + content_component
        return page_content
