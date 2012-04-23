""" Module: elements

Provide generic HTML5 tag implementations as subclasses of python's 
cElementTree library to be wielded for rendering by Tornado's UIModule.

Mobile, web, and native application views should extend these to create
context-specific components.

Over time and as needed, this module will codify portions of the HTML5
spec. To wit, when front-end code for generating markup seems broadly
applicable to building anything on any platform, it likely belongs here.


All Element subclasses have access to and may override:
    def tag(self)
    def text(self)
    def set_text(self, text)
    def tail(self)
    def set_tail(self, tail)
    def attributes(self)
    def id(self)
    def set_id(self, id)
    def classes(self)
    def set_classes(self, classes)
    def append_class(self, c)
    def append_classes(self, c)
    def href(self)
    def set_href(self, href)
    def children(self)
    def first_child(self)
    def last_child(self)
    def append_child(self, element)
    def append_children(self, elements)


The base class Element also provides static cElementTree wrappers:
    def validate(tags)
    def to_string(element)


The following tags are implemented as Element subclasses:
    div
    span
    ol
    ul
    li
    nav
    a
    h1
    h2


The following tags are not implemented because they are hard-coded in
the top-level templates, which are not dynamically generated:
    html
    head
    body
    meta
    link
    header
    footer
    script
    hgroup


The following global html5 attributes are currently implemented:
    class
    id

    http://www.w3.org/community/webed/wiki/HTML/Attributes/_Global
    http://www.w3schools.com/html5/html5_ref_globalattributes.asp
    http://www.w3schools.com/html5/html5_ref_eventattributes.asp


The following non-global html5 attributes are currently implemented:

    Attribute       Tag[s]
    ----------------------
    href            a

"""

import xml.etree.cElementTree as ET

from exceptions import NotImplementedError

from constants import HTML_TAG, HTML_ATTRIBUTE, HTML_CLASS, HTML_CONSTANT


