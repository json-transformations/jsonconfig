from .errors import FileError

import os

import click


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
