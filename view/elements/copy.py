""" Module: copy

Reusable copy for the element components. Currently, these are strings,
but later they should probably be templates.

"""


class _Copy(object):


    @property
    def on(self):
        return "On"

    @property
    def off(self):
        return "Off"

    @property
    def login(self):
        return "Login"

    @property
    def login_with_facebook(self):
        return "Login with Facebook"

    @property
    def post(self):
        return "Post"

    @property
    def close(self):
        return "Close"

    @property
    def okay(self):
        return "Okay"


Copy = _Copy()
