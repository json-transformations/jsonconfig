import inspect
import sys

VER = sys.version_info
PY2 = VER.major < 3
PY35_PLUS = VER.major > 2 and not (VER.major == 3 and VER.minor < 5)


def get_parameters(funct):
    if PY2:
        return inspect.getargspec(funct).args
    return inspect.signature(funct).parameters


if PY35_PLUS:
    OPEN_PARAMETERS = get_parameters(open)
else:
    OPEN_PARAMETERS = ['name', 'mode', 'buffering']
