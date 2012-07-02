""" HTML Constants

Provide constants for view.html.

    HTML_TAG
    HTML_ATTRIBUTE
    HTML_TYPE
    HTML_CONSTANT

"""

from util.decorators import constant


class _HTMLTag(object):

    """ _HTMLTag class to hold all implemented HTML tags. """


    @constant
    def DIV(self):
        """ DIV is a type of HTML tag. """
        return "div"


    @constant
    def SPAN(self):
        """ SPAN is a type of HTML tag. """
        return "span"


    @constant
    def OL(self):
        """ OL is a type of HTML tag. """
        return "ol"


    @constant
    def UL(self):
        """ UL is a type of HTML tag. """
        return "ul"


    @constant
    def LI(self):
        """ LI is a type of HTML tag. """
        return "li"


    @constant
    def NAV(self):
        """ NAV is a type of HTML tag. """
        return "nav"


    @constant
    def A(self):
        """ A is a type of HTML tag. """
        return "a"


    @constant
    def H1(self):
        """ H1 is a type of HTML tag. """
        return "h1"


    @constant
    def H2(self):
        """ H2 is a type of HTML tag. """
        return "h2"


    @constant
    def HEADER(self):
        """ HEADER is a type of HTML tag. """
        return "header"


    @constant
    def FOOTER(self):
        """ FOOTER is a type of HTML tag. """
        return "footer"


    @constant
    def SECTION(self):
        """ SECTION is a type of HTML tag. """
        return "section"


    @constant
    def BR(self):
        """ BR is a type of HTML tag. """
        return "br"


    @constant
    def TABLE(self):
        """ TABLE is a type of HTML tag. """
        return "table"


    @constant
    def TR(self):
        """ TR is a type of HTML tag. """
        return "tr"


    @constant
    def TD(self):
        """ TD is a type of HTML tag. """
        return "td"


    @constant
    def TH(self):
        """ TH is a type of HTML tag. """
        return "th"


    @constant
    def FORM(self):
        """ FORM is a type of HTML tag. """
        return "form"


    @constant
    def INPUT(self):
        """ INPUT is a type of HTML tag. """
        return "input"


    @constant
    def BUTTON(self):
        """ BUTTON is a type of HTML tag. """
        return "button"


class _HTMLAttribute(object):

    """ _HTMLAttribute class to hold all implemented HTML attributes. """


    @constant
    def CLASS(self):
        """ CLASS is a type of HTML global attribute. """
        return "class"


    @constant
    def ID(self):
        """ ID is a type of HTML global attribute. """
        return "id"


    @constant
    def HREF(self):
        """ HREF is a type of HTML attribute. """
        return "href"


    @constant
    def NAME(self):
        """ NAME is a type of HTML attribute. """
        return "name"


    @constant
    def ACTION(self):
        """ ACTION is a type of HTML attribute. """
        return "action"


    @constant
    def TYPE(self):
        """ TYPE is a type of HTML attribute. """
        return "type"


    @constant
    def VALUE(self):
        """ VALUE is a type of HTML attribute. """
        return "value"


    @constant
    def CHECKED(self):
        """ CHECKED is a type of HTML boolean attribute. """
        return "checked"


    @constant
    def DATA(self):
        """ DATA is a type of HTML attribute. In fact it's the special
        data-* one. """
        return "data-"


    @constant
    def PLACEHOLDER(self):
        """ PLACEHOLDER is a type of HTML attribute. """
        return "placeholder"


    @constant
    def AUTOFOCUS(self):
        """ AUTOFOCUSis a type of HTML attribute. """
        return "autofocus"


