""" Module: data_errors

Contain all database oriented errors.

"""


class DbInputError(Exception):

    """ Exception raised when the incoming request has bad input.

    Required:
    string param_name       which param has bad data
    string param_value      the value of the parameter
    string reason           the quality which makes the data bad

    Returns reason

    """
    reason = None

    def __init__(self, param_name, param_value, msg):
        """ Initialize DbInputError. """
        self.reason = "DbInputError: {0} - {1}: {2}".format(
            param_name,
            param_value,
            msg)


class DbWriteError(Exception):

    """ Exception raised when the database cannot be written to.

    Required:
    string write_type   type of write that has failed
    string reason       why/how the write failed

    Returns reason

    """
    reason = None

    def __init__(self, write_type, msg):
        """ Initialize DbWriteError. """
        self.reason = "DbWriteError: {0}: {1}".format(write_type, msg)


class DbReadError(Exception):

    """ Exception raised when the database cannot be read from.

    Required:
    string reason       why/how the read failed

    Returns msg

    """
    reason = None

    def __init__(self, read_type, msg):
        """ Initialize DbReadError. """
        self.reason = "DbReadError: {0}: {1}".format(read_type, msg)


class DbConnectionError(Exception):

    """ Exception raised when the database connection breaks. """
    reason = None

    def __init__(self, msg):
        """ Initialize DbConnectionError. """
        self.reason = msg
