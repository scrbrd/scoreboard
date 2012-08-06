""" Module: base

All data requests are processed by request type and the appropriate
data is retrieved and returned as a Model.

"""

from exceptions import NotImplementedError


class BaseModel(object):

    """ Fetch and/or edit all data necessary for a model request.

    BaseModels wrap around returned data to provide controlled access
    outside of model.

    Required:
    dict    _session    all the user data that's stored as a cookie

    """


    def __init__(self, session):
        """ BaseModel is an abstract superclass.

        Required:
        dict    session     all the User/Person session data

        """
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
    League  _context        container of objects (id, name fields required)
    dict    _aggregations   aggregated stats describing context
    list    _objects        discrete units describing context
    list    _rivals         list of Opponents (id, name)
    list    _sports         list of Sports

    """


    def __init__(self, session):
        """ ReadModel is an Abstract superclass.

        Required:
        dict    session     all the User/Person session data

        """
        super(ReadModel, self).__init__(session)

        self._context = None
        self._aggregations = None
        self._objects = None
        self._rivals = None
        self._sports = None


    def dispatch(self):
        """ Propagate a write to a model. """
        raise NotImplementedError("Unused Method: DO NOT CALL OR OVERRIDE!")


    @property
    def context(self):
        """ Context/Container of fetched data. """
        return self._context


    @property
    def aggregations(self):
        """ Return a dict of aggregated data describing context. """
        return self._aggregations


    @property
    def objects(self):
        """ Return a list of discrete units of data. """
        return self._objects


    @property
    def rivals(self):
        """ List of Opponents with name and id. """
        return self._rivals


    @property
    def sports(self):
        """ List of Sports. """
        return self._sports


class WriteModel(BaseModel):

    """ Write data to a model and return success.

    Optional:
    SqNode  _object     the newly created object

    """


    def __init__(self, session):
        """ WriteModel is an Abstract superclass.

        Required:
        dict    session     all the User/Person session data

        """
        super(WriteModel, self).__init__(session)

        self._object = None


    def load(self):
        """ Return a model. """
        raise NotImplementedError("Unused Method: DO NOT CALL OR OVERRIDE!")


    @property
    def success(self):
        """ Return whether this Model successfully dispatched a write. """
        return bool(self._object)
