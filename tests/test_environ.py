import os

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
