Timeline
########

HTTP
****

POST
====

Control a timeline in the project.

``POST /api/timeline``

Payload is a JSON object with the following attributes:

.. list-table::
   :widths: 2 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``action``
     - string
     - The action to perform on the timeline(s): ``start``, ``release``, ``toggle``, ``pause``, ``resume``, ``set_rate``, ``set_position``
     - ``"start"``
   * - ``num``
     - integer
     - The number of the timeline to perform the action on. If not present, the action will be applied to all timelines in the project; omitting this attribute is valid for ``release``, ``pause`` and ``resume``.
     - ``1``
   * - ``fade``
     - number
     - Optional. The fade time to apply to a ``release`` action, in seconds, or the timeline release that results from a ``toggle`` action. If not provided, the default release fade time will be used.
     - ``2.0``
   * - ``group``
     - string
     - Optional. Timeline group name: ``A``, ``B``, ``C`` or ``D``. Prepend the group name with ``!`` to apply the action to all groups *except* the specified group, e.g. ``!A``. This attribute is valid for a ``release`` action without a specified ``num``, meaning *release all timelines*.
     - ``"B"``
   * - ``rate``
     - string
     - Required for a ``set_rate`` action; invalid otherwise. Value should be a string containing a floating point number or a bounded integer, where 1.0 means the timeline's default rate.
     - ``"0.1"`` or ``"10:100"``
   * - ``position``
     - string
     - Required for a ``set_position`` action; invalid otherwise. Value should be a string containing a floating point number or a bounded integer, representing a fraction of the timeline length.
     - ``"0.1"`` or ``"10:100"``

For example, to start a timeline 2, the request payload is:

.. code-block:: json

   {
     "action": "start",
     "num": 2
   }

To release timeline 2 in 3.5 seconds, the request payload would be:

.. code-block:: json

   {
     "action": "release",
     "num": 2,
     "fade": 3.5
   }

To toggle timeline 2, and release it in 2 seconds if it's running, the request payload would be:

.. code-block:: json

   {
     "action": "toggle",
     "num": 2,
     "fade": 2.0
   }

To pause timeline 4, the request payload is:

.. code-block:: json

   {
     "action": "pause",
     "num": 4
   }

To resume timeline 4, the request payload is:

.. code-block:: json

   {
     "action": "resume",
     "num": 4
   }

To pause all timelines, the request payload is:

.. code-block:: json

   {
     "action": "pause"
   }

To resume all timelines, the request payload is:

.. code-block:: json

   {
     "action": "resume"
   }

To release all timelines in 2 seconds, the request payload would be:

.. code-block:: json

   {
     "action": "release",
     "fade": 2.0
   }

To release all timelines except those in group B in 2 seconds, the request payload would be:

.. code-block:: json

   {
     "action": "release",
     "group": "!B",
     "fade": 2.0
   }

To set the rate of timeline 5 to half the default rage, the request payload would be:

.. code-block:: json

   {
     "action": "set_rate",
     "num": 5,
     "rate": "0.5"
   }

To set the position of timeline 1 to a third of the way through, the request payload would be:

.. code-block:: json

   {
     "action": "set_rate",
     "num": 1,
     "position": "1:3"
   }

GET
===

Returns data about the timelines in the project and their state on the controller.

``GET /api/timeline[?num=timelineNumbers]``

``num`` can be used to filter which timelines are returned and is expected to be either a single number or a string expressing the required timelines, e.g. ``"1,2,5-9"``.

Returns a JSON object with a single ``timelines`` attribute, which has an array value. Each item in the array is a Timeline object with the following attributes:

.. list-table::
   :widths: 2 2 10 5
   :header-rows: 1

   * - Attribute
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
     - string
     - ``internal``, ``timecode_1`` ... ``timecode_6``, ``audio_1`` ... ``audio_4``
     - ``"internal"``
   * - ``timecode_format``
     - string
     - Timecode format
     - ``"SMPTE30"``
   * - ``audio_band``
     - integer
     - 0 is volume band
     - ``0``
   * - ``audio_channel``
     - string
     - ``left``, ``right`` or ``combined``
     - ``"combined"``
   * - ``audio_peak``
     - boolean
     - The Peak setting of the timeline, if set to an audio time source
     - ``false``
   * - ``time_offset``
     - integer
     - 1/1000 of a second
     - ``5000``
   * - ``state``
     - string
     - ``none``, ``running``, ``paused``, ``holding_at_end`` or ``released``
     - ``"running"``
   * - ``onstage``
     - boolean
     - Whether the timeline is affecting output of any fixtures
     - ``true``
   * - ``position``
     - integer
     - 1/1000 of a second
     - ``10000``
   * - ``priority``
     - string
     - ``high``, ``above_normal``, ``normal``, ``below_normal`` or ``low``
     - ``"normal"``
   * - ``custom_properties``
     - object
     - Object properties and property values correspond to custom property names and values
     - ``{}``

