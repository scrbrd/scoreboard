""" Module: data_errors

Contain all database oriented errors.

"""


class DbInputError(Exception):

    """ Exception raised when the incoming request has bad input.

    Variables:
    str reason  the reason for the error.

    """


    def __init__(self, param_name, param_value, reason):
        """ Initialize DbInputError.

        Required:
        str param_name       which param has bad data
        str param_value      the value of the parameter
        str reason           the quality which makes the data bad

        """
        self.reason = "DbInputError: {0} - {1}: {2}".format(
            param_name,
            param_value,
            reason)


class DbWriteError(Exception):

    """ Exception raised when the database cannot be written to.

    Variables:
    str reason  the reason for the error.

    """


    def __init__(self, write_type, reason):
        """ Initialize DbWriteError.

        Required:
        str write_type   type of write that has failed
        str reason       why/how the write failed

        """
        self.reason = "DbWriteError: {0}: {1}".format(write_type, reason)


class DbReadError(Exception):

    """ Exception raised when the database cannot be read from.

    Variables:
    str reason  the reason for the error.

    """

    def __init__(self, read_type, reason):
        """ Initialize DbReadError.

        Required:
        str reason       why/how the read failed

        """
        self.reason = "DbReadError: {0}: {1}".format(read_type, reason)


class DbConnectionError(Exception):

    """ Exception raised when the database connection breaks.

    Variables:
    str reason  the reason for the error.

    """

    def __init__(self, reason):
        """ Initialize DbConnectionError.

        Required:
        str reason  why the database connection didn't work.

        """
        self.reason = reason
