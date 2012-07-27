""" Module: landing

Element components for Landing Page.

"""

from view.constants import PAGE_NAME

from view.elements.base import Section, Div
from view.elements.components import FacebookLoginAnchor

from constants import PAGE_CLASS


class LandingPage(Section):

    """ Landing Page extending <section>. """


    def __init__(self, login_url):
        """ Construct  the landing page. """
        super(LandingPage, self).__init__()
        self.set_id(PAGE_NAME.LANDING)

        self.append_child(LoginAnchorSection(login_url))


class LoginAnchorSection(Div):

    """ Component that has a login button in a <div> (for centering). """

    def __init__(self, login_url):
        """ Construct a dialog component for a login button. """
        super(LoginAnchorSection, self).__init__()
        # WRAPPER helps position button on page.
        self.append_classes([PAGE_CLASS.LOGIN_ANCHOR_WRAPPER])

        self.append_child(FacebookLoginAnchor(login_url))
