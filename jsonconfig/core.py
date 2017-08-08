import inspect
import json
import os.path
from functools import partial

import box
import click
import keyring

from .dictutils import (EnvironAttrDict, KeyringAttrDict)
from .errors import (
    FileError, FileEncodeError,
    JsonEncodeError, JsonDecodeError,
    KeyringNameError, KeyringTypeError
)

# data types
PLAIN = lambda x: x
BOXED = box.Box
FROZEN = partial(BOXED, frozen_box=True)
NESTED = partial(BOXED, default_box=True)

DEFAULT_FILENAME = 'config.json'

to_json = box._to_json
from_json = box._from_json


def get_module_name(depth=2):
    """Return the module name that called the calling function."""
    stack = inspect.stack()
    mod = inspect.getmodule(stack[depth][0])
    if mod.__name__ == '__main__':
        return os.path.splitext(os.path.basename(mod.__file__))[0]
    return mod.__name__


def get_config_file(app_name=None, path=None, filename=DEFAULT_FILENAME,
                    **app_dir_kwargs):
    """Return the configuration file's full pathname.

    If path does not exist, this function will attempt to create the
    directories.

    :param app_name: The application name.
        If app_name is not set it will default to the caller's module
        name. The app name should be properly capitalized and can
        contain whitespace.

    :param path: Optional configuration file or directory.
        * if not path --> `{app_dir}/{app_name}/{filename}`
        * if path endswith '.json' --> `{path}`
        * else' --> `{path}/{filename}`

    :param **app_dir_kwargs: roaming, force_posix, etc.
        See click.get_app_dir for a list of available options.
    """
    if path and path.endswith('.json'):
        path, filename = os.path.split(path)
    elif not path:
        app_name = app_name or get_module_name()
        path = click.get_app_dir(app_name, **app_dir_kwargs)
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
    """Select a Keyring backend name or object.

    Supported backend names:
        * OS_X
        * Windows
        * kwallet (requires dbus)
        * SecretService (requires SecretStorage)

    Also accepts any valid keyring.backend object.

    For additional information on Keyring backends see:
        https://github.com/jaraco/keyring
    """
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

    def __init__(self, type_=PLAIN, name=__name__, mode='rw',
                 keyring=True, service=None, **app_dir_kwargs):
        """
        :param type_: PLAIN, BOXED, FROZEN or NESTED

            * PLAIN: No type conversion.
                Feel free to use an JSON serializable object.

            * BOXED: Default Python-box object.

            * FROZEN

        :param name:

        :param mode:
            * None: Not using JSON configuration files ...
                Do not read or write to the JSON configuration file.
                Useful if you're using JsonConfig to only store
                secrets (passwords) and/or environment variables.
            * 'r': Read-only ...
                Load from config file, but don't write the changes back.
            * 'w': Write-only ...
                Don't load from config file, write the new data to it.
            * 'rw': Read-Write ...
                Load from JSON config file and write the changes back.

        :param keyring:
            * `True`: Use the recommended default keyring.
            * `False`: Not using passwords; Keyring services not needed.
            * `str` or `keyring.backend`:
                  Explicitly set a Keyring backend name or object.

        :param service:
            Simliar to how app_name is used, but for the keyring.

        :param **attrs:
            See click.get_app_dir for a list of available options.
        """
        if name == '__main__':
            raise ValueError('App Name is Required.')

        if mode and type_ is not None:
            self.type = type_
            self.filename = get_config_file(name, **app_dir_kwargs)
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
