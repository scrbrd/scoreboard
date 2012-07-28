""" Module: dialog

Define a DialogModel to provide the DialogHandler with the set of
constant values required to correctly prompt the User to enter new
information to be written to our database.

For now, only CreateGameDialogHandler exists, but we will need to
subclass both here and in the controller's Handler reasonably soon.

"""

from model.api.constants import API_EDGE_TYPE

from base import ReadModel


class DialogModel(ReadModel):

    """ Return input fields for generating a dialog form.

    Required:
    dict    _constants      node context type, result edge types

    """

    _won_result = None
    _lost_result = None
    _played_result = None


    def load(self):
        """ Load Node/Edge Property/Type constants. """
        # FIXME: we should be pulling these result edge types from static
        # methods on the player/person, not accessing constants this module
        # isn't really allowed to see. no big deal for now, though.
        self._won_result = API_EDGE_TYPE.WON
        self._lost_result = API_EDGE_TYPE.LOST
        self._played_result = API_EDGE_TYPE.PLAYED


    @property
    def won_result(self):
        """ Result value representing an Opponent who won. """
        return self._won_result


    @property
    def lost_result(self):
        """ Result value representing an Opponent who lost. """
        return self._lost_result


    @property
    def played_result(self):
        """ Result value representing an Opponent who played. """
        return self._played_result
