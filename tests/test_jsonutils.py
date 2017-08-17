import os

import pytest

from jsonconfig.errors import FileError, JsonDecodeError
from jsonconfig.jsonutils import (
    from_json_file, to_json_file, from_json, to_json
)


def test_from_json_file_not_found():
    assert from_json_file('there aint no file here') == {}


def test_from_json_file_decode_error(tmpdir):
    p = tmpdir.mkdir("drat").join("doubledrat.json")
    p.write(b'#$@&%*!')
    with pytest.raises(JsonDecodeError):
        from_json_file(os.path.join(p.dirname, p.basename))


def test_to_json_file_error():
    with pytest.raises(FileError):
        to_json_file(None, '#$@&%*!')


def test_from_json_decode_error():
    with pytest.raises(JsonDecodeError):
        from_json(b'#$@&%*!')


def test_from_json_decode():
    data = '{"Flying Colors": "Everything Changes"}'
    result = from_json(data)
    assert result == {'Flying Colors': 'Everything Changes'}


def test_to_json():
    data = {'Flying Colors': 'Everything Changes'}
    result = to_json(data)
    assert result == '{"Flying Colors": "Everything Changes"}'
