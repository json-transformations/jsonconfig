.. topic:: JSONConfig parameters

.. topic:: Configuration data:

  Packaged data types:

   None
     The data can be any JSON serializable object.

   BOXED
      A Python dictionary with recursive dot notation access.

      Box is simply a subclass of dict which overrides some base
      functionality to make sure everything stored in the dict can be
      accessed as an attribute or key value.

      It slugify's key names to allow attribute access to any key:

      1. Converts to a string using UTF-8 encoding with errors ignored.
      2. Replaces spaces with underscores.
      3. Removes anything other than ascii letters, numbers and underscores.
      4. If the first character is a digit then prepend with 'x'.
      5. If string is a built-in that can't be used then prepend with 'x'.
      6. Removes duplicate underscores.

      Note: It does not check for duplicate keys when slugifying.
      For more information see https://github.com/cdgriffith/Box.

  FROZEN
     Same as BOXED except that the box will be immutable.  It will also be
     hashable if all of the objects in it are also non-mutable. For more
     information see https://github.com/cdgriffith/Box.

     Frozen also bypasses writing data back to the configuration file when
     exiting the context manager.

  NESTED
     A dictionary that when assigning key values automatically creates
     missing keys, even when they are nested.

     If a key doesn't exist it will return None, even if it's nested and
     multiple keys are missing.

     For more information see https://stackoverflow.com/questions/16724788.

.. topic:: Application Directory Settings::

   For additional information see 
   http://click.pocoo.org/5/utils/#finding-application-folders.

   name
      The application name. This should be properly capitalized and can
      contain whitespace.
    
   roaming
      Controls if the folder should be roaming or not on Windows. Has no
      affect otherwise.
    
   force_posix
      If this is set to `True` then on any POSIX system the folder will be
      stored in the home folder with a leading dot instead of the XDG config
      home or darwin's application support folder.

   path
      Manually overides the application directory setting.

   filename
      The name of the configuration file.

.. topic:: Keyring Settings::
  
   service
      An optional name of the location within the keyring to store the
      key/value. By default it's set to the `name`.

    keyring
      An optional keyring backend name or KeyringBackend object. The default
      is to use the current backend set in the Keyring configuration file
      if one exists or select the most appropriate keyring backend for your
      platform. Valid backend names are os_x, kwallet, secretservice and
      windows.


      backend.KeyringBackend

      Mac OS X Keychain
      Freedesktop Secret Service (requires secretstorage)
      KWallet (requires dbus)
      Windows Credential Locker
      Other keyring implementations are provided in the keyrings.alt package.

appname=__name__, roaming=True, force_posix=False,
                 path=None, filename='config.json', readonly=False,
                 encoding='utf-8', errors=None, newline=None,
                 keyring_service=None, keyring_backend=None

.. topic:: JSONConfig uses Box objects for configuration data:

  Python dictionaries with recursive dot notation access.

  Box is simply a subclass of dict which overrides some base functionality
  to make sure everything stored in the dict can be accessed as an attribute
  or key value.


.. topic:: JSONConfig uses click's get_app_dir function

  Returns the config folder for the application.  The default behavior
  is to return whatever is most appropriate for the operating system.

  To give you an idea, for an app called ``"Foo Bar"``, something like
  the following folders could be returned:

  Mac OS X:
    ``~/Library/Application Support/Foo Bar``
  Mac OS X (POSIX):
    ``~/.foo-bar``
  Unix:
    ``~/.config/foo-bar``
  Unix (POSIX):
    ``~/.foo-bar``
  Win XP (roaming):
    ``C:\Documents and Settings\<user>\Local Settings\Application Data\Foo Bar``
  Win XP (not roaming):
    ``C:\Documents and Settings\<user>\Application Data\Foo Bar``
  Win 7 (roaming):
    ``C:\Users\<user>\AppData\Roaming\Foo Bar``
  Win 7 (not roaming):
    ``C:\Users\<user>\AppData\Local\Foo Bar``

.. topic:: JSONConfig uses Python's `os.enivron` method for environment variables

  Allows attribute style notation.

.. topic:: Keyring

   It also adds attribute access for keys that could not normally be
   attributes:


   The Python keyring lib provides a easy way to access the system keyring service from python. It can be used in any application that needs safe password storage.

The keyring library is licensed under both the MIT license and the PSF license.

These recommended keyring backends are supported by the Python keyring lib:

Mac OS X:
  Keychain
Unix (with dbus installed)
  Freedesktop Secret Service
Unix (with secretstorage installed)
  Windows Credential Locker

Other keyring implementations are provided in the keyrings.alt package.
