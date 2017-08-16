import pytest

from jsonconfig.core import set_keyring
from jsonconfig.datawrap import Keyring
from jsonconfig.errors import (
    SetPasswordError, DeletePasswordError, KeyringNameError, KeyringTypeError
)

import keyring


def test_passwords():
    with Keyring('myapp') as cfg:
        cfg.pwd['some user'] = 'supercalifragilisticexpialidocious'

    password = keyring.get_password('myapp', 'some user')
    assert password == 'supercalifragilisticexpialidocious'

    with Keyring('myapp') as cfg:
        assert cfg.pwd['some user'] == 'supercalifragilisticexpialidocious'
        del cfg.pwd['some user']
        assert cfg.pwd['some user'] is None


def test_password_attrs():
    with Keyring('myapp') as cfg:
        cfg.pwd.somekey = 'open sesame'

    with Keyring('myapp') as cfg:
        assert cfg.pwd.somekey == 'open sesame'
        del cfg.pwd.somekey
        assert cfg.pwd.someuser is None


def test_set_password_error():
    with pytest.raises(SetPasswordError):
        with Keyring('myapp') as cfg:
            cfg.pwd[5] = None


def test_delete_password_error():
    with pytest.raises(DeletePasswordError):
        with Keyring('myapp') as cfg:
            del cfg.pwd[5]


def test_keyring_name_error():
    with pytest.raises(KeyringNameError):
        set_keyring('my precious')


def test_keyring_type_error():
    with pytest.raises(KeyringTypeError):
        set_keyring(b'test')


def test_set_keyring():
    set_keyring(keyring.get_keyring())


def test_set_keyring():
    with Keyring('myapp', keyring=keyring.get_keyring()) as cfg:
        assert keyring.get_keyring() is not None


def test_keyring_str():
    with Keyring('myapp') as cfg:
        assert str(cfg.pwd) == keyring.get_keyring().name


def test_keyring_repr():
    with Keyring('myapp') as cfg:
        assert repr(cfg.pwd) == repr(keyring.backend)


def test_keyring_pop():
    with Keyring('myapp') as cfg:
        cfg.pwd['__test__'] = '123'
        assert cfg.pwd.pop('__test__') == '123'
        assert cfg.pwd['__test__'] is None


def test_keyring_update():
    with Keyring('myapp') as cfg:
        d = {'__test1__': '123', '__test2__': '456'}
        cfg.pwd.update(d)
        assert cfg.pwd.pop('__test1__') == '123'
        assert cfg.pwd.pop('__test2__') == '456'
