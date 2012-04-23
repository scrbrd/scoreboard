""" HTML Constants

Provide constants for view.html.

    HTML_TAG
    HTML_ATTRIBUTE
    HTML_CONSTANT

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


class _HTMLTag(object):
    
    """ _HTMLTag class to hold all implemented HTML tags. """


    @constant
    def DIV():
        """ DIV is a type of HTML tag. """
        return "div"


    @constant
    def SPAN():
        """ SPAN is a type of HTML tag. """
        return "span"


    @constant
    def OL():
        """ OL is a type of HTML tag. """
        return "ol"


    @constant
    def UL():
        """ UL is a type of HTML tag. """
        return "ul"


    @constant
    def LI():
        """ LI is a type of HTML tag. """
        return "li"


    @constant
    def NAV():
        """ NAV is a type of HTML tag. """
        return "nav"


    @constant
    def A():
        """ A is a type of HTML tag. """
        return "a"


    @constant
    def H1():
        """ H1 is a type of HTML tag. """
        return "h1"


    @constant
    def H2():
        """ H2 is a type of HTML tag. """
        return "h2"


class _HTMLAttribute(object):

    """ _HTMLAttribute class to hold all implemented HTML attributes. """


    @constant
    def CLASS():
        """ CLASS is a type of HTML attribute. """
        return "class"


    @constant
    def ID():
        """ ID is a type of HTML attribute. """
        return "id"


    @constant
    def HREF():
        """ HREF is a type of HTML attribute. """
        return "href"


class _HTMLClass(object):

    """ _HTMLClass class to hold all defined HTML classes. """


    # TODO: FILL ME IN AND REMOVE pass!
    pass


HTML_TAG = _HTMLTag()
HTML_ATTRIBUTE = _HTMLAttribute()
HTML_CLASS = _HTMLClass()


class _HTMLConstant(object):

    """ _HTMLConstant class holds all HTML constants. """


    @constant
    def TAGS():
        """ TAGS is a list of implemented tags. """
        return [
                HTML_TAG.DIV,
                HTML_TAG.SPAN,
                HTML_TAG.OL,
                HTML_TAG.UL,
                HTML_TAG.LI,
                HTML_TAG.NAV,
                HTML_TAG.A,
                HTML_TAG.H1,
                HTML_TAG.H2
                ]


    @constant
    def GLOBAL_ATTRIBUTES():
        """ GLOBAL_ATTRIBUTES is a list of allowed attributes. """
        return [
                HTML_ATTRIBUTE.CLASS,
                HTML_ATTRIBUTE.ID
                ]


    @constant
    def ATTRIBUTES():
        """ ATTRIBUTES is a dict of attributes allowed per tag. """

        attributes = {}

        # populate dict with all global attributes for each tag
        for tag in self.TAGS():
            attributes[tag] = self.GLOBAL_ATTRIBUTES()

        # anchor tags can also have the href attribute set
        attributes[HTML_TAG.A].append(HTML_ATTRIBUTE.HREF)

        return attributes


    @constant
    def CLASSES():
        """ CLASSES is a dict of css classes defined per tag. """

        classes = {}

        # TODO: FILL IN AND UNCOMMENT1!
        #classes[HTML_TAG.] = [
        #        HTML_CLASS.,
        #        HTML_CLASS.
        #        ]

        return classes


HTML_CONSTANT = _HTMLConstant()

