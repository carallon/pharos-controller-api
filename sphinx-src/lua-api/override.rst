Override
########

An ``Override`` object is returned from :ref:`Lua_get_fixture_override` and :ref:`Lua_get_group_override`.

Member functions
****************

The following are member functions of ``Override`` objects.

.. _Lua_override_set_irgb:

set_irgb
========

``set_irgb(intensity, red, green, blue, [fade, [path]])``

Overrides the intensity, red, green and blue levels for the fixture or group according to the parameters:

.. list-table::
   :widths: 3 3 7 3
   :header-rows: 1

   * - Parameter
     - Value Type
     - Description
     - Value Example
   * - ``intensity``
     - integer (0-255)
     - Intensity level to set as an override.
     - ``128``
   * - ``red``
     - integer (0-255)
     - Red level to set as an override.
     - ``128``
   * - ``green``
     - integer (0-255)
     - Green level to set as an override.
     - ``128``
   * - ``blue``
     - integer (0-255)
     - Blue level to set as an override.
     - ``128``
   * - ``fade``
     - float
     - Optional. Fade time to apply the override change, in seconds.
     - ``2.0``
   * - ``path``
     - string
     - Optional. Crossfade path to use when applying the override: |fade-paths|
     - ``"Linear"``

For example:

.. include:: code-examples/fixture-override.rst


.. _Lua_override_set_intensity:

set_intensity
=============

``set_intensity(intensity, [fade, [path]])``

Overrides the intensity level for the fixture or group according to the parameters:

.. list-table::
   :widths: 3 3 7 3
   :header-rows: 1

   * - Parameter
     - Value Type
     - Description
     - Value Example
   * - ``intensity``
     - integer (0-255)
     - Intensity level to set as an override.
     - ``128``
   * - ``fade``
     - float
     - Optional. Fade time to apply the override change, in seconds.
     - ``2.0``
   * - ``path``
     - string
     - Optional. Crossfade path to use when applying the override: |fade-paths|
     - ``"Linear"``

For example:

.. include:: code-examples/group-override.rst


.. _Lua_override_set_red:

set_red
=======

``set_red(red, [fade, [path]])``

Overrides the red level for the fixture or group according to the parameters:

.. list-table::
   :widths: 3 3 7 3
   :header-rows: 1

   * - Parameter
     - Value Type
     - Description
     - Value Example
   * - ``red``
     - integer (0-255)
     - Red level to set as an override.
     - ``128``
   * - ``fade``
     - float
     - Optional. Fade time to apply the override change, in seconds.
     - ``2.0``
   * - ``path``
     - string
     - Optional. Crossfade path to use when applying the override: |fade-paths|
     - ``"Linear"``


.. _Lua_override_set_green:

set_green
=========

``set_green(green, [fade, [path]])``

Overrides the green level for the fixture or group according to the parameters:

.. list-table::
   :widths: 3 3 7 3
   :header-rows: 1

   * - Parameter
     - Value Type
     - Description
     - Value Example
   * - ``green``
     - integer (0-255)
     - Green level to set as an override.
     - ``128``
   * - ``fade``
     - float
     - Optional. Fade time to apply the override change, in seconds.
     - ``2.0``
   * - ``path``
     - string
     - Optional. Crossfade path to use when applying the override: |fade-paths|
     - ``"Linear"``


.. _Lua_override_set_blue:

set_blue
=========

``set_blue(blue, [fade, [path]])``

Overrides the blue level for the fixture or group according to the parameters:

.. list-table::
   :widths: 3 3 7 3
   :header-rows: 1

   * - Parameter
     - Value Type
     - Description
     - Value Example
   * - ``blue``
     - integer (0-255)
     - Blue level to set as an override.
     - ``128``
   * - ``fade``
     - float
     - Optional. Fade time to apply the override change, in seconds.
     - ``2.0``
   * - ``path``
     - string
     - Optional. Crossfade path to use when applying the override: |fade-paths|
     - ``"Linear"``


.. _Lua_override_set_temperature:

set_temperature
===============

``set_temperature(temperature, [fade, [path]])``

Overrides the temperature level for the fixture or group according to the parameters:

.. list-table::
   :widths: 3 3 7 3
   :header-rows: 1

   * - Parameter
     - Value Type
     - Description
     - Value Example
   * - ``temperature``
     - integer (0-255)
     - Temperature level to set as an override.
     - ``128``
   * - ``fade``
     - float
     - Optional. Fade time to apply the override change, in seconds.
     - ``2.0``
   * - ``path``
     - string
     - Optional. Crossfade path to use when applying the override: |fade-paths|
     - ``"Linear"``


.. _Lua_override_clear:

clear
=====

``clear([fade])``

Removes any override on the fixture or group. Optionally specify a ``fade`` time in seconds as a float, e.g. ``2.0``.

For example:

.. code-block:: lua

   -- Clear the override on fixture 1
   get_fixture_override(1):clear()

See also: :ref:`Lua_clear_all_overrides`.


.. |fade-paths| replace::
   ``Default``, ``Linear``, ``Start``, ``End``, ``Braked``, ``Accelerated``, ``Damped``, ``Overshoot``, ``Col At Start``, ``Col At End``, ``Int At Start``, ``Int At End``, ``Colour First``, ``Intensity First``
