#########################
Configuration File Basics
#########################

==========
Definition
==========

A configuration file is used for the persistent storage of data, like
when a user shuts down a program, turns the power off, etc. the information
is loaded again the next time they open it so that they can continue where
they left off.

Rather than being hard-coded in the program, the information is user-
configurable and typically stored in a plain text format, in this case JSON.

Source: `Configuration file`_

.. tip::

    For the most part, you don't even need to worry about JSON, you just
    assign your data to the context manager's attributes and JSON Config
    takes care of the rest.

=========================================================
Most Interesting Programs Need Some Kind of Configuration
=========================================================

There’s no defined standard on how config files should work, *what goes
into a configuration file is entirely up to the whim of the developer*, but
here are some examples:

Content Management Systems
    That need store information about where the database server is (the
    hostname) and how to login (username and password.)

Proprietary Software
    That need to record whether the software was already registered
    (the serial key.)

Scientific Software
    That need to store the path to BLAS libraries.

And the list goes on, and on ....

Source: `Configuration files in Python`_

**************
Author's Notes
**************

*What is the author storing in the JSON config file? Training set data,
information about RESTful API’s (authentication information, endpoints,
parameters, data extraction & transformation rules, etc.), and much more.
It’s part of the JSON Transformations project which is the tip of the
iceberg for a research project he's working on*.

**********
References
**********

.. target-notes::

.. _`Configuration file`:
    https://en.wikipedia.org/wiki/Configuration_file

.. _`Configuration files in Python`:
    https://martin-thoma.com/configuration-files-in-python

.. _`How to write a JSON configuration file`:
    https://github.com/KratosMultiphysics/Kratos/wiki/How-to-write-a-JSON-configuration-file
