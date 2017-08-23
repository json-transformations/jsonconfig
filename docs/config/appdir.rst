.. _`appdir`:

############################
Configuration File Locations
############################

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

    Win 7 (roaming):
    C:\Users\<user>\AppData\Roaming\Foo Bar

    Win 7 (not roaming):
    C:\Users\<user>\AppData\Local\Foo Bar

For additional information visit:
  .. _click's: http://github.com/pallets/click

===============
App Dir Options
===============

app_name (required)
    The ``app_name`` should be properly capitalized and can contain
    whitespace.  See file location patterns below.
    

roaming (default: True)
    Controls if the folder should be roaming or not on Windows; has no
    effect otherwise.
    
force_posix (default: False)
    If this is set to `True` then on any POSIX system the folder will be
    stored in the home folder with a leading dot instead of the XDG config
    home or darwin's application support folder.

====================================
The Three (3) File Location Patterns
====================================

app_name
  *app_name is a required argument*

  .. code::

    with Config('app_name') as data:
        cfg.data = 'Any JSON serializable object ...'

  *The default configuration filename is `config.json`*.

  .. rubric:: The destination would be:
    `{click.get_app_dir()}/app_name/config.json` 

app_name + cfg_name

  .. code::

    with Config('app_name', cfg_name='example.json') as data:
        cfg.data = 'Any JSON serializable object ...'

  **The destination would be**:

    `{click.get_app_dir()}/app_name/example.json`

app_name w/ path separator (i.e. an explicit filename)

  .. code::

    with Config('../example.json') as data:
        cfg.data = 'Any JSON serializable object ...'

  *The destination would literally be*:

    `../example.json`

===================
Missing Directories
===================

If any directories in the path are missing JsonConfig will automatically
attempt to create them.

=============
Missing Files
=============
If a configuration file is missing it will automatically create it.


**********
References
**********

.. target-notes::

.. _Click:
    http://click.pocoo.org/5/utils/
