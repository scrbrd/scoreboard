""" Module: base

All data requests are processed by request type and the appropriate
data is retrieved and returned as a Model.

"""

from exceptions import NotImplementedError


class BaseModel(object):

    """ Fetch and/or edit all data necessary for a model request.

    BaseModels wrap around returned data to provide controlled access
    outside of model.

    """

    _session = None


    def __init__(self, session):
        """ BaseModel is an abstract superclass. """
        self._session = session


    @property
    def session(self):
        """ Return a Session with some User/Person session data. """
        return self._session


    def load(self):
        """ Return a model. """
        raise NotImplementedError("Abstract Class: SUBCLASS MUST OVERRIDE!")


    def dispatch(self):
        """ Propagate a write to a model. """
        raise NotImplementedError("Abstract Class: SUBCLASS MUST OVERRIDE!")


class ReadModel(BaseModel):

    """ Read and return all data for a model request.

    Required:
    League  _context    container of objects (id, name fields required)
    dict    _summary    aggregated stats describing context
    list    _feed       discrete units describing context
    list    _rivals     list of Opponents (id, name)

    """

    _context = None
    _summary = None
    _feed = None
    _rivals = None


    def dispatch(self):
        """ Propagate a write to a model. """
        raise NotImplementedError("Unused Method: DO NOT CALL OR OVERRIDE!")


    @property
    def context(self):
        """ Context/Container of fetched data. """
        return self._context


    @property
    def summary(self):
        """ Return a dict of aggregated data describing context. """
        return self._summary


    @property
    def feed(self):
        """ Return a list of discrete units of data describing context. """
        return self._feed


    @property
    def rivals(self):
        """ List of Opponents with name and id. """
        return self._rivals


class WriteModel(BaseModel):

    """ Write data to a model and return success.

    Required:
    bool    success     was this dispatched write successful?

    """

    _model = None


    def load(self):
        """ Return a model. """
        raise NotImplementedError("Unused Method: DO NOT CALL OR OVERRIDE!")


    @property
    def success(self):
        """ Return whether this Model successfully dispatched a write. """
        return bool(self._model)
