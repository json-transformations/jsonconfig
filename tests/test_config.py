import os

import box
import keyring
import pytest

from jsonconfig.core import JsonConfig, BOXED, FROZEN, NESTED


def test_boxed_data():
    with JsonConfig(BOXED, mode='w', keyring=None) as cfg:
        cfg.data.widget = {}
        cfg.data.widget.window = {}
        cfg.data.widget.debug = True
        cfg.data.widget.window.title = 'Sample Konfabulator Widget'
        cfg.data.widget.window.width = 500

    with JsonConfig(BOXED, mode='r', keyring=None) as cfg:
        assert cfg.data.widget.debug is True
        assert cfg.data.widget.window.title == 'Sample Konfabulator Widget'
        assert cfg.data.widget.window.width == 500


def test_frozen_data():
    with JsonConfig(keyring=False) as cfg:
        cfg.debug = True

    with pytest.raises(box.BoxError):
        with JsonConfig(FROZEN, keyring=None) as cfg:
            cfg.data.debug = False
            assert cfg.data.debug is True


def test_nested_data():
    with JsonConfig(NESTED, mode='w', keyring=None) as cfg:
        cfg.data['widget']['debug'] = True
        cfg.data['widget']['window']['title'] = 'Sample Konfabulator Widget'
        cfg.data['widget']['window']['width'] = 800

    with JsonConfig(mode='r', keyring=None) as cfg:
        assert cfg.data['widget']['debug'] is True
        title = cfg.data['widget']['window']['title']
        assert title == 'Sample Konfabulator Widget'
        assert cfg.data['widget']['window']['width'] == 800


def test_any_json_data():
    with JsonConfig() as cfg:
        cfg.data = [1, 2, 3]

    with JsonConfig() as cfg:
        assert cfg.data == [1, 2, 3]


def test_environ_vars():
    with JsonConfig(mode=None, keyring=None) as cfg:
        cfg.env['TESTING'] = 'some value'

    assert os.environ['TESTING'] == 'some value'

    with JsonConfig(mode=None, keyring=None) as cfg:
        assert cfg.env['TESTING'] == 'some value'
        del cfg.env['TESTING']
        assert cfg.env['TESTING'] is None


def test_environ_attrs():
    with JsonConfig(mode=None, keyring=None) as cfg:
        cfg.env.TESTIT = 'some value'

    with JsonConfig(mode=None, keyring=None) as cfg:
        assert cfg.env['TESTIT'] == 'some value'
        del cfg.env['TESTIT']
        assert cfg.env['TESTIT'] is None


def test_passwords():
    with JsonConfig(mode=None) as cfg:
        cfg.pwd['some user'] = 'some password'

    password = keyring.get_password('jsonconfig.core', 'some user')
    assert password == 'some password'

    with JsonConfig(mode=None) as cfg:
        assert cfg.pwd['some user'] == 'some password'
        del cfg.pwd['some user']
        assert cfg.pwd['some user'] is None


def test_password_attrs():
    with JsonConfig(mode=None) as cfg:
        cfg.pwd.somekey = 'a secret'

    with JsonConfig(mode=None) as cfg:
        assert cfg.pwd.somekey == 'a secret'
        del cfg.pwd.somekey
        assert cfg.pwd.someuser is None

