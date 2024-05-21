Websocket Subscriptions
#######################

Websocket subscriptions allow data to be pushed to the web client whenever there is a change within the project. The query.js library includes functions with callbacks to subscribe to each channel and return any data received.

Functions
*********

subscribe_timeline_status
=========================

Subscribe to changes in timeline status.

``subscribe_timeline_status(callback)``

The ``callback`` is called each time a timeline changes state on the controller. Each time it is passed an object with the following attributes:

.. list-table::
   :widths: 3 3 10 4
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``num``
     - integer
     - Timeline number
     - ``1``
   * - ``state``
     - string
     - The new state of the timeline: ``none``, ``running``, ``paused``, ``holding_at_end``, ``released``
     - ``"running"``
   * - ``onstage``
     - boolean
     - Whether the timeline is currently affecting the output of any fixtures in the project.
     - ``true``
   * - ``position``
     - integer
     - Current time position of the timeline playback, in milliseconds
     - ``5000``

For example:

.. code-block:: js

   Query.subscribe_timeline_status(t => {
     alert(t.num + ": " + t.state)
   })

subscribe_scene_status
======================

Subscribe to changes in scene status.

``subscribe_scene_status(callback)``

The ``callback`` is called each time a scene changes state on the controller. Each time it is passed an object with the following attributes:

.. list-table::
   :widths: 3 3 10 4
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``num``
     - integer
     - Scene number
     - ``1``
   * - ``state``
     - string
     - The new state of the scene: ``none``, ``started``, ``released``
     - ``"started"``
   * - ``onstage``
     - boolean
     - Whether the scene is currently affecting the output of any fixtures in the project.
     - ``true``

For example:

.. code-block:: js

   Query.subscribe_scene_status(s => {
     alert(s.num + ": " + s.state)
   })

subscribe_group_status
======================

Subscribe to changes in group level, as set by the Master Intensity action.

``subscribe_group_status(callback)``

The ``callback`` is called each time the group master level changes on the controller. Each time it is passed an object with the following attributes:

.. list-table::
   :widths: 3 3 10 4
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``num``
     - integer
     - Group number
     - ``1``
   * - ``name``
     - string
     - Group name
     - ``"Group 1"``
   * - ``level``
     - integer
     - New master intensity level of the group: 0-255
     - ``128``

For example:

.. code-block:: js

   Query.subscribe_group_status(g => {
     alert(g.num + ": " + g.level)
   })

subscribe_remote_device_status
==============================

Subscribe to changes in remote device online/offline status.

``subscribe_remote_device_status(callback)``

The ``callback`` is called each time the remote device online/offline status changes. Each time it is passed an object with the following attributes:

.. list-table::
   :widths: 3 3 10 4
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``num``
     - integer
     - Remote device number
     - ``1``
   * - ``type``
     - string
     - Type of remote device: ``RIO 80``, ``RIO 44``, ``RIO 08``, ``BPS``, ``RIO A``, ``RIO D``, ``EDN 20``, ``EDN 10``
     - ``"RIO 80"``
   * - ``online``
     - boolean
     - New online state of the remote device
     - ``true``
   * - ``serial``
     - string
     - Remove device serial number
     - ``"001001"``

For example:

.. code-block:: js

   Query.subscribe_remote_device_status(r => {
     alert(r.num + ": " + (r.online ? "online" : "offline"))
   })

subscribe_beacon
================

Subscribe to changes in the device beacon.

``subscribe_beacon(callback)``

The ``callback`` is called each time the controller beacon status changes. Each time it is passed an object with the following attributes:

.. list-table::
   :widths: 3 3 10 4
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``on``
     - boolean
     - New beacon status
     - ``true``

For example:

.. code-block:: js

   Query.subscribe_beacon(b => {
     alert(b.on ? "Beacon turned on" : "Beacon turned off")
   })


.. _websocket_subscribe_lua:

subscribe_lua
=============

The receiver for the ``push_to_web()`` Lua function.

``subscribe_lua(callback)``

The ``callback`` is called each time a script on the controller calls the ``push_to_web()`` function. Each time it is passed an object with a single attribute - the name or key string passed as the first argument to ``push_to_web()``. The value of this attribute is the second argument passed to ``push_to_web()``, converted to a string.

