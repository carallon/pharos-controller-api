Universe
########

A ``Universe`` object is returned from e.g. :ref:`Lua_get_dmx_universe`.

Member functions
****************

The following are member functions of ``Universe`` objects.


.. _Lua_universe_get_channel_value:

get_channel_value
=================

``get_channel_value(channel)``

Gets the current level of a channel in the universe, where ``channel`` is the integer channel number (1-512).

For example:

.. include:: code-examples/universe.rst


.. _Lua_universe_park:

park
====

``park(channel, value)``

Parks an output channel at a given value according to the parameters:

.. list-table::
   :widths: 3 3 7 3
   :header-rows: 1

   * - Parameter
     - Value Type
     - Description
     - Value Example
   * - ``channel``
     - integer (1-512)
     - Number of the output channel
     - ``1``
   * - ``value``
     - integer (0-255)
     - Level to set the channel to
     - ``128``

For example:

.. code-block:: lua

   -- Park channel 4 of DMX universe 1 at 128 (50%)
   get_dmx_universe(1):park(4,128)


.. _Lua_universe_unpark:

unpark
======

``unpark(channel)``

Clears the parked value on an output channel, where ``channel`` is the integer channel number (1-512).

For example:

.. code-block:: lua

    -- Unpark channel 4 of DMX universe 1
    -- (it will go back to normal output levels)
   get_dmx_universe(1):unpark(4)
