import functools
import json
import os

import box
import click
import keyring

from .dictutils import (
    identity, nested_dict,
    EnvironAttrDict, KeyringAttrDict
)
from .errors import (
    FileError, FileEncodeError,
    JsonEncodeError, JsonDecodeError,
    KeyringNameError, KeyringTypeError
)

to_json, from_json = box._to_json, box._from_json

# data types
PLAIN = identity
BOXED = box.Box
FROZEN = functools.partial(BOXED, frozen_box=True)
NESTED = nested_dict

DEFAULT_FILENAME = 'config.json'


def get_config_file(app_name=__name__, path=None, filename=DEFAULT_FILENAME,
                    roaming=True, force_posix=False):
    """Get config filename with full path."""
    if not path:
        kwargs = dict(roaming=roaming, force_posix=force_posix)
        path = click.get_app_dir(app_name, **kwargs)
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except EnvironmentError as e:
            raise FileError(e)
    return os.path.join(path, filename)


def delete_config_file(**config_file_attrs):
    filename = get_config_file(**config_file_attrs)
    try:
        os.remove(filename)
    except EnvironmentError as e:
        raise FileError(e)


def set_keyring(backend):
    """Select keyring backend."""
    try:
        if not isinstance(backend, keyring.backend.KeyringBackend):
            backend = getattr(keyring.backends, backend.lstrip('_'))
        keyring.set_keyring(backend)
    except AttributeError as e:
        raise KeyringNameError(e)
    except TypeError as e:
        raise KeyringTypeError(e)


def from_json(filename):
    try:
        return box._from_json(filename=filename)
    except FileNotFoundError:
        return {}
    except EnvironmentError as e:
        raise FileError(e)
    except ValueError as e:
        raise FileEncodeError(e)
    except json.JSONDecodeError as e:
        raise JsonDecodeError(e)


def to_json(data, filename):
        try:
            return box._to_json(data, filename=filename)
        except TypeError as e:
            raise JsonEncodeError(e)
        except EnvironmentError as e:
            raise FileError(e)


class JsonConfig:

    def __init__(self, type_=None, name=__name__, mode='rw',
                 keyring=True, service=None, **attrs):

        if name == '__main__':
            raise ValueError('App Name is Required.')

        if mode:
            self.type = type_
            self.filename = get_config_file(name, **attrs)
        self.mode = mode or ''

        if keyring:
            KeyringAttrDict.service = service or name
            if keyring and keyring is not True:
                self.set_keyring(keyring)
        self.keyring = keyring

    def __enter__(self):
        self.env = EnvironAttrDict(os.environ)

        if self.keyring:
            self.pwd = KeyringAttrDict()

        if self.mode:
            self.data = None
            if 'r' not in self.mode and self.type:
                self.data = self.type({})
            else:
                self.data = from_json(self.filename)
                if self.type:
                    self.data = self.type(self.data)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if 'w' in self.mode and self.type is not FROZEN:
            to_json(self.data, self.filename)
