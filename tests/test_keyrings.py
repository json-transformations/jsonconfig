import os

import keyring
import pytest

from jsonconfig._compat import get_user
from jsonconfig.pwd import KeyringAttrDict
from jsonconfig.shortcuts import Keyring
from jsonconfig.errors import (
    SetPasswordError, DeletePasswordError, KeyringNameError
)

SERVICE_NAME = 'myservice'


class TestKeyring(keyring.backend.KeyringBackend):

    priority = 1
    vault = {SERVICE_NAME: {}}

    def set_password(self, servicename, username, password):
        if not isinstance(password, (str, bytes)):
            raise ValueError()
        if servicename not in TestKeyring.vault:
            TestKeyring.vault[servicename] = {}
        TestKeyring.vault[servicename][username] = password

    def get_password(self, servicename, username):
        if servicename in TestKeyring.vault:
            return TestKeyring.vault[servicename].get(username)

    def delete_password(self, servicename, username):
        del TestKeyring.vault[servicename][username]


test_keyring = TestKeyring()
KeyringAttrDict.keyring = keyring


def test_passwords():
    with Keyring('', service_name=SERVICE_NAME, keyring=test_keyring) as cfg:
        cfg.pwd['some user'] = 'supercalifragilisticexpialidocious'

    with Keyring('', service_name=SERVICE_NAME, keyring=test_keyring) as cfg:
        assert cfg.pwd['some user'] == 'supercalifragilisticexpialidocious'
        del cfg.pwd['some user']
        assert cfg.pwd['some user'] is None
        assert cfg.pwd.get('some user', 'some value') == 'some value'


def test_password_attrs():
    with Keyring('', service_name=SERVICE_NAME, keyring=test_keyring) as cfg:
        cfg.pwd.somekey = 'open sesame'

    with Keyring('', service_name=SERVICE_NAME, keyring=test_keyring) as cfg:
        assert cfg.pwd.somekey == 'open sesame'
        del cfg.pwd.somekey
        assert cfg.pwd.someuser is None


def test_set_password_error():
    with pytest.raises(SetPasswordError):
        with Keyring('', service_name=SERVICE_NAME,
                     keyring=test_keyring) as cfg:
            cfg.pwd[5] = None


def test_delete_password_error():
    with pytest.raises(DeletePasswordError):
        with Keyring('', service_name=SERVICE_NAME,
                     keyring=test_keyring) as cfg:
            del cfg.pwd[5]


def test_keyring_name_error():
    with pytest.raises(KeyringNameError):
        KeyringAttrDict.set_keyring('my precious')


def test_get_keyring():
    result = KeyringAttrDict.get_keyring()
    assert result == test_keyring


def test_get_keyrings():
    result = KeyringAttrDict.get_keyrings()
    expect = keyring.backend.get_all_keyring()
    assert type(result) == type(expect)


def test_keyring_str():
    with Keyring('') as cfg:
        result = str(cfg.pwd)
        assert result == KeyringAttrDict.get_keyring().name


def test_keyring_repr():
    with Keyring('') as cfg:
        result = repr(cfg.pwd)
        assert result == repr(test_keyring)


def test_keyring_pop():
    with Keyring('', service_name=SERVICE_NAME,
                 keyring=test_keyring) as cfg:
        cfg.pwd['__test__'] = '123'
        assert cfg.pwd.pop('__test__') == '123'
        assert cfg.pwd['__test__'] is None


def test_keyring_update():
    with Keyring('', service_name=SERVICE_NAME,
                 keyring=test_keyring) as cfg:
        d = {'__test1__': '123', '__test2__': '456'}
        cfg.pwd.update(d)
        assert cfg.pwd.pop('__test1__') == '123'
        assert cfg.pwd.pop('__test2__') == '456'


def test_getuser_import_error():
    result = get_user(is_test=True)
    assert result == os.getenv('username', '')
