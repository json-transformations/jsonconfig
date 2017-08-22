#########################################
Data Served in the Wrapper of Your Choice
#########################################

Box_ *is the package used to handle data access*.

PLAIN
    No wrapping.  Organic, free-ranging data.  If it's JSON serializable
    we'll work with it.  This is the default.

BOXED
    Delivers the data in a Box_; a Python dictionary that supports both
    recursive dot notation access and standard dictionary key access.

FROZEN
    Ices the data in a ``Frozen Box``, same as BOXED except immutable; will
    also be hashable if all objects in it are immutable.

NESTED
     Nests the data in a default dictionary that can automatically create
     missing intermediary keys. It's also very forgiving when retrieving
     data from the dictionary; for example, it won't throw an error if a key
     doesn't exist.  Instead, it'll return None; even if the key's nested
     and multiple keys are missing.



Data Conversion
---------------

* ``BOXED``, ``FROZEN`` and ``NESTED`` are all subclasses of dicts or
  defaultdicts.  You can convert back-and-forth between any of them at any
  time.

* You convert from ``BOXED``, ``FROZEN`` or ``NESTED`` to ``PLAIN`` at
  anytime.

* You can convert from ``PLAIN`` to ``BOXED``, ``FROZEN`` or ``NESTED`` only
  if the data is a Mapping.

* ``PLAIN`` is the only data type that supports non-Mapping objects.