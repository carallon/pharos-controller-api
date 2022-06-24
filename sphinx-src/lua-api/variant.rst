Variant
#######

Introduction
************

Within Lua Scripting (as with other scripting languages) it is possible to store data within a named location (variable).

Lua typically doesn't differentiate between the contents of a variable (unlike some programming languages) and the type (integer, string, boolean) of the variable can change at any time.

Pharos has added an object to the scripting environment called a ``Variant``, which can be used to contain the data with an assignment as to the type of data that is contained. This means that a single ``Variant`` can be utilised and handled differently depending on the data that is contained and how it is being used.

Definition
**********

Properties
==========

A ``Variant`` object has the following properties:

.. list-table::
   :widths: 5 10
   :header-rows: 1

   * - Property
     - Description
   * - ``integer``
     - Get or set an integer data type
   * - ``range``
     - Get or set the range of an integer data type
   * - ``real``
     - Get or set a real data type (number with decimal point)
   * - ``string``
     - Get or set a string data type
   * - ``ip_address``
     - Get or set an IP address data type

Member functions
================

Constructor
-----------

``Variant()``

Create new variant.

is_integer
----------

Returns ``true`` or ``false`` to show whether the stored data has an integer representation.

is_string
---------

Returns ``true`` or ``false`` to show whether the stored data has a string representation.

is_ip_address
-------------

Returns ``true`` or ``false`` to show whether the stored data has an IP address representation.


Usage
*****

``Variant(value, range)``

Defining a variant
==================

Within your Lua script you can create a Variant with the following syntax:

.. code-block:: lua

   var = Variant() -- where var is the name of the variant.

Variant types
=============

Integer
-------

An integer variant can be used to store a whole number:

.. code-block:: lua

   var = Variant() -- where var is the name of the variant

   var.integer = 123 -- set var to an integer value of 123

   log(var.integer) -- get the integer value stored in var

   log(var.real) -- get the integer value stored in var and convert it to a float

   log(var.string) -- get the integer value stored in var and convert it to a string

As shown in the example code, above, the ``integer`` property of a ``Variant`` can be used to either get or set the value of the ``Variant`` as an integer (whole number).

.. code-block:: lua

   var:is_integer() -- returns a boolean if the variant contains an integer

Range
-----

An integer can be stored with an optional range parameter:

.. code-block:: lua

   var = Variant() -- where var is the name of the variant

   var.integer = 123 -- set var to an integer value of 123

   var.range = 255 -- set the range of var to be 255

This can be used to calculate fractions and/or to define that a ``Variant`` is a 0-1, 0-100 or 0-255 value.

The range of a ``Variant`` should be set if you intend to use the ``Variant`` to set an intensity or colour value.

Some captured variables have a range attribute, and this is indicated in the log like this::

   Trigger 7 (Ethernet Input): Captured 3 variables
   Captured variables
     1 - Integer: 100 of 255

Real
----

A real ``Variant`` can be used to store a floating point (decimal) number.

.. code-block:: lua

   var = Variant() -- where var is the name of the variant.

   var.real = 12.3 -- set var to an integer value of 12.3

   log(var.real) -- get the integer value stored in var

As shown in the example code, above, the ``real`` property of a ``Variant`` can be used to either get or set the value of the ``Variant`` as a real number.

String
------

A string ``Variant`` can be used to store a string of ASCII characters.

.. code-block:: lua

   var = Variant() -- where var is the name of the variant

   var.string = "example" -- set var to a string value of "example"

   log(var.string) -- get the string value stored in var

As shown in the example code, above, the ``string`` property of a ``Variant`` can be used to either get or set the value of the ``Variant`` as a string.

.. code-block:: lua

   var:is_string() -- returns a boolean if the variant contains a string

IP address
----------

.. code-block:: lua

   var = Variant() -- where var is the name of the variant

   var.ip_address = "192.168.1.23" -- set var to the IP Address 192.168.1.23 or -1062731497

   log(var) -- get the stored data ("192.168.1.23")

   log(var.ip_address) -- get the stored IP Address (-1062731497)

   log(var.string) -- get the stored IP Address and convert it to a string ("192.168.1.23")

   log(var.integer) -- get the stored IP Address and convert it to an integer (-1062731497)

As shown in the example code, above, the ``ip_address`` property of a ``Variant`` can be used to either get or set the value of the ``Variant`` as an IP Address.

As a setter, you can pass a dotted decimal string (e.g. "192.168.1.23" or the integer representation -1062731497).

.. code-block:: lua

   var:is_ip_address() -- returns a boolean if the variant contains a IP Address

Shorthand
=========

A ``Variant`` can also be defined using a shorthand:

.. code-block:: lua

   var = Variant(128,255) -- create variable var as an integer (128) with range 0-255

   var = Variant(128) -- create variable var as a real number (128.0)

   var = Variant(12.3) -- create variable var as a real number (12.3)

   var = Variant("text") -- create variable var as a string ("text")

.. note::

   There isn't a shorthand for IP Addresses.

Default variants
****************

Some script functions return a ``Variant``, including :ref:`Lua_get_trigger_variable`. For example:

.. code-block:: lua

   get_trigger_variable(1).integer

The ``master_intensity_level`` properties of :doc:`group` and :doc:`content-target` are both Variants:

.. code-block:: lua

   get_group(1).master_intensity_level.integer

   get_group(1).master_intensity_level.range

   get_content_target(1).master_intensity_level.integer

   get_content_target(1).master_intensity_level.range
