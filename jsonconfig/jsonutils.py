from .errors import FileError, JsonDecodeError

import box


def from_json_file(filename, **from_json_kwargs):
    try:
        return box._from_json(filename=filename, **from_json_kwargs)
    except EnvironmentError:
        return {}
    except ValueError as e:
        raise JsonDecodeError(e)


def to_json_file(data, filename, **to_json_kwargs):
    try:
        return box._to_json(data, filename=filename, **to_json_kwargs)
    except EnvironmentError as e:
        raise FileError(e)


def from_json(data, **from_json_kwargs):
    try:
        return box._from_json(data, **from_json_kwargs)
    except (ValueError, TypeError) as e:
        raise JsonDecodeError(e)


to_json = box._to_json
