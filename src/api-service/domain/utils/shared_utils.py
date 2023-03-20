
class DictToObj(object):
    """
    Turns a dictionary into a class
    """
    # ----------------------------------------------------------------------

    def __init__(self, dictionary):
        """Constructor"""
        try:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        except:
            dictionary

class ConvertDictToClass(dict):

    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    # def __init__(self, my_dict):
    #     for key in my_dict:
    #         setattr(self, key, my_dict[key])


def DictFromClass(cls, _excluded_keys={}):

    # _excluded_keys = set(A.__dict__.keys())
   
    return dict(
        (key, value)
        for (key, value) in cls.__dict__.items()
        if key not in _excluded_keys
    )
