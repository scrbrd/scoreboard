""" Module: util

Utilities modules for templates.
"""

def generate_tag(start_tag, object, attribute, end_tag):
    """ Generate mark up from tags and object. 

    Required:
    str     start_tag   element start tag
    object  object      object that has requested attribute
    str     attribute   object's attribute that will be displayed
    str     end_tag     element end tag

    """

    mark_up = "{0}{1}{2}".format(
            start_tag, 
            getattr(object, attribute),
            end_tag) 
    return mark_up

