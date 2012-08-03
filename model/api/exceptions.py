""" Module: exceptions

API Exceptions to throw.

"""


class InputError(Exception):

    """ Exception raise when the incoming request has bad input.

    Variables:
    str     reason      an explanation for the error

    """


    def __init__(self, parameter_name, parameter_value):
        """ Construct an bad input error.

        Required:
        str     parameter_name  the parameter that threw the exception.
        str     parameter_value the value of that parameter.

        """
        self.reason = "InputError: {0} can't have value, {1}.".format(
                parameter_name,
                parameter_value)
