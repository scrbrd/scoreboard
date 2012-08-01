""" Module: copy

Reusable copy for the module components. Currently, these are strings,
but later they should probably be templates.

IT SEEMS VERY WRONG THAT WE HAVE COPY IN THIS PACKAGE AT ALL. HELP!

"""


class _Copy(object):


    @property
    def app_name(self):
        return "Scoreboard"

    @property
    def create_game_dialog_header(self):
        return "Add Game"


Copy = _Copy()
