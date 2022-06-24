Content Target
##############

.. note::

   Only supported on |VLC| and |VLC+|.

A ``ContentTarget`` object is returned from :ref:`Lua_get_content_target`.

Properties
**********

.. list-table::
   :widths: 5 3 5
   :header-rows: 1

   * - Property
     - Value Type
     - Description
   * - ``master_intensity_level``
     - :doc:`variant`
     - 
   * - ``rotation_offset``
     - float
     - |VLC+| only
   * - ``x_position_offset``
     - float
     - |VLC+| only
   * - ``y_position_offset``
     - float
     - |VLC+| only

For example, on a |VLC|:

.. include:: code-examples/content-target-vlc.rst

And on a |VLC+|:

.. include:: code-examples/content-target-vlcp.rst


Member functions
****************

The following are member functions of ``ContentTarget`` objects.

.. _Lua_content_target_set_master_intensity:

set_master_intensity
====================

``set_master_intensity(level[, fade[, delay]])``

Masters the intensity of the content target according to the parameters:

.. list-table::
   :widths: 3 3 7 3
   :header-rows: 1

   * - Parameter
     - Value Type
     - Description
     - Value Example
   * - ``level``
     - float (0.0-1.0) or integer (0-255)
     - Master level to set on the content target.
     - ``0.5`` or ``128``
   * - ``fade``
     - float
     - Optional. Fade time to apply the intensity change, in seconds.
     - ``2.0``
   * - ``delay``
     - float
     - Optional. Time to wait before applying the intensity change, in seconds.
     - ``3.0``

For example, on a |VLC|:

.. code-block:: lua

   -- Master the primary content target in composition 1 to 50% (128/255 = 0.5) in 3 seconds
   get_content_target(1):set_master_intensity(128,3)

Or on a |VLC+|:

.. code-block:: lua

   -- Master the secondary content target in composition 2 to 100% in 2.5 seconds
   get_content_target(2, SECONDARY):set_master_intensity(255,2.5)


.. _Lua_content_target_transition_rotation:

transition_rotation
===================

.. note::

   Only supported on |VLC+|.

``transition_rotation([angle[, count[, period[, delay[, useShortestPath]]]]])``

Applies a rotation to the content target according to the parameters:

.. include:: snippets/transition-rotation-params.rst


.. _Lua_content_target_transition_y_position:

transition_y_position
=====================

``transition_y_position([y_offset[, count[, period[, delay]]]])``

Moves the content target along the y axis according to the parameters:

.. include:: snippets/transition-y-params.rst
