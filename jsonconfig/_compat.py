import inspect
import sys

VER = sys.version_info
PY2 = VER.major < 3
PY35_PLUS = VER.major > 2 and not (VER.major == 3 and VER.minor < 5)


def get_parameters(funct):
    return (inspect.getargspec(funct).args if PY2
            else inspect.signature(funct).parameters)


OPEN_PARAMETERS = (
    'file', 'mode', 'buffering', 'encoding', 'errors', 'newline'
)
OPEN_PARAMETERS = get_parameters(open) if PY35_PLUS else OPEN_PARAMETERS
