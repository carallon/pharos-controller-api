Ping
####

Methods
*******

.. _ping-http-post:

POST
====

Send a single ping to a remote target.

Reply is broadcast on WebSocket. (see :ref:`websocket_subscribe_ping`)

``POST /api/beacon``

Payload is a JSON object with the following attributes:

.. list-table::
   :widths: 5 2 10 5
   :header-rows: 1

   * - Attribute
     - Value Type
     - Description
     - Value Example
   * - ``target``
     - string
     - Target IP Address or host name
     - ``"8.8.8.8"`` or ``"google.com"``
   * - ``interface``
     - integer
     - Optional. Network interface index.
     - 1
