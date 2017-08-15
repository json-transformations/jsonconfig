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
