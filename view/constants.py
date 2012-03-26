""" View Constants

...

"""

def constant(f):
    """ Constant Decorator to make constants Final. """
    

    def fset(self, value):
        """ Overload constant function's set to disable."""
        raise SyntaxError
    

    def fget(self):
        """ Overload constant function's get. """
        return f()

    return property(fget, fset)


class _Template(object):
    
    """ _Template class to hold all Template oriented constants. """

    # FIXME - break this class into logical groups.
    
    @constant
    def START_TAG():
        """ Be the start tag of a displayed object. """
        return "c_start_tag"


    @constant
    def END_TAG():
        """ Be the closing tag of a displayed object. """
        return "c_end_tag"


    @constant
    def DISPLAY_PROPERTY():
        """ Determine the displayable property of an object. """
        return "c_display_property"


TEMPLATE = _Template()

