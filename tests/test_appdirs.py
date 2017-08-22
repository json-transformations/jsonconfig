import os
import shutil
import tempfile

import pytest

from jsonconfig.appdir import get_filename, mkdirs
from jsonconfig.core import Config
from jsonconfig.errors import FileError


def test_mkdirs():
    with pytest.raises(FileError):
        dirpath = tempfile.mkdtemp()
        mkdirs(dirpath)
        shutil.rmtree(dirpath)


def test_config_file_make_dirs():
    get_filename('./__test1/__test2/config.json', None)
    assert os.path.isdir('./__test1/__test2') is True
    os.removedirs('./__test1/__test2')


def test_get_filename():
    path = get_filename('myapp', Config.cfg_name)
    path, filename = os.path.split(path)
    path, app_name = os.path.split(path)
    assert app_name == 'myapp'
    assert filename == Config.cfg_name

    result = get_filename('/test/config.json', None)
    path, filename = os.path.split(result)
    assert path == '/test'
    assert filename == 'config.json'
