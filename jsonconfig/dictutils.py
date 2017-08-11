"""Attribute & Dictionary Access for Dictories"""
import os

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
        except (keyring.errors.PasswordSetError, TypeError) as e:
            raise SetPasswordError(e)

    def __delattr__(self, attr):
        try:
            keyring.delete_password(KeyringAttrDict.service, attr)
        except (keyring.errors.PasswordDeleteError, TypeError) as e:
            raise DeletePasswordError(e)

    __getitem__ = __getattr__
    __setitem__ = __setattr__
    __delitem__ = __delattr__
