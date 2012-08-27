""" Module: landing

Element components for Landing Page.

"""
from view.constants import PAGE_NAME

from view.elements.base import Section, Div
from view.elements.components import FacebookLoginAnchor


class LandingPage(Section):

    """ Landing Page extending <section>. """


    def __init__(self, login_url):
        """ Construct  the landing page. """
        super(LandingPage, self).__init__()
        self.set_id(PAGE_NAME.LANDING)

        self.append_child(LoginAnchorSection(login_url))


class LoginAnchorSection(Div):

    """ Component that has a login button in a <div> (for centering). """

    LOGIN_ANCHOR_WRAPPER_CLASS = "login-anchor-wrapper"


    def __init__(self, login_url):
        """ Construct a dialog component for a login button. """
        super(LoginAnchorSection, self).__init__()
        # WRAPPER helps position button on page.
        self.append_class(self.LOGIN_ANCHOR_WRAPPER_CLASS)

        self.append_child(FacebookLoginAnchor(login_url))
