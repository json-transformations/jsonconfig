.. _`pwd`:

#############
Encryped Data
#############

Keyring_ *is the package used to manage encryption*.

To save a secret ...

.. code::

    from jsonconfig import Config

    with Config('myapp') as cfg:
        cfg.pwd.some_user = 'some value'

To retrieve the secret ...

.. code::

    with Config('myapp') as cfg:
        password = cfg.pwd.some_user

================
Default Behavior
================

The default behavior is to select the most secure backend supported
by the user's platform. To give you an idea, the following Keyring
backends would likely be returned:

Mac OS X:
    Keychain_

Unix (with secretstorage installed):
    Freedesktop `Secret Service`_

Unix (with dbus installed):
    kwallet_

Windows:
    `Windows Credential Locker`_

===========================
How-to Set the Service Name
===========================

You can think of the service name as the folder where Keyring stores the
key/value pair.  By default the service name is set the current logged in
`username + '_' + app_name`.  You can override this behavior by explicitly
setting the `service_name` in the context manager.

.. code::

    with Config('my_app_name', service_name='my_service_name') as cfg:
        cfg.pwd.secret = 'Open Seasame!'

==================================
Enabling and Disabling the Keyring
==================================

The `keyring` keyword argument controls this.

True
    This is the default.  Enable Keyring and use the default backend.

False
    Disable the Keyring.  The Keyring will not be initalized and the `pwd`
    attribute will not be available.

    .. code::

        with Config('myapp', keyring=False) as cfg:
            cfg.data = 'Some value'

KeyringConfig
    This shortcut will enable Keyring and disable data configurations.  The
    `data` attributed will not be available.

    from jsonconfig import Keyring

    with Keyring('myapp') as vault:
        vault.pwd.key1 = 'a secret'
        vault.pwd.key2 = 'another secret'

====================================
Manually Setting the Keyring Backend
====================================

Of course, you or the user are free to override the defaults.  The user can
also change their Keyring backend preferences system-wide from the
command-line or via configuration files.  JSON Config will then use the
user's preferred Keyring backend unless told otherwise.

From the Command Line
---------------------

.. code::

    $ keyring set system username
    <enter hidden password for 'username' in 'system'>

    $ keyring get system username
    password

From inside JSON Config
-----------------------

keyring.backends
    The keyring option accepts a `keyring.backends` class.

    .. code::

        import keyring.backends

        from jsonconfig import Config

        backend = keyring.backends.Windows.WinVaultKeyring
        with Config('myapp', keyring=backend) as cfg:
            cfg.pwd.some_key = 'a secret'

Keyring Backend Name
    The keyring option accepts a keyring backend name.

    .. code::

        import keyring.backends

        from jsonconfig import Config

        with Config('myapp', keyring='WinVaultKeyring') as cfg:
            cfg.pwd.some_key = 'a secret'

    **Valid Keyring names are**:
        * OS_X
        * WIndows
        * kwallet
        * SecretService

============
How it Works
============

Keyring describes setting a password as follows:
`set_password(service, username, password)`.  `Username` and `password` do
not have to contain user names and password, they are not special; JSON
Config treats `username` and `password` as `key` and `value`. 

When you set a `pwd` key to a value it calls
`set_password(service_name, key, value)`.

When you get a value from a `pwd` key it calls
`get_password(service_name, key)`.

==========
References
==========

.. target-notes::

.. _Keyring: https://github.com/jaraco/keyring

.. _Keychain: https://en.wikipedia.org/wiki/Keychain_%28software%29

.. _Secret Service: http://standards.freedesktop.org/secret-service

.. _kwallet: https://en.wikipedia.org/wiki/KWallet

.. _dbus: https://pypi.python.org/pypi/dbus-python

.. _Windows Credential Locker: https://technet.microsoft.com/en-us/library/jj554668.aspx