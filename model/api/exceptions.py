""" Module: exceptions

API Exceptions to throw.

"""


class InputError(Exception):

    """ Exception raise when the incoming request has bad input.

    Required:
    str     parameter_name  the parameter that threw the exception.
    str     parameter_value the value of that parameter.

    """
    reason = None


    def __init__(self, parameter_name, parameter_value):
        self.reason = "InputError: {0} can't have value, {1}.".format(
                parameter_name,
                parameter_value)
