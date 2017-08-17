import inspect
import sys
from collections import namedtuple

PY2 = sys.version_info[0] == 2

def get_parameters(funct):
    if PY2:
        return inspect.getargspec(funct).args
    return inspect.signature(funct).parameters


if PY2:
    OPEN_PARAMETERS = ['name', 'mode', 'buffering']
else:
    OPEN_PARAMETERS = get_parameters(open)