For example, if a project needs to send a touch slider level to the web interface, it might have the following in a trigger Lua script:

.. code-block:: lua

   level = getMySliderLevel() -- user-defined function to get the current slider level
   push_to_web("slider_level", level) -- invoke callbacks on subscribers

If ``level`` is equal to e.g. 56 then the object passed the JavaScript callback will be:

.. code-block:: json

   {
     "slider_level": "56"
   }

And the subscription could be setup as follows:

.. code-block:: js

   Query.subscribe_lua(l => {
    key = Object.keys(l)[0] // "slider_level" in the above example
    value = l.key           // "56" in the above example
    alert(key + ": " + value)
   })

.. _websocket_subscribe_ping:

subscribe_ping
==============

Subscribe to ping responses.

``subscribe_ping(callback)``

The ``callback`` is called each time the controller receives a ping response initiated by the web api. Each time it is passed an object with the following attributes:

.. list-table::
   :widths: 3 3 10 4
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``target``
     - string
     - The target IP Address of the ping
     - ``8.8.8.8``
   * - ``reply_ms``
     - integer
     - Optional. The round trip time (ms) of the reply.
     - ``8``
   * - ``timeout_ms``
     - integer
     - Optional. The reply didn't arrive, in after this interval (ms).
     - ``1000``

``reply_ms`` and ``timeout_ms`` are mutually exclusive.

For example:

.. code-block:: js

   Query.subscribe_ping(p => {
      if (p.hasOwnProperty('reply_ms'))
      {
        alert("Ping reply in " + p.reply_ms + "ms from " + p.target)
      }
      else if (p.hasOwnProperty('timeout_ms'))
      {
        alert("Ping timeout after " + p.timeout_ms + "ms sending to " + p.target)
      }
   })

.. _websocket_subscribe_rdm_discovery:

subscribe_rdm_discovery
=======================

Subscribe for results from RDM discovery operations.

``subscribe_rdm_discovery(callback)``

The callback is called every time an RDM device is found during an RDM discovery operation, and to announce when the RDM discovery operation is finished or has been cancelled. The callback is passed an object with the following attributes:

.. list-table::
   :widths: 3 3 10
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
   * - ``message_type``
     - string
     - Categorises the message, defining what ``data`` is present, if any (see below).
   * - ``universe``
     - string
     - The universe on which the RDM operation is acting, in the `Universe Key String Format`_.
   * - ``data``
     - object
     - Optional. Data appropriate for the message type.

Device found
------------

``"message_type" : "device_found"``

The ``data`` object will have the following attributes:

.. list-table::
   :widths: 3 3 10
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
   * - ``device_info``
     - :doc:`../../http-api/objects/rdm-device-info`
     - RDM device info from the discovered device.
   * - ``fixture_num``
     - integer
     - User number of the fixture in the project with the same DMX address and footprint as the discovered device, or `null` if there is no matching fixture in the project.

Discovery finished
------------------

``"message_type" : "finished"``

The ``data`` object will not be present, or will be empty.

Discovery cancelled
-------------------

``"message_type" : "cancelled"``

The ``data`` object will have the following attributes:

.. list-table::
   :widths: 3 3 10
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
   * - ``error``
     - string
     - A description of why the discovery was cancelled.


.. _websocket_subscribe_rdm_get_set:

subscribe_rdm_get_set
=====================

Subscribe for results from RDM Get and Set operations.

``subscribe_rdm_get_set(callback)``

The callback is called to provide the response from RDM Get and Set operations, and to announce when the RDM operation is finished or has been cancelled. The callback is passed an object with the following attributes:

.. list-table::
   :widths: 3 3 10
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
   * - ``message_type``
     - string
     - Categorises the message, defining what ``data`` is present, if any (see below).
   * - ``universe``
     - string
     - The universe on which the RDM operation is acting, in the `Universe Key String Format`_.
   * - ``device_id``
     - string
     - Format is ``{manuId}:{deviceId}(:{subId})``
       where ``{manuId}`` is a padded unsigned hexadecimal integer of width 4, lowercase, e.g. ``072c``;
       ``{deviceId}`` is a padded unsigned hexadecimal integer of width 8, lowercase, e.g. ``0004fe02``;
       ``{subId}`` is an optional unsigned decimal integer.
   * - ``pid``
     - string
     - RDM PID as a human-readable string, e.g. ``DEVICE_INFO``, or a string containing the hex representation of the enum value of the PID as defined by the RDM standard, e.g. ``"c1"``.
   * - ``data``
     - object
     - Optional. Data appropriate for the message type.

