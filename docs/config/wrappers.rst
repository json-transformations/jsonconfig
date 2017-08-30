#########################################
Data Served in the Wrapper of Your Choice
#########################################

Box_ *is the package used to handle data access*.

Data wrappers are purely optional, and are designed solely for the purpose
of making Mapping/dictionary keys easier to access and improving the
readability of your code.  If you are not storing Mappings/Dictionaries then
you can skip this section.

=========
Shortcuts
=========

BoxConfig
    A shortcut for `Config('myapp', box=True)`.  It converts the config data
    attribute into a dictionary that allows both dictionary key and
    attribute-style access.

.. code::

    with BoxConfig('myapp') as cfg:
        cfg.data.widget = {}
        cfg.data.widget.window = {}
        cfg.data.widget.debug = True
        cfg.data.widget.window.title = 'Sample Konfabulator Widget'
        cfg.data.widget.window.width = 500

    with BoxConfig('myapp') as cfg:
        assert cfg.data.widget.debug is True
        assert cfg.data.widget.window.title == 'Sample Konfabulator Widget'
        assert cfg.data.widget.window.width == 500

FrozenBox
    A shortcut for `Config('myapp', frozen_box=True)`.  Same as `BoxConfig`
    except that it is read-only.  It will not allow updates to the data and
    will not write back to the configuration file when exitting the context
    manager.

.. code::

    with FrozenBox('myapp') as cfg:
        cfg.debug = True

DefaultBox
    A shortcut for `Config('myapp', default_box=True)`.  Acts like a
    recursive default dict.  It automatically creates missing keys.    


.. code::

        with DefaultBox('myapp') as cfg:
            cfg.data['widget']['debug'] = True
            cfg.data['widget']['window']['title'] = 'Sample Konfabulator Widget'
            cfg.data['widget']['window']['width'] = 800

        with DefaultBox('myapp') as cfg:
            assert cfg.data['widget']['debug'] is True
            title = cfg.data['widget']['window']['title']
            assert title == 'Sample Konfabulator Widget'
            assert cfg.data['widget']['window']['width'] == 800

=======================
Data Conversion Helpers
=======================

The following conversion functions are provided as shortcuts:

BOXED
    A shorcut for box.Box(self.data).  Converts data attribute to a Box
    object.

FROZEN
    A shorcut for box.Box(self.data, frozen_box=True).  Converts data
    attribute to a Frozen-Box object.

NESTED
    A shorcut for box.Box(self.data, default_box=True).  Converts data
    attribute to a Default-Box object.

DATA CONVERSION
    ``BOXED``, ``FROZEN`` and ``NESTED`` are all subclasses of dicts or
    defaultdicts.  You can convert back-and-forth between any of them at any
    time.

OTHER TYPES
    To return to a standard dict just use `dict(cfg.data)` where `cfg` is
    your context manager instance.  It's just plain Python, just about
    anything you can do to Python objects you can do to the data attrribute.

==============
Advanced Usage
==============

JSON Config will pass any valid keyword arguments that box.Box accepts

.. code::

        with Config('myapp', camel_killer_box=True) as cfg:
            result = cfg.data

See Box's documentation for additional information.


**********
References
**********

.. topic:: All about Python context managers ...

    * https://dbader.org/blog/python-context-managers-and-with-statement
    * https://pymotw.com/3/contextlib/
    * https://jeffknupp.com/blog/2016/03/07/python-with-context-managers
    * http://book.pythontips.com/en/latest/context_managers.html