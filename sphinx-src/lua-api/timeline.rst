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
     - Timeline group name
     - ``"Group 1"``
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
     - Incoming timecode format on source bus
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
     - Integer value of the state - see `Timeline States`_ below for definitions
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

Timeline States
===============

The timeline state is one of the following states (available as Lua :ref:`constants <constants>`) :

.. list-table::
   :widths: 20 10 70
   :header-rows: 1

   * - State
     - Value
     - Description
   * - ``Timeline.NONE``
     - 0
     - The timeline has never been run (since the last reset of the controller).
   * - ``Timeline.RUNNING``
     - 1
     - The timeline is running (although might not be actively controlling outputs - see the ``onstage`` property).
   * - ``Timeline.PAUSED``
     - 2
     - The timeline has been paused by another action.
   * - ``Timeline.HOLDING_AT_END``
     - 3
     - The timeline has reached the end, and is holding.
   * - ``Timeline.RELEASED``
     - 4
     - The timeline has been run and has now been released.

Timeline Reference Type
=======================

The timeline reference type is one of the following (available as Lua :ref:`constants <constants>`) :

.. list-table::
   :widths: 20 10 70
   :header-rows: 1

   * - State
     - Value
     - Description
   * - ``Timeline.RELATIVE``
     - 0
     - The timeline position value is relative.
   * - ``Timeline.ABSOLUTE``
     - 1
     - The timeline position value is absolute.
   * - ``Timeline.FLAG``
     - 2
     - The timeline position value is obtained from a timeline flag.

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


.. _Lua_timeline_start_release_others:

start_release_others
====================

``start_release_others(group[, fade[, same_group]])``

Starts the timeline and releases others.

.. list-table::
   :widths: 3 3 7 3
   :header-rows: 1

   * - Parameter
     - Value Type
     - Description
     - Value Example
   * - ``group``
     - string **or** integer
     - Optional timeline group name or number.  If name, prepend the name with ``!`` to apply the action to all timelines *except* those in the specified group. Omit to apply the action to all timelines.
     - ``"Group 1"``, ``"!Group 2"`` or ``3``
   * - ``fade``
     - float
     - Optional fade time to use when releasing other timelines, in seconds
     - ``2.0``
   * - ``same_group``
     - boolean
     - Optional flag to target the same group as the selected timeline. This flag has no effect when ``group`` is set.
     - ``true``

For example:

.. code-block:: lua

   -- start timeline 1 and release all others in the default time
   get_timeline(1):start_release_others()
   -- start timeline 1 and release others except those in group B in 2 seconds
   get_timeline(1):start_release_others('!B', 2.0)
   -- start timeline 1 and release others in the same group in the default time
   get_timeline(1):start_release_others(nil, nil, true)


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

There are multiple overloaded calling parameters:

``set_position(position)``
Legacy behaviour, operates the same as ``set_position(timeline.RELATIVE, position)``

``set_position(timeline.RELATIVE, position)``
Jumps playback of a timeline to a relative position within the timeline. Set ``position`` as a float or an integer with range, e.g. ``0.1`` or ``Variant(10, 100)`` would set the position to 10% of the timeline length.

``set_position(timeline.ABSOLUTE, position)``
Jumps playback of a timeline to an absolute position within the timeline. Set ``position`` as a float or an integer, as the absolute timeline position in seconds.

``set_position(timeline.FLAG, flag_name)``
Jumps playback of a timeline to the position of first matching timeline flag. Set the ``flag_name`` as a string, matching the name of the target timeline flag.

For example:

.. code-block:: lua

   -- set the position of timeline 1 to 50% of timeline length
   get_timeline(1):set_position(timeline.RELATIVE, 0.5)
   -- set the position of timeline 2 to 20% of timeline length
   get_timeline(2):set_position(timeline.RELATIVE, Variant(2,10))

   -- set the position of timeline 3 to 180 seconds
  get_timeline(3):set_position(ABSOLUTE, 180)
  -- set the position of timeline 4 to 12.34 seconds
  get_timeline(4):set_position(ABSOLUTE, 12.34)

  -- set the position of timeline 5 to the "Start sparkle" flag
  get_timeline(5):set_position(FLAG,"Start sparkle")

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

