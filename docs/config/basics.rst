###########################################
What is a JSON Configuration File Used For?
###########################################

The JSON is solely for serializing the data (described below), just about
any type of information can go in the `configuration file`, for example:

A `configuration file`_ is used for the persistent storage of
data, like when a user shuts down a program, turns the power off, etc. the
information is loaded again the next time they open it so that they can
continue where they left off.

Rather than being hard-coded in the program, the information is user-
configurable and typically stored in a plain text format, in this case JSON.

=========================================================
Most Interesting Programs need some kind of configuration
=========================================================

.. rubric:: For Example ...::

Content Management Systems
    That store the information where the database server is (the
    hostname) and how to login (username and password/)

Proprietary Software
    Might need to store if the software was registered already (the serial
    key.)

Scientific Software
    Could store the path to BLAS libraries There’s no defined standard on
    how config files should work, … 

.. rubric:: And the list goes on, and on ...

**What goes into a configuration file is entirely up to the whim of the
developer** … [1]

Source: `Configuration files in Python`_

=====================
Serialization Formats
=====================

A number of general-purpose serialization formats exist that can represent
complex data structures in an easily stored format, and these are often used
as a basis for configuration files, particularly in open-source and
platform-neutral software applications and libraries. The specifications
describing these formats are routinely made available to the public, thus
increasing the availability of parsers and emitters across programming
languages. Examples include: XML, YAML and JSON. I am intentionally keeping
my project ultra-lite and sticking with JSON; this was a design decision.
For anyone interested in working with other formats check out the
`dynaconf project`_.

When it reads back the data the `JSON decoder performs the following
translations`_:

+--------+---------------+
| Python | JSON          |
+========+===============+
| dict   | object        |
+--------+---------------+
| list   | array         |
+--------+---------------+
| str    | string        |
+--------+---------------+
| int    | number (int)  |
+--------+---------------+
| float  | number (real) |
+--------+---------------+
| True   | true          |
+--------+---------------+
| False  | false         |
+--------+---------------+
| None   | null          |
+--------+---------------+

What am I personally storing in the JSON config file? Training set data
information about RESTful API’s (authentication information, endpoints,
parameters, data extraction & transformation rules, etc.), and more. It’s
part of the JSON Transformations project which in return is the tip of the
iceberg for the mothership project.

.. topic:: Interested in learning more about serialization?

    Here are some additional resources:

        * `How to write a JSON configuration file`_
        * `Serialization and deserialization`_

**********
References
**********

.. target-notes::

_`configuration file`:
    https://en.wikipedia.org/wiki/Configuration_file

_`Configuration files in Python`:
    https://martin-thoma.com/configuration-files-in-python

_`How to write a JSON configuration file`:
    https://github.com/KratosMultiphysics/Kratos/wiki/How-to-write-a-JSON-configuration-file

_`JSON decoder performs the following translations`:
    https://docs.python.org/3.6/library/json.html

_`Serialization and Deserialization`:
    https://code.tutsplus.com/tutorials/serialization-and-deserialization-of-python-objects-part-1--cms-26183

_`dynaconf project`:
    https://github.com/rochacbruno/dynaconf
