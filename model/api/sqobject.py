"""
SqNode module

...
"""

#import Utils

class SqObject(object):

    """
    SqObject is a subclass of the __new__ python object

    Provide access to the common attributes of a League, Team, Player,
    User, and Game, including fields and edges connecting to other 
    nodes.

    Required:
    id          _id         SqObject node id
    timestamp   _created_ts when was this SqObject created
    timestamp   _updated_ts when was this SqObject last updated
    timestamp   _deleted_ts when, if at all, was this SqObject deleted
    """

    _id = None
    _created_ts = None
    _updated_ts = None
    _upddeleted_ts = None

    def __init__(self, id, attributes_dict):
        """
        Construct a SqObject extending the __new__ python object and 
        set private members common to all subclasses.
        """
        self._id = id

        # created_ts/updated_ts/deleted_ts to be defined in Utils constants
        self._created_ts = attributes_dict["created_ts"]
        self._updated_ts = attributes_dict["updated_ts"]
        self._deleted_ts = attributes_dict["deleted_ts"]

    def get_id():
        """
        Return a SqObject node id.
        """
        return self._id

