InputThreshold
##############

A ``InputThreshold`` object is returned from :ref:`Lua_rio_get_input_threshold` for a RIO device, or :ref:`Lua_get_input_threshold` for the local inputs of a controller.

Properties
**********

.. list-table::
   :widths: 4 3 9 4
   :header-rows: 1

   * - Property
     - Value Type
     - Description
     - Value Example
   * - ``low``
     - integer
     - If the input type is ``DIGITAL``, this is the low voltage threshold. If the input type is ``ANALOG``, this marks the low end of the voltage range and voltages at or below this value will be reported as 0%.
     - ``4``
   * - ``high``
     - integer
     - If the input type is ``DIGITAL``, this is the high voltage threshold. If the input type is ``ANALOG``, this marks the high end of the voltage range and voltages at or above this value will be reported as 100%.
     - ``16``
