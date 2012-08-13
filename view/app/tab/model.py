""" Module: model

Element components that are for the tab's model div that sends model pieces to
the client as part of the DOM.

"""

import json

from view.constants import SQ_DATA, MODEL_ID

from view.elements.base import DataInput


class SessionModel(DataInput):

    """ Session Model container that extends DataInput. """

    def __init__(self, model):
        """ Construct a session model div element tree. """
        super(SessionModel, self).__init__()
        self.set_id(MODEL_ID.SESSION)

        # set rivals data for friend/rival player selection
        view_rivals = []
        # TODO make session an object instead of a dictionary
        for r in model.rivals:
            view_rivals.append({
                    SQ_DATA.ID: r.id,
                    SQ_DATA.NAME: r.full_name,
                    SQ_DATA.PICTURE: r.picture_url,
                    })
        self.set_data(SQ_DATA.RIVALS, json.dumps(view_rivals))

        # set sports data for sport selection
        view_sports = []
        for sport_id, sport_name in model.sports.items():
            view_sports.append({
                    SQ_DATA.ID: sport_id,
                    SQ_DATA.NAME: sport_name,
                    SQ_DATA.PICTURE: "",
                    })
        self.set_data(SQ_DATA.SPORTS, json.dumps(view_sports))

        # set person id from session
        pid = model.session.person_id
        self.set_data(SQ_DATA.PERSON_ID, pid)


class ContextModel(DataInput):

    """ Context Model container that extends DataInput. """

    def __init__(self, context):
        """ Construct a context model div element tree. """
        super(ContextModel, self).__init__()
        self.set_id(MODEL_ID.CONTEXT)

        self.set_data(SQ_DATA.ID, context.id)
        self.set_data(SQ_DATA.NAME, context.name)
        self.set_data(SQ_DATA.OBJECT_TYPE, context.type)


class PageModel(DataInput):

    """ Content Model container that extends DataInput. """

    def __init__(self, content):
        """ Construct a content model div element tree. """
        super(PageModel, self).__init__()
        self.set_id(MODEL_ID.PAGE_STATE)

        self.set_data(SQ_DATA.PAGE_TYPE, content[SQ_DATA.PAGE_TYPE])
        self.set_data(SQ_DATA.PAGE_NAME, content[SQ_DATA.PAGE_NAME])
