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


    @constant
    def LABEL(self):
        """ LABEL is a value of the HTML attribute Type. """
        return "label"


HTML_TAG = _HTMLTag()


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
    def DISABLED(self):
        """ DISABLED is a type of HTML boolean attribute. """
        return "disabled"


    @constant
    def FOR(self):
        """ FOR is a type of HTML attribute. It refers to an ID. """
        return "for"


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


HTML_ATTRIBUTE = _HTMLAttribute()


class _HTMLType(object):

    """ _HTMLType class to hold all 'Type' atttribute values. """


    @constant
    def BUTTON(self):
        """ BUTTON is a value of the HTML attribute Type. """
        return "button"


    @constant
    def CHECKBOX(self):
        """ CHECKBOX is a value of the HTML attribute Type. """
        return "checkbox"


    @constant
    def RADIO(self):
        """ RADIO is a value of the HTML attribute Type. """
        return "radio"


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


HTML_TYPE = _HTMLType()


class _HTMLClass(object):

    """ _HTMLClass class holds all w3c classes for standard HTML tags. """


    @constant
    def ANCHOR(self):
        """ ANCHOR is a w3c class. """
        return "anchor"


    @constant
    def BUTTON(self):
        """ BUTTON is a w3c class. """
        return "button"



HTML_CLASS = _HTMLClass()


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
            HTML_TAG.LABEL,
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
        attributes[HTML_TAG.FORM].append(HTML_ATTRIBUTE.ACTION)
        attributes[HTML_TAG.FORM].append(HTML_ATTRIBUTE.DISABLED)
        attributes[HTML_TAG.FORM].append(HTML_ATTRIBUTE.NAME)

        # input tags can also have these attributes:
        attributes[HTML_TAG.INPUT].append(HTML_ATTRIBUTE.AUTOFOCUS)
        attributes[HTML_TAG.INPUT].append(HTML_ATTRIBUTE.CHECKED)
        attributes[HTML_TAG.INPUT].append(HTML_ATTRIBUTE.DISABLED)
        attributes[HTML_TAG.INPUT].append(HTML_ATTRIBUTE.NAME)
        attributes[HTML_TAG.INPUT].append(HTML_ATTRIBUTE.PLACEHOLDER)
        attributes[HTML_TAG.INPUT].append(HTML_ATTRIBUTE.TYPE)
        attributes[HTML_TAG.INPUT].append(HTML_ATTRIBUTE.VALUE)

        attributes[HTML_TAG.LABEL].append(HTML_ATTRIBUTE.FOR)

        # button tags can also have these attributes:
        attributes[HTML_TAG.BUTTON].append(HTML_ATTRIBUTE.ACTION)
        attributes[HTML_TAG.BUTTON].append(HTML_ATTRIBUTE.AUTOFOCUS)
        attributes[HTML_TAG.BUTTON].append(HTML_ATTRIBUTE.DISABLED)
        attributes[HTML_TAG.BUTTON].append(HTML_ATTRIBUTE.NAME)
        attributes[HTML_TAG.BUTTON].append(HTML_ATTRIBUTE.TYPE)
        attributes[HTML_TAG.BUTTON].append(HTML_ATTRIBUTE.VALUE)

        return attributes


    @constant
    def TYPES(self):
        """ TYPES is a list of allowed types. """
        return [
            HTML_TYPE.BUTTON,
            HTML_TYPE.CHECKBOX,
            HTML_TYPE.HIDDEN,
            HTML_TYPE.RADIO,
            HTML_TYPE.SUBMIT,
            HTML_TYPE.TEXT,
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


class _ComponentClass(object):

    """ _ComponentClass holds all w3c classes for the components module. """


    @constant
    def NON_ROUTING_ANCHOR(self):
        """ NON_ROUTING_ANCHOR is a w3c class. """
        return "non-routing-anchor"


    @constant
    def CREATE_BUTTON(self):
        """ CREATE_BUTTON is a w3c class. """
        return "create-button"


    @constant
    def CLOSE_BUTTON(self):
        """ CLOSE_BUTTON is a w3c class. """
        return "close-button"


    @constant
    def LOGIN_ANCHOR(self):
        """ LOGIN_ANCHOR is a w3c class. """
        return "login-anchor"


    @constant
    def FACEBOOK_LOGIN_ANCHOR(self):
        """ FACEBOOK_LOGIN_ANCHOR is a w3c class. """
        return "facebook-login-anchor"


    @constant
    def MENU_BUTTON(self):
        """ MENU_BUTTON is a w3c class. """
        return "menu-button"


    @constant
    def SUBMIT_BUTTON(self):
        """ SUBMIT_BUTTON is a w3c class. """
        return "submit-button"


    @constant
    def MAIN_HEADER(self):
        """ MAIN_HEADER is a w3c class. """
        return "main-header"


    @constant
    def LIST_COLUMN(self):
        """ LIST_COLUMN is a w3c class. """
        return "list-column"


    @constant
    def NUMBERED_LIST(self):
        """ NUMBERED_LIST is a w3c class. """
        return "numbered-list"


    @constant
    def HEADED_LIST(self):
        """ HEADED_LIST is a w3c class. """
        return "headed-list"


    @constant
    def LIST_HEADER(self):
        """ LIST_HEADER is a w3c class. """
        return "list-header"


    @constant
    def HEADED_LIST_ITEM(self):
        """ HEADED_LIST_ITEM is a w3c class. """
        return "headed-list-item"


COMPONENT_CLASS = _ComponentClass()
