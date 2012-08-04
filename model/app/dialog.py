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
    str     _won_result
    str     _lost_result
    str     _played_result

    """


    def __init__(self, session):
        """ Construct a DialogModel.

        Required:
        dict    session     all the User/Person session data

        """
        super(DialogModel, self).__init__(session)

        self._won_result = None
        self._lost_result = None
        self._played_result = None


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
