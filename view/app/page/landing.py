""" Module: landing

Element components for Landing Page.

"""

from view.constants import PAGE_NAME

from view.elements.base import Section, Div
from view.elements.components import FacebookLoginButton

from constants import PAGE_CLASS


class LandingPage(Section):

    """ Landing Page extending <section>. """

    def __init__(self, login_link):
        """ Construct  the landing page. """
        super(LandingPage, self).__init__()
        self.set_id(PAGE_NAME.LANDING)

        login_button_section = LoginButtonSection(
                FacebookLoginButton(login_link))
        self.append_child(login_button_section)


class LoginButtonSection(Div):

    """ Component that has a login button in a <div> (for centering). """

    def __init__(self, login_button):
        """ Construct a dialog component for a login button. """
        super(LoginButtonSection, self).__init__()
        self.append_classes([PAGE_CLASS.LOGIN_BUTTON_WRAPPER])

        self.append_child(login_button)
