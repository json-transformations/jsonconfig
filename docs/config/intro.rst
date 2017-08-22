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

======================
With Stability in Mind
======================

JSON Config is basically just a pass-through to mature, stable 3rd party
packages, and built-in Python modules: click, box, keyring, open, json.load,
json.dump, and os.environ.  JSON Config takes extra care to stay out of your
way as a Python programmer and to NOT introduce any magic.  Any keyword
arguments that you would normally be able pass to these functions is still
available through the context manager. And sure, you could import each of
these packages idependently rather than using JSON Config but then you'd be
responsible for writing a lot more code, for tracking what all needs to be
imported, for writing a lot more tests, and for dealing with  error handling
from disparate source. The more custom code you write, the greater the
chance of introducing bugs.  JSON Config also aims to create consistency
among the packages.  For example, bringing attribute-style access across
data, encrypted data, and environment variables, along with providing
consitent error handling control around the entire configuration process;
this allows you to employ exception management at the granualarity-level
most suitable to your project.  JSON Config also simplifies the process of
cross- checking configuration settings across multiple sources.  An example
might be first checking to see if a environment variable is set, if not set
then checking to see if the setting has been stored in the configuration
file, and if not prompting the user for the required setting and then
writing it back to the configuration; in JSON Config this can all be
done in one simple line of code.


=============
Basic Example
=============

.. code::

    with Config('myapp') as cfg:
        cfg.data = 'Any JSON serializable object ...'
        cfg.pwd.a_secret = 'Encrypted data ...'
        cfg.env.a_variable = 'Environment variables.'

.. topic:: In the context manager above:

    * The ``data`` is stored in the user's local application directory.
    * The ``pwd`` data is encrypted and stored in a keyring vault.
    * The ``env`` data is stored in environment variables.

===========
Easy Access
===========

With Box as a data access wrapper you can reference Mapping data as either
dictionary keys or attribute style notation.  For example,

.. code::

    with BoxConfig('myapp') as cfg:
        cfg.data.key1 = 'Some configuration data ...'
        cfg.data.key2 = 'Some more data ...'


============
Installation
============

.. code::

    pip install jsonconfig
