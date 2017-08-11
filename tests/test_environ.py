import os

from jsonconfig.datawrap import Environ


def test_environ_vars():
    with Environ('myapp') as cfg:
        cfg.env['TESTING'] = 'some value'

    assert os.environ['TESTING'] == 'some value'

    with Environ('myapp') as cfg:
        assert cfg.env['TESTING'] == 'some value'
        del cfg.env['TESTING']
        assert cfg.env['TESTING'] is None


def test_environ_attrs():
    with Environ('myapp') as cfg:
        cfg.env.TESTIT = 'some value'

    with Environ('myapp') as cfg:
        assert cfg.env['TESTIT'] == 'some value'
        del cfg.env['TESTIT']
        assert cfg.env['TESTIT'] is None