Get Finished
------------

``"message_type" : "get_finished"``

The GET operation indicated by the PID has finished. No ``data`` object is expected.

Set Finished
------------

``"message_type" : "set_finished"``

The SET operation indicated by the PID has finished. No ``data`` object is expected.

Get/Set result error
--------------------

``"message_type" : "result_error"``

The ``data`` object will have the following attributes:

.. list-table::
   :widths: 3 3 10
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
   * - ``error``
     - string
     - Description of the error with the response.

Get/Set operation cancelled
---------------------------

``"message_type" : "get_cancelled"``
``"message_type" : "set_cancelled"``

The ``data`` object will have the following attributes:

.. list-table::
   :widths: 3 3 10
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
   * - ``error``
     - string
     - Description of why the operation was cancelled.

Get/Set Result
--------------

``"message_type" : "result"``

Provides the results of the operation, parsed from the response from the device. The ``data`` object will be appropriate for the PID. If ``pid`` is a human-readable string, e.g. ``DEVICE_INFO`` then ``data`` is described under `RDM PID result data`_. Otherwise, if ``pid`` is the hex representation of the enum value of a PID, then ``data`` will have one key, ``raw``, the value of which will be the base64-encoded raw payload data received from the device.

RDM PID result data
^^^^^^^^^^^^^^^^^^^

When the object passed to the ``subscribe_rdm_get_set`` callback has ``"message_type": "result"`` and where ``pid`` is a human-readable string, e.g. ``DEVICE_INFO``, the format of the ``data`` object is described in one of the following sections.

Get Communication Status (COMMS_STATUS)
"""""""""""""""""""""""""""""""""""""""

Following a successful GET operation for ``COMMS_STATUS``, the ``data`` object in the ``subscribe_rdm_get_set`` callback argument will have the following attributes, which map to the attributes of the same names in the RDM specification for this response:

* ``short_message`` - number (16 bit)
* ``length_mismatch`` - number (16 bit)
* ``checksum_fail`` - number (16 bit)

Get Status Messages (STATUS_MESSAGES)
"""""""""""""""""""""""""""""""""""""

Following a successful GET operation for ``STATUS_MESSAGES``, the ``data`` object in the ``subscribe_rdm_get_set`` callback argument will have a ``status_messages`` attribute with an array value, the items of which will each have the following attributes, which map to the attributes of the same names in the RDM specification for this response:

* ``sub_device_id`` - number (16 bit)
* ``status_type`` - number (8 bit)
* ``status_message_id`` - number (16 bit)
* ``data_value_1`` - number (16 bit)
* ``data_value_2`` - number (16 bit)

Get Supported Parameters (SUPPORTED_PARAMETERS)
"""""""""""""""""""""""""""""""""""""""""""""""

Following a successful GET operation for ``SUPPORTED_PARAMETERS``, the ``data`` object in the ``subscribe_rdm_get_set`` callback argument will have a ``supported_parameters`` attribute with an array value. The array will contain numbers, corresponding to the 16 bit parameter IDs supported by the RDM device, as described in the RDM specification.

Get Parameter Description (PARAMETER_DESCRIPTION)
"""""""""""""""""""""""""""""""""""""""""""""""""

Following a successful GET operation for ``PARAMETER_DESCRIPTION``, the ``data`` object in the ``subscribe_rdm_get_set`` callback argument will have the following attributes, which map to the attributes of the same names in the RDM specification for this response:

* ``pid_requested`` - number (16 bit)
* ``pdl_size`` - number (8 bit)
* ``data_type`` - number (8 bit)
* ``command_class`` - number (8 bit)
* ``type`` - number (8 bit)
* ``unit`` - number (8 bit)
* ``prefix`` - number (8 bit)
* ``min_valid_value`` - number (32 bit)
* ``max_valid_value`` - number (32 bit)
* ``default_value`` - number (32 bit)
* ``description`` - string (ASCII, max 32 characters)

