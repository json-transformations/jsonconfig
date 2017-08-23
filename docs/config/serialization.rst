#############
Serialization
#############

==========
Definition
==========

A number of general-purpose serialization formats exist that can represent
complex data structures in an easily stored format, and these are often used
as a basis for configuration files, *particularly in open-source and
platform-neutral software applications and libraries*. The specifications
describing these formats are routinely made available to the public, thus
increasing the availability of parsers and emitters across programming
languages. Examples include: XML, YAML and JSON.

This project is ultra-lite, and is focused solely on JSON; this was a
deliberate design decision. For anyone interested in working with the other
formats check out the `dynaconf project`_.

============================
Python Data Type Conversions
============================

The `JSON decoder performs the following translations`_:

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


***************************************
Want to Learn More about Serialization?
***************************************

Here are some additional resources:

    * `How to write a JSON configuration file`_
    * `Serialization and deserialization`_

**********
References
**********

.. target-notes::

_`JSON decoder performs the following translations`:
    https://docs.python.org/3.6/library/json.html

_`Serialization and deserialization`:
    https://code.tutsplus.com/tutorials/serialization-and-deserialization-of-python-objects-part-1--cms-26183

_`dynaconf project`:
    https://github.com/rochacbruno/dynaconf