class Element(object):

    """ Abstract Element proxy-subclassing xml.etree.cElementTree.Element. 

    class xml.etree.cElementTree.Element(tag, attrib={}, **extra)

    http://docs.python.org/library/xml.etree.elementtree.html

    Version 2.7

    Note that this documentation is for ElementTree, but we subclass
    cElementTree for speed. The problem is that cElementTree is not as
    up-to-date, so be wary of anything new or deprecated in v2.7.

    To protect against this uncertainty, we define convenience wrappers
    around most of the cElementTree.Element API in this subclass to
    avoid a widespread and massively obnoxious change in the event that
    we need to swap out this library for another implementation.

    This class defines the Element interface, and provides a reference
    implementation of this interface.

    The element name, attribute names, and attribute values can be either
    bytestrings or Unicode strings. tag is the element name. attrib is an
    optional dictionary, containing element attributes. extra contains
    additional attributes, given as keyword arguments.

    Properties:
    str     tag     element type
    str     text    additional data found between the element's tags
    str     tail    additional data found after the element's end tag
    dict    attrib  the element's attributes

    Methods:
    def clear()

    def get(key, default=None)
    def items()
    def keys()
    def set(key, value)
    
    def append(subelement)
    def extend(subelements)         <-- New
    def find(match)
    def findall(match)
    def findtext(match, default=None)
    def getchildren()               <-- Deprecated. Use list(elem)
    def getiterator(tag=None)       <-- Deprecated. Use Element.iter().
    def insert(index, element)
    def iter(tag=None)              <-- New
    def iterfind(match)             <-- New
    def itertext()                  <-- New
    def makeelement(tag, attrib)    <-- Use SubElement() factory.
    def remove(subelement)

    Elements also support the following sequence type methods for
    working with subelements: __delitem__(), __getitem__(), 
    __setitem__(), __len__().

    Caution: Elements with no subelements will test as False. This
    behavior will change in future versions. Use specific len(elem) or
    elem is None test instead.

    """

    _element = None

    def __init__(self, tag):
        """ Construct an abstract Element. """
        # enforce that the attributes and extra parameters are unused and that
        # attributes are explicitly set. it's not even clear what extra is.
        self._element = ET.Element(tag)


    def element(self):
        """ Return this element. Bitches. """
        return self._element


    def tag(self):
        """ Return this element's tag with <> removed for convenience. """
        return self.element().tag[1:-1]


    def text(self):
        """ Return this element's text. """
        return self.element().text


    def set_text(self, text):
        """ Set this element's text content. """
        self.element().text = text


    def tail(self):
        """ Return this element's tail. """
        return self.element().tail


    def set_tail(self, tail):
        """ Set this element's tail content. """
        self.element().tail = tail


    def attributes(self):
        """ Return this element's attributes as a dictionary. """
        return self.element().attrib


    def id(self):
        """ Return this element's id attribute. """
        return self.attributes().get(HTML_ATTRIBUTE.ID, "")


    def set_id(self, id):
        """ Set the id attribute for this element. """
        self.element().set(HTML_ATTRIBUTE.ID, id)


    def classes(self):
        """ Return this element's classes as a list."""
        classes = self.attributes().get(HTML_ATTRIBUTE.CLASS, "")
        # in the case where classes is empty, split should return an empty
        # list, not [''], which means passing nothing to split(), not " ".
        return classes.split()


    def set_classes(self, classes):
        # TODO: add a constant for class delimiter?
        """ Set a list of css classes for this element. """
        class_delimiter = " "
        self.element().set(HTML_ATTRIBUTE.CLASS, class_delimiter.join(classes))


    def append_class(self, c):
        """ Add a css class for this element. """
        classes = self.classes()
        classes.append(c)
        self.set_classes(classes)


    def append_classes(self, c):
        """ Add multiple css classes for this element. """
        classes = self.classes()
        classes.extend(c)
        self.set_classes(classes)


    def href(self):
        """ Return this element's href attribute. """
        return self.attributes().get(HTML_ATTRIBUTE.HREF, "")


    def set_href(self, href):
        """ Set the href attribute for this element. """
        self.element().set(HTML_ATTRIBUTE.HREF, href)


    def children(self):
        """ Return a list of the immediate children for this element. """
        # TODO: elementTree suggests list(element) over element.getchildren(),
        # which is deprecated in v2.7, but iter(), iterfind(), and itertext()
        # are not yet available in cElementTree. update this when they are.
        #return self.element().getchildren()
        return list(self.element())


    def first_child(self):
        """ Return the first immediate child for this element. """
        return self.children()[0]


    def last_child(self):
        """ Return the last immediate child for this element. """
        return self.children()[-1:]


    def append_child(self, element):
        """ Append a child element to this element's direct children. """
        self.element().append(element)


    def append_children(self, elements):
        """ Append child elements to this element's direct children. """
        self.element().extend(elements)


    @staticmethod
    def validate(tags):
        """ Validate data being used to create a new HTML element. """

        for tag in tags:
            
            # is this a valid tag that has been implemented?
            if tag not in HTML_CONSTANT.TAGS:
                raise InvalidTagError(tag, "HTML tag not implemented.")

            invalid_attributes = []
            invalid_classes = []

            for attribute, value in tag.attributes():
                
                # is this a valid attribute that has been implemented?
                if attribute not in HTML_CONSTANT.ATTRIBUTES[tag]:
                    invalid_attributes.append(attribute)
                
                # if this is the class attribute, is its value valid?
                if attribute == HTML_ATTRIBUTE.CLASS:
                    class_set = set(tag.classes())
                    valid_class_set = set(HTML_CONSTANT.CLASSES[tag])
                    diff_set = class_set.difference(valid_class_set)
                    # TODO: this should be a dictionary keyed on tag.
                    invalid_classes.extend(list(diff_set))

            if invalid_attributes is not []:
                raise InvalidAttributeError(
                        invalid_attributes,
                        "HTML attributes not allowed.")

            # TODO: define InvalidClassError and pass it a dictionary.
            if invalid_attributes is not []:
                raise InvalidAttributeError(
                        invalid_classes,
                        "HTML classes not allowed for this tag.")


    @staticmethod
    def to_string(element_tree):
        """ Convenience wrapper to standardize on utf-8 and html. """
        # TODO: elementree and celementree differ; does method="html" exist?
        #return ET.tostring(element_tree, "utf-8", "html")
        return ET.tostring(element_tree, "utf-8")


class Div(Element):

    """ Div element <div>. """


    def __init__(self):
        """ Construct a <div>. """
        super(Div, self).__init__(HTML_TAG.DIV)


class Span(Element):

    """ Span element <span>. """


    def __init__(self):
        """ Construct a <span>. """
        super(Span, self).__init__(HTML_TAG.SPAN)


class List(Element):

    """ Abstract list element. """


    def __init__(self, tag, items):
        """ Construct an abstract List. """
        super(List, self).__init__(tag)

        # guarantees direct children of subclasses are <li> elements
        self.set_list_items(items)


    def set_list_items(self, items):
        """ Construct and add list items as this list's children. """
        for item in items:
            self.set_list_item(item)


    def set_list_item(self, item):
        """ Construct and add a list item as a child of this list. """
        return self.append_child(LI(item).element())


class OL(List):

    """ Ordered List element <ol>.
    
    Attribute   Value           Description
    ---------------------------------------
    reversed    reversed        Specifies that the list order should be
                                descending (9,8,7...)
    start       {number}        Specifies the start value of an ordered
                                list
    type        1               Specifies the kind of marker to use in
                A               the list
                a
                I
                i

    """


    def __init__(self, items):
        """ Construct a <ol>. """
        super(OL, self).__init__(HTML_TAG.OL, items)


