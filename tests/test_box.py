import box
import pytest

from jsonconfig.datawrap import BoxConfig, FrozenBox, DefaultBox


def test_boxed_data():
    with BoxConfig('myapp', 'w', keyring=False) as cfg:
        cfg.data.widget = {}
        cfg.data.widget.window = {}
        cfg.data.widget.debug = True
        cfg.data.widget.window.title = 'Sample Konfabulator Widget'
        cfg.data.widget.window.width = 500

    with BoxConfig('myapp', 'r', keyring=False) as cfg:
        assert cfg.data.widget.debug is True
        assert cfg.data.widget.window.title == 'Sample Konfabulator Widget'
        assert cfg.data.widget.window.width == 500


def test_frozen_data():
    with FrozenBox('myapp', keyring=False) as cfg:
        cfg.debug = True

    with pytest.raises(box.BoxError):
        with FrozenBox('myapp', keyring=False) as cfg:
            cfg.data.debug = False
            assert cfg.data.debug is True


def test_nested_data():
    with DefaultBox('myapp', 'w', keyring=False) as cfg:
        cfg.data['widget']['debug'] = True
        cfg.data['widget']['window']['title'] = 'Sample Konfabulator Widget'
        cfg.data['widget']['window']['width'] = 800

    with DefaultBox('myapp', 'r', keyring=False) as cfg:
        assert cfg.data['widget']['debug'] is True
        title = cfg.data['widget']['window']['title']
        assert title == 'Sample Konfabulator Widget'
        assert cfg.data['widget']['window']['width'] == 800
