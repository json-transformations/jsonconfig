import json
import os.path

import box
import click
import keyring
from click.termui import hidden_prompt_func as get_passwd

from .dictutils import (EnvironAttrDict, KeyringAttrDict)
from .kwargs import box_, group_kwargs_by_funct
from .errors import (
    FileError, FileEncodeError,
    JsonEncodeError, JsonDecodeError,
    KeyringNameError, KeyringTypeError
)


def mkdirs(path):
    try:
        os.makedirs(path)
    except EnvironmentError as e:
        raise FileError(e)


def get_filename(app_name, cfg_name, **app_dir_kwargs):
    path, filename = os.path.split(app_name)
    if not path:
        path = click.get_app_dir(app_name, **app_dir_kwargs)
        filename = cfg_name
    if not os.path.exists(path):
        mkdirs(path)
    return os.path.join(path, filename)


def set_keyring(backend):
    """Select a Keyring backend name or object.

    Supported backend names: OS_X, WIndows, kwallet, and SecretService
    Also accepts any valid keyring.backend object.
    For additional information on Keyring backends see
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


def from_json(filename, **from_json_kwargs):
    try:
        return box._from_json(filename=filename, **from_json_kwargs)
    except FileNotFoundError as e:
        return {}
    except EnvironmentError as e:
        raise FileError(e)
    except json.JSONDecodeError as e:
        raise JsonDecodeError(e)


def to_json(data, filename, **to_json_kwargs):
    try:
        return box._to_json(data, filename=filename, **to_json_kwargs)
    except (TypeError, json.JSONDecodeError) as e:
        raise JsonEncodeError(e)
    except EnvironmentError as e:
        raise FileError(e)


class Config:

    cfg_name = 'config.json'
    functs = (open, click.get_app_dir, box_, json.load, json.dump)
    bad_kwds = {'fp'}
    safe_kwds = set()

    def __init__(self, app_name, mode='r+', *, cfg_name=None, box=None,
                 keyring=True, service_name=None, **kwargs):

        args = (kwargs, Config.functs, Config.bad_kwds, Config.safe_kwds)
        self.kwargs = group_kwargs_by_funct(*args)

        self.box = box
        mode = mode or ''
        frozen = kwargs.get('frozen_box')
        self.readable = 'r' in mode or mode.endswith('+') and not frozen
        self.writeable = 'w' in mode or mode.endswith('+')
        if self.readable or self.writeable:
            cfg_name = cfg_name or Config.cfg_name
            app_dir_kwargs = self.kwargs['get_app_dir']
            self.filename = get_filename(app_name, cfg_name, **app_dir_kwargs)

        self.keyring = keyring
        if keyring:
            KeyringAttrDict.service = service_name or app_name
            if keyring and keyring is not True:
                set_keyring(keyring)

    def __enter__(self):
        self.env = EnvironAttrDict(os.environ)

        if self.keyring:
            self.pwd = KeyringAttrDict()

        if self.readable or self.writeable:
            self.data = None
            if self.readable:
                json_kwargs = self.kwargs['open']
                json_kwargs.update(self.kwargs['load'])
                self.data = from_json(self.filename, **json_kwargs)
                if self.box:
                    self.data = self.box(self.data, **self.kwargs['box_'])
            else:
                self.data = self.box({}, **self.kwargs['box_'])
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.writeable:
            json_kwargs = self.kwargs['open']
            json_kwargs.update(self.kwargs['dump'])
            to_json(self.data, self.filename, **json_kwargs)
