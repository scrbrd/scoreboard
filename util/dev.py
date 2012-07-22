""" Module: dev

Use these tools in a dev environment only.

"""
from pprint import pprint
import os


def print_timing(func):
    """ Debug decorator to see how long functions take. """


    def wrapper(*arg):
        t1 = os.times()[4]
        return_value = func(*arg)
        t2 = os.times()[4]
        print "{0} took {1}ms".format(func.func_name, (t2 - t1) * 1000.0)
        return return_value
    return wrapper


def obj_to_dict(obj, classkey=None):
    if isinstance(obj, dict):
        for k in obj.keys():
            obj[k] = obj_to_dict(obj[k], classkey)
        return obj
    elif hasattr(obj, "__iter__"):
        return [obj_to_dict(v, classkey) for v in obj]
    elif hasattr(obj, "__dict__"):
        data = dict(
                [
                    (key, obj_to_dict(value, classkey))
                    for key, value in obj.__dict__.iteritems()
                    if not callable(value) and not key.startswith('_')
                ])
        if classkey is not None and hasattr(obj, "__class__"):
            data[classkey] = obj.__class__.__name__
        return data
    else:
        return obj


def print_obj(obj, classkey=None):
    pprint(obj_to_dict(obj, classkey))
