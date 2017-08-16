import os
from copy import copy

import pytest

from jsonconfig.datawrap import Environ
from jsonconfig.errors import SetEnvironVarError, DeleteEnvironVarError


def test_environ_vars():
    with Environ('myapp') as cfg:
        cfg.env['SHUTUP'] = 'Oh shut up! And go change your armour!'

    assert os.environ['SHUTUP'] == 'Oh shut up! And go change your armour!'

    with Environ('myapp') as cfg:
        assert cfg.env['SHUTUP'] == 'Oh shut up! And go change your armour!'
        del cfg.env['SHUTUP']
        assert cfg.env['SHUTUP'] is None


def test_environ_attrs():
    with Environ('myapp') as cfg:
        cfg.env.FOOL = 'Next time I send a damn fool, I go myself.'

    with Environ('myapp') as cfg:
        assert cfg.env['FOOL'] == 'Next time I send a damn fool, I go myself.'
        del cfg.env['FOOL']
        assert cfg.env['FOOL'] is None


def test_environ_type_error():
    with pytest.raises(SetEnvironVarError):
        with Environ('myapp') as cfg:
            cfg.env[5] = None


def test_environ_key_error():
    with pytest.raises(DeleteEnvironVarError):
        with Environ('myapp') as cfg:
            del cfg.env['oops... what did you really expect to find in here?']


def test_environ_iter():
    with Environ('myapp') as cfg:
        assert tuple(iter(cfg.env)) == tuple(iter(os.environ))


def test_environ_len():
    with Environ('myapp') as cfg:
        assert len(cfg.env) == len(os.environ)


def test_environ_str():
    with Environ('myapp') as cfg:
        assert str(cfg.env) == str(os.environ)


def test_environ_repr():
    with Environ('myapp') as cfg:
        assert repr(cfg.env) == repr(os.environ)


def test_environ_contains():
    with Environ('myapp') as cfg:
        os.environ['__test__'] = 'banana spiders'
        assert '__test__' in cfg.env


def test_environ_eq():
    with Environ('myapp') as cfg:
        return cfg.env == os.environ


def test_environ_ne():
    with Environ('myapp') as cfg:
        return cfg.env != {}


def test_environ_copy():
    with Environ('myapp') as cfg:
        assert copy(cfg.env) == copy(os.environ)


def test_environ_items():
    with Environ('myapp') as cfg:
        assert cfg.env.items() == os.environ.items()


def test_environ_keys():
    with Environ('myapp') as cfg:
        assert cfg.env.keys() == os.environ.keys()


def test_environ_pop():
    with Environ('myapp') as cfg:
        cfg.env['__test_key__'] = 'OK'
        assert os.environ['__test_key__'] == 'OK'
        assert cfg.env.pop('__test_key__') == 'OK'
        assert '__test_key__' not in os.environ


def test_environ_popitem():
    with Environ('myapp') as cfg:
        key, value = cfg.env.popitem()
        assert key not in os.environ
        os.environ[key] = value


def test_environ_update():
    with Environ('myapp') as cfg:
        cfg.env.update({'__test_key1__': 'I', '__test_key2__': 'II'})
        assert os.environ['__test_key1__'] == 'I'
        assert os.environ['__test_key2__'] == 'II'
        del os.environ['__test_key1__']
        del os.environ['__test_key2__']


def test_environ_values():
    with Environ('myapp') as cfg:
        assert tuple(cfg.env.values()) == tuple(os.environ.values())


def test_environ_setdefault():
    with Environ('myapp') as cfg:
        cfg.env.setdefault('some key', 'a value')
        assert cfg.env.get('some key2', 'a value2') == 'a value2'
