import os

from .errors import SetEnvironVarError, DeleteEnvironVarError


class EnvironAttrDict(dict):
    """Access to environment variables using attribute-style notation."""

    def __getattr__(self, attr):
        return os.environ.get(attr)

    def __setattr__(self, attr, value):
        try:
            os.environ[attr] = value
        except TypeError as e:
            raise SetEnvironVarError(e)

    def __delattr__(self, attr):
        try:
            del os.environ[attr]
        except (KeyError, TypeError) as e:
            raise DeleteEnvironVarError(e)

    def __iter__(self):
        return iter(os.environ)

    def __len__(self):
        return len(os.environ)

    def __str__(self):
        return str(os.environ)

    def __repr__(self):
        return repr(os.environ)

    def __contains__(self, key):
        return key in os.environ

    def __eq__(self, d):
        return os.environ == d

    def __ne__(self, d):
        return os.environ != d

    def items(self):
        return os.environ.items()

    def keys(self):
        return os.environ.keys()

    def pop(self, key):
        return os.environ.pop(key)

    def popitem(self):
        return os.environ.popitem()

    def update(self, d):
        os.environ.update(d)

    def values(self):
        return os.environ.values()

    def setdefault(self, key, d=None):
        os.environ.setdefault(key, d)

    __getitem__ = __getattr__
    __setitem__ = __setattr__
    __delitem__ = __delattr__
