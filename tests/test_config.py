import pytest

from jsonconfig.core import Config
from jsonconfig.errors import JsonConfigError


def test_any_json_data():
    with Config('myapp') as cfg:
        cfg.data = [1, 2, 3]

    with Config('myapp') as cfg:
        assert cfg.data == [1, 2, 3]


def test_json_config_error():
    err = JsonConfigError('aliens with fleas; what type of collar to buy?')
    assert err.message == 'aliens with fleas; what type of collar to buy?'

    with pytest.raises(SystemExit):
        err.show()
