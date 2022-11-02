Group
#####

A ``Group`` object is returned from :ref:`Lua_get_group`.

Properties
**********

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Property
     - Value Type
     - Description
     - Value Example
   * - ``name``
     - string
     - Group name
     - ``"Group 1"``
   * - ``master_intensity_level``
     - :doc:`variant`
     - The intensity level that this group is currently being mastered to
     - 

For example:

.. include:: code-examples/group.rst

Member functions
****************

The following are member functions of ``Group`` objects.

.. _Lua_group_set_master_intensity:

set_master_intensity
====================

``set_master_intensity(level[, fade[, delay]])``

Masters the intensity of the group according to the parameters:

.. list-table::
   :widths: 3 3 7 3
   :header-rows: 1

   * - Parameter
     - Value Type
     - Description
     - Value Example
   * - ``level``
     - float (0.0-1.0) or integer (0-255)
     - Master level to set on the group
     - ``0.5`` or ``128``
   * - ``fade``
     - float
     - Optional. Fade time to apply the intensity change, in seconds
     - ``2.0``
   * - ``delay``
     - float
     - Optional. Time to wait before applying the intensity change, in seconds
     - ``3.0``

For example:

.. code-block:: lua

   -- Master group 1 to 50% (128/255 = 0.5) in 3 seconds
   get_group(1):set_master_intensity(128,3)
