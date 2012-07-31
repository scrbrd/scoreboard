""" Module: home

Provide a handler for the home page. Delegate processing of the request
to whatever is currently understood to be the default logged-in view
or else forward to the landing page.

"""

from handlers.landing import LandingHandler
from handlers.league import LeagueHandler


class HomeHandler(LeagueHandler, LandingHandler):

    """ Determine if the user needs to see the Landing page or the Home page.

    Check for a logged in user and then route appropriately.

    IMPORTANT: LeagueHandler must be inherited before LandingHandler
    in order to make sure that self.current_user refers to the
    LeagueHandler implementation, which will always return a
    Session if one exists.

    from http://docs.python.org/release/1.5/tut/node66.html

    It is clear that indiscriminate use of multiple inheritance is a
    maintenance nightmare, given the reliance in Python on conventions
    to avoid accidental name conflicts. A well-known problem with
    multiple inheritance is a class derived from two classes that happen
    to have a common base class. While it is easy enough to figure out
    what happens in this case (the instance will have a single copy of
    ``instance variables'' or data attributes used by the common base
    class), it is not clear that these semantics are in any way useful.

    """

    # NOT @tornado.web.authenticated because LandingHandler is not.
    def get(self):
        """ Handle GET request for the Home page. """

        # if the user is logged in, go to the home page.
        if self.current_user is not None:
            LeagueHandler.process_request(self)

        # otherwise, go to the landing page.
        else:
            LandingHandler.process_request(self)
