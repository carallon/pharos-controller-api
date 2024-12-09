Touch Device
############

A ``TouchDevice`` object is returned from :ref:`Lua_get_touch_device`.

Member functions
****************

The following are member functions of ``TouchDevice`` objects.


.. _Lua_touch_device_set_control_value:

set_control_value
-----------------

``set_control_value(name, [index,] value[, emitChange])``

Set the value on a Touch Slider or Colour Picker according to the parameters:

.. list-table::
   :widths: 3 3 7 3
   :header-rows: 1

   * - Parameter
     - Value Type
     - Description
     - Value Example
   * - ``name``
     - string
     - The Key of the Touch Control.
     - ``slider001``
   * - ``index``
     - integer (1-3)
     - Optional. Axis of movement - a slider has 1; a colour picker has 3. Will default to 1 if this parameter isn't specified.
     - ``1``
   * - ``value``
     - integer (0-255)
     - New value to set.
     - ``128``
   * - ``emitChange``
     - boolean
     - Optional. Whether to fire associated triggers as a result of the control value change. Defaults to ``false``.
     - ``true``

For example:

.. code-block:: lua

   -- Set slider001 to half (and don't fire any associated triggers) on TPS 1
   get_touch_device(TPS, 1):set_control_value("slider001", 128)
   -- Set the second axis (green) to full on colour020 on TPS5 2
   get_touch_device(TPS5, 2):set_control_value("colour020", 2, 255)


.. _Lua_touch_device_set_control_state:

set_control_state
-----------------

``set_control_state(name, state)``

Set the state on a Touch control according to the parameters:

.. list-table::
   :widths: 3 3 7 3
   :header-rows: 1

   * - Parameter
     - Value Type
     - Description
     - Value Example
   * - ``name``
     - string
     - The Key of the Touch Control.
     - ``slider001``
   * - ``state``
     - string
     - The name of the state as defined in the Touch theme.
     - ``Green``

For example:

.. code-block:: lua

   -- Set slider001 to a state called "Green" on TPS8 3
   get_touch_device(TPS8, 3):set_control_state("slider001", "Green")


.. _Lua_touch_device_set_control_caption:

set_control_caption
-------------------

``set_control_caption(name, caption)``

Set the caption on a Touch control according to the parameters:

.. list-table::
   :widths: 3 3 7 3
   :header-rows: 1

   * - Parameter
     - Value Type
     - Description
     - Value Example
   * - ``name``
     - string
     - The Key of the Touch Control.
     - ``button001``
   * - ``caption``
     - string
     - The text to display as the control's caption.
     - ``On``

For example:

.. code-block:: lua

   -- Set button001's caption to "On" on TPS 2
   get_touch_device(TPS, 2):set_control_caption("button001", "On")


.. _Lua_touch_device_set_touch_button_pressed:

set_touch_button_pressed
------------------------

``set_touch_button_pressed(name, pressed)``

Sets the pressed or released state of a Touch button according to the parameters:

.. list-table::
   :widths: 3 3 7 3
   :header-rows: 1

   * - Parameter
     - Value Type
     - Description
     - Value Example
   * - ``name``
     - string
     - The Key of the Touch Button.
     - ``button001``
   * - ``pressed``
     - boolean
     - Whether the button is Pressed(true) or Released(false).
     - ``true``

For example:

.. code-block:: lua

   -- Set button001 to be pressed on TPS 4
   get_touch_device(TPS, 4):set_touch_button_pressed("button001", true)


.. _Lua_touch_device_is_touch_button_pressed:

is_touch_button_pressed
------------------------

``is_touch_button_pressed(name)``

Returns the pressed or released state of a touch button.

For example:

.. code-block:: lua

   -- Enqueue a trigger conditionally based on whether a button is pressed
   if get_touch_device(TPS5, 3):is_touch_button_pressed("button001") then
      enqueue_trigger(1)
   end


.. _Lua_touch_device_set_interface_page:

set_interface_page
------------------

``set_interface_page(number[, transition])``

Change the current page on the Touch interface according to the parameters:

.. list-table::
   :widths: 3 3 7 3
   :header-rows: 1

   * - Parameter
     - Value Type
     - Description
     - Value Example
   * - ``number``
     - integer
     - Touch interface page to change to.
     - ``2``
   * - ``transition``
     - integer
     - Optional page transition. Integer value of constants: ``SNAP``, ``PAN_LEFT``, ``PAN_RIGHT``
     - ``PAN_LEFT``

.. note::

   Must be executed on the |TPC| that hosts the interface.

For example:

.. code-block:: lua

   -- Change the touch screen interface to page 4 with a snap transition on TPS5 3
   get_touch_device(TPS5, 3):set_interface_page(4, SNAP)


.. _Lua_touch_device_set_interface_enabled:

set_interface_enabled
---------------------

``set_interface_enabled([enabled])``

Enable/disable the touchscreen, according to the optional boolean parameter ``enabled`` (default: ``true``).

.. note::

   Must be executed on the |TPC| that hosts the interface.

For example:

.. code-block:: lua

   -- Disable the touchscreen TPS8 4
   get_touch_device(TPS8, 4):set_interface_enabled(false)


.. _Lua_touch_device_set_interface_locked:

set_interface_locked
--------------------

``set_interface_locked([lock])``

Lock/unlock the touchscreen, according to the optional boolean parameter ``lock`` (default: ``true``).

.. note::

   Must be executed on the |TPC| that hosts the interface.

For example:

.. code-block:: lua

   -- Lock the touchscreen TPS 3
   get_touch_device(TPS, 3):set_interface_locked()
   -- Unlock the touchscreen TPS5 4
   get_touch_device(TPS5, 4):set_interface_locked(false)
