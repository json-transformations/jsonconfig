Welcome to JSON Config
======================

*Configuration doesn't get any easier than this ...*

What's it Used For?
-------------------
 
* Managing settings, configuration information, application data, etc.
 
* Managing secrets, tokens, keys, passwords, etc.
 
* Managing environment settings.

Basic Example
-------------

.. code::

    with Config('myapp') as cfg:
        cfg.data = 'Any JSON serializable object ...'
        cfg.pwd.a_secret = 'Encrypted data ...'
        cfg.env.a_variable = 'Environment variables.'

Additional Examples can be found in the documentation_.

Simply Sane
-----------
*No bad juju here* ...

.. topic:: In the context manager above:

    * The ``data`` is stored in the user's local application directory.
    * The ``pwd`` data is encrypted and stored in a keyring vault.
    * The ``env`` data is stored in environment variables.

Installation
------------

.. code::

    pip install jsonconfig

Configuration File Locations
----------------------------

Click_ *is the package used to determine the default application directory*.

The default behavior is to return whatever is most appropriate for the
operating system. To give you an idea, an app called ``Foo Bar`` would
likely return the following:

.. code-block:: text

    Mac OS X:
    ~/Library/Application Support/Foo Bar

    Mac OS X (POSIX):
    ~/.foo-bar

    Unix:
    ~/.config/foo-bar

    Unix (POSIX):
    ~/.foo-bar

    Win XP (roaming):
    C:\Documents and Settings\<user>\Local Settings\Application Data\Foo Bar

    Win XP (not roaming):
    C:\Documents and Settings\<user>\Application Data\Foo Bar

    Win 7+ (roaming):
    C:\Users\<user>\AppData\Roaming\Foo Bar

    Win 7+ (not roaming):
    C:\Users\<user>\AppData\Local\Foo Bar

Of course, you or the user are free to override this behavior and set the
location to wherever you want.

Encryption Backends
-------------------

Keyring_ *is the package used to manage encryption*.

The default behavior is to select the most secure backend supported by the
user's platform. To give you an idea, the following Keyring backends would
likely be returned:

Mac OS X:
    Keychain_

Unix (with secretstorage installed):
    `Secret Service`_

Unix (with dbus installed):
    kwallet_

Windows:
    `Windows Credential Locker`_

Of course, you or the user are free to override the defaults. The user can
also change their Keyring backend preferences system-wide from the
command-line or via configuration files.  JSON Config will then use the
user's preferred Keyring backend unless told otherwise.
  
How Do You Want Your Data Served?
---------------------------------

Box_ *is the package used to handle the data access wrappers*.

PLAIN
    No wrapping.  Organic, free-ranging data.  If it's JSON serializable
    we'll work with it.  This is the default.

BOXED
    Delivers your data in a Box_; a Python dictionary that supports both
    recursive dot notation access and standard dictionary key access. If
    you have a fear of being *boxed-in*, don't panic!  You can get in and
    out of the box at anytime, see the data conversion section below.

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

* The objects listed above are Mappings, if your data object is not
  a Mapping then use ``PLAIN`` to free yourself of all of the trappings.
  With ``PLAIN`` it's just you and your buddy Python; we get out of the way.

References
----------

.. target-notes::

.. _documentation:
    http://jsonconfig.readthedocs.io

.. _Click: http://github.com/pallets/click

.. _Keyring: https://github.com/jaraco/keyring

.. _Box: http://github.com/cdgriffith/Box

.. _Keychain: https://en.wikipedia.org/wiki/Keychain_%28software%29

.. _Secret Service: http://standards.freedesktop.org/secret-service

.. _kwallet: https://en.wikipedia.org/wiki/KWallet

.. _dbus: https://pypi.python.org/pypi/dbus-python

.. _Windows Credential Locker: https://technet.microsoft.com/en-us/library/jj554668.aspx

.. _3rd-party Keyring encryption backends: http://github.com/jaraco/keyrings.alt
