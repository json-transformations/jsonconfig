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

    with JsonConfig() as cfg:
        cfg.data = 'Any JSON serializable object ...'
        cfg.pwd.a_secret = 'Encrypted data ...'
        cfg.env.a_variable = 'Environment variables.'

.. topic:: In the context manager above:

    * The ``data`` is stored in the user's local application directory.
    * The ``pwd`` data is encrypted and stored in a keyring vault.
    * The ``env`` data is stored in environment variables.

Installation
------------

.. code::

    pip install jsonconfig
