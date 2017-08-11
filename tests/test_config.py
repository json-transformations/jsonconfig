import os

from jsonconfig.core import get_filename, Config


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
