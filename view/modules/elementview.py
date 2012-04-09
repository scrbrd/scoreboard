""" Module: elementview

Provide generic HTML5 tag wrappers as subclasses of Tornado's UIModule.
Mobile views should extend these to create context-specific components.

"""

import xml.etree.cElementTree as ET
from exceptions import NotImplementedError

import tornado.web


class ElementView(tornado.web.UIModule):

    """ Abstract Element. """

    def render(self):
        """ Raise NotImplementedError. """
        raise NotImplementedError("No generic HTML element.")


    def html(self):
        """ Raise NotImplementedError. """
        raise NotImplementedError("No generic HTML element.")


    def to_string(self, markup):
        """ Convenience wrapper to centralize encoding. """
        return ET.tostring(markup, encoding="utf-8")


class DivView(ElementView):

    """ Wrapper class for the <div> element. """

    def render(self):
        """ Render a <div> element. """
        return self.to_string(self.html())


    def html(self):
        """ Generate and return a <div> element. """
        return ET.Element("div")


class SpanView(ElementView):

    """ Wrapper class for the <span> element. """

    def render(self, text, attributes={}):
        """ Render a <span> element. """
        # FIXME: <span> should be able to take inline display element too
        return self.to_string(self.html(text, attributes))


    def html(self, text, attributes={}):
        """ Generate and return a <span> element. """
        # FIXME: returns <span text="foo" />, not <span>foo</span>
        return ET.Element("span", attributes, text=text)


class ListView(ElementView):

    """ Abstract Wrapper around a List Element. """

    def _html_generate_list_items(self, list_elem, items):
        """ Generate all the html list items for a list. """
        for item in items:
            list_elem.append(self._html_generate_list_item(item))

        return list_elem


    def _html_generate_list_item(self, item):
        """ Generate the html for an individual list_item. """
        return LIView(self).html(item)


class OLView(ListView):

    """ Wrapper around an Ordered List Element. <ol> """

    def render(self, items):
        """ Render the <ol> element. """
        return self.to_string(self.html(items))


    def html(self, items):
        """ Generate and return Element for <ol>. """
        return self._html_generate_list_items(ET.Element("ol"), items)


class ULView(ListView):

    """ Wrapper around an Unordered List Element. <ul> """
    
    def render(self, items):
        """ Render a <ul> element. """
        return self.to_string(self.html(li_items))

    def html(self, li_items):
        """ Generate and return Element for <ul>. """
        return self._html_generate_list_items(ET.Element("ul"), li_items)


class LIView(ElementView):

    """ Wrapper around a List Item Element. <li> """

    def render(self, item):
        """ Render the <li> element. """
        return self.to_string(self.html(item))


    def html(self, item):
        """ Generate and return Element for <li>. """
        li_elem = ET.Element("li")
        # FIXME: is li_item guaranteed to be an element?
        li_elem.append(item)
        return li_elem

class NavView(ElementView):

    """ Wrapper class for the <nav> element. """

    def render(self, nav_items):
        """ Render a <nav> element. """
        return self.to_string(self.html(nav_items))


    def html(self, nav_items):
        """ Generate and return a <nav> element. """
        nav_elem = ET.Element("nav")

        # FIXME: does this belong here?
        # FIXME: build a URL class to formalize these anchors
        anchors = []
        for text, href in nav_items.items():
            anchors.append(AView(self).html(text, {"href" : href}))
        
        ul_elem = ULView(self).html(anchors)
        nav_elem.append(ul_elem)

        return nav_elem


class AView(ElementView):

    """ Wrapper class for the <a> element. """

    def render(self, text, attributes={}):
        """ Render a <a> element. """
        return self.to_string(self.html(text, attributes))


    def html(self, text, attributes={}):
        """ Generate and return a <a> element. """
        # FIXME: returns <a href="foo" text="bar />, not <a href="foo">bar</a>
        return ET.Element("a", attributes, text=text)

class H1View(ElementView):

    """ Wrapper class for the <h1> element. """

    def render(self, text):
        """ Render a <h1> element. """
        return self.to_string(self.html(text))


    def html(self, text):
        """ Generate and return <h1> element. """
        elem = ET.Element("h1")

        # FIXME move this to generic Element
        # FIXME add attributes dictionary
        elem.text = text

        return elem


class H2View(ElementView):

    """ Wrapper class for the <h2> element. """

    def render(self, text):
        """ Render a <h2> element. """
        return self.to_string(self.html(text))


    def html(self, text):
        """ Generate and return a <h2> element. """
        elem = ET.Element("h2")

        # FIXME move this to generic Element
        # FIXME add attributes dictionary
        elem.text = text
        
        return elem

