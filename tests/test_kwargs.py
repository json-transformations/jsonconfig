import json

import box
import click
import pytest

from jsonconfig._compat import OPEN_PARAMETERS
from jsonconfig.kwargs import group_kwargs_by_funct, Signature


FUNCTS = (
    Signature('open', OPEN_PARAMETERS),
    Signature('box', box.BOX_PARAMETERS),
    click.get_app_dir,
    json.load,
    json.dump
)


def test_kwarg_splitter():
    kwargs = {'frozen_box': True, 'indent': 2}
    result = group_kwargs_by_funct(kwargs, FUNCTS)
    expect = {'open': {}, 'box': {'frozen_box': True},
              'get_app_dir': {}, 'load': {}, 'dump': {'indent': 2}}
    assert result == expect


def test_kwarg_splitter_dup_kwd_error():
    with pytest.raises(TypeError):
        group_kwargs_by_funct({'cls': None}, FUNCTS)


def test_kwarg_splitter_bad_kwd_error():
    with pytest.raises(TypeError):
        group_kwargs_by_funct({'fp': None}, FUNCTS, ('fp',))
