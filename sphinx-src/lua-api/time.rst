Time
####

Information about the controller's clock is available in the ``time`` namespace. In trigger action scripts the ``time`` namespace is added directly to the environment; in IO modules it is in the ``controller`` namespace, i.e. ``controller.time``.

Properties
**********

The ``time`` namespace has the following properties:

.. list-table::
   :widths: 3 3 3
   :header-rows: 1

   * - Property
     - Value Type
     - Value Example
   * - ``is_dst``
     - boolean
     - ``true``
   * - ``gmt_offset``
     - integer (minutes)
     - | ``-300``
       | 300 Minutes (5 hours) behind

Functions
*********

The ``time`` namespace has the following functions, which each return a :doc:`date-time` object:

* ``get_current_time()``
* ``get_sunrise()``
* ``get_sunset()``
* ``get_civil_dawn()``
* ``get_civil_dusk()``
* ``get_nautical_dawn()``
* ``get_nautical_dusk()``
* ``get_new_moon()``
* ``get_first_quarter()``
* ``get_full_moon()``
* ``get_third_quarter()``

For example:

.. code-block:: lua

   current_hour = time.get_current_time().hour