JavaScript
**********

start_timeline
==============

``start_timeline(params, callback)``

``params`` is expected to be an object with the following attributes:

.. list-table::
   :widths: 2 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``num``
     - integer
     - Timeline number
     - ``5``

For ``callback`` please see `JavaScript Command Callback`_.

release_timeline
================

``release_timeline(params, callback)``

``params`` is expected to be an object with the following attributes:

.. list-table::
   :widths: 2 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``num``
     - integer
     - Timeline number
     - ``5``
   * - ``fade``
     - float
     - Optional. Release fade time in seconds. If not provided, the default fade time will be used.
     - ``2.0``

For ``callback`` please see `JavaScript Command Callback`_.

toggle_timeline
===============

``toggle_timeline(params, callback)``

``params`` is expected to be an object with the following attributes:

.. list-table::
   :widths: 2 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``num``
     - integer
     - Timeline number
     - ``5``
   * - ``fade``
     - float
     - Optional. The release fade time in seconds to apply if the toggle action results in the timeline being released. If not provided, the default fade time will be used.
     - ``2.0``

For ``callback`` please see `JavaScript Command Callback`_.

pause_timeline
==============

``pause_timeline(params, callback)``

``params`` is expected to be an object with the following attributes:

.. list-table::
   :widths: 2 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``num``
     - integer
     - Timeline number
     - ``5``

For ``callback`` please see `JavaScript Command Callback`_.

resume_timeline
===============

``resume_timeline(params, callback)``

``params`` is expected to be an object with the following attributes:

.. list-table::
   :widths: 2 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``num``
     - integer
     - Timeline number
     - ``5``

For ``callback`` please see `JavaScript Command Callback`_.

pause_all
=========

Pause all timelines in the project which are currently running.

``pause_all(callback)``

For ``callback`` please see `JavaScript Command Callback`_.

resume_all
==========

Resume all timelines in the project which are currently paused.

``resume_all(callback)``

For ``callback`` please see `JavaScript Command Callback`_.

release_all_timelines
=====================

``release_all_timelines(params, callback)``

``params`` is expected to be an object with the following attributes:

.. list-table::
   :widths: 2 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``fade``
     - float
     - Optional. Release fade time in seconds. If not provided, the default fade time will be used.
     - ``2.0``
   * - ``group``
     - string
     - Optional. Timeline group name: ``A``, ``B``, ``C`` or ``D``. Prepend the group name with ``!`` to apply the action to all groups *except* the specified group, e.g. ``!A``.
     - ``"B"``

For ``callback`` please see `JavaScript Command Callback`_.

release_all
===========

Release all timelines and scenes.

``release_all(params, callback)``

``params`` is expected to be an object with the following attributes:

.. list-table::
   :widths: 2 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``fade``
     - float
     - Optional. Release fade time in seconds. If not provided, the default fade time will be used.
     - ``2.0``
   * - ``group``
     - string
     - Optional. Timeline/Scene group name: ``A``, ``B``, ``C`` or ``D``. Prepend the group name with ``!`` to apply the action to all groups *except* the specified group, e.g. ``!A``.
     - ``"B"``

For ``callback`` please see `JavaScript Command Callback`_.

set_timeline_rate
=================

``set_timeline_rate(params, callback)``

``params`` is expected to be an object with the following attributes:

.. list-table::
   :widths: 2 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``num``
     - integer
     - Timeline number
     - ``5``
   * - ``rate``
     - string
     - A string containing a floating point number or a bounded integer, where 1.0 means the timeline's default rate.
     - ``"0.1"`` or ``"10:100"``

For ``callback`` please see `JavaScript Command Callback`_.

set_timeline_position
=====================

``set_timeline_position(params, callback)``

``params`` is expected to be an object with the following attributes:

.. list-table::
   :widths: 2 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``num``
     - integer
     - Timeline number
     - ``5``
   * - ``position``
     - string
     - A string containing a floating point number or a bounded integer, representing a fraction of the timeline length.
     - ``"0.1"`` or ``"10:100"``

For ``callback`` please see `JavaScript Command Callback`_.

get_timeline_info
=================

``get_timeline_info(callback[, num])``

Returns data about the timelines in the project and their state on the controller.

Returns an object with a single ``timelines`` attribute, which has an array value. Each item in the array is a Timeline object with the same attributes as in the HTTP GET response.

``num`` can be used to filter which timelines are returned and is expected to be an object with the following attributes:

.. list-table::
   :widths: 2 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``num``
     - string **or** integer
     - Define the numbers of the timeline that should be returned
     - ``"1,2,5-9"`` **or** ``5``

For example:

.. code-block:: js

   Query.get_timeline_info(t => {
     let name = t.timelines[0].name // name of the first timeline returned
   }, {"num":"1-4"})


JavaScript Command Callback
***************************

.. include:: ../snippets/js-command-callback.rst
