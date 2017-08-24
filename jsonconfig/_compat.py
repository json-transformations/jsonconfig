import getpass
import inspect
import os
import sys

VER = sys.version_info
PY2 = VER.major < 3
PY35_PLUS = VER.major > 2 and not (VER.major == 3 and VER.minor < 5)


def get_parameters(funct):
    return (inspect.getargspec(funct).args if PY2
            else inspect.signature(funct).parameters)


OPEN_PARAMS = ('file', 'mode', 'buffering', 'encoding', 'errors', 'newline')
OPEN_PARAMETERS = get_parameters(open) if PY35_PLUS else OPEN_PARAMS


def get_user(is_test=False):
    """Compatibility with tox & Windows.

    Work around for pwd import Error when running tox in Windows.
    """
    try:
        if is_test:
            raise ImportError
        return getpass.getuser()
    except ImportError:
        return os.getenv('username', '')
