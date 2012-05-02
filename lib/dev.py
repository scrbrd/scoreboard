""" Module: dev

Use these tools in a dev environment only.

"""

import time

def print_timing(func):
    """ Time decorated function. Print output. """

    def wrapper(*arg):
        t1 = time.time()
        print "{0} LAUNCHED".format(func.func_name)
        res = func(*arg)
        t2 = time.time()
        print '%s took %0.3f ms' % (func.func_name, (t2-t1)*1000.0)
        return res
    return wrapper

