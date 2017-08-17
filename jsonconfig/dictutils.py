"""Attribute & Dictionary Access for Dictories"""
import os
from copy import copy

import keyring

from .errors import (
    SetEnvironVarError, DeleteEnvironVarError,
    SetPasswordError, DeletePasswordError
)


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


class KeyringAttrDict(dict):
    """Ability to get & set passwords using attribute-style notation."""

    service = None

    def __getattr__(self, attr):
        return keyring.get_password(KeyringAttrDict.service, attr)

    def __setattr__(self, attr, value):
        try:
            keyring.set_password(KeyringAttrDict.service, attr, value)
        except Exception as e:
            raise SetPasswordError(e)

    def __delattr__(self, attr):
        try:
            keyring.delete_password(KeyringAttrDict.service, attr)
        except Exception as e:
            raise DeletePasswordError(e)

    def __str__(self):
        return keyring.get_keyring().name

    def __repr__(self):
        return repr(keyring.backend)

    def pop(self, key):
        value = self[key]
        del self[key]
        return value

    def update(self, d):
        for key, value in d.items():
            self[key] = value

    __getitem__ = __getattr__
    __setitem__ = __setattr__
    __delitem__ = __delattr__
