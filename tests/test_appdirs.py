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


def test_config_file_make_dirs(tmpdir):
    d = tmpdir.mkdir('test')
    p = d.join('config.json')
    get_filename(str(p), None)
    result = os.path.isdir(str(d))
    assert result is True


def test_get_filename():
    path = get_filename('myapp', Config.cfg_name)
    path, filename = os.path.split(path)
    path, app_name = os.path.split(path)
    assert app_name == 'myapp'
    assert filename == Config.cfg_name


def test_get_explicit_filename(tmpdir):
    f = 'config.json'
    d = tmpdir.mkdir('test')
    p = d.join(f)
    result = get_filename(str(d.join(f)), None)
    path, filename = os.path.split(result)
    assert path == str(d)
    assert filename == str(f)
