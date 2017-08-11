import keyring

import pytest

from jsonconfig.datawrap import Keyring
from jsonconfig.errors import SetPasswordError, DeletePasswordError


def test_passwords():
    with Keyring('myapp') as cfg:
        cfg.pwd['some user'] = 'some password'

    password = keyring.get_password('myapp', 'some user')
    assert password == 'some password'

    with Keyring('myapp') as cfg:
        assert cfg.pwd['some user'] == 'some password'
        del cfg.pwd['some user']
        assert cfg.pwd['some user'] is None


def test_password_attrs():
    with Keyring('myapp') as cfg:
        cfg.pwd.somekey = 'a secret'

    with Keyring('myapp') as cfg:
        assert cfg.pwd.somekey == 'a secret'
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
