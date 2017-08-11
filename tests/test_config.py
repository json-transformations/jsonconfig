import os
from tempfile import NamedTemporaryFile

import pytest

from jsonconfig.core import get_filename, from_json, Config
from jsonconfig.errors import FileError, JsonConfigError, JsonDecodeError


def test_any_json_data():
    with Config('myapp') as cfg:
        cfg.data = [1, 2, 3]

    with Config('myapp') as cfg:
        assert cfg.data == [1, 2, 3]


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


def test_config_file_make_dirs():
    get_filename('./__test1/__test2/config.json', None)
    assert os.path.isdir('./__test1/__test2') is True
    os.removedirs('./__test1/__test2')


def test_json_config_error():
    err = JsonConfigError('aliens with fleas; what type of collar to buy?')
    assert err.message == 'aliens with fleas; what type of collar to buy?'

    with pytest.raises(SystemExit):
        err.show()


def test_from_json_file_not_found():
    assert from_json('there aint no file here') == {}


def test_from_json_environ_error():
    with pytest.raises(FileError):
        from_json('whaaz u looking at?') == {}


def test_from_json_decode_error():
    tf = NamedTemporaryFile(delete=False)
    tf.write(b'#$@&%*!')
    tf.close()
    with pytest.raises(JsonDecodeError):
        from_json(tf.name)
    os.unlink(tf.name)
