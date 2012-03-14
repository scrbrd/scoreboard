""" Module: mobileviews

Provide generic mobile views.
"""

import tornado.web

class ListView(tornado.web.UIModule):

    """ View of mobile list. """

    def render(self, listed_entries, sort_field, display_fields):
        """ Override render to use components to build list view. """
        page_content_component = self.render_string(
                "mobile/components/content_list.html", 
                listed_entries=listed_entries,
                sort_field=sort_field,
                display_fields=display_fields,
                numbered=True)

        return page_content_component


class ContentHeaderView(tornado.web.UIModule):

    """ View of content header. """

    def render(self, header_entry):
        """ Override render to use components to build content header. """
        content_header_component = self.render_string(
                "mobile/components/content_header.html",
                header=header_entry.name)
        return content_header_component
