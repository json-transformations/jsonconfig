import json
import os.path

import box
import click

from ._compat import OPEN_PARAMETERS
from .appdirs import get_filename
from .environs import EnvironAttrDict
from .jsonutils import to_json_file, from_json_file
from .keyrings import set_keyring, KeyringAttrDict
from .kwargs import group_kwargs_by_funct, Signature


class Config:

    cfg_name = 'config.json'
    funct_args = (Signature('open', OPEN_PARAMETERS), click.get_app_dir,
                  Signature('box', box.BOX_PARAMETERS), json.load, json.dump)
    bad_kwds = {'fp', 'name'}
    safe_kwds = set()

    def __init__(self, app_name, mode='r+', cfg_name=None, box=None,
                 keyring=True, service_name=None, **kwargs):

        args = (kwargs, Config.funct_args, Config.bad_kwds, Config.safe_kwds)
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
                self.data = from_json_file(self.filename, **json_kwargs)
                if self.box:
                    self.data = self.box(self.data, **self.kwargs['box'])
            else:
                self.data = self.box({}, **self.kwargs['box'])
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.writeable:
            json_kwargs = self.kwargs['open']
            json_kwargs.update(self.kwargs['dump'])
            to_json_file(self.data, self.filename, **json_kwargs)
