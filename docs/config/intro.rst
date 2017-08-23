######################
Welcome to JSON Config
######################

*Configuration doesn't get any easier than this ...*

===================
What's it Used For?
===================

 * Managing settings, configuration information, application data, etc.
 * Managing secrets, tokens, keys, passwords, etc.
 * Managing environment settings.

=============
Basic Example
=============

.. code::

    with Config('myapp') as cfg:
        cfg.data = 'Any JSON serializable object ...'
        cfg.pwd.a_secret = 'Encrypted data ...'
        cfg.env.a_variable = 'Environment variables.'

.. topic:: In the context manager above:

    * The ``data`` is stored in the user's local :ref:`application directory <appdir>`.
    * The ``pwd`` data is encrypted and stored in a :ref:`keyring vault <pwd>`.
    * The ``env`` data is stored in :ref:`environment variables <env>`.

===========
Easy Access
===========

With Python-Box_ as a data access wrapper you can reference Mapping data as
either dictionary-keys or attribute-style notation.  For example,

.. code::

    with BoxConfig('myapp') as cfg:
        cfg.data.key1 = 'Some configuration data ...'
        cfg.data.key2 = 'Some more data ...'

============
Installation
============

.. code::

    pip install jsonconfig

===============================
Designed with Stability in Mind
===============================

* JSON Config is just a pass-through to mature, stable 3rd party packages,
  and built-in Python modules: Click_, Keyring_, Python-Box_, open, json.load,
  json.dump, and os.environ.

* JSON Config takes extra care to stay out of your way as a Python
  programmer, it does NOT introduce magic.  And any keyword arguments that you
  would normally be able to pass to the above functions are still available
  through the context manager.

* You could import each of the above packages independently rather than
  using JSON Config but then you'd be responsible for writing a lot more
  code, tracking what all needs to be imported, writing a lot more tests,
  and dealing with error handling from different sources. The more custom
  code you write, the greater the chance of introducing bugs.

=========================================================
Consistency across Multiple Sources of Configuration Data
=========================================================

* JSON Config aims to create consistency across different types of
  configuration data.  For example, bringing both dictionary key and
  attribute-style access to data, encrypted data, and environment
  variables.

* JSON Config provides consistent error handling around the entire
  configuration process; this allows you to employ sane exception
  management and logging at the granularity-level most suitable to your
  project.

* JSON Config also simplifies the process of cross-checking configuration
  settings across multiple sources. An example might be first checking to
  see if an environment variable is set.  If not set, then checking to see
  if the setting has been recorded in the configuration file, and if not
  prompting the user for the required setting and then writing it back to
  the configuration.  In JSON Config this can all be done in one simple line
  of code.

**********
References
**********

.. target-notes::

.. _Click: http://github.com/pallets/click
.. _Keyring: https://github.com/jaraco/keyring
.. _Python-Box: http://github.com/cdgriffith/Box