Get Device Info (DEVICE_INFO)
"""""""""""""""""""""""""""""

Following a successful GET operation for ``DEVICE_INFO``, the ``data`` object in the ``subscribe_rdm_get_set`` callback argument will have the following attributes, which map to the attributes of the same names in the RDM specification for this response:

* ``rdm_protocol_version`` - number (16 bit)
* ``device_model_id`` - number (16 bit)
* ``product_category`` - number (16 bit)
* ``software_version_id`` - number (32 bit)
* ``dmx512_footprint`` - number (16 bit)
* ``dmx512_personality`` - number (16 bit)
* ``start_address`` - number (16 bit)
* ``sub_device_count`` - number (16 bit)
* ``sensor_count`` - number (8 bit)

Get Device Model Description (DEVICE_MODEL_DESCRIPTION)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""

Following a successful GET operation for ``DEVICE_MODEL_DESCRIPTION``, the ``data`` object in the ``subscribe_rdm_get_set`` callback argument will have a ``model_description`` attribute with a string value. The string will be the ASCII model description, 0-32 characters, as described in the RDM specification.

Get Manufacturer Label (MANUFACTURER_LABEL)
"""""""""""""""""""""""""""""""""""""""""""

Following a successful GET operation for ``MANUFACTURER_LABEL``, the ``data`` object in the ``subscribe_rdm_get_set`` callback argument will have a ``manufacturer_label`` attribute with a string value. The string will be the ASCII manufacturer description, 0-32 characters, as described in the RDM specification.

Get/Set Device Label (DEVICE_LABEL)
"""""""""""""""""""""""""""""""""""

Following a successful GET operation for ``DEVICE_LABEL``, the ``data`` object in the ``subscribe_rdm_get_set`` callback argument will have a ``device_label`` attribute with a string value. The string will be the current ASCII device label, 0-32 characters, as described in the RDM specification.

No ``data`` is expected in the response for a SET operation.

Get/Set Factory Defaults (FACTORY_DEFAULTS)
"""""""""""""""""""""""""""""""""""""""""""

Following a successful GET operation for ``FACTORY_DEFAULTS``, the ``data`` object in the ``subscribe_rdm_get_set`` callback argument will have a ``factory_defaults`` attribute with a boolean value, indicating whether the device is currently set to is factory defaults.

No ``data`` is expected in the response for a SET operation.

Get Software Version Label (SOFTWARE_VERSION_LABEL)
"""""""""""""""""""""""""""""""""""""""""""""""""""

Following a successful GET operation for ``SOFTWARE_VERSION_LABEL``, the ``data`` object in the ``subscribe_rdm_get_set`` callback argument will have a ``software_version_label`` attribute with a string value. The string will be the ASCII software version label, 0-32 characters, as described in the RDM specification.

Get Boot Software Version ID (BOOT_SOFTWARE_VERSION_ID)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""

Following a successful GET operation for ``BOOT_SOFTWARE_VERSION_ID``, the ``data`` object in the ``subscribe_rdm_get_set`` callback argument will have a ``boot_software_version_id`` attribute with a 32 bit number value, as described in the RDM specification.

Get Boot Software Version Label (BOOT_SOFTWARE_VERSION_LABEL)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Following a successful GET operation for ``BOOT_SOFTWARE_VERSION_LABEL``, the ``data`` object in the ``subscribe_rdm_get_set`` callback argument will have a ``boot_software_version_label`` attribute with a string value. The string will be the ASCII boot version label, 0-32 characters, as described in the RDM specification.

Get/Set DMX512 Personality (DMX_PERSONALITY)
""""""""""""""""""""""""""""""""""""""""""""

Following a successful GET operation for ``DMX_PERSONALITY``, the ``data`` object in the ``subscribe_rdm_get_set`` callback argument will have the following attributes, which map to the attributes of the same names in the RDM specification for this response:

* ``current_personality`` - number (8 bit)
* ``num_personalities`` - number (8 bit)

No ``data`` is expected in the response for a SET operation.

Get DMX512 Personality Description (DMX_PERSONALITY_DESCRIPTION)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Following a successful GET operation for ``DMX_PERSONALITY_DESCRIPTION``, the ``data`` object in the ``subscribe_rdm_get_set`` callback argument will have the following attributes, which map to the attributes of the same names in the RDM specification for this response:

* ``personality_requested`` - number (8 bit)
* ``dmx512_slots_required`` - number (16 bit)
* ``description`` - string (ASCII, 0-32 characters)

Get/Set DMX512 Starting Address (DMX_START_ADDRESS)
"""""""""""""""""""""""""""""""""""""""""""""""""""

