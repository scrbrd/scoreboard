""" Module: model

Element components that are for the tab's model div that sends model pieces to
the client as part of the DOM.

"""
import json

from view.constants import SQ_DATA, MODEL_ID
from view.html.elements import DataInput


class ViewerContextModel(DataInput):

    """ Viewer Context Model container that extends DataInput. """

    def __init__(self, viewer_context):
        """ Construct a viewer context model div element tree. """
        super(ViewerContextModel, self).__init__()
        self.set_id(MODEL_ID.VIEWER_CONTEXT)

        # set rivals data for friend/rival player selection
        view_rivals = []
        # TODO make viewer_context an object instead of a dictionary
        for r in viewer_context[SQ_DATA.RIVALS]:
            view_rivals.append({SQ_DATA.ID: r.id, SQ_DATA.NAME: r.name})
        self.set_data(SQ_DATA.RIVALS, json.dumps(view_rivals))


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
