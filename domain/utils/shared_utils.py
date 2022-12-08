

class ConvertDictToClass(dict):

    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    # def __init__(self, my_dict):
    #     for key in my_dict:
    #         setattr(self, key, my_dict[key])
