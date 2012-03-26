""" Module: mobileviews

Provide generic mobile views.
"""

import tornado.web

class ListView(tornado.web.UIModule):

    """ View of mobile list. """

    def render(self, 
            primary_entries, 
            primary_fields,
            sort_field,
            secondary_entries, 
            secondary_fields):
        """ Override render to use components to build list view. 
        
        Required:
        list    primary_entries     list of displayable elements
        list    primary_fields      dict of tag into start, end, value
        str     sort_field          field that list has been sorted by
        dict    secondary_entries   dict of displayable sub-elements
        list    secondary_fields    dict of tag into start, end, value

        primary_entries SqNodes must have the properties included
        in marked_up_fields

        primary_fields keys: START_TAG, DISPLAY_PROPERTY, END_TAG
        
        secondary_entries:
        key = primary_entries id
        value = list of secondary entries
        
        secondary_fields keys: START_TAG, DISPLAY_PROPERTY, END_TAG

        """
        page_content_component = "mobile/components/content_list.html"

        return self.render_string(
                page_content_component, 
                primary_entries=primary_entries,
                primary_fields=primary_fields,
                secondary_entries=secondary_entries,
                secondary_fields=secondary_fields,
                sort_field=sort_field,
                numbered=True)


class ContentHeaderView(tornado.web.UIModule):

    """ View of content header. """

    def render(self, header_entry):
        """ Override render to use components to build content header. """
        content_header_component = self.render_string(
                "mobile/components/content_header.html",
                header=header_entry.name)
        return content_header_component
