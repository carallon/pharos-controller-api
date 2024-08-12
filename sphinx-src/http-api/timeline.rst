Timeline
########

Methods
*******

POST
====

Control a timeline in the project. Action will propagate to all controllers in a project.

``POST /api/timeline``

Payload is a JSON object with the following attributes:

.. list-table::
   :widths: 3 3 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``action``
     - string
     - The action to perform on the timeline(s): ``start``, ``start_release_others``, ``release``, ``toggle``, ``pause``, ``resume``, ``set_rate``, ``set_position``
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
     - string **or** integer
     - Optional. Timeline group name or number. If name, prepend the name with ``!`` to apply the action to all groups *except* the specified group. This attribute is valid for a ``release`` action without a specified ``num``, meaning *release all timelines*.
     - ``"Group 1"``, ``"!Group 2"`` or ``3``
   * - ``same_group``
     - boolean
     - Optional flag to target the same group as the selected timeline. This flag has no effect when ``group`` is set.
     - ``true``
   * - ``rate``
     - string
     - Required for a ``set_rate`` action; invalid otherwise. Value should be a string containing a floating point number or a bounded integer, where 1.0 means the timeline's default rate.
     - ``"0.1"`` or ``"10:100"``

If the ``action`` is ``set_position``, then **one** of the following is required:

.. list-table::
   :widths: 3 3 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``position``
     - string
     - Value should be a string containing a floating point number or a bounded integer, representing a fraction of the timeline length.
     - ``"0.1"`` or ``"10:100"``
   * - ``time``
     - number
     - Value represents an absolute time point (seconds) within the timeline.
     - ``0.1`` or ``180``
   * - ``flag``
     - string
     - The name of the timeline flag, representing an absolute time point within the timeline.
     - ``Start sparkle`` or ``My Flag 1``

For example, to start timeline 2, the request payload is:

.. code-block:: json

   {
     "action": "start",
     "num": 2
   }

To start timeline 2 and release others in group ``B`` in 2 seconds, the request payload is:

.. code-block:: json

   {
     "action": "start_release_others",
     "num": 2,
     "group": "B",
     "fade": 2.0
   }

To start timeline 2 and release others in the same group, the request payload is:

.. code-block:: json

   {
     "action": "start_release_others",
     "num": 2,
     "same_group": true
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

To set the rate of timeline 5 to half the default range, the request payload would be:

.. code-block:: json

   {
     "action": "set_rate",
     "num": 5,
     "rate": "0.5"
   }

To set the position of timeline 1 to a third of the way through, the request payload would be:

.. code-block:: json

   {
     "action": "set_position",
     "num": 1,
     "position": "1:3"
   }

To set the position of timeline 1 to 50% of the way through, the request payload would be:

.. code-block:: json

  {
    "action": "set_position",
    "num": 1,
    "position": "0.5"
  }

To set the position of timeline 3 to 180 seconds, the request payload would be:

.. code-block:: json

  {
    "action": "set_position",
    "num": 3,
    "time": 180
  }

To set the position of timeline 4 to 12.34 seconds, the request payload would be:

.. code-block:: json

  {
    "action": "set_position",
    "num": 4,
    "time": 12.34
  }

To set the position of timeline 5 at the timeline flag named "Start sparkle", the request payload would be:

.. code-block:: json

  {
    "action": "set_position",
    "num": 5,
    "flag": "Start sparkle"
  }

GET
===

Returns data about the timelines in the project and their state on the controller.

``GET /api/timeline[?num=timelineNumbers]``

``num`` can be used to filter which timelines are returned and is expected to be either a single number or a string expressing the required timelines, e.g. ``"1,2,5-9"``.

Returns a JSON object with a single ``timelines`` attribute, which has an array value. Each item in the array is a Timeline object with the following attributes:

.. list-table::
   :widths: 5 2 10 5
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
     - Timeline group name (``A`` through ``H`` or empty string)
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
     - Incoming timecode format on source bus
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
