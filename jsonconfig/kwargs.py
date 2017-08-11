"""Keyword Argument Router."""
from collections import Counter
from inspect import signature

EMPTY = frozenset()


def box_(
        default_box, default_box_attr, conversion_box, frozen_box,
        camel_killer_box, box_it_up
    ):
    """Inspection doesn't work on Box, so use this signature."""


def group_kwargs_by_funct(kwargs, functs, bad_kwds=EMPTY, safe_kwds=EMPTY):
    """Fan keyword arguments out into their repective functions.

    :params kwargs: incomming arguments
    :params functs: a sequence of functions
    :params bad_kwds: a sequence of disallowed keywords
    :params safe_kwds: a sequence of (name, keywords) tuples
    :returns: {funct-name: {key1:val1, key2:val2, ...}, ...}

    Keywords are derived by inpecting the function signatures.
    Keywords found in more than one function are not allowed.
    """
    kwds, bad_kwds, safe_kwds = map(set, (kwargs, bad_kwds, safe_kwds))
    funct_kwargs = [signature(f).parameters for f in functs]
    funct_kwds = [key for f in funct_kwargs for key in f]
    dup_kwds = {i for i, count in Counter(funct_kwds).items() if count > 1}
    safe_kwds |= set(funct_kwds) - dup_kwds - bad_kwds
    unexpected_kwds =  kwds - safe_kwds
    if unexpected_kwds:
        err_mesg = 'Type Error: Config got unexpected keyword arguments {!r}'
        raise TypeError(err_mesg.format(unexpected_kwds))
    kwds = [{k: v for k, v in kwargs.items() if k in i} for i in funct_kwargs]
    return dict(zip((f.__name__ for f in functs), kwds))