class UL(List):

    """ Unordered List element <ul>. """
    
 
    def __init__(self, items):
        """ Construct a <ul>. """
        super(UL, self).__init__(HTML_TAG.UL, items)


class LI(Element):

    """ List Item element <li>.
    
    Attribute   Value           Description
    ---------------------------------------
    value       number          Specifies the value of a list item. The
                                following list items will increment from
                                that number (only for <ol> lists)

    """


    def __init__(self, item):
        """ Construct a <li>. """
        super(LI, self).__init__(HTML_TAG.LI)

        # TODO: are there special members we want applied to a generic list
        # item, such as special_item or this_is_you?


class Nav(Element):

    """ Nav element <nav>.

    <nav> elements should always have a <ul> as a first direct child. It
    may later become necessary to allow for mobility among direct
    direct children, but this seems sufficient for now.

        <nav>
            <ul>
                ...
            </ul>
        </nav>

    """


    def __init__(self, items, special_item=None, special_item_index=0):
        """ Construct a <nav>. """
        super(Nav, self).__init__(HTML_TAG.NAV)

        #if special_item is not None:
        #    items.insert(special_item_index, special_item)

        self.append_child(NavUL(items).element())

        # TODO: is there css we want applied even to this base class?
        #self.append_classes([])


class A(Element):

    """ Anchor element <a>.

    Attribute   Value           Description
    ---------------------------------------
    href        {URL}           Specifies the URL of the page the link
                                goes to
    hreflang    {language_code} Specifies the language of the linked
                                document
    media       {media_query}   Specifies what media/device the linked
                                document is optimized for
    rel         alternate       Specifies the relationship between the
                                current document and the linked document
                author
                bookmark
                help
                license
                next
                nofollow
                noreferrer
                prefetch
                prev
                search
                tag
    target      _blank          Specifies where to open the linked
                _parent         document
                _self
                _top
                {framename}
    type        {MIME_type}     Specifies the MIME type of the linked
                                document

    """


    def __init__(self, link):
        """ Construct a <a>. """
        super(A, self).__init__(HTML_TAG.A)
        
        # TODO: these are hardcoded strings and not constants because once we
        # have a Link class [and an Item interface or some such thing for it
        # to implement] we will just be accessing properties there. this makes
        # it more obvious what to change.
        self.set_href(link["href"])
        self.set_text(link["text"])

        # TODO: is there css we want applied even to this base class?
        #self.append_classes([])


class H1(Element):

    """ Header 1 element <h1>."""


    def __init__(self):
        """ Construct a <h1>. """
        super(H1, self).__init__(HTML_TAG.H1)


class H2(Element):

    """ Header 2 element <h2>."""


    def __init__(self):
        """ Construct a <h2>. """
        super(H2, self).__init__(HTML_TAG.H2)


class ElementError(Exception):

    """ ElementError is a subclass of Exception.
    
    Provide an exception superclass from which all Element errors
    should inherit.

    Required:
    str     reason      what went wrong?
    
    """

    reason = None

    def __init__(self, error, parameters, description):
        """ Construct a generic, not quite abstract ElementError. """
        self.reason = "{0}: <{1}> : {2}".format(
                error,
                ", ".join(parameters),
                description)


class InvalidTagError(ElementError):

    """ InvalidTagError is a subclass of ElementError.

    Provide an exception to be raised when an attempt is made to create
    an element from an invalid html tag.

    """

    def __init__(self, parameter, description):
        """ Construct a InvalidTagError extending ElementError. """
        super(InvalidTagError, self).__init__(
                "InvalidTagError",
                [parameter],
                description)


class InvalidElementError(ElementError):

    """ InvalidElementError is a subclass of ElementError.

    Provide an exception to be raised when an attempt is made to modify
    an invalid element as though it were valid HTML.

    """

    def __init__(self, parameter, description):
        """ Construct a InvalidElementError extending ElementError. """
        super(InvalidElementError, self).__init__(
                "InvalidElementError",
                [parameter],
                description)


class InvalidContentError(ElementError):

    """ InvalidContentError is a subclass of ElementError.

    Provide an exception to be raised when an element has both text and
    child HTML content.

    """

    def __init__(self, parameters, description):
        """ Construct a InvalidContentError extending ElementError. """
        super(InvalidContentError, self).__init__(
                "InvalidContentError",
                parameters,
                description)


class InvalidAttributeError(ElementError):

    """ InvalidAttributeError is a subclass of ElementError.

    Provide an exception to be raised when an element has invalid
    attributes.

    """

    def __init__(self, parameters, description):
        """ Construct a InvalidAttributeError extending ElementError. """
        super(InvalidAttributeError, self).__init__(
                "InvalidAttributeError",
                parameters,
                description)

