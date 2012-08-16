""" Module: json

Provide subclasses of Tornado's UIModule that render a number of components and
package them as a JSON dictionary. Typically called asynchronously.

Each class has a single requirement...override render.

"""

import tornado.web
from tornado import escape

from view.elements import xsrf
from view.elements.base import Element
from view.app.tab.league import LeagueContentSection


# TODO: Put the dictionary generation for the handlers here. Once that's done
# you won't need templates/mobile/components or the UILeagueContent class
# below. You'll also probably not be using UIModules.
class UILeagueContent(tornado.web.UIModule):

    def render(self, model=None, state=None):
        self._current_person = None
        for rival in model.rivals:
            if (rival.id == self.current_user.person_id):
                self._current_person = rival

        xsrf.set_xsrf_token(escape.xhtml_escape(self.handler.xsrf_token))

        return Element.to_string(LeagueContentSection(
                model.context,
                model.aggregations,
                model.objects,
                self._current_person))
