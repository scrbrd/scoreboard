""" Module: debug

...

"""

from pprint import pprint


def obj_to_dict(obj, classkey=None):
    if isinstance(obj, dict):
        for k in obj.keys():
            obj[k] = obj_to_dict(obj[k], classkey)
        return obj
    elif hasattr(obj, "__iter__"):
        return [obj_to_dict(v, classkey) for v in obj]
    elif hasattr(obj, "__dict__"):
        data = dict([
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

