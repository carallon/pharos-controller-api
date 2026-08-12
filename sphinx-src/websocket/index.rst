WebSocket API
#############

|Vendor| controllers provide an API to interact with the controller via WebSockets. Unlike HTTP calls, which are stateless, a WebSocket is a maintained connection.
This allows facilities which are not available with HTTP calls such as subscribing to the state of objects within the system.

Using the WebSocket is more complicated than the simple HTTP API calls, but can be useful for creating a responsive web page or connecting to a third party system.

.. toctree::
   :hidden:

   beacon
   content-target
   group
   io-module
   log
   lua
   network-adapters
   remote-device
   scene
   timeline
   rdm/index

Endpoint
********

WebSocket clients can make a WebSocket upgrade request to the `/query` endpoint of the controller, e.g.

`wss://{{controller-ip}}/query`

The controller supports both `ws` (default port: 80) or `wss` (default port: 443) URI schemes.

.. caution::

  |LPC| Controllers support a maximum of 8 simultaneous HTTP connections. |LPC X| and |VLC| controllers support a maximum of 16 connections.

  Using a WebSocket maintains use of one of those connections.

  Therefore, be careful to not establish too many WebSocket connections to a controller; once the maximum is reached the controller will not accept further HTTP connections. This includes connections to the default web interface, so if you see effects such as the web interface failing to load, it may be due to too many open WebSocket connections.

.. _websocket_authentication:

Authentication
**************

If the controller does not have security enabled, the WebSocket can be accessed freely without a token.

If the controller does have security enabled then:

* You must obtain a bearer token

  * For a webpage, you can extract the bearer token from the cookie provided by the login system, for example:

    .. code-block:: javascript

      var match = document.cookie.match(new RegExp('(^| )token=([^;]+)'));
      if (match) {
         token = match[2];
      }

  * For a third party system, you can retrieve a token by requesting one from the Authentication endpoint - see :ref:`HTTP Authentication <authenticate-http-post>`.

* The user with which the token was requested must have at least the `status` access level.
* The `token` attribute must be added to the transmitted JSON with the bearer token received from authenticating a user.

.. code-block:: json

   {
      "subscribe": "{{channel-name}}",
      "token": "{{bearer-token}}"
   }

Tokens can be refreshed through the keep alive message, described below.

Keep Alive and Detecting Disconnect
***********************************

A message should be sent every ~10 seconds to keep the connection alive. A keepalive message may be an empty JSON object.

If controller security is enabled, then the object should have a `token` attribute with a valid bearer token as its string value. Otherwise, the object should be empty.

If the response contains a binary object of all zeros, that indicates that the session has timed out. You should close the WebSocket and re-authenticate, either by showing a login page (if you are developing a web interface), or automatically re-authenticating for non-browser clients. If the response binary object is non-zero, it is a session key and indicates the session is still valid.

If controller security is not enabled the response will contain an empty JSON object.

Requesting a value
******************

Some commands allow values to be requested over the WebSocket. Requests can include an *id* value which is simply a number which is reported with the reply; the number can be used to track multiple requests occurring at once.

For example:

Request message:

.. code-block:: json

   {
      "request": "system",
      "id": 1
   }


Response message:

.. code-block:: json

   {
      "request": "system",
      "id": 1,
      "data": {
         "hardware_type": "VLC",
         "channel_capacity": 768000,
         "serial_number": "030208",
         "memory_total": "6982288 KB",
         "memory_used": "522244 KB",
         "memory_available": "6460044 KB",
         "storage_size": "3063 MB",
         "bootloader_version": "V5.0.0.17 R1.8.0.SR.1",
         "firmware_version": "2.15.0 BETA2",
         "reset_reason": "Hardware Reset",
         "last_boot_time": "24 Apr 2025 10:49:25",
         "ip_address": "172.20.30.225",
         "subnet_mask": "255.255.252.0",
         "default_gateway": "172.20.28.250"
      }
   }

The complete set of available commands for request is listed below.

Subscribing to Broadcast Channels
*********************************

To create a subscription to a broadcast channel, send a JSON object over the WebSocket connection in the following format:

.. code-block:: json

   {
      "subscribe": "{{channel-name}}"
   }


WebSocket functions
*******************

The following functions are provided over the WebSocket - see the notes for further details


.. list-table::
   :widths: 5 5 3 3 10
   :header-rows: 1

   * - Function
     - Channel Name
     - Request
     - Subscribe
     - Notes
   * - :doc:`network-adapters`
     - ``network_adapters``
     - ✔
     - ✖
     -
   * - :doc:`timeline`
     - ``timeline``
     - ✔
     - ✔
     -
   * - :doc:`scene`
     - ``scene``
     - ✔
     - ✔
     -
   * - :doc:`group`
     - ``group``
     - ✔
     - ✔
     -
   * - :doc:`content-target`
     - ``content_target``
     - ✔
     - ✔
     -
   * - :doc:`remote-device`
     - ``remote-device``
     - ✔
     - ✔
     -
   * - :doc:`beacon`
     - ``beacon``
     - ✖
     - ✔
     -
   * - :doc:`log`
     - ``log``
     - ✔
     - ✔
     -
   * - :doc:`lua`
     - ``lua``
     - ✖
     - ✔
     -
   * - :doc:`io-module`
     - ``io_module``
     - ✔
     - ✔
     -
   * - System
     - ``system``
     - ✔
     - ✖
     - Returns the same data as the :doc:`../http-api/system` endpoint
   * - Current Time
     - ``current_time``
     - ✔
     - ✖
     - Returns the same data as the :doc:`../http-api/time` endpoint
   * - Project
     - ``project``
     - ✔
     - ✖
     - Returns the same data as the :doc:`../http-api/project` endpoint
   * - Controller
     - ``controller``
     - ✔
     - ✖
     - Returns the same data as the :doc:`../http-api/controller` endpoint
   * - Text Slot
     - ``text_slot``
     - ✔
     - ✖
     - Returns the same data as the :doc:`../http-api/text-slots` endpoint
   * - Temperature
     - ``temperature``
     - ✔
     - ✖
     - Returns the same data as the :doc:`../http-api/temperature` endpoint
   * - Fan Speed
     - ``fan_speed``
     - ✔
     - ✖
     - Returns the same data as the :doc:`../http-api/fan-speed` endpoint
   * - Protocol
     - ``protocol``
     - ✔
     - ✖
     - Returns the same data as the :doc:`../http-api/protocol` endpoint
   * - Output
     - ``output``
     - ✔
     - ✖
     - Returns the same data as the :doc:`../http-api/output` endpoint
   * - Input
     - ``input``
     - ✔
     - ✖
     - Returns the same data as the :doc:`../http-api/input` endpoint
   * - Trigger
     - ``trigger``
     - ✔
     - ✖
     - Returns the same data as the :doc:`../http-api/trigger` endpoint
   * - DALI Interface
     - ``dali_interface``
     - ✔
     - ✖
     - Returns the same data as the :doc:`../http-api/trigger` endpoint
   * - Replication
     - ``replication``
     - ✔
     - ✖
     - Returns the same data as the :doc:`../http-api/replication` endpoint
   * - Config
     - ``config``
     - ✔
     - ✖
     - Returns the same data as the :doc:`../http-api/config` endpoint
   * - Playback Group
     - ``playback_group``
     - ✔
     - ✖
     - Returns the same data as the :doc:`../http-api/playback-group` endpoint
