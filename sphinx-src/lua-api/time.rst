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

Each of these functions can either be called with no argument, or with a :doc:`date-time` object as an argument.

If called with no arguments, it will return the specified astronomical event for the current day.

If a :doc:`date-time` object is provided, it will return the astronomical event for the date provided.

.. caution::
  Calculation of astronomical events is processor intensive. Do not use these functions when time critical - where possible, cache the results of the calculation so it is performed once per day, for example.

Examples
========

Getting current hour
--------------------

.. code-block:: lua

   current_hour = time.get_current_time().hour

Getting sunrise time for a specified date
-----------------------------------------

.. code-block:: lua

   local result = time.get_sunrise(DateTime.new(2003, 8, 13))

   local logString = string.format("Sunrise on %d-%d-%d is at %02d:%02d",
      result.year,
      result.month,
      result.monthday,
      result.hour,
      result.minute
   )

   log(logString)
