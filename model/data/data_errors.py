""" Module: data_errors

Contain all database oriented errors.

"""

class DbInputError(Exception):
    
    """ Exception raised when the incoming request has bad input.

    Required:
    string param_name       which param has bad data
    string param_value      the value of the parameter  
    string reason           the quality which makes the data bad

    Returns msg
    
    """
    
    msg = None

    def __init__(self, param_name, param_value, reason):
        """ Initialize DbInputError. """
        self.msg = "DbInputError: {0} - {1}: {2}".format(
            param_name, 
            param_value,
            reason)


class DbWriteError(Exception):

    """ Exception raised when the database cannot be written to.

    Required:
    string write_type   type of write that has failed
    string reason       why/how the write failed

    Returns msg

    """
    
    msg = None

    def __init__(self, write_type, reason):
        """ Initialize DbWriteError. """
        self.msg = "DbWriteError: {0}: {1}".format(write_type, reason)


class DbReadError(Exception):
     
    """ Exception raised when the database cannot be read from.

    Required:
    string reason       why/how the read failed

    Returns msg
    
    """
    
    msg = None

    def __init__(self, reason):
        """ Initialize DbReadError. """
        self.msg = "DbReadError: {0}".format(reason)

class DbConnectionError(Exception):

    """ Exception raised when the database connection breaks. """

    msg = None

    def __init__(self, msg):
        """ Initialize DbConnectionError. """
        self.msg = msg

