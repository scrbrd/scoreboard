""" Module: constants

View Constants - provide constants for view.

    HTML_COPY

"""

# TODO: this file should be malleable strings instead of constants.

def constant(f):
    """ Constant Decorator to make constants Final. """


    def fset(self, value):
        """ Overload constant function's set to disable."""
        raise SyntaxError
    

    def fget(self):
        """ Overload constant function's get. """
        return f(self)


    return property(fget, fset)


class _HTMLCopy(object):

    """ _HTMLCopy class holds all HTML copy. """


    @constant
    def SUBMIT(self):
        """ SUBMIT is the copy for the submit button. """
        return "Submit!"


    @constant
    def CLOSE(self):
        """ CLOSE is the copy for the close button. """
        return "Close it"


    @constant
    def CREATE_GAME_DIALOG_HEADER(self):
        """ CREATE_GAME_DIALOG_HEADER is the copy for the creat game dialog's
        header. """
        return "Add Game"


    @constant
    def PLAYER_PLACEHOLDER(self):
        """ PLAYER_PLACEHOLDER is the copy for a player placeholer. """
        return "Who played?"

    
    @constant
    def SCORE_PLACEHOLDER(self):
        """ SCORE_PLACEHOLDER is the copy for a score placeholder. """
        return "And the score?"


HTML_COPY = _HTMLCopy()


