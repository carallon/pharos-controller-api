Lua Functions
#############

System
******

The ``system`` namespace has the following properties:

.. list-table::
   :widths: 3 2 5
   :header-rows: 1

   * - Property
     - Value Type
     - Value Example
   * - ``hardware_type``
     - string
     - ``"lpc"``
   * - ``channel_capacity``
     - integer
     - ``512``
   * - ``etc``
     - etc
     - **To do:** complete table


For example:

.. code-block:: lua

   capacity = system.channel_capacity

   boot_time = system.last_boot_time.time_string

Project
*******

``get_current_project()``

Returns an object with the following properties:

.. list-table::
   :widths: 3 2 5
   :header-rows: 1

   * - Property
     - Value Type
     - Value Example
   * - ``name``
     - string
     - ``"Help Project"``
   * - ``author``
     - string
     - ``"Pharos"``
   * - ``etc``
     - etc
     - **To do:** complete table


For example:

.. code-block:: lua

   project_name = get_current_project().name

Timeline
********

**TODO** - adaptor for Lua from HTTP; table may only need headers changing

Returns data about the timelines in the project and their state on the controller.

HTTP
====

GET
---

``GET /api/timeline[?num=timelineNumbers]``

``num`` can be used to filter which timelines are returned and is expected to be either a single number or a string expressing the required timelines, e.g. ``"1,2,5-9"``.

Returns a JSON object with a single ``timelines`` attribute, which has an array value. Each item in the array is a timeline object with the following attributes:

.. list-table::
   :widths: 2 2 10 5
   :header-rows: 1

   * - Property
     - Value Type
     - Description
     - Value Example
   * - ``num``
     - integer
     - Timeline number
     - ``1``
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
     - 1/1000 of a second
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
     - 1/1000 of a second
     - ``5000``
   * - ``priority``
     - integer
     - Integer value of constants: ``HIGH_PRIORITY``, ``ABOVE_NORMAL_PRIORITY``, ``NORMAL_PRIORITY``, ``BELOW_NORMAL_PRIORITY`` or ``LOW_PRIORITY``
     - ``0``
   * - ``custom_properties``
     - table
     - Table keys and values correspond to custom property names and values
     - 