class _HTMLType(object):

    """ _HTMLType class to hold all 'Type' atttribute values. """

    @constant
    def CHECKBOX(self):
        """ CHECKBOX is a value of the HTML attribute Type. """
        return "checkbox"


    @constant
    def HIDDEN(self):
        """ HIDDEN is a value of the HTML attribute Type. """
        return "hidden"


    @constant
    def SUBMIT(self):
        """ SUBMIT is a value of the HTML attribute Type. """
        return "submit"


    @constant
    def TEXT(self):
        """ TEXT is a value of the HTML attribute Type. """
        return "text"


HTML_TAG = _HTMLTag()
HTML_ATTRIBUTE = _HTMLAttribute()
HTML_TYPE = _HTMLType()


class _HTMLConstant(object):

    """ _HTMLConstant class holds all HTML constants. """


    @constant
    def TAGS(self):
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
            HTML_TAG.H2,
            HTML_TAG.HEADER,
            HTML_TAG.SECTION,
            HTML_TAG.FORM,
            HTML_TAG.INPUT,
            HTML_TAG.BUTTON,
            HTML_TAG.BR,
            HTML_TAG.FOOTER,
            HTML_TAG.TABLE,
            HTML_TAG.TR,
            HTML_TAG.TD,
            HTML_TAG.TH
        ]


    @constant
    def GLOBAL_ATTRIBUTES(self):
        """ GLOBAL_ATTRIBUTES is a list of allowed attributes. """
        return [
            HTML_ATTRIBUTE.CLASS,
            HTML_ATTRIBUTE.ID,
            HTML_ATTRIBUTE.DATA,
        ]


    @constant
    def ATTRIBUTES(self):
        """ ATTRIBUTES is a dict of attributes allowed per tag. """

        attributes = {}

        # populate dict with all global attributes for each tag
        for tag in self.TAGS:
            attributes[tag] = self.GLOBAL_ATTRIBUTES

        # anchor tags can also have the href attribute set
        attributes[HTML_TAG.A].append(HTML_ATTRIBUTE.HREF)

        # form tags can also have these attributes:
        attributes[HTML_TAG.FORM].append(HTML_ATTRIBUTE.NAME)
        attributes[HTML_TAG.FORM].append(HTML_ATTRIBUTE.ACTION)

        # input tags can also have these attributes:
        attributes[HTML_TAG.INPUT].append(HTML_ATTRIBUTE.NAME)
        attributes[HTML_TAG.INPUT].append(HTML_ATTRIBUTE.TYPE)
        attributes[HTML_TAG.INPUT].append(HTML_ATTRIBUTE.VALUE)
        attributes[HTML_TAG.INPUT].append(HTML_ATTRIBUTE.PLACEHOLDER)
        attributes[HTML_TAG.INPUT].append(HTML_ATTRIBUTE.CHECKED)
        attributes[HTML_TAG.INPUT].append(HTML_ATTRIBUTE.AUTOFOCUS)

        # button tags can also have these attributes:
        attributes[HTML_TAG.BUTTON].append(HTML_ATTRIBUTE.NAME)
        attributes[HTML_TAG.BUTTON].append(HTML_ATTRIBUTE.ACTION)
        attributes[HTML_TAG.BUTTON].append(HTML_ATTRIBUTE.TYPE)
        attributes[HTML_TAG.BUTTON].append(HTML_ATTRIBUTE.VALUE)
        attributes[HTML_TAG.BUTTON].append(HTML_ATTRIBUTE.AUTOFOCUS)

        return attributes


    @constant
    def TYPES(self):
        """ TYPES is a list of allowed types. """
        return [
            HTML_TYPE.TEXT,
            HTML_TYPE.CHECKBOX,
            HTML_TYPE.SUBMIT,
            HTML_TYPE.HIDDEN,
        ]


    @constant
    def CLASSES(self):
        """ CLASSES is a dict of css classes defined per tag. """

        classes = {}

        # TODO: FILL IN AND UNCOMMENT1!
        #classes[HTML_TAG.] = [
        #        HTML_CLASS.,
        #        HTML_CLASS.
        #        ]

        return classes


HTML_CONSTANT = _HTMLConstant()
