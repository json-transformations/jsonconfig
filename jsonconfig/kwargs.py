"""Keyword Argument Router.

The internal _group_kwargs_by_funct was split out to allow signature
injection.  This was necessary because:

    * PY2 can't inspect built-ins, in this case `open`.
    * `box.Box` returns a signature of Box(*args, **kwds); however,
      the parameters can be found in box.PARAMETERS.

"""
import inspect
from collections import namedtuple, Counter

from ._compat import get_parameters

EMPTY = frozenset()

Signature = namedtuple('Signature', ['name', 'args'])


def get_funct_parameters(funct):
    if inspect.isfunction(funct) or inspect.isbuiltin(funct):
        return Signature(funct.__name__, set(get_parameters(funct)))
    return Signature(funct.name, set(funct.args))


def group_kwargs_by_funct(kwargs, funct_args, bad_kwds=EMPTY, safe_kwds=EMPTY):
    """Fan keyword arguments out into their repective functions.

    :params kwargs: incomming arguments
    :params funct_args: a sequence of functions and/or arg/param lists
    :params bad_kwds: a sequence of disallowed keywords
    :params safe_kwds: a sequence of permitted keywords
    :returns: {funct-name: {key1:val1, key2:val2, ...}, ...}

    Keywords are derived by inpecting the function signatures.
    Keywords found in more than one function are not allowed.
    """
    kwds, bad_kwds, safe_kwds = map(set, (kwargs, bad_kwds, safe_kwds))
    funct_params = [get_funct_parameters(f) for f in funct_args]
    funct_kwds = [key for f in funct_params for key in f.args]
    dup_kwds = {i for i, count in Counter(funct_kwds).items() if count > 1}
    safe_kwds |= set(funct_kwds) - dup_kwds - bad_kwds
    unexpected_kwds = kwds - safe_kwds
    if unexpected_kwds:
        err_mesg = 'Type Error: Config got unexpected keyword arguments {!r}'
        raise TypeError(err_mesg.format(unexpected_kwds))
    kwds = [{k: v for k, v in kwargs.items() if k in (i.args & safe_kwds)}
            for i in funct_params]
    return dict(zip((f.name for f in funct_params), kwds))
