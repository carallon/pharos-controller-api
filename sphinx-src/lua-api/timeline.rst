Timeline
########

A ``Timeline`` object is returned from :ref:`Lua_get_timeline`.

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
     - Timeline name
     - ``"Timeline 1"``
   * - ``group``
     - string
     - Timeline group name (``A``, ``B``, ``C``, ``D`` or empty string)
     - ``"A"``
   * - ``length``
     - integer
     - Timeline length, in milliseconds
     - ``10000``
   * - ``source_bus``
     - integer
     - Integer value of constants: ``DEFAULT``, ``TCODE_1`` ... ``TCODE_6``, ``AUDIO_1`` ... ``AUDIO_4``
     - ``1``
   * - ``timecode_format``
     - string
     - Timecode format
     - ``"SMPTE30"``
   * - ``audio_band``
     - integer
     - 0 is equivalent to the constant: ``VOLUME``
     - ``0``
   * - ``audio_channel``
     - integer
     - Integer value of constants: ``LEFT``, ``RIGHT`` or ``COMBINED``
     - ``1``
   * - ``audio_peak``
     - boolean
     - The Peak setting of the timeline, if set to an audio time source
     - ``false``
   * - ``time_offset``
     - integer
     - Milliseconds
     - ``5000``
   * - ``state``
     - integer
     - Integer value of constants: ``Timeline.NONE``, ``Timeline.RUNNING``, ``Timeline.PAUSED``, ``Timeline.HOLDING_AT_END`` or ``Timeline.RELEASED``
     - ``1``
   * - ``onstage``
     - boolean
     - Whether the timeline is affecting output of any fixtures
     - ``true``
   * - ``position``
     - integer
     - Milliseconds
     - ``5000``
   * - ``priority``
     - integer
     - Integer value of constants: ``HIGH_PRIORITY``, ``ABOVE_NORMAL_PRIORITY``, ``NORMAL_PRIORITY``, ``BELOW_NORMAL_PRIORITY`` or ``LOW_PRIORITY``
     - ``0``
   * - ``custom_properties``
     - table
     - Table keys and values correspond to custom property names and values
     - 

For example:

.. include:: code-examples/timeline.rst

Member functions
****************

The following are member functions of ``Timeline`` objects.

.. _Lua_timeline_start:

start
=====

``start()``

Starts the timeline. For example:

.. code-block:: lua

   -- start timeline 1
   get_timeline(1):start()


.. _Lua_timeline_release:

release
=======

``release([fade])``

Releases the timeline. Optionally specify a ``fade`` time in seconds as a float, e.g. ``2.0``.

For example:

.. code-block:: lua

   -- release timeline 3
   get_timeline(3):release(1.0)


.. _Lua_timeline_toggle:

toggle
======

``toggle([fade])``

Toggles the playback of the timeline - if it's running, release it; if it's not running, start it. Optionally specify a release ``fade`` time in seconds as a float, e.g. ``2.0``.

For example:

.. code-block:: lua

   -- toggle timeline 2, releasing in time 3 secs if it's running
   get_timeline(2):release(3.0)


.. _Lua_timeline_pause:

pause
=====

``pause()``

Pauses the timeline.


.. _Lua_timeline_resume:

resume
======

``resume()``

Resumes the timeline.


.. _Lua_timeline_set_rate:

set_rate
========

``set_rate(rate)``

Sets the rate of playback of the timeline. Set the ``rate`` as a float or an integer with range, e.g. ``0.1`` or ``Variant(10, 100)`` would set the rate to 10% of normal speed.

For example:

.. code-block:: lua

   -- set the rate of timeline 1 to 20% of normal speed
   get_timeline(1):set_rate(0.2)
   -- set the rate of timeline 2 to 30% of normal speed
   get_timeline(2):set_rate(Variant(30,100))


.. _Lua_timeline_set_position:

set_position
============

``set_position(position)``

Jumps the position of playback of the timeline. Set the ``position`` as a float or an integer with range, e.g. ``0.1`` or ``Variant(10, 100)`` would set the position to 10% of the timeline length.

For example:

.. code-block:: lua

   -- set the position of timeline 1 to 50% of timeline length
   get_timeline(1):set_position(0.5)
   -- set the position of timeline 2 to 20% of timeline length
   get_timeline(2):set_position(Variant(2,10))


.. _Lua_timeline_set_default_source:

set_default_source
==================

Set the time source for the timeline to the default.

For example:

.. code-block:: lua

   get_timeline(1):set_default_source()


.. _Lua_timeline_set_timecode_source:

set_timecode_source
===================

``set_timecode_source(timecodeBus[, offset])``

Set a timecode source for the timeline according to the parameters:

.. list-table::
   :widths: 3 3 7 3
   :header-rows: 1

   * - Parameter
     - Value Type
     - Description
     - Value Example
   * - ``timecodeBus``
     - integer
     - Integer value of constants: ``TCODE_1`` ... ``TCODE_6``
     - ``TCODE_1``
   * - ``offset``
     - integer
     - Optional offset to apply to the timecode, in milliseconds
     - ``1000``


.. _Lua_timeline_set_audio_source:

set_audio_source
================

``set_audio_source(audioBus, band, channel[, peak])``

Set a audio band as the time source for the timeline according to the parameters:

.. list-table::
   :widths: 3 3 7 3
   :header-rows: 1

   * - Parameter
     - Value Type
     - Description
     - Value Example
   * - ``audioBus``
     - integer
     - Integer value of constants: ``AUDIO_1`` ... ``AUDIO_4``
     - ``AUDIO_1``
   * - ``band``
     - integer
     - The audio band to sample (number of bands depends on audio source configuration; 0 => volume)
     - ``0``
   * - ``channel``
     - integer
     - Integer value of constants: ``LEFT``, ``RIGHT`` or ``COMBINED``
     - ``LEFT``
   * - ``peak``
     - boolean
     - Optional. Whether to use the peak levels from the audio band as the time source input (default false)
     - ``false``

