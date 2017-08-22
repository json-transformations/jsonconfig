"""Data Access Wrapper."""
from functools import partial

from box import Box

from .core import Config

PLAIN = dict
BOXED = Box
FROZEN = partial(Box, frozen_box=True)
NESTED = partial(Box, default_box=True)

BoxConfig = partial(Config, box=Box)
FrozenBox = partial(Config, box=Box, frozen_box=True)
DefaultBox = partial(Config, box=Box, default_box=True)

Keyring = partial(Config, mode=None)
Environ = partial(Config, mode=None, keyring=False)