Following a successful GET operation for ``DMX_START_ADDRESS``, the ``data`` object in the ``subscribe_rdm_get_set`` callback argument will have a ``dmx512_address`` attribute with a 16 bit number value, as described in the RDM specification.

No ``data`` is expected in the response for a SET operation.

Get Slot Info (SLOT_INFO)
"""""""""""""""""""""""""

Following a successful GET operation for ``SLOT_INFO``, the ``data`` object in the ``subscribe_rdm_get_set`` callback argument will have a ``slot_info`` attribute with an array value, the items of which will each have the following attributes, which map to the attributes of the same names in the RDM specification for this response:

* ``slot_offset`` - number (16 bit)
* ``slot_type`` - number (8 bit)
* ``slot_label_id`` - number (16 bit)

Get Slot Description (SLOT_DESCRIPTION)
"""""""""""""""""""""""""""""""""""""""

Following a successful GET operation for ``SLOT_DESCRIPTION``, the ``data`` object in the ``subscribe_rdm_get_set`` callback argument will have the following attributes, which map to the attributes of the same names in the RDM specification for this response:

* ``slot_number_requested`` - number (16 bit)
* ``description`` - string (ASCII, 0-32 characters)

Get Sensor Definition (SENSOR_DEFINITION)
"""""""""""""""""""""""""""""""""""""""""

Following a successful GET operation for ``SENSOR_DEFINITION``, the ``data`` object in the ``subscribe_rdm_get_set`` callback argument will have the following attributes, which map to the attributes of the same names in the RDM specification for this response:

* ``sensor_number_requested`` - number (8 bit)
* ``type`` - number (8 bit)
* ``unit`` - number (8 bit)
* ``prefix`` - number (8 bit)
* ``range_minimum_value`` - number (16 bit)
* ``range_maximum_value`` - number (16 bit)
* ``normal_minimum_value`` - number (16 bit)
* ``normal_maximum_value`` - number (16 bit)
* ``recorded_value_support`` - number (8 bit)
* ``description`` - string (ASCII, 0-32 characters)

Get/Set Sensor (SENSOR_VALUE)
"""""""""""""""""""""""""""""

Following a successful GET or SET operation for ``SENSOR_VALUE``, the ``data`` object in the ``subscribe_rdm_get_set`` callback argument will have the following attributes, which map to the attributes of the same names in the RDM specification for this response:

* ``sensor_number_requested`` - number (8 bit)
* ``present_value`` - number (16 bit)
* ``lowest_detected_value`` - number (16 bit)
* ``highest_detected_value`` - number (16 bit)
* ``recorded_value`` - number (16 bit)

Get/Set Lamp Hours (LAMP_HOURS)
"""""""""""""""""""""""""""""""

Following a successful GET or SET operation for ``LAMP_HOURS``, the ``data`` object in the ``subscribe_rdm_get_set`` callback argument will have the following attributes, which map to the attributes of the same names in the RDM specification for this response:

* ``lamp_hours`` - number (32 bit)

Get/Set Lamp State (LAMP_STATE)
"""""""""""""""""""""""""""""""

Following a successful GET or SET operation for ``LAMP_STATE``, the ``data`` object in the ``subscribe_rdm_get_set`` callback argument will have the following attributes, which map to the attributes of the same names in the RDM specification for this response:

* ``lamp_state`` - number (8 bit)

Universe Key String Format
**************************

.. include:: ../../snippets/universe-key-string-format-rdm.rst
