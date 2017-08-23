.. _`env`:

#####################
Environment Variables
#####################

*JSON Config provides both dictionary-key and attribute-style access to
environment variables via* `os.environ`_.

.. code::

    from jsonconfig import Environ

    with Environ('myapp') as cfg:
        cfg.env.a_variable = 'some value'

Environ is a shortcut to Config(mode=None, keyring=False).  When mode is
None it disables reading & writing to the configuration file and the
``data`` attribute is not available.  When keyring is False it bypasses the
Keyring service and the ``pwd`` attribute is not available.

.. note::

    The app_name for Environ is a required argument, but it doesn't doesn't
    do anything.

=======================================
Attribute & Dictionary Key Style Access
=======================================

*Nested keys are not permitted with environment variables*.

Environment variables are accessible through dict style keys and attribute-
style notation.  When you assign a value to a attribute or a key it will
update the environment variable in real-time.

When getting a value if a key is not found it will return ``None``.

.. code::

    with Environ('myapp') as cfg:
        var = cfg.env.a_variable

-- or --

.. code::

    with Environ('myapp') as cfg:
        var = cfg.env['a_variable']

The `env` attribute has most of the attributes and methods associated with
dictionaries.  For example:

.. code::

    with Environ('myapp') as cfg:
        print(cfg.env.keys())

=======================
Getpass Helper Function
=======================

There is a helper function called ``getpass()`` that will allow you to
prompt the user for a passowrd.

For example to prompt for a password in an environment variable is not
set ...

.. code::

    with Environ('myapp') as cfg:
        password = cfg.env.mypassword or getpass

Or to check the keyring vault first, if it's not set there then check
the environment variables, if it is not set there then prompt for
a password.


.. code::

    with Config('myapp', mode=None) as cfg:
        password = cfg.pwd.mypassword or cfg.env.mypassword or getpass

You can also set it if it's not set:

.. code::

    with Config('myapp', mode=None) as cfg:
        cfg.env.mypassword = cfg.pwd.mypassword or cfg.env.mypassword or getpass

=====================
JSON Helper Functions
=====================

It's not usually used with environment variables, but it is possible to
store JSON serialized objects in environment variables.

.. code::

    with Environ('myapp', mode=None) as cfg:
        cfg.env.settings = to_json({'debug': True, 'width': 80})

To retrieve it ...

.. code::

    with Environ('myapp', mode=None) as cfg:
        settings = from_json(cfg.env.settings)



.. _`os.environ`:
    https://docs.python.org/3/library/os.html#os.environment