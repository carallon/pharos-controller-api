Adjustment Target
#################

.. note::

   Only supported on |VLC+|.

An ``Adjustment`` object is returned from :ref:`Lua_get_adjustment`.

Properties
**********

.. list-table::
   :widths: 5 5
   :header-rows: 1

   * - Property
     - Value Type
   * - ``rotation_offset``
     - float
   * - ``x_position_offset``
     - float
   * - ``y_position_offset``
     - float

For example:

.. code-block:: lua

   target = get_adjustment(1)
   r_offset = target.rotation_offset


Member functions
****************

The following are member functions of ``Adjustment`` objects.


.. _Lua_adjustment_transition_rotation:

transition_rotation
===================

``transition_rotation([angle[, count[, period[, delay[, useShortestPath]]]]])``

Applies a rotation to the adjustment target according to the parameters:

.. include:: snippets/transition-rotation-params.rst


.. _Lua_adjustment_transition_x_position:

transition_x_position
=====================

``transition_x_position([x_offset[, count[, period[, delay]]]])``

Moves the adjustment target along the x axis according to the parameters:

.. include:: snippets/transition-x-params.rst


.. _Lua_adjustment_transition_y_position:

transition_y_position
=====================

``transition_y_position([x_offset[, count[, period[, delay]]]])``

Moves the adjustment target along the y axis according to the parameters:

.. include:: snippets/transition-y-params.rst
