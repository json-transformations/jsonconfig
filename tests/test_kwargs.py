import json

import pytest

from jsonconfig.kwargs import group_kwargs_by_funct


FUNCTS = (open, json.load, json.dump)


def test_kwarg_splitter():
    kwargs = {'encoding': 'utf-8', 'indent': 2}
    result = group_kwargs_by_funct(kwargs, FUNCTS)
    expect = {'open': {'encoding': 'utf-8'}, 'load': {}, 'dump': {'indent': 2}}
    assert result == expect


def test_kwarg_splitter_dup_kwd_error():
    with pytest.raises(TypeError):
        group_kwargs_by_funct({'cls': None}, FUNCTS)


def test_kwarg_splitter_bad_kwd_error():
    with pytest.raises(TypeError):
        group_kwargs_by_funct({'fp': None}, FUNCTS, ('fp',))
