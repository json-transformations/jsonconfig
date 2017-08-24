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
    cfgdir = os.path.join(tmpdir, './test1/test2/config.json')
    get_filename(os.path.join(cfgdir, 'config.json'), None)
    assert os.path.isdir(cfgdir) is True


def test_get_filename(tmpdir):
    path = get_filename('myapp', Config.cfg_name)
    path, filename = os.path.split(path)
    path, app_name = os.path.split(path)
    assert app_name == 'myapp'
    assert filename == Config.cfg_name

    f = 'config.json'
    d = tmpdir.mkdir('test')
    result = get_filename(d.join(f), None)
    path, filename = os.path.split(result)
    assert path == d
    assert filename == f
