Websocket Subscriptions
#######################

Subscriptions allow data to be pushed to the web client whenever there is a change within the project.

JavaScript
**********

subscribe_timeline_status
=========================

Subscribe to changes in timeline status.

``subscribe_timeline_status(callback)``

The ``callback`` is called each time a timeline changes state on the controller. Each time it is passed an object with the following attributes:

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
   :widths: 5 2 10 5
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
   :widths: 5 2 10 5
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
   :widths: 5 2 10 5
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
   :widths: 5 2 10 5
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
