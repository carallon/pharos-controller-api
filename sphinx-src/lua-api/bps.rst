BPS
###

A ``BPS`` object is returned from :ref:`Lua_get_bps`.

Member functions
****************

The following are member functions of ``BPS`` objects.


.. _Lua_bps_get_state:

get_state
=========

``get_state(buttonNum)``

Returns the state of the button with integer number ``buttonNum``, which can be one of the constants ``RELEASED``, ``PRESSED``, ``HELD`` or ``REPEAT``.

For example:

.. include:: code-examples/bps-get-state.rst


.. _Lua_bps_set_led:

set_led
=======

``set_led(button, effect[, intensity[, fade]])``

Set the effect and intensity of a BPS button LED according to the parameters:

.. list-table::
   :widths: 3 3 7 3
   :header-rows: 1

   * - Parameter
     - Value Type
     - Description
     - Value Example
   * - ``button``
     - integer (1-8)
     - Number of the BPS button to set an effect on
     - ``1``
   * - ``effect``
     - integer
     - Integer value of constants: ``OFF``, ``ON``, ``SLOW_FLASH``, ``FAST_FLASH``, ``DOUBLE_FLASH``, ``BLINK``, ``PULSE``, ``SINGLE``, ``RAMP_ON``, ``RAMP_OFF``
     - ``SLOW_FLASH``
   * - ``intensity``
     - integer (0-255)
     - Optional. Intensity level to set on the LED. If this parameter is not specified, full intensity will be set on the LED.
     - ``255``
   * - ``fade``
     - float
     - Optional. Fade time to apply the override change, in seconds.
     - ``2.0``

For example:

.. code-block:: lua

   -- Set button 1 on BPS 1 to Fast Flash at full intensity
   get_bps(1):set_led(1,FAST_FLASH,255)
